# Windows Word Fields

## Preferred path

On Windows, prefer Microsoft Word COM automation to update:

- table of contents
- page-related fields
- other dynamic fields that headless renderers may not fully materialize

## Recommended sequence

1. Build or edit the DOCX.
2. Apply real Word heading styles to all TOC-relevant headings.
3. Insert a TOC field such as `TOC \o "1-3" \h \z \u` or preserve an existing automatic TOC field.
4. End cover/TOC front matter with a Word section break, remove body `PAGE` fields from front matter footers, and restart page numbering at 1 for the body section. The cover page and TOC page are not body pages, so the first visible page number 1 must be on the first chapter/body page.
5. Open the DOCX in Word through COM.
6. Update TOC and fields.
7. Save the DOCX.
8. Export PDF for verification.
9. Render PDF pages or inspect the PDF visually if needed.
10. For final layout QA, Word COM update/export must happen before PDF page rendering; otherwise TOC, fields, and page numbers may not reflect Word's real layout.

Use `scripts/update_word_fields.ps1`.

Recommended command:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
  -File "$env:CODEX_HOME\skills\docx-course-report-writer\scripts\update_word_fields.ps1" `
  -DocxPath report.docx `
  -ExportPdf `
  -UseAsciiTemp
```

After this succeeds, prefer page-image review:

```powershell
python scripts\render_pdf_review_pages.py `
  --pdf report.pdf `
  --pages-dir build\pdf-pages `
  --sheets-dir build\pdf-review-sheets `
  --dpi 150
```

The script will render the final PDF pages to PNG, run blank-page detection, and combine four pages per contact sheet. A near-blank page is blocking unless it is deliberate and documented. PDF page render images are not screenshots; use them for layout review and describe them as rendered PDF pages.

## Important caveat

Artifact-tool or PNG rendering is great for layout QA, but a valid dynamic TOC may still appear blank in that render path. If this happens:

1. Verify the field exists in the DOCX.
2. Update fields in Word.
3. Check the exported PDF or the Word text content before concluding the TOC failed.

## ASCII-path fallback

If Word export, PDF rendering, or downstream tooling fails because of non-ASCII or Chinese paths:

1. Copy the DOCX or PDF to a temporary ASCII-only path.
2. Run the Word or render step there.
3. Copy the resulting file back to the working location.

This fallback is acceptable and often more robust than trying to force every tool to cooperate with the original path.

Recommended pattern:

1. Close stale `WINWORD.EXE` instances only when they are blocking automation and `-KillExistingWord` is safe for the current task.
2. Create a temp directory such as `%TEMP%\report_work`.
3. Copy the DOCX to a simple name such as `report.docx`.
4. Run `scripts/update_word_fields.ps1` there with optional PDF export.
5. Copy the updated DOCX/PDF back to the original project directory.

The bundled script handles this when `-UseAsciiTemp` is set. Use `-KeepTemp` only when debugging field-update failures.

## Verification

Do not trust visible TOC-looking text alone. Verify at least one of:

- DOCX package XML contains a TOC field.
- Word shows an updated TOC with page numbers.
- Exported PDF shows the TOC entries and page numbers.
- Page-rendered QA confirms the TOC and nearby pages are visually correct.
- Four-page contact sheets or individual rendered pages were inspected when the report is long.

For formal reports, also inspect whether TOC page numbers share one right edge. If the rightmost page numbers drift, reset TOC style tab stops to the usable page width and update the TOC again through Word COM before exporting PDF.

Also inspect whether the first body/chapter page is numbered 1 after Word updates the fields. If the TOC page itself visibly shows page 1, or the first chapter starts at page 2/3, repair the front matter footer, section break, and page-number restart before delivery.

Treat these as blocking issues unless the user accepts the limitation:

- static hand-typed TOC when automatic TOC is expected
- TOC field missing
- stale page numbers
- body page numbering that counts cover or TOC front matter
- visibly misaligned TOC page numbers or missing dot leaders
- failed field update without Word/ASCII-path fallback attempt
- PDF export missing when page-sensitive QA is required

## Failure Handling

- If Word COM is unavailable, document that the TOC field was inserted but still needs a Word-side refresh.
- If the DOCX opens interactively but automation fails, retry with `-UseAsciiTemp`.
- If stale Word processes lock the file, ask only if closing Word could destroy user work; otherwise use `-KillExistingWord` for unattended report automation.
- If PDF export fails after field update, keep the updated DOCX and run visual QA through another available renderer, documenting the limitation.

## Fallback when Word is unavailable

- Use a static TOC approach if the user accepts it.
- Or document that the TOC field was inserted but still needs Word-side field refresh.
- Do not pretend a blank rendered TOC means the report is broken without additional verification.
