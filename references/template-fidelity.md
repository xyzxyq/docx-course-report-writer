# User-Provided DOCX Template Fidelity

Use this when a user provides a `.docx` template and says to use it, follow it, base the report on it, or write in that template.

## Core Principle

A user-provided template is the source document, not a style hint. The safest path is:

1. Copy the template to the target report path.
2. Inspect and record what must be preserved.
3. Replace placeholders/sample regions inside that copy.
4. Update fields/TOC in Word.
5. Compare final rendered pages against the template contract.

Do not build a blank document and "make it look similar" unless the user explicitly approves that fallback.

## Template Fidelity Contract

Before writing report body content, record:

| Area | What to capture | How to verify |
|---|---|---|
| Cover | exact visible layout, logo/media, field labels, date placement | render template page 1 and final page 1 |
| Page setup | size, margins, section breaks, columns | inspect section properties / PDF render |
| Headers/footers | text, page numbers, lines, logos | inspect OOXML or rendered pages |
| TOC | field/static status, levels, dot leaders, tab stops | Word field update + PDF page |
| Headings | style names, outline levels, fonts, spacing, numbering | style inventory + TOC output |
| Body | normal style, indentation, line spacing | style inventory / sample paragraph |
| Tables | style, borders, fills, alignment | rendered comparison |
| Captions | prefix, numbering, font, alignment | rendered comparison |
| Placeholders | exact text/content controls to replace | text extraction / controls inspection |
| Sample content | body ranges to delete | contract notes before deletion |

Bundled helper:

```powershell
python "$env:CODEX_HOME\skills\docx-course-report-writer\scripts\inspect_template.py" `
  --template template.docx `
  --json-out report/template-fidelity.json `
  --md-out report/template-fidelity.md
```

## Editing Rules

- Prefer direct replacement in the copied template: replace placeholder paragraphs, content controls, table cells, and sample body regions.
- Preserve section properties and style definitions. Do not call a whole-document clear operation until after the contract identifies what structural elements must be retained.
- When using the bundled `scripts/build_report.py`, pass the user template through `--template`; the script now uses copy-first preservation by default for user-provided templates. Use `--drop-template-body` only after the Template Fidelity Contract or the user explicitly says the body may be discarded.
- Use `scripts/qa_docx_report.py --template-fidelity-template template.docx` during final QA. Do not pass `--allow-section-drift` or `--allow-style-loss` unless the fallback is documented and approved.
- If body sample content must be removed, delete only the sample-content range and keep cover, TOC container, headers/footers, page numbering, styles, and section breaks.
- If generating from Markdown, map each Markdown block to an existing Word style from the template instead of creating generic styles.
- If the template has an automatic TOC, keep that TOC field and update it. If it has a static TOC, replace it with an automatic field only when that does not visibly break the template.
- Unknown personal metadata should be handled according to the template: leave the field blank, mark `未提供`, or ask the user if the field is required for submission. Do not leave unrelated sample names.

## Fallback Rules

A fallback away from copy-first editing is allowed only when:

- the template is corrupt or cannot be opened;
- the template uses unsupported constructs that cannot be preserved by available tools;
- the user explicitly says layout fidelity is not important; or
- the user approves the fallback after being told what will be lost.

Record the fallback reason in the run record.

## Critic Checklist

The Critic must inspect the actual final artifact, not only the script:

- final page 1 materially matches the template cover layout;
- page size, margins, headers/footers, and page numbers remain consistent;
- heading and table styles come from the template or intentionally modified contract;
- TOC is updated and visually resembles the template's TOC style;
- no old sample text, stale screenshots, or placeholder instructions remain;
- all inserted figures/tables fit within the template's content width;
- final PDF/page renders were checked around cover, TOC, figure-heavy pages, tables, and references.

Blocking defect: "template was used as a style source only" when the user asked to use the template.
