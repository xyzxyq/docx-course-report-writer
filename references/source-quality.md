# Source Quality

## References

Prefer this order:

1. Official instructions or institutional pages for assignment context
2. Foundational references for stable facts
3. Recent authoritative papers for updated interpretation
4. Publicly accessible figure sources with traceable provenance

## Reference Metadata Lock

No report drafting may start until every intended citation has a verified `Reference Metadata Ledger` entry. GB/T 7714-2015 is the default citation standard for course reports unless the assignment or user template explicitly requires another standard.

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

Drafting and QA rules:

- Use sequential numeric GB/T 7714-2015 style by default.
- In-text citations must be superscript bracketed numeric citations like `[1]`, `[2-3]`, or `[1,3]`.
- The final reference list must be ordered by first citation appearance.
- The final reference list must use GB/T 7714-2015 punctuation, item order, reference type marker, DOI/URL placement, and template-consistent reference typography.
- Citation padding is a defect: cite only sources that support a specific sentence, claim, figure, method, or interpretation.

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
