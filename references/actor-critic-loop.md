# Bounded review

Perform one complete artifact review, followed by at most two focused repair rounds. Substantial reports use an independent reviewer when delegation is enabled and available; short edits use main-agent self-review. Model settings and first-use disclosure come from [multi-agent-workflow.md](multi-agent-workflow.md), not a second reviewer configuration. Analysis-only and skill maintenance do not automatically create report-review roles.

## Review handoff

After the initial build and automatic checks, give a read-only reviewer the assignment/acceptance requirements, authoritative source, key-claim evidence, verified references, actual artifacts/pages, build ID/hash and check results. Do not lead with the writer's desired verdict. The reviewer must not have authored the reviewed content; a fresh context with relevant source pointers is preferred. If review is unavailable, state that limitation; self-review is not independent review.

Return PASS / NEEDS_FIXES / UNVERIFIED, the reviewed artifact identity, check scope and blocking issues with location, evidence, impact and minimum fix. Optional style suggestions stay separate and do not block delivery. Missing evidence or an unavailable required check cannot be counted as PASS. Use [report-qa-checklist.md](report-qa-checklist.md); Word-specific gates apply only to DOCX.

The reviewer performs the single full content/rendered-page pass. The main agent verifies material findings, reconciles conflicts against primary evidence and owns the delivery decision. Do not repeat the full review merely to change reviewer/model or add a second opinion. User-requested independent checks can expand review scope but do not silently reset the repair budget.

## Repair budget

- Batch confirmed defects into one source edit and rebuild per round; maximum two repair rounds across self-review and independent review.
- Recheck affected claims, calculations, sections/assets and downstream TOC, citations, numbering and page flow. Reuse unaffected evidence; do not reread the entire conversation.
- Stop on pass, exhausted budget, repeated unchanged failure or an external blocker. Remaining defects are pending, never silently accepted. Report a concrete next step instead of restarting the loop under a new role.
- Optional stylistic changes do not trigger another round. Reject incorrect findings with evidence, not with a vote among agents.
- Record artifact identity, check scope, blocking findings, repairs and unresolved items in the existing run record. No separate Actor/Critic transcript is needed.
