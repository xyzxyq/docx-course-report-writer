# Bounded multi-agent report workflow

Read for the first-use settings notice and whenever report delegation is useful. The main agent owns the argument, integrated source and final delivery. Follow host capabilities and higher-priority restrictions; this policy does not grant new external-action permissions.

## Defaults and first-use disclosure

These are starting settings, not a measured optimum or a promise of better accuracy/speed. Check the current host's model identifiers, supported reasoning efforts, ability to select them and available worker slots before dispatch.

| Role | Default model | Reasoning effort |
|---|---|---|
| Evidence/materials or bounded artifact task | `gpt-6.1-sol` | `medium` |
| Independent final reviewer | `gpt-6.1-sol` | `high` |

Default cap: **2 active subagents**, also bounded by the host's available capacity. This does not count the main agent and is a ceiling, not a target. It does not change the main agent's model or effort. Users may change any role's model/effort, lower concurrency, or disable subagents.

On the first report task without a reusable setting/disclosure record, combine the following notice with existing intake, substituting verified settings:

> 本 skill 对需要调研、实验或综合分析的报告，默认按需使用 subagent。资料与专项任务默认使用 gpt-6.1-sol / medium，独立终审使用 gpt-6.1-sol / high，最多同时运行 2 个。你可以调整模型、思考强度或关闭协作；小改动由主智能体直接处理。

If a role will not run, say so. A model/effort list is only capability evidence, not a comparative quality benchmark. A short optional “沿用默认 / 自定义 / 关闭协作” choice may accompany intake; a separate approval question is unnecessary when the host permits this skill's delegation. This is a disclosed default, not an explicit user answer. An unanswered required format/AI question remains unanswered.

Preference order: current explicit instruction → earlier explicit conversation preference → existing project run-record setting → this default. Prefer the existing project report run record (for example `report-run.md`); otherwise keep task notes. Record model/effort per role, concurrency, enabled/disabled, setting source, disclosure state and any actual override. Reuse it instead of asking every report turn. Notes alone do not imply cross-session persistence. Do not edit global account settings or a user's skill installation to store report preferences. Redisclose a changed or unavailable setting before affected dispatch.

## Capability failures

Do not invent a supported model, effort or parameter. If the requested/default model is unavailable, name the unavailable setting and the verified alternatives once; continue independent work locally while an optional replacement choice is pending. Do not silently substitute a cheaper/different model. If the user explicitly requires that setting or an independent review, that requirement remains pending until resolved.

Some hosts allow only inherited settings. State the actual inherited model/effort when exposed; otherwise state that they cannot be verified. Use inheritance only when the user accepts it or a reusable preference already permits it. Without that, keep the work local and disclose the unavailable independent check. A failed launch is not a successful review and does not justify repeated model guessing. Respect an explicit no-subagents choice.

When explicit overrides are supported, send the selected model and effort using the host's real parameters. Prefer a fresh task context (`fork_turns="none"` when supported) with a bounded brief; do not copy the full conversation merely to give a worker its task. Record requested settings separately from observed runtime settings if the host does not report the latter. Never claim runtime confirmation from a requested parameter alone.

## When and what to delegate

Use the main agent alone for short edits, formatting fixes and straightforward work with complete supplied evidence. For a substantial report involving external literature, experiment evidence, multi-section synthesis or complex figures, enable useful specialists and one independent final review when available. This skill authorizes those bounded report subtasks; do not add a second permission gate unless the host or a particular action requires it.

| Work | Parallel with | Dependency / boundary |
|---|---|---|
| Evidence/materials specialist: inspect requirements, verify sources and key claims | Main agent's outline, source organization and template setup | Give distinct questions/source ranges; return source locators, conditions and uncertainty; do not author conclusions ahead of evidence |
| Optional artifact specialist: runtime proof, figure or selected-format build preparation | Evidence retrieval and main-agent work | Only assigned assets/files; use confirmed data and wait for required AI/format choices; no shared final-output writes |
| Independent reviewer: assignment coverage, claims/calculations and rendered artifact | Main agent's packaging or delivery notes | Start after a coherent draft/build and automatic checks; reviewer must not be the author of the reviewed content |

Do not launch every listed role. Default to at most **3 worker tasks total per report request**: evidence, optional artifact, final review. Reuse their results and use focused follow-ups within the shared repair budget. A report request spans all turns devoted to that deliverable; replies, context compaction and repairs do not reset the cap. A user-requested larger project may justify a revised division of work; disclose its scope before expansion. Workers must not spawn further workers.

The main agent remains the single integrator. Independent sections may be drafted in assigned source files, but terminology, figures, reference numbering, repeated material and conclusions must be reconciled before build. Do not concatenate independent essays and call that integration. A final reviewer reads the actual evidence/artifact, not just the writer's reassurance.

## Minimal handoff and ownership

Each task brief gives the deliverable, allowed read/write paths, relevant user requirements and source/evidence pointers, completion check, and applicable model/effort. Use [specialist-prompts.md](specialist-prompts.md) only when a prompt template helps.

- Assign one owner per writable file. Main agent owns the run record, merged bibliography, report source integration and final artifacts. Concurrent office exports or edits of the same PPT/DOCX are not independent work.
- Shared evidence entries identify the claim, raw/source location, observation versus interpretation, conditions and verification status. One worker's confidence or another worker's agreement is not evidence.
- Return concise findings, changed files/artifact paths and unresolved blockers. Keep long logs/data in files; do not paste full documents into every response. Prioritize the top 3–5 issues, without dropping additional mandatory blockers.
- Batch independent reads and searches, reuse verified material, and inspect only references needed for the assigned task. Avoid duplicate literature searches and repeated full-text/style reviews.
- Use event-based completion or bounded waits. Work on independent tasks while waiting. Do not poll unchanged progress or relaunch a live worker because it is slow.

## Review and stopping

Use [actor-critic-loop.md](actor-critic-loop.md). The independent reviewer owns the single full content/page review when assigned; main-agent integration and final sign-off do not require another duplicate full review. On a small local edit, self-review affected content and downstream changes.

All agents share **at most two repair rounds**. New roles, follow-ups and extra turns cannot reset that budget. Repair at the authoritative source, rebuild once per round and recheck affected claims/pages. An unavailable check is UNVERIFIED, not PASS; report self-review honestly if the independent reviewer cannot run. Do not deliver an artifact changed after its last applicable check.
