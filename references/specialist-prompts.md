# Specialist briefs

Use only for selected tasks under [multi-agent-workflow.md](multi-agent-workflow.md). Apply that file's disclosed/selected model settings and caps; these prompts do not create extra workers or review rounds. Substitute real paths and requirements before dispatch.

## Task worker

```text
Complete this bounded part of the report: <deliverable>.
User requirements: <only relevant constraints and explicit choices>.
Read: <assignment/evidence/template/source paths and specific sections>.
Write only: <owned paths, or read-only>. Do not edit shared final report files.
Use verified evidence: <claim/source pointers and known uncertainty>.
Completion check: <observable result>.
Do not delegate further. Do not run unrelated experiments or fetch sources already verified unless the assigned claim requires it.
Return artifact paths, a concise result with evidence locators, verification performed and unresolved blockers. Keep raw logs and long content in files.
```

Select only the applicable task detail:

| Task | Additional instructions |
|---|---|
| Materials/source analysis | Map mandatory assignment requirements to sections/evidence/checks. Preserve template metadata and identify stale content. Check source passages supporting key claims, not just metadata. |
| Runtime evidence | Use the intended OS/runtime; macOS is not proof of Linux behavior. Preserve real commands/logs/data. Missing prerequisites remain blockers; do not invent outcomes or perform unapproved system setup. |
| Figure/evidence preparation | Use the selected figure route and confirmed facts. A screenshot must be an actual application capture. Preserve originals/provenance; verify labels, arrows and insertion-size readability. Honor the user's AI/PPT choices. |
| Assigned drafting | Write only the owned section using confirmed claims and the shared terminology. Explain what the evidence supports and its limits; no filler or unsupported comparisons. Main agent integrates the argument and citation numbering. |
| Format/build preparation | Operate only on the assigned source/copy. DOCX needs the available office field/export route; LaTeX/Typst need their selected compiler. Report actual output, commands and limitations; do not infer target-app fidelity. |

## Independent reviewer

```text
Review this completed report against its assignment and primary evidence. Read only; do not modify files or spawn workers.
Inputs: <assignment, requirement map, claim evidence, sources, actual artifact/page paths, check results, build ID/hash>.
Check required coverage, whether key claims match their sources/conditions, numerical calculations/units, argument consistency and rendered-page defects.
Inspect actual artifacts. Writer summaries and model agreement are not evidence. Word-specific fields/OOXML checks apply only to DOCX; native formats use compiler/reference/page checks.
Return the reviewed build ID/hash, scope and PASS / NEEDS_FIXES / UNVERIFIED.
For each blocker give its location, evidence, impact and minimum fix. Prioritize major issues; list optional style suggestions separately.
List every required check you could not perform. On a repair follow-up, recheck changed claims/pages and downstream effects against the new artifact version; do not restart a full review without a specific reason.
```
