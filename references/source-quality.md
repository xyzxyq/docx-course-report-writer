# Source Quality

## References

Prefer this order:

1. Official instructions or institutional pages for assignment context
2. Foundational references for stable facts
3. Recent authoritative papers for updated interpretation
4. Publicly accessible figure sources with traceable provenance

## Reference Metadata Lock

Verify each source in the `Reference Metadata Ledger` before drafting claims that cite it. Reuse verified metadata; update only changed or missing entries. Uncited sections do not need to wait for unrelated reference checks. GB/T 7714-2015 is the default citation standard for course reports unless the assignment or user template explicitly requires another standard.

For each cited source, record:

- citation number and short key
- source role: assignment rule / foundational source / recent literature / dataset / webpage / standard
- GB/T 7714-2015 source category and reference type marker, such as `[J]`, `[M]`, `[C]`, `[D]`, `[R]`, `[S]`, `[P]`, `[EB/OL]`, or another applicable marker
- authors or responsible organization exactly as verified
- title exactly as verified
- venue/source, publisher or official host
- year/date, volume, issue, pages, and update/access date when applicable
- DOI, or if no DOI exists, canonical URL, arXiv/PMLR/official paper page, publisher page, library record, standard record, or institutional metadata page
- metadata verification source and verification date
- intended in-text citation number and sections where it will be used

Verification rules:

- Do not invent authors, titles, venues, years, pages, issue numbers, DOI values, URLs, publishers, or access dates.
- Verify DOI values through the DOI resolver, Crossref, publisher page, official paper page, or another authoritative metadata source before writing the reference list.
- If a DOI is absent or cannot be resolved, record the authoritative substitute source used for the metadata. A missing DOI is acceptable only when the ledger explains why the reference is still valid.
- If a title or author list cannot be verified, do not cite the source. Replace it with a verifiable source or ask the user.
- Treat "paper exists" and "reference metadata is correct" as separate checks.

Identity and version checks when merging or updating references:

- Detect duplicates by normalized DOI or another verified identifier plus bibliographic identity, not citation-key spelling or a similar title alone. Consolidate confirmed duplicates and update citation keys/numbers in the source and rendered reference list together.
- Distinguish preprint versions, accepted manuscripts, final publications and corrections. Prefer the appropriate verified publication for the claim; do not silently swap versions or count them as independent evidence. If changing the cited version, reread the supporting passage/table and retain the actual version in the ledger.
- For online-first articles, use verified article numbers and publication state; absent volume, pages or DOI are not values to invent. Record unavailable/not-applicable fields in the ledger. Reuse an available citation-management tool for metadata work, but its output does not prove claim support.

Drafting and QA rules:

- Use sequential numeric GB/T 7714-2015 style by default.
- In-text citations must be superscript bracketed numeric citations like `[1]`, `[2-3]`, or `[1,3]`.
- The final reference list must be ordered by first citation appearance.
- The final reference list must use GB/T 7714-2015 punctuation, item order, reference type marker, DOI/URL placement, and template-consistent reference typography.
- Citation padding is a defect: cite only sources that support a specific sentence, claim, figure, method, or interpretation.

## Claim support and calculations

Metadata verification and claim support are separate. For central numerical, comparative, causal or conclusion-bearing statements, extend the existing evidence/run record with:

| Claim / section | Source locator | Evidence and conditions | Status / limitation |
|---|---|---|---|
| Precise statement to support | DOI/URL + page, table or section; or raw file + row/field | Observed / computed / literature-reported / interpretation; sample, units and setting | Verified / contradicted / unverified; permitted wording |

Use passage-level reading for these claims. An abstract, title, search snippet or a real DOI alone does not establish support. Check whether a reported result is experimental, simulated or predicted and whether the report's population, baseline and conditions match. Do not generalize a narrow result into an unconditional claim.

For derived percentages, improvements, averages and totals, retain the source values and calculation in the same record. Check units, denominator, sample size, uncertainty when reported, and percent versus percentage points. Prefer a small deterministic calculation over asking another model to agree. Do not rerun expensive experiments to reformat their saved results.

When sources disagree, record the differing conditions and preserve the uncertainty; do not resolve it by majority vote among agents. Unsupported essential claims stay unverified or block the relevant section. Optional unsupported claims can be removed. An unavailable full text limits what can be asserted; it is not permission to invent detail.

Reuse verified source and claim entries across workers. Reopen a source only for a changed claim, a missing locator, a substantive conflict or a time-sensitive update. This is a compact record of important claims, not a transcript of every sentence or search result.

## Recent Literature

- Use recent papers when they support a specific claim, section, or interpretation.
- Prefer reviews or major journal papers when the report needs synthesis.
- Avoid citation padding.

## Figures

For each figure, capture:

- file name
- figure role
- intended caption
- source page title
- source URL
- direct asset URL if available
- attribution or license note
- reason for inclusion

Also capture source type:

- experiment output
- self-drawn
- paper crop
- screenshot
- AI-generated

## AI-Generated Figures

If a figure is AI-generated, additionally record:

- the full prompt card from `references/ai-image-prompting.md`
- prompt summary
- final prompt
- negative prompt / avoid list
- generation method
- why AI was chosen instead of other figure types
- whether the figure is `concept-enhancement` or `explanatory`
- accepted/rejected iteration notes
- original generated file path when the image was copied into the project

Never mark an AI-generated figure as evidence unless the user explicitly wants to document that AI generation itself is the subject of the assignment.

## Screenshots

- Use screenshots for positioning or interface evidence, not as substitutes for all diagrams.
- Crop noisy UI where possible.
- Record the page the screenshot came from.

## Attribution Rule

If a figure is inserted, it must appear in the image attribution file. No exceptions.
