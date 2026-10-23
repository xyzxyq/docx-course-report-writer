# Platform Support Matrix

Updated 2026-10-23. Generation, compilation and office finalization are separate capabilities. See [current verification](verification-2026-10-23.md) for commands and limits.

| Platform | DOCX | LaTeX PDF | Typst PDF |
|---|---|---|---|
| macOS (tested host) | Python generation/package tests pass; LibreOffice PDF export runs, but sample TOC fields remain unupdated; Word/WPS field update/save still required for final DOCX | Built-in six-page template compiled and source snapshot rebuilt; PDF reviewed | Built-in six-page template compiled and source snapshot rebuilt; PDF reviewed |
| Windows | Existing Word COM finalization retained; no real Windows run in this update | Portable XeLaTeX/Fandol route provided; not run on Windows | Native CLI route provided; select installed Windows CJK fonts; not run on Windows |
| Linux/WSL | Python route exists; no execution evidence in this update | Not run in this update | Not run in this update |

- PowerShell/COM applies only to Windows; Python generation and native PDF compilation do not require it.
- Fonts must be present. LaTeX explicitly uses Fandol; Typst defaults use macOS Songti/Heiti and document Windows/Noto alternatives.
- A detected executable/import is not proof of a completed report. `check_environment.py` reports capabilities, not QA verdicts.
- LibreOffice rendering does not prove Word/WPS appearance and may leave TOC fields stale. Inspect and update in the target office application before claiming finalization.
- The native templates adapt the default DOCX structure and normalized styling. Arbitrary school DOCX templates are not converted losslessly.

PDF/SVG figure insertion was additionally exercised on macOS with PyMuPDF 2.0 and LibreOfficeDev 26.8.0.0.alpha0. Both PDF-input and SVG-input DOCX exports retained vector paths with zero raster instances in the one-page Transformer example. This sample has no TOC and does not settle the earlier field-update limitation. Microsoft Word/WPS and Windows exports remain unverified; clients may use the embedded PNG fallback. See the [actual run and artifacts](verification-2026-10-23.md#transformer-vector-figure-end-to-end-run).

[Commands and limits](../references/output-formats.md) · [Template mapping](../references/native-templates.md) · [Earlier September review](review-and-repair-2026-09-11.md)
