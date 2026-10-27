# Report QA Checklist

Use this checklist on the actual generated DOCX/PDF, not only on the plan.

Word-specific fields, styles, template and office-export checks apply only to DOCX. For LaTeX/Typst use native structure/reference checks and inspect compiled PDF pages. Apply the selected-format rules in `output-formats.md`.

## Gate results

Map mandatory assignment requirements to report locations, supporting evidence and observable checks in the existing run record. Record each applicable gate as **PASS / NEEDS_FIXES / UNVERIFIED**, with the checked build ID/hash. An inapplicable check needs a reason; missing evidence, a failed tool or an uninspected artifact is not a pass. Overall PASS requires all applicable mandatory gates to pass. This is a submission-readiness assessment, not a promise of the teacher's grade.

When measuring this skill's quality or comparing runs, reuse these records: mandatory gates passed / total applicable gates; verified key claims / key claims checked; first-build and first-review pass separately; repair rounds; actual elapsed time and token usage only when available. Keep unknowns in the applicable denominator. Claim coverage is not an accuracy estimate for the whole report, and instruction length is not token usage. Do not impose a benchmark or subjective score on every report. Any claimed improvement needs comparable assignments, evidence, model settings and an explicit baseline.

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
- AI-image intake was answered explicitly; if enabled, count and PPT-reconstruction preference are recorded before figure production. If disabled, those follow-ups are skipped. User silence is not recorded as `off`.
- No extra workflow/plugin is required. First-use subagent settings, any explicit preference and actual task/review status follow `multi-agent-workflow.md`; an unavailable independent check is reported accurately.
- Review the actual artifact once, batch blockers and use at most two focused repair rounds as specified in SKILL.md. Small edits require affected-content and downstream layout checks, not a full unrelated audit.
- Latest user-approved fact ledger is reflected in the whole artifact: final scores, dataset sizes, model names, filenames, class names, dates, and "final" claims are not stale.
- Result-heavy reports contain real analysis, not only implementation narrative: plots/tables from real data, interpretation, error causes, limitations, and personal understanding.
- Claims clearly separate direct model outputs, ensemble outputs, OCR/fusion outputs, probe/debug corrections, and official/final submission results.
- Central numerical, comparative and causal claims match a read source passage/table or raw result, including conditions and limits; valid reference metadata alone is insufficient.
- Derived numbers were recomputed from recorded inputs with units, denominators and relevant uncertainty checked. Percent change and percentage-point change are distinguished.
- Conflicting evidence and unsupported mandatory conclusions are resolved or marked pending; agreement between agents does not establish truth.

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

### TOC And Fields (DOCX only)

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
- On the Windows Word route, Word COM update/export must happen before PDF page rendering unless an explicit limitation is documented.
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
- Body, headings and references have readable separation; an over-dense page fails even without clipping. For Typst, verify actual CJK baseline spacing against the chosen template (default about 17 pt at 10.5 pt body), not just `par.leading` or page count. Compare representative body and reference pages at the same physical size.
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
- Substantive sections answer the assignment's questions with supported analysis; conclusions do not exceed the results. Terminology, figures, numbers and citations agree across sections.
- Section length follows the grading criteria and information needed; repeated introductions, generic filler and concatenated specialist drafts are removed during main-agent integration.

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
- Merged references have no confirmed duplicate identities under different keys; cited versions and any version changes were checked against the supporting evidence under [source-quality.md](source-quality.md).

### Figures And Tables

- Every figure has a caption.
- Every figure has a source line or attribution record.
- Every figure has a clear role: `evidence`, `explanatory`, or `concept-enhancement`.
- Image sizes are visually balanced.
- Tables fit the page and remain readable.
- Figure labels are readable at final PDF size.
- Data plots use meaningful axes/grouping and define sample size and any error intervals; aggregation, significance and visual encoding follow [Data Plot Semantics](figures-and-diagrams.md#data-plot-semantics).
- Captions and source lines remain close to the figure/table they describe.
- TikZ/self-drawn arrows are visible, point to the intended node/region, avoid unnecessary crossings, and remain readable after DOCX/PDF scaling.
- Flowcharts, pipelines, architecture diagrams, timelines, and mechanism figures completed a Review And Revise pass after rendering.
- Arrow audit passed: no hidden arrowheads, wrong targets, ambiguous direction, cramped spacing, or overlaps with modules/text that reduce readability or visual quality.
- Text-layout audit passed for every TikZ/self-drawn/process diagram: no label touches or overlaps box borders, arrows, arrowheads, legends, captions, other labels, or important evidence.
- Diagram density is acceptable: if two source-level revisions cannot remove crossings, overlaps, or cramped labels, the diagram was split or rebuilt in a simpler layout.
- The figure ledger records arrow audit status for every TikZ/self-drawn/process diagram used in the report.
- The figure ledger records text-layout audit status for every TikZ/self-drawn/process diagram used in the report.
- AI-generated figures have a pre-generation drawing spec and post-generation text check. Reject figures with unrelated names, fake logos, wrong numbers, or hallucinated labels.
- If AI-generated figures are used, the report plan/source notes record the user's opt-in and maximum count. If AI images were enabled for a nontrivial creation report, at least one AI-generated conceptual/explanatory figure is inserted unless the assignment or user forbids it.
- Report-visible figures, captions, paragraphs, and tables do not contain production-process claims about source encoding, drawing tools, renderers, image models, prompt mechanics, screenshot scripts, or QA scripts. Keep those details in the run record, figure ledger, or attribution sidecar.
- External screenshots show the intended source content. 403/CAPTCHA/login/error pages are replaced with verifiable metadata cards or source tables.
- Browser screenshots were inspected for wrong page, blank page, loading state, login wall, 403, CAPTCHA, and error pages.
- Terminal screenshots include command/result context and remain readable at final DOCX/PDF scale.

### Optional PPT Figure Reconstruction

Only if selected: confirm editable native PPT objects, exported figure PDF, any residual raster regions, target-app insertion behavior and final report rendering according to `ppt-figure-reconstruction.md`. Preserve PPTX/PDF and insertion SVG when used. Neither a raster image in PPT nor a PDF attachment alone proves a vector, editable report illustration. Reuse the same review/repair budget.

### Deliverables

- Selected output exists: DOCX, or PDF plus the LaTeX/Typst source project.
- Final artifact identity matches the checked build; user is reminded to review.
- For substantial reports, independent review follows the enabled, available settings in `multi-agent-workflow.md`; small edits use self-review. State which actually ran, on which build, and any unavailable checks without duplicating the full review.
- PDF exists if required or useful for QA.
- Source draft exists when a source-first workflow was used.
- References file exists when citations were used.
- Image attribution file exists when figures were inserted.
- Optional QA intermediates are kept only when useful.
- For submission folders, README and directory structure describe the actual files present, and unnecessary build/cache/training-data artifacts are excluded unless required for reproducibility.
