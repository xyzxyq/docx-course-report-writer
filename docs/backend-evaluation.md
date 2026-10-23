# Backend Evaluation Status

> Historical evaluation status (2026-09-11). Later work added native templates and exercised their compilation; see [current verification](verification-2026-10-23.md) and [output routes](../references/output-formats.md). A Quarto/Pandoc comparative benchmark remains unperformed. The earlier provisional design below is preserved for traceability, not as current routing instructions.

Status after review, 2026-09-11: **comparative evaluation is not complete**.

The earlier working draft marked Quarto/Pandoc “Not selected” and native routes “Selected” without same-content comparative builds. That is insufficient evidence to reject either candidate or mark handoff phase A complete.

| Candidate | Verified conclusion | Remaining evaluation |
|---|---|---|
| Quarto | Not evaluated here | Build the common samples in all three formats; inspect Chinese fonts, references, templates and source delivery |
| Pandoc | Not evaluated here | Same samples; compare dependencies, additional code and template limitations |
| Existing DOCX + native LaTeX/Typst | Existing generation/compilation paths retained for compatibility | Full report quality, strict templates and platform validation; compiler probes alone are insufficient |

Keep existing DOCX behavior and native-source compilation as provisional capabilities. This does not select the general-report backend. The native router requires already-authored `.tex`/`.typ`; it does not implement Markdown conversion or supply new academic templates.

Use the three representative sample types and decision criteria in [the handoff](skill-optimization-handoff.md#6-构建方案与选型边界). Record exact inputs, commands, versions, results, failures and patch footprint for each candidate. Mark untested as untested, not failed.

For this review's validation see [review and repair](review-and-repair-2026-09-11.md). Earlier reported local smoke runs remain in [the prior log](local-verification-macos-2026-09-11.md), with their limitations noted there.
