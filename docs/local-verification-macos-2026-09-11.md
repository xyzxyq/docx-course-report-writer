> Review note (2026-09-11): this is the previous agent's reported smoke-run record, not a new end-to-end verification. Its old router safety/reproducibility assertions are superseded by [the review](review-and-repair-2026-09-11.md). No Quarto/Pandoc comparison, Windows validation or macOS Word finalization is established here.

# Local Verification: macOS DOCX / LaTeX / Typst (2026-09-11)

Date: 2026-09-11
Host: zxydeMacBook-Air.local

## Environment check

- python scripts/check_environment.py --json --summary
  - DOCX: true (python-docx importable)
  - LaTeX: true (latexmk/xelatex/pdflatex available)
  - Typst: true (typst 0.15.1)

## DOCX route validation

Executed:

```bash
python scripts/route_report_output.py --format docx \
  --draft examples/sample-report/report-draft.md \
  --refs examples/sample-report/references.md \
  --root examples/sample-report \
  --output /tmp/docx-course-report-writer-verify/doc-output.docx
```

Result: exit code 0, /tmp/docx-course-report-writer-verify/doc-output.docx generated.

Notes:

- Initial run had a bad --root path case; final run used the sample root explicitly and passed.
- This verifies DOCX route execution only; final DOCX field/page fidelity pass is still separate.

## LaTeX route validation

Executed:

```bash
tmp=$(mktemp -d)
cat > "$tmp/minimal.tex" <<'EOF'
\documentclass{article}
\usepackage{fontspec}
\setmainfont{Times New Roman}
\begin{document}
\section{verification}
本地验证文档。
\end{document}
EOF
python scripts/route_report_output.py --format latex \
  --source "$tmp/minimal.tex" \
  --output "$tmp/final-output.pdf"
```

Result: exit code 0, $tmp/final-output.pdf generated.

Notes:

- Build copied the source parent into the output build root for reproducibility of local single-source projects.
- XeLaTeX reported missing-glyph warnings for Chinese characters under Times New Roman during compilation; this is a font constraint warning, not a route failure.
- Chinese sample docs/tikz-chinese-training-flow-demo.tex fails on this host under XeLaTeX because Microsoft YaHei font is missing.
- Route-level success is valid, but source/template font alignment is still required for Chinese production quality.

## Typst route validation

Executed:

```bash
tmp=$(mktemp -d)
cat > "$tmp/minimal.typ" <<'EOF'
#set page(width: 148mm, height: 210mm)
= verification
a
EOF
python scripts/route_report_output.py --format typst \
  --source "$tmp/minimal.typ" \
  --output "$tmp/typst-output.pdf"
```

Result: exit code 0, $tmp/typst-output.pdf generated.

## Script-level validation

- scripts/route_report_output.py normalizes and enforces --output for LaTeX/Typst routes and keeps --source project artifacts reproducible for the copied build root.
- docs/backend-evaluation.md and docs/platform-support.md now both reference this run.
