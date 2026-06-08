# Historical Failure Scenarios For `docx-course-report-writer`

Evidence sources checked:

- Recent session user messages under `C:\Users\20795\.codex\sessions`, modified after 2026-05-24.
- `C:\Users\20795\.codex\session_index.jsonl`.
- `C:\Users\20795\.codex\logs_2.sqlite` schema and sampled matching rows.
- Current `docx-course-report-writer` references and scripts.

## Pressure Scenarios

| Scenario | Evidence signal | Expected skill behavior | Test coverage |
|---|---|---|---|
| AI images contained unrelated school/company names and wrong labels | 2026-06-07 report work required replacing AI text such as unrelated school/company names with the real class sample | Require AI-image opt-in/count, pre-generation drawing specs, allowed/forbidden text whitelist, post-generation text verification, and deterministic overlay when text matters | Skill search checks for AI-image intake and figure ledger; README/docs must document this gate |
| Final result text kept obsolete `100%` claims after user corrected final score to `99.69%` | User explicitly required replacing final 100% claims with 99.69%/99.61% and scanning text, tables, TikZ, AI images, captions | Require fact ledger and stale claim scan across DOCX text, PDF text, figure sources, captions, and generated image specs | Sample DOCX QA scans stale terms and explicit forbidden score terms |
| TikZ/diagram arrows needed full review | User required all LaTeX/TikZ figures to be reviewed and corrected; later asked to strengthen arrow review | Every diagram must enter Review And Revise, with arrow audit after rendering and after DOCX/PDF insertion | Skill rule search checks Review And Revise and arrow audit; sample report contains figure ledger notes |
| LaTeX report to DOCX conversion had strict template/TOC/visual QA requirements | User requested LaTeX-to-template-DOCX conversion preserving cover, automatic TOC, chapters, formulas, figures, references, and visual QA | Require template preservation, real Word headings, automatic TOC field, no LaTeX residue, and rendered/PDF visual QA when possible | Sample DOCX checks heading styles, TOC XML, tables, images, placeholders, and stale terms |
| Windows Chinese path and terminal encoding can look broken | Profile/logs show PowerShell GBK display can garble valid UTF-8 paths/text | Verify actual file bytes with Unicode-aware tools; use absolute paths and ASCII temp fallback for Word COM/PDF | Script compile and Unicode repr checks were run before artifact testing |
| Tool logs contain broad DOCX/PDF matches but many are noisy current-turn traces | `logs_2.sqlite` matched many current tracing rows rather than actionable historical failures | Treat logs as weak signals unless they identify a concrete failure; prefer parsed user messages and artifact evidence | Audit notes distinguish user-message evidence from noisy logs |

## Derived Skill Requirements

- Keep Superpowers invocation mandatory when installed.
- Keep Actor/Critic minimum two cycles with no maximum.
- Keep AI-image opt-in/count default 3.
- Keep fact ledger and figure ledger as run-record fields.
- Keep source-first repair: never edit only the final DOCX when a generator or figure source exists.
- Keep Word field/TOC and rendered visual QA gates.
- Keep explicit diagram Review And Revise and arrow audit.
