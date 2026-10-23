---
name: docx-course-report-writer
description: Create, revise, or verify Chinese course reports, lab reports, course papers and literature reviews in DOCX, LaTeX or Typst, using templates, verified evidence and rendered-page checks.
---

# Course Report Writer — DOCX / LaTeX / Typst

## Check available companion skills

Before task execution, consider whether an installed, available skill would materially improve this report. Inspect the host's skill catalog/descriptions once; read only selected skills and their task-relevant references, not every installed skill. For example, use `nature-academic-search` for literature retrieval/citation verification, `nature-writing` for drafting, `nature-polishing` for existing prose, and `nature-image2ppt` for requested editable figure reconstruction when available and suitable. These are examples, not required dependencies or a mandatory chain. Preserve course requirements, language, facts and evidence boundaries; a Nature-related skill does not imply a Nature-journal writing style. Reuse the selection during the task; do not install missing skills or add review loops just for discovery. Briefly state which selected skill serves which purpose.

## Start and select format

For report creation or editing, **ask which output format: DOCX, LaTeX or Typst, unless the user explicitly specified it**. Ask before drafting or building; do not infer a choice solely from an attached template or silently default to DOCX. When asking, explain both advantages and limitations: DOCX is familiar and fits Word/WPS school templates but layout/fields can vary by office application; LaTeX handles equations/references and stable PDF typesetting well but needs syntax/compiler knowledge; Typst offers concise source and convenient typesetting but its template ecosystem and Word/LaTeX compatibility are more limited. LaTeX/Typst delivery includes editable source plus PDF. If requirements conflict, resolve the conflict first. Repository maintenance and analysis-only requests do not trigger report intake.

Use the host's available question tool, or a short text question. Ask only missing information, together: output format, essential assignment/cover information, and whether AI illustrations are wanted. If enabled, ask the insertion count and whether to reconstruct the AI illustrations as editable PPT objects, export PDF, and insert them into the report. Explain the extra reconstruction work and distinguish editable PPT source from vector preservation in the final report. If AI is disabled, skip both follow-ups. Reuse explicit answers. Preselection and silence are not answers. Read [intake-and-run-record.md](references/intake-and-run-record.md) only if an intake/record template is useful.

On first report use, also disclose the subagent models, reasoning efforts and concurrency cap from [multi-agent-workflow.md](references/multi-agent-workflow.md), after checking the host's actual capabilities. Offer adjustment or disabling, reuse explicit preferences, and distinguish a disclosed default from a user-selected setting. This notice does not add a mandatory approval round. Save the choice in the existing project run record; do not modify global model settings. Small edits stay local; substantial reports use bounded delegation when available and permitted.

## Default workflow and stopping rule

1. Inspect the assignment, supplied template, evidence and existing source. Map mandatory requirements to sections, evidence and acceptance checks in the run record. Identify authoritative files and selected-format dependencies; check these before expensive figure work. Reuse saved experiment data; layout edits must not restart experiments.
2. Write around the assignment's questions and grading criteria: each substantive section needs a supported point, analysis and any relevant limitation. Allocate length by importance, not equal section sizes; remove repeated introductions and unsupported padding. Main-agent integration owns terminology, numerical consistency and the argument. Build once using [output-formats.md](references/output-formats.md), with the matching default or supplied template. Replace final artifacts only after a successful build.
3. Run relevant automatic checks, then perform one complete content/rendered-page review, delegated to an independent reviewer for substantial reports when enabled. The main agent resolves findings and owns delivery; do not duplicate the full review under multiple roles. On small edits check affected content and downstream pagination, TOC, citation or numbering effects.
4. Fix confirmed defects together at the source and rebuild. **At most two repair rounds per request**, checking only affected requirements/pages plus build success. Stop earlier on a repeated unchanged failure or missing external input. Preserve the latest useful artifact and report unresolved blockers as pending; reaching the limit never means passing QA.
5. Deliver the requested artifact and editable sources/assets, identifying what passed and what remains unverified. Remind the user to check personal information and submission requirements. Do not change a checked artifact without rerunning affected checks.

Delegation follows [multi-agent-workflow.md](references/multi-agent-workflow.md); review follows [actor-critic-loop.md](references/actor-critic-loop.md). Both share the same two-repair budget. No nested delegation, mandatory Superpowers, duplicate plans or role transcripts. If independent review is unavailable, disclose that limitation and perform self-review; do not claim independence. Optional stylistic suggestions do not restart full review.

## Evidence and citations

- Do not invent results, screenshots or reference metadata. Separate observations, interpretations and predictions. Preserve raw logs/data and source identity; keep experiment processes independent of the chat session.
- For cited reports, verify sources and keep a compact **Reference Metadata Ledger** before drafting cited claims: authors, title, source/type, date, DOI or canonical URL, verification source and required bibliographic fields. Reuse verified entries; investigate only missing/changed facts. Do not invent reference metadata. Details: [source-quality.md](references/source-quality.md).
- A valid reference does not prove a claim. Link central numerical, comparative and causal claims to a source passage/table or raw result, including conditions and limits. Recalculate reported derived values, check units/denominators, and qualify conflicting or missing evidence. Share this compact evidence record across workers; model agreement is not independent evidence.
- Unless the assignment specifies otherwise, use **GB/T 7714-2015**, **superscript bracketed numeric citations**, and template-consistent **reference list typography**. Native formats use their citation engines, not manually renumbered prose. Check actual output for unresolved citations and mismatched reference order.
- Real screenshots must show the intended page/window/result; preserve raw captures. Rendered PDF pages are not screenshots. Linux-specific experiments need a verified Linux runtime: WSL on Windows or an existing VM/remote host on macOS; macOS POSIX support alone is insufficient.

## Templates and finalization

| Format | Default asset | Build and validation |
|---|---|---|
| DOCX | `skill-assets/default-course-report-template.docx` | `build_report.py`, `qa_docx_report.py`, office field update/export and page review |
| LaTeX | `skill-assets/latex/main.tex` and `references.bib` | Copy project, author native source, compile with latexmk/XeLaTeX, inspect log and PDF |
| Typst | `skill-assets/typst/main.typ` and `references.bib` | Copy project, author native source, compile with Typst, inspect warnings and PDF |

User templates take precedence. For a user DOCX template, copy first and inspect before replacing identified body/placeholder regions; preserve cover, sections, styles, fields and required media. Read [template-fidelity.md](references/template-fidelity.md) for this case. Never clear the entire template as a shortcut. The native defaults adapt the built-in Word structure; they are not lossless converters for arbitrary Word templates.

Keep the cover on one page, an automatic hierarchical TOC, body page numbering restarted at 1, numbered chapters/sections, and references on a new page. Remove sample content and placeholders before delivery. For DOCX, see [chinese-docx-style.md](references/chinese-docx-style.md); for native templates, see [native-templates.md](references/native-templates.md).

Python commands work on Windows/macOS with the selected environment's interpreter. PowerShell/Word COM is **Windows-only**, not a global prerequisite. On macOS use available Word/WPS UI or LibreOffice for export and inspect the result; never claim Word/WPS fidelity from LibreOffice alone. Read [output-formats.md](references/output-formats.md) for finalization commands and limits; read [windows-word-fields.md](references/windows-word-fields.md) only for Windows Word.

## Figures and quality gate

Use plots for real data, deterministic diagrams for structure and actual captures for screenshot evidence. Figures are included when useful or required, with formal chapter-scoped captions and sidecar provenance. Check arrow direction, text, clipping and readability at insertion size. See [figures-and-diagrams.md](references/figures-and-diagrams.md) only when figures are needed; TikZ is optional.

AI illustrations require explicit enablement/count and a PPT-reconstruction choice, and are non-evidence. Only for AI work, load [ai-image-prompting.md](references/ai-image-prompting.md): knowledge-structure-driven information architecture, named modules and directional relationships; a visible text plan and, for direct raster insertion, readable final text labels in a one-pass text-to-image result. For direct AI-image insertion, faulty labels must be regenerated or replaced by a deterministic diagram; no repeated cosmetic regeneration. If PPT reconstruction is selected, follow [ppt-figure-reconstruction.md](references/ppt-figure-reconstruction.md): use the AI image as a reference, rebuild semantic elements as native objects, export PDF and preserve the editable PPTX. This separate reconstruction route permits correcting/rebuilding text and arrows; it is not prohibited by the direct-image one-pass rule. A raster image placed in PPT/PDF is still raster, and PDF insertion into Word does not guarantee vector preservation or object-level editing. Use available image-generation capabilities under their current instructions, never assume a machine-specific skill path or credential requirement.

Use `scripts/render_pdf_review_pages.py` to render the final PDF pages to PNG and detect blank or near-blank pages. On initial/full builds inspect every rendered page; contact sheets are an index, not the proof. On repairs inspect affected pages and downstream layout changes. A required unavailable check remains pending. For detailed applicable checks, consult [report-qa-checklist.md](references/report-qa-checklist.md); for a recurring known defect, consult [experience-lessons.md](references/experience-lessons.md) as history-derived experience, not an extra workflow.
