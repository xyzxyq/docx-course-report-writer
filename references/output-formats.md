# Output Formats And Current Tool Boundaries

Choose the user's output format through `intake-and-run-record.md`, then inspect its template and runtime. A choice is not proof that the host can finalize that format.

## Current capabilities

- DOCX: existing `build_report.py` generates from its Markdown subset and the supplied/default Word template. `qa_docx_report.py` checks the DOCX package. Field updates and page layout require a verified office-software route; Windows COM exists, macOS can export via available Word/WPS or LibreOffice; verify the chosen renderer's output.
- LaTeX: `route_report_output.py` compiles an existing `.tex` project with latexmk and an explicit engine (default XeLaTeX). Start new reports from `skill-assets/latex/`; it does not convert Markdown into LaTeX.
- Typst: the router compiles an existing `.typ` project. Start new reports from `skill-assets/typst/`; it does not convert Markdown or automatically adapt an arbitrary Word template.
- No Quarto/Pandoc migration is required: the existing DOCX builder and native compilers cover these three authoring routes. This is not a claim that a comparative benchmark was completed.

For native formats the main agent must author or edit the appropriate native source/template first. If a supplied template requires unsupported tooling, use its verified build instructions and record that route; never silently switch LaTeX engines. Keep `.tex`/`.typ`, bibliography, template dependencies and assets in the delivered project.

## Probe only the selected route

Use the Python interpreter that contains the report dependencies (python-docx, Pillow, and a PDF renderer such as pypdfium2). Do not assume `python` and `python3` resolve to the same environment.

```sh
python scripts/check_environment.py --format docx --require docx --json
python scripts/check_environment.py --format latex --require latex --json
python scripts/check_environment.py --format typst --require typst --json
```

A probe confirms imports/command responsiveness only. It does not verify fonts, bibliography packages, Word automation, Linux/WSL distribution readiness or end-to-end rendering. The LaTeX probe describes the default latexmk/XeLaTeX path; custom engines need their own check.

## Start a native report

Copy `skill-assets/latex/` or `skill-assets/typst/` into a new report project; edit `main.tex` / `main.typ` and `references.bib`. See `native-templates.md` for cover fields, fonts and template mapping. Preserve existing projects instead of overwriting them.

## Native project compilation

```sh
python scripts/route_report_output.py --format latex --source reports/main.tex --project-root reports --output output/report.pdf
python scripts/route_report_output.py --format typst --source reports/main.typ --project-root reports --output output/report.pdf
```

- `--format` is required; missing format is an error, never an implicit DOCX choice. The legacy DOCX-only builder retains its original interface.
- `--project-root` defaults to the source file's parent. Set it to include required sibling assets/templates; relative paths keep their project structure. Keep outputs outside the source subtree where possible.
- `--latex-engine xelatex|lualatex|pdflatex` is explicit, default `xelatex`; there is no silent fallback to a different engine. All LaTeX routes require latexmk.
- `--timeout` is a positive number of seconds, default 300.
- `--output` must have the correct extension: `.pdf` for native formats, `.docx` for DOCX. It is not silently renamed.
- Existing output files require `--force`. Builds happen in a fresh temporary workspace; failed builds preserve previous output. No pre-existing source-named output folder is deleted.
- Successful native builds retain a unique `<output-stem>-sources-*` snapshot and its sibling `.log` compiler transcript beside the PDF. Deliver this with any required environment/build instructions; its presence alone does not prove reproducibility on another host.
- The selected output directory (when nested below the source root), prior same-output snapshots, `.git`, `__pycache__` and `._*` are excluded. Keep input files out of the output directory. Symlinks are rejected; provide a self-contained project instead.
- Compilation must create a fresh PDF. Success means compiled, not reviewed. Font, reference, semantic and page checks still follow.

The existing DOCX CLI remains available with all its original template flags. The new router offers a common subset; do not assume it supports every legacy option. DOCX router output remains pending office field/layout verification until the office export is checked.

## Optional editable PPT figures

When the user chooses AI-figure reconstruction, read `ppt-figure-reconstruction.md`. Preserve native editable PPTX plus exported PDF. The DOCX builder accepts single-page PDF and self-contained static SVG figure paths with the optional PyMuPDF dependency; it embeds SVG plus a PNG compatibility preview. Keep those paths in the authoritative draft. Verify the actual report export because a client may use the preview. Do not claim object-level Word editing or vector preservation from the PDF extension alone.

## Authoritative source and experiment results

Record the authoritative source: native project, DOCX draft/template, or a selected publication tool's source. Fix that source and rebuild. Never patch a generated `.typ`/`.tex` and later overwrite it from unchanged Markdown.

Run long experiments independently and save data/logs. Rebuilding a report for layout changes reads saved results and must not relaunch training. Missing inputs are blockers, not grounds to invent results.

## Final checks

- DOCX: template fidelity, styles/fields, actual field update/export and page review; if unavailable, state pending finalization.
- LaTeX/Typst: compiler log, unresolved citations/labels, missing glyphs, source/assets, clean rebuild, and PDF pages.
- All: validated facts/references, no placeholders, readable diagrams, per-page review using `render_pdf_review_pages.py`, one final-build review under `multi-agent-workflow.md`, then user-review reminder. Use SKILL.md's shared maximum of two repair rounds.

Word-specific rules apply only to DOCX. There is no mandatory TikZ figure count. Native formats use native template mechanisms and do not require Word or the integrated DOCX cover.

## macOS DOCX finalization

Python generation and package QA do not require PowerShell. With LibreOffice already installed, use its executable (commonly `/Applications/LibreOffice.app/Contents/MacOS/soffice`, or `soffice` on PATH):

```sh
soffice --headless --convert-to pdf --outdir output/pdf output/report.docx
python scripts/render_pdf_review_pages.py --pdf output/pdf/report.pdf --out-dir output/review
```

Use a new output directory so a stale PDF cannot be mistaken for this export; inspect the exit status, fresh PDF, TOC and page numbers. This exports a PDF but does **not** establish that cached fields inside the delivered DOCX were updated. For a final editable Word/WPS document, update/save its fields in that application and validate there. A LibreOffice-rendered PDF proves only LibreOffice appearance. Windows Word uses `update_word_fields.ps1`; do not run COM on macOS. A missing office application leaves DOCX field/layout finalization pending, while native PDF routes remain independent of Office.
