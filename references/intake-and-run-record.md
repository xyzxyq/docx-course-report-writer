# Intake And Run Record

Use this file as a compact, copyable record template for every run of `docx-course-report-writer`. The record may live in the working folder as `report-run-record.md`, in source notes, or in the final work log.

## Mandatory Intake

Ask or infer these before writing final deliverables:

- Assignment/report type:
- Required deliverables:
- Template/prior report to preserve:
- Template decision: user-provided / integrated default / blank document by explicit request
- Template fidelity mode: copy-first strict / integrated default / user-approved fallback
- Template Fidelity Contract path or notes:
- Required evidence:
- Runtime environment:
- Linux/WSL requirement and availability:
- Screenshot requirements and capture targets:
- PDF/export requirement:
- PDF page render QA requirement:
- Naming/metadata requirements:
- References required: yes/no
- Citation standard: GB/T 7714-2015 unless assignment/template says otherwise
- Reference Metadata Ledger status: not needed / pending / locked before drafting
- GB/T 7714-2015 format source: provided standard file / assignment rule / template rule / default skill rule
- Superpowers installed/available: yes/no
- Superpowers skills invoked:
- AI text-to-image enabled: yes/no, must be answered explicitly before artifact creation unless already specified by the user
- Maximum AI-generated images to generate/insert: integer, must be answered explicitly when AI text-to-image is enabled
- Minimum AI-generated images to insert: 1 for nontrivial creation reports when enabled, unless the assignment or user forbids AI images
- Minimum LaTeX TikZ figures to insert: 1, mandatory unless the user explicitly forbids TikZ or the assignment forbids self-drawn/LaTeX figures

If the user already gave enough information, record the answer instead of asking again. The AI-image permission and count must still be explicitly recorded. Do not treat user silence as `off`, and do not begin report drafting, figure generation, DOCX assembly, or PDF export before this intake is resolved.

## Required Run Record

```markdown
# Report Run Record

## Scope Lock
- Report type:
- Deliverables:
- Template/source files:
- Template decision:
- Template fidelity mode:
- Template Fidelity Contract:
- Evidence required:
- Runtime plan:
- Linux/WSL decision:
- Screenshot plan:
- AI text-to-image: off/on
- AI image maximum:
- AI image minimum:
- TikZ minimum: 1 unless explicitly forbidden
- TikZ minimum gate:
- AI-image intake answer source: user answered / already specified in request
- Superpowers availability:
- Superpowers skills invoked:
- Known limitations:

## Role Activation
- Orchestrator:
- Actor:
- Critic:
- Real subagents used: yes/no
- If no real subagents, local separation method:

## Fact Ledger
| Claim type | Approved value/source | Where used | Verification |
|---|---|---|---|
| score/result |  |  |  |
| dataset/files |  |  |  |
| model/class/name |  |  |  |
| date/version |  |  |  |
| final-vs-intermediate claim |  |  |  |

## Reference Metadata Ledger
No cited prose may be drafted until this ledger is complete for every intended citation.

| Citation no. | GB/T 7714-2015 type marker | Verified authors/organization | Verified title | Venue/source/publisher | Year/volume/issue/pages | Verified DOI or canonical URL | Metadata source checked | Used in section |
|---|---|---|---|---|---|---|---|---|
| [1] |  |  |  |  |  |  |  |  |

- In-text citation style: superscript bracketed numeric citations, e.g. `[1]`, `[2-3]`, `[1,3]`.
- Reference-list style: GB/T 7714-2015 sequential numeric order by first citation appearance.
- Missing metadata decision: do not cite / ask user / replace source.

## Figure Ledger
| Figure | Role | Method | Source/evidence | Review And Revise status |
|---|---|---|---|---|
|  | evidence/explanatory/concept | screenshot/TikZ/plot/AI |  | arrows checked / text-layout checked / rendered checked |

## AI Figure Prompt Cards
Use this section only when AI text-to-image is enabled. Each generated or attempted image must have one card.

```markdown
### AI Figure Prompt Card: <figure id>
- Report section:
- Figure role:
- Reader question answered:
- Why AI was chosen:
- Visual density target:
- Focal subject:
- Foreground / midground / background:
- Composition:
- Lighting/color/material:
- Camera/framing/aspect ratio:
- Allowed visible text:
- One-pass text-to-image plan:
- Text/arrow/legend regeneration triggers:
- Positive prompt:
- Negative prompt / avoid:
- Rejection criteria:
- Accepted/rejected iteration notes:
```

## Actor -> Critic Cycle 1
- Actor changes:
- Critic artifact reviewed:
- Critic blocking findings:
- Fix plan:

## Actor -> Critic Cycle 2
- Actor changes:
- Critic artifact reviewed:
- Critic blocking findings:
- Fix plan:

## Extra Cycles
- Cycle 3+ notes:

## Final Gates
- Superpowers verification/fallback:
- Evidence authenticity:
- Linux/WSL runtime:
- Screenshot authenticity:
- Reference hallucination audit:
- GB/T 7714-2015 citation and bibliography audit:
- In-text citation superscript audit:
- Reference typography audit:
- Template residue:
- User-template fidelity:
- Default-template visible cover/style:
- Word fields/TOC:
- Fact ledger scan:
- Figure arrow/text-layout review:
- PDF/rendered visual QA:
- Every rendered page inspected:
- Blank/near-blank page detection:
- Contact sheets used only as index:
- Failed QA from user feedback:
- Remaining limitations:
```

## Use Rules

- The record must show at least two complete Actor -> Critic cycles.
- The Critic must audit the current artifact, not only the plan.
- If a blocking issue is found, the Actor fixes the source of truth before regeneration.
- If AI-generated images are used, each image must appear in the figure ledger with permission, maximum count, prompt/spec source, text verification, and attribution.
- If Linux/POSIX behavior is required, the record must show host OS check, native Linux/WSL decision, WSL availability or install-permission outcome, distribution/kernel/compiler facts, and exact build/run/test commands.
- If screenshots are required, the record must show capture targets, raw screenshot paths, annotated/cropped paths when used, and whether each screenshot was inspected for wrong-page/error/login/CAPTCHA problems.
- If TikZ, flowcharts, pipelines, architecture diagrams, timelines, or mechanism diagrams are used, each must show `Review And Revise status` with arrow audit and text-layout audit completed after rendering and after DOCX/PDF insertion.
- A nontrivial report with zero TikZ figures fails this gate unless the run record documents the user's explicit TikZ prohibition or an assignment prohibition.
- If no user template is provided, the template decision must record `integrated default: skill-assets/default-course-report-template.docx`.
