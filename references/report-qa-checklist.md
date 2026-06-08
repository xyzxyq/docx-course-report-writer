# Report QA Checklist

Use this checklist on the actual generated DOCX/PDF, not only on the plan.

## Blocking Gates

### Content And Compliance

- Topic matches the assignment.
- Chapter structure matches the requested report type.
- Cover metadata and filename match the assignment or are explicitly pending.
- No old experiment names, old topic words, old screenshots, old TOC entries, `{{...}}`, `[[TOC]]`, or `待补` remain.
- If the task is item-by-item, the report contains visible requirement coverage.
- Run record exists or equivalent notes are present, including scope lock, AI-image permission/count, fact ledger, figure ledger, and final gates.
- Superpowers availability and invoked workflow skills are recorded; if unavailable, the fallback process from `superpowers-adapter.md` was used.
- Actor and Critic agents/roles were created or activated. The loop record exists for at least two complete cycles, has no artificial iteration cap, and the Critic audited the current artifact, not only the plan.
- Latest user-approved fact ledger is reflected in the whole artifact: final scores, dataset sizes, model names, filenames, class names, dates, and "final" claims are not stale.
- Result-heavy reports contain real analysis, not only implementation narrative: plots/tables from real data, interpretation, error causes, limitations, and personal understanding.
- Claims clearly separate direct model outputs, ensemble outputs, OCR/fusion outputs, probe/debug corrections, and official/final submission results.

### Evidence Authenticity

- Required experiment outputs are real outputs, not AI substitutes.
- Real screenshots are actual terminal/application captures when requested.
- Log-rendered images are not described as screenshots.
- Raw logs or raw screenshots are preserved when screenshots are cropped or annotated.
- Code-related reports include implementation-facing evidence such as a responsibility table, snippet, pseudocode, or test matrix.

### Screenshot Annotation

- Red boxes mark the intended evidence region.
- Labels are red text with transparent background unless explicitly requested otherwise.
- Labels are no more than 10 Chinese characters.
- Labels stay inside image bounds.
- Labels and boxes do not obscure proof text.
- If a hand-marked style was requested, boxes have mild deterministic jitter.

### TOC And Fields

- Word heading styles are used for TOC-relevant headings.
- Automatic TOC field is inserted or preserved.
- TOC and fields are updated in Word when available.
- Page numbers and headings remain consistent after the final field update.
- A static hand-typed TOC is not used when an automatic TOC is expected.
- The rendered TOC page was inspected after final export. It must not contain only "please update in Word" placeholder text.
- Later report-script reruns preserve or rebuild the TOC update/export step; fixing the current DOCX by hand is not enough when a generator exists.

### Rendered Visual QA

- PDF or page renders were inspected, not only DOCX XML/text.
- TOC pages render correctly.
- The first rendered page is not accidentally blank. A pre-TOC page break is allowed only when a real cover/template opening is preserved.
- Figure-heavy pages render correctly.
- Table-heavy pages render correctly.
- Code-block pages render correctly.
- No image is missing.
- No table overflows the page.
- No text is clipped.
- No caption is isolated from its figure/table.
- PDF/page text was scanned for obsolete scores, forbidden result claims, LaTeX residue, and stale template phrases.
- If PDF export or page rendering failed, the final response states that limitation instead of implying visual QA passed.
- Fresh completion verification was run after the latest DOCX/PDF regeneration.

## Polish Checks

### Content Quality

- The report includes explanation, analysis, and reflection, not only pasted outputs.
- Method-heavy sections use diagrams, tables, or snippets when prose alone is weak.
- Requirement mapping is easy for a reviewer to scan.
- Error handling or abnormal cases are discussed when relevant.

### References

- Every citation maps to a real source.
- Citation style is consistent.
- Central claims are backed by actual reading, not abstract-level padding.
- Recent sources are used when the topic requires current information.

### Figures And Tables

- Every figure has a caption.
- Every figure has a source line or attribution record.
- Every figure has a clear role: `evidence`, `explanatory`, or `concept-enhancement`.
- Image sizes are visually balanced.
- Tables fit the page and remain readable.
- Figure labels are readable at final PDF size.
- Captions and source lines remain close to the figure/table they describe.
- TikZ/self-drawn arrows are visible, point to the intended node/region, avoid unnecessary crossings, and remain readable after DOCX/PDF scaling.
- Flowcharts, pipelines, architecture diagrams, timelines, and mechanism figures completed a Review And Revise pass after rendering.
- Arrow audit passed: no hidden arrowheads, wrong targets, ambiguous direction, cramped spacing, or overlaps with modules/text that reduce readability or visual quality.
- Text-layout audit passed for every TikZ/self-drawn/process diagram: no label touches or overlaps box borders, arrows, arrowheads, legends, captions, other labels, or important evidence.
- Diagram density is acceptable: if two source-level revisions cannot remove crossings, overlaps, or cramped labels, the diagram was split or rebuilt in a simpler layout.
- The figure ledger records arrow audit status for every TikZ/self-drawn/process diagram used in the report.
- The figure ledger records text-layout audit status for every TikZ/self-drawn/process diagram used in the report.
- AI-generated figures have a pre-generation drawing spec and post-generation text check. Reject figures with unrelated names, fake logos, wrong numbers, or hallucinated labels.
- If AI-generated figures are used, the report plan/source notes record the user's opt-in and maximum count. Default maximum is 3 when enabled without a count.
- External screenshots show the intended source content. 403/CAPTCHA/login/error pages are replaced with verifiable metadata cards or source tables.

### Deliverables

- Final DOCX exists.
- PDF exists if required or useful for QA.
- Source draft exists when a source-first workflow was used.
- References file exists when citations were used.
- Image attribution file exists when figures were inserted.
- Optional QA intermediates are kept only when useful.
- For submission folders, README and directory structure describe the actual files present, and unnecessary build/cache/training-data artifacts are excluded unless required for reproducibility.
