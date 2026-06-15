# Report QA Checklist

Use this checklist on the actual generated DOCX/PDF, not only on the plan.

## Blocking Gates

### Content And Compliance

- Topic matches the assignment.
- Chapter structure matches the requested report type.
- Cover metadata and filename match the assignment or are explicitly pending.
- Default-template cover placeholders such as `放置`, `校徽`, `《XXXX》`, and `实验题目` are replaced or removed; the cover must look like a formal course-report cover, not a partially preserved template.
- No old experiment names, old topic words, old screenshots, old TOC entries, `{{...}}`, `[[TOC]]`, `待补`, `待确认`, or mojibake strings such as `鐩綍` remain.
- If the task is item-by-item, the report contains visible requirement coverage.
- Run record exists or equivalent notes are present, including scope lock, AI-image permission/count, fact ledger, figure ledger, and final gates.
- If citations are used, the run record includes a locked `Reference Metadata Ledger` created before drafting, with verified DOI or canonical URL, metadata source, GB/T 7714-2015 type marker, and intended citation number for every cited source.
- AI-image intake was answered explicitly before report drafting/DOCX assembly. User silence is not recorded as `off`.
- Superpowers availability and invoked workflow skills are recorded; if unavailable, the fallback process from `superpowers-adapter.md` was used.
- Actor and Critic agents/roles were created or activated. The loop record exists for at least two complete cycles, has no artificial iteration cap, and the Critic audited the current artifact, not only the plan.
- Latest user-approved fact ledger is reflected in the whole artifact: final scores, dataset sizes, model names, filenames, class names, dates, and "final" claims are not stale.
- Result-heavy reports contain real analysis, not only implementation narrative: plots/tables from real data, interpretation, error causes, limitations, and personal understanding.
- Claims clearly separate direct model outputs, ensemble outputs, OCR/fusion outputs, probe/debug corrections, and official/final submission results.

### Evidence Authenticity

- Required experiment outputs are real outputs, not AI substitutes.
- Linux/POSIX outputs came from native Linux or verified WSL when Linux behavior matters. If no Linux runtime was available, the report records the limitation and user install decision.
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
- Default-template body headings use formal chapter/section text such as `第一章`, `1.1`, and `1.1.1`; a flat set of unnumbered headings is blocking.
- Automatic TOC field is inserted or preserved.
- TOC and fields are updated in Word when available.
- Page numbers and headings remain consistent after the final field update.
- Cover and TOC pages are front matter and are not counted as body pages. They must not display the body `PAGE` field. The body/chapter section starts on a new Word section with page numbering restarted at 1.
- `参考文献` starts on a new page and appears as a TOC-relevant section heading.
- A static hand-typed TOC is not used when an automatic TOC is expected.
- The rendered TOC page was inspected after final export. It must not contain only "please update in Word" placeholder text.
- Later report-script reruns preserve or rebuild the TOC update/export step; fixing the current DOCX by hand is not enough when a generator exists.

### Rendered Visual QA

- PDF or page renders were inspected, not only DOCX XML/text.
- Word COM update/export must happen before PDF page rendering unless an explicit limitation is documented.
- The final PDF pages were rendered to PNG when layout matters.
- Every rendered page PNG was inspected when layout matters; contact sheets are an index, not the proof.
- Blank or near-blank page detection was run for every rendered page; each blank or near-blank page is either fixed or documented as intentional.
- For medium/long reports, review sheets combine four pages per contact sheet and were inspected only as navigation aids.
- PDF page render images are not screenshots and are not described as browser/terminal proof.
- TOC pages render correctly.
- The rendered first visible page number 1 is on the first body/chapter page, not on the cover or TOC page.
- The first rendered page is not accidentally blank. A pre-TOC page break is allowed only when a real cover/template opening is preserved.
- No blank or near-blank page appears anywhere unless the template/assignment explicitly requires it and the run record names the page and reason.
- If no user template was supplied, the rendered report shows the integrated default template's visible cover/style unless the user explicitly requested a blank or no-cover document.
- Figure-heavy pages render correctly.
- Table-heavy pages render correctly.
- Code-block pages render correctly.
- No image is missing.
- No table overflows the page.
- No text is clipped.
- No caption is isolated from its figure/table.
- PDF/page text was scanned for obsolete scores, forbidden result claims, LaTeX residue, and stale template phrases.
- Reference pages were inspected in DOCX/PDF render for GB/T 7714-2015 punctuation/order, hanging indent, bracketed sequence numbers, and reference list typography.
- Body pages were inspected for superscript bracketed numeric citations; plain body-sized `[1]` citations are blocking.
- If PDF export or page rendering failed, the final response states that limitation instead of implying visual QA passed.
- Fresh completion verification was run after the latest DOCX/PDF regeneration.
- User feedback after delivery was converted into a failed QA test, fixed at the source of truth, regenerated, and rechecked.

## Polish Checks

### Content Quality

- The report includes explanation, analysis, and reflection, not only pasted outputs.
- Method-heavy sections use diagrams, tables, or snippets when prose alone is weak.
- Requirement mapping is easy for a reviewer to scan.
- Error handling or abnormal cases are discussed when relevant.

### References

- Every citation maps to a real source and verified `Reference Metadata Ledger` entry.
- No reference hallucination is present: no invented DOI, URL, title, author, year, pages, venue, publisher, or access date.
- Citation style is GB/T 7714-2015 unless the assignment/template explicitly requires another style.
- In-text citations use superscript bracketed numeric citations such as `[1]`, `[2-3]`, and `[1,3]`.
- Final references are ordered by first citation appearance under sequential numeric GB/T 7714-2015 rules.
- The reference list uses GB/T 7714-2015 item order, punctuation, reference type marker, DOI/URL treatment, and required access dates for online sources.
- The reference list typography is checked: sequence number font/size, reference information font/size, line spacing, and hanging indent match the template or the skill default.
- Every reference-list entry is cited in the body, unless the report explicitly separates "reading references" and records why uncited entries remain.
- Every in-text citation has a corresponding reference-list entry; dangling citation numbers are blocking.
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
- TikZ minimum gate: nontrivial report creation includes at least one LaTeX TikZ figure unless the user explicitly forbids TikZ or the assignment forbids self-drawn/LaTeX figures.
- A nontrivial report with zero TikZ figures fails this gate; AI figures, screenshots, paper crops, and Python plots do not satisfy the required TikZ minimum.
- AI-generated figures have a pre-generation drawing spec and post-generation text check. Reject figures with unrelated names, fake logos, wrong numbers, or hallucinated labels.
- If AI-generated figures are used, the report plan/source notes record the user's opt-in and maximum count. If AI images were enabled for a nontrivial creation report, at least one AI-generated conceptual/explanatory figure is inserted unless the assignment or user forbids it.
- Report-visible figures, captions, paragraphs, and tables do not contain production-process claims about source encoding, drawing tools, renderers, image models, prompt mechanics, screenshot scripts, or QA scripts. Keep those details in the run record, figure ledger, or attribution sidecar.
- External screenshots show the intended source content. 403/CAPTCHA/login/error pages are replaced with verifiable metadata cards or source tables.
- Browser screenshots were inspected for wrong page, blank page, loading state, login wall, 403, CAPTCHA, and error pages.
- Terminal screenshots include command/result context and remain readable at final DOCX/PDF scale.

### Deliverables

- Final DOCX exists.
- PDF exists if required or useful for QA.
- Source draft exists when a source-first workflow was used.
- References file exists when citations were used.
- Image attribution file exists when figures were inserted.
- Optional QA intermediates are kept only when useful.
- For submission folders, README and directory structure describe the actual files present, and unnecessary build/cache/training-data artifacts are excluded unless required for reproducibility.
