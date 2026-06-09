param(
    [Parameter(Mandatory = $true)]
    [string]$DocxPath,

    [string]$PdfOutPath = "",

    [switch]$ExportPdf,

    [switch]$UseAsciiTemp,

    [switch]$KillExistingWord,

    [switch]$KeepTemp
)

$ErrorActionPreference = "Stop"

function Invoke-WordFieldUpdate {
    param(
        [Parameter(Mandatory = $true)]
        [string]$InputDocx,

        [string]$OutputPdf = "",

        [switch]$DoExportPdf
    )

    $resolvedDocx = (Resolve-Path $InputDocx).Path
    $word = $null
    $doc = $null

    function Set-TocTabStops {
        param(
            [Parameter(Mandatory = $true)]
            $Document
        )

        $wdAlignTabRight = 2
        $wdTabLeaderDots = 1
        $contentWidth = $Document.PageSetup.PageWidth - $Document.PageSetup.LeftMargin - $Document.PageSetup.RightMargin
        $tocStyleNames = @("TOC 1", "TOC 2", "TOC 3", "toc 1", "toc 2", "toc 3")

        foreach ($styleName in $tocStyleNames) {
            try {
                $style = $Document.Styles.Item($styleName)
                $style.ParagraphFormat.TabStops.ClearAll()
                $null = $style.ParagraphFormat.TabStops.Add($contentWidth, $wdAlignTabRight, $wdTabLeaderDots)
            }
            catch {
                # Style names vary by Word locale; paragraph-level formatting below is the fallback.
            }
        }

        foreach ($paragraph in $Document.Paragraphs) {
            $styleName = ""
            try { $styleName = [string]$paragraph.Style.NameLocal } catch {}
            if ($styleName -match "^(TOC|toc)\s*[1-3]$") {
                $paragraph.Format.TabStops.ClearAll()
                $null = $paragraph.Format.TabStops.Add($contentWidth, $wdAlignTabRight, $wdTabLeaderDots)
            }
        }
    }

    try {
        $word = New-Object -ComObject Word.Application
        $word.Visible = $false
        $word.DisplayAlerts = 0

        $doc = $word.Documents.Open($resolvedDocx)

        foreach ($toc in $doc.TablesOfContents) {
            $toc.Update()
        }

        Set-TocTabStops -Document $doc

        foreach ($toc in $doc.TablesOfContents) {
            $toc.Update()
        }

        foreach ($tof in $doc.TablesOfFigures) {
            $tof.Update()
        }

        $null = $doc.Fields.Update()
        $doc.Save()

        if ($DoExportPdf) {
            if (-not $OutputPdf) {
                $OutputPdf = [System.IO.Path]::ChangeExtension($resolvedDocx, ".pdf")
            }
            $doc.ExportAsFixedFormat($OutputPdf, 17)
        }
    }
    finally {
        if ($doc -ne $null) {
            $doc.Close($false)
        }
        if ($word -ne $null) {
            $word.Quit()
        }
        [System.GC]::Collect()
        [System.GC]::WaitForPendingFinalizers()
    }

    Write-Output "Updated Word fields for: $resolvedDocx"
    if ($DoExportPdf) {
        Write-Output "Exported PDF to: $OutputPdf"
    }
}

if ($KillExistingWord) {
    Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
    Write-Output "Closed existing WINWORD processes because -KillExistingWord was set."
}

$sourceDocx = (Resolve-Path $DocxPath).Path

if (-not $PdfOutPath -and $ExportPdf) {
    $PdfOutPath = [System.IO.Path]::ChangeExtension($sourceDocx, ".pdf")
}

if ($UseAsciiTemp) {
    $workRoot = Join-Path $env:TEMP "docx_report_word_fields"
    $stamp = Get-Date -Format "yyyyMMdd_HHmmss_fff"
    $workDir = Join-Path $workRoot $stamp
    New-Item -ItemType Directory -Path $workDir -Force | Out-Null

    $tempDocx = Join-Path $workDir "report.docx"
    $tempPdf = Join-Path $workDir "report.pdf"
    Copy-Item -LiteralPath $sourceDocx -Destination $tempDocx -Force

    Write-Output "Using ASCII temp path: $workDir"
    Invoke-WordFieldUpdate -InputDocx $tempDocx -OutputPdf $tempPdf -DoExportPdf:$ExportPdf

    Copy-Item -LiteralPath $tempDocx -Destination $sourceDocx -Force
    if ($ExportPdf) {
        Copy-Item -LiteralPath $tempPdf -Destination $PdfOutPath -Force
    }

    if (-not $KeepTemp) {
        Remove-Item -LiteralPath $workDir -Recurse -Force
    }
}
else {
    Invoke-WordFieldUpdate -InputDocx $sourceDocx -OutputPdf $PdfOutPath -DoExportPdf:$ExportPdf
}
