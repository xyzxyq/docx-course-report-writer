# Testing Report / 测试报告

Test date: 2026-06-08

## Summary

The skill was tested with a source-first sample report fixture under:

`C:\Users\20795\Documents\codex 第一次进化\artifacts\docx-course-report-writer-release-audit\sample-report`

The release repository includes the final sample artifacts under `docs/`.

The release repository was also re-run from `examples/sample-report/` after packaging. The rebuilt `output/sample-report.docx` passed package QA, Word COM field update, PDF export, PDF text checks, and rendered first-page nonblank inspection.

On 2026-06-08, the default template integration was regression-tested. `scripts/build_report.py` was run without `--template`; it selected `skill-assets/default-course-report-template.docx`, cleared stale template body content, generated DOCX successfully, passed DOCX QA with stale terms such as `XXXX`, `图3-1`, and `宋体，小四号`, and exported PDF through Word COM.

On 2026-06-12, PDF render review was regression-tested from a real course-report PDF in `X:\PROJECT\DOCX-COURSE-SKILLS\TEST7`. The first implementation rendered 11 page PNGs and 3 four-page review sheets but allowed an accidental near-blank second page to be missed during manual sheet inspection. The script was then hardened with per-page ink-ratio blank-page detection, `BLANK_PAGE` output, nonzero default exit on near-blank pages, page labels, and red borders for near-blank sheet cells.

## Historical Issues Covered

- AI image text hallucination or unrelated labels.
- Stale final score claims such as `100%` after user-approved values changed.
- TikZ/diagram arrows needing final Review And Revise.
- DOCX conversion requiring real Word heading styles and automatic TOC fields.
- Visual QA needing rendered PDF/page inspection.
- Four-page PDF review sheets for faster post-export layout inspection.
- Near-blank page detection so a non-empty contact sheet cannot hide an empty quadrant.
- Windows Chinese-path and PowerShell encoding hazards.
- Accidental blank first page before TOC when no cover/template opening is preserved.
- Body page numbering accidentally counting cover/TOC front matter; the body must start in a new section with page numbering restarted at 1.

## Commands Run

```powershell
python -m py_compile scripts\build_report.py scripts\qa_docx_report.py scripts\annotate_screenshot.py
```

```powershell
python scripts\build_report.py `
  --draft artifacts\docx-course-report-writer-release-audit\sample-report\report-draft.md `
  --refs artifacts\docx-course-report-writer-release-audit\sample-report\references.md `
  --output artifacts\docx-course-report-writer-release-audit\sample-report\docx-course-report-writer-sample.docx `
  --root artifacts\docx-course-report-writer-release-audit\sample-report
```

```powershell
python scripts\qa_docx_report.py `
  --docx artifacts\docx-course-report-writer-release-audit\sample-report\docx-course-report-writer-sample.docx `
  --require-toc `
  --require-body-page-start-1 `
  --min-images 1 `
  --min-tables 2 `
  --min-heading1 1 `
  --stale-term '100%' `
  --stale-term '100.0%' `
  --stale-term '100.00%' `
  --json
```

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File scripts\update_word_fields.ps1 `
  -DocxPath <sample.docx> `
  -ExportPdf `
  -PdfOutPath <sample.pdf> `
  -UseAsciiTemp
```

```powershell
pdftoppm -png -r 140 sample-report.pdf rendered-pages\page
```

## Verified Results

DOCX package QA:

```json
{
  "paragraphs": 20,
  "tables": 2,
  "inline_shapes": 1,
  "heading_counts": {
    "Heading 1": 1,
    "Heading 2": 5
  },
  "toc_field": true,
  "placeholder_hits": {},
  "stale_hits": {},
  "failures": [],
  "status": "PASS"
}
```

PDF/rendered-page QA:

```json
{
  "pdf_exists": true,
  "pdf_bytes": 276893,
  "rendered_pages": 3,
  "page1_nonwhite_ratio": 0.008184546545891083,
  "page1_not_blank": true,
  "pages": 3,
  "final_score_in_pdf": true,
  "control_score_in_pdf": true,
  "forbidden_accuracy_100": false,
  "placeholder_residue": false
}
```

Release-package re-run from `examples/sample-report/`:

```json
{
  "docx_status": "PASS",
  "pdf_exists": true,
  "pdf_bytes": 276893,
  "pages": 3,
  "final_score_in_pdf": true,
  "control_score_in_pdf": true,
  "forbidden_accuracy_100": false,
  "placeholder_residue": false,
  "rendered_pages": 3,
  "page1_nonwhite_ratio": 0.008924478882462075,
  "page1_not_blank": true
}
```

## Fixes Made During Testing

- `scripts/build_report.py` no longer inserts an unconditional page break before TOC. A pre-TOC page break is now inserted only when a template cover/opening is preserved.
- `scripts/build_report.py` now starts the body in a new section after the TOC and restarts body page numbering at 1, so cover and TOC pages are not counted as body pages.
- `scripts/qa_docx_report.py` now supports `--require-body-page-start-1` to block DOCX outputs where the first body page is not page 1.
- `scripts/build_report.py` now uses `skill-assets/default-course-report-template.docx` when no user template is supplied, while clearing stale template body content by default.
- `scripts/build_report.py` now creates missing `Heading 1/2/3` paragraph styles when a DOCX template does not contain them, preserving automatic TOC compatibility.
- `references/report-qa-checklist.md` now includes a first-rendered-page blank check.
- `references/failure-patterns.md` now includes the accidental blank first page failure pattern.
- TikZ/diagram QA was tightened with strict arrow and text-layout rejection criteria.

## Known Notes

- `pdftoppm` emitted `Syntax Error: No display font for 'ArialUnicode'`, but rendered page inspection and PDF text checks passed for the sample artifact.
- `pypdf` did not reliably extract the Chinese TOC title from the PDF text, so the TOC was verified through DOCX XML and rendered-page inspection.
