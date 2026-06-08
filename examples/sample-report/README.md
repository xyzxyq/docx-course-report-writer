# Sample Report Fixture

This folder contains the source inputs used to generate the checked sample artifacts in `docs/`.

## Build

From the repository root:

```powershell
New-Item -ItemType Directory -Force output

python scripts\build_report.py `
  --draft examples\sample-report\report-draft.md `
  --refs examples\sample-report\references.md `
  --output output\sample-report.docx `
  --root examples\sample-report
```

## Check

```powershell
python scripts\qa_docx_report.py `
  --docx output\sample-report.docx `
  --require-toc `
  --min-images 1 `
  --min-tables 2 `
  --min-heading1 1 `
  --stale-term '100%' `
  --stale-term '100.0%' `
  --stale-term '100.00%' `
  --json
```

On Windows with Microsoft Word installed:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File scripts\update_word_fields.ps1 `
  -DocxPath output\sample-report.docx `
  -ExportPdf `
  -PdfOutPath output\sample-report.pdf `
  -UseAsciiTemp
```

The committed `docs/sample-report.docx`, `docs/sample-report.pdf`, and rendered page PNGs were produced from this fixture during the release audit.
