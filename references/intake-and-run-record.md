# Intake And Run Record

Use this file as a compact, copyable record template for every run of `docx-course-report-writer`. The record may live in the working folder as `report-run-record.md`, in source notes, or in the final work log.

## Mandatory Intake

Ask or infer these before writing final deliverables:

- Assignment/report type:
- Required deliverables:
- Template/prior report to preserve:
- Required evidence:
- Runtime environment:
- Screenshot requirements:
- PDF/export requirement:
- Naming/metadata requirements:
- Superpowers installed/available: yes/no
- Superpowers skills invoked:
- AI text-to-image enabled: yes/no
- Maximum AI-generated images to generate/insert: integer; default is 3 when enabled without a count

If the user already gave enough information, record the answer instead of asking again. The AI-image permission and count must still be explicitly recorded.

## Required Run Record

```markdown
# Report Run Record

## Scope Lock
- Report type:
- Deliverables:
- Template/source files:
- Evidence required:
- Runtime/screenshot plan:
- AI text-to-image: off/on
- AI image maximum:
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

## Figure Ledger
| Figure | Role | Method | Source/evidence | Review And Revise status |
|---|---|---|---|---|
|  | evidence/explanatory/concept | screenshot/TikZ/plot/AI |  | arrows checked / text checked / rendered checked |

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
- Template residue:
- Word fields/TOC:
- Fact ledger scan:
- Figure arrow/text review:
- PDF/rendered visual QA:
- Remaining limitations:
```

## Use Rules

- The record must show at least two complete Actor -> Critic cycles.
- The Critic must audit the current artifact, not only the plan.
- If a blocking issue is found, the Actor fixes the source of truth before regeneration.
- If AI-generated images are used, each image must appear in the figure ledger with permission, maximum count, prompt/spec source, text verification, and attribution.
- If TikZ, flowcharts, pipelines, architecture diagrams, timelines, or mechanism diagrams are used, each must show `Review And Revise status` with arrow audit completed after rendering.
