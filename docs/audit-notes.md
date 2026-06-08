# DOCX Course Report Writer Release Audit Notes

## Scope

This audit tests and packages `C:\Users\20795\.codex\skills\docx-course-report-writer`.

## Skill Rules Under Test

- Superpowers invocation when installed.
- Mandatory Actor/Critic roles and at least two full Actor -> Critic cycles.
- Mandatory AI-image opt-in/count intake; default maximum 3.
- Source-first evidence and fact ledger.
- Figure ledger with Review And Revise / arrow audit.
- Automatic Word TOC field and real heading styles.
- Placeholder/stale-template scan.
- DOCX package inspection and PDF/rendered visual QA when available.

## Actor/Critic Run Record For This Audit

### Scope Lock

- Report type: synthetic Chinese course report fixture.
- Deliverables: sample source files, sample DOCX, QA JSON/text logs, historical failure summary, release repository.
- Superpowers availability: installed locally; `using-superpowers`, `writing-plans`, `systematic-debugging`, and `verification-before-completion` read and applied.
- AI text-to-image for sample DOCX: off. Release README assets will use image generation separately.

### Actor -> Critic Cycle 1

- Actor changes: inspected skill/scripts, mined sessions/logs, wrote plan, created historical failure summary.
- Critic findings: needed actual DOCX build and script-level QA before claiming skill quality.
- Fix plan: build sample fixture with image/table/code/TOC and run `qa_docx_report.py`.

### Actor -> Critic Cycle 2

- Actor changes: generated sample DOCX and ran package/text QA.
- Critic findings: QA correctly blocked the first sample because a negative sentence still contained the forbidden stale score token `100%`. Rendered PDF review then found a blank first page caused by unconditional pre-TOC page break when no template cover is preserved.
- Fix plan: remove the stale score token from the source draft, patch `build_report.py` so pre-TOC page break only happens when a template cover is preserved, regenerate DOCX/PDF, and rerun package/text/rendered-page QA.
