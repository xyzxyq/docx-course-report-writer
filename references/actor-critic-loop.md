# Actor-Critic Loop

Use this loop for every use of `docx-course-report-writer`, including report creation, conversion, repair, polishing, figure updates, packaging notes, and "small" DOCX edits.

## Mandatory Agent Setup

Before creating report roles, invoke applicable Superpowers skills when installed. For repair/debug work, use `superpowers:systematic-debugging`; for planned execution, use `superpowers:subagent-driven-development` or `superpowers:executing-plans`; before delivery, use `superpowers:verification-before-completion`.

Create/activate exactly these two baseline agents or agent roles before work starts:

- **Actor**: builds or repairs the report artifact.
- **Critic**: independently audits the actual artifact and blocks delivery when defects remain.

If real subagent tooling is available and permitted, create two separate agents. If it is not available, run two explicitly separated local roles with separate notes, but still preserve the Actor/Critic boundary: the Critic must not merely summarize what the Actor intended.

## Actor Pass

The Actor builds or repairs the artifact:

1. Read assignment, template/prior report, source files, available evidence, and user constraints.
2. For reported defects, inspect the actual DOCX/PDF/source/log/figure first and identify the root cause before changing files.
3. Lock report archetype, chapter structure, metadata, naming, citation style, and final deliverables.
4. If citations are used, build the `Reference Metadata Ledger` before drafting: verify each source's authors, title, venue/source, year, pages, DOI or canonical URL, GB/T 7714-2015 type marker, and intended citation number.
5. Decide what evidence must be visible inside the report.
6. Make missing runtime evidence real before writing final result claims.
7. Draft source files and assemble DOCX.
8. Insert required tables, code snippets, screenshots, diagrams, captions, and attributions.
9. Update TOC/fields when Word is available.
10. Export PDF or render pages for visual QA.

## Critic Pass

The Critic evaluates the actual artifact, not the plan:

- assignment coverage and success criteria
- cover metadata and final file naming
- stale template/topic residue
- evidence authenticity and visibility
- screenshot identity and annotation quality
- content depth, design explanation, testing analysis, and reflection
- reference hallucination: every citation maps to a verified ledger entry; no invented DOI, title, author, venue, page, date, publisher, or URL
- GB/T 7714-2015 citation and bibliography compliance
- superscript bracketed numeric citations in the body, including `[1]`, `[2-3]`, and `[1,3]`
- reference list typography, including bracketed sequence number, reference information font/size, hanging indent, and order by first citation appearance
- figure roles, captions, attribution, and readability
- table and code-block layout
- TOC, fields, page numbers, and PDF/page-render state

Critic output should list blocking issues first, then small polish items. It should include exact sections, pages, files, or search terms when possible.

## Iteration Policy

- Run at least **two complete Actor -> Critic cycles** for every skill use before delivery.
- There is **no maximum** iteration count.
- The second cycle is mandatory even when the first Critic pass is clean; it catches regressions introduced by field updates, PDF export, figure replacement, source-script reruns, and late content edits.
- After the second cycle, continue iterating while any blocking issue remains.
- Stop only when the minimum two cycles are complete, required content and evidence are present, final DOCX/PDF exist when required, and the Critic reports no blocking defects or only explicitly documented acceptable limitations.
- Do not replace the second cycle with a checklist, a final answer summary, or "I inspected it mentally." It must include an actual Critic audit of the current artifact.

## Iteration Record

Keep a compact record in notes, plan, or final summary:

- Cycle 1 Actor changes
- Cycle 1 Critic blocking findings
- Cycle 2 Actor changes
- Cycle 2 Critic blocking findings
- Extra cycles if needed

For short edits, the record may be brief, but the two-cycle loop still runs.

## Common Blocking Findings

- required evidence missing or not visible in the report
- reference hallucination or unverified reference metadata
- citations not formatted as superscript bracketed numeric citations
- final references not in GB/T 7714-2015 order, punctuation, type-marker, DOI/URL, or reference list typography
- fake or mislabeled screenshot evidence
- AI image used as experimental proof
- static TOC pretending to be automatic
- old report topic, old screenshot, old TOC entry, or placeholder residue
- unreadable screenshot, table, diagram, or code block
- PDF visual QA shows clipped text, broken page flow, missing images, or isolated captions
- defect repair skipped root-cause investigation and patched only the final artifact
