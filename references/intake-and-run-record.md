# Intake and compact run record

For report creation/editing, ask the output format unless explicitly specified: **DOCX / LaTeX / Typst**. An attached template alone is not an explicit output selection. A PDF-only request still needs the source-format choice. Do not ask again once answered. Analysis and skill maintenance skip this intake.

Use the host's available interactive question tool; otherwise ask in text. Explain the trade-offs in the choice labels/descriptions or a short preceding message, not only in internal notes. Ask only unanswered questions.

## First interaction: format and AI enablement

Suggested wording: “报告需要哪种格式？三者的主要取舍如下。是否需要 AI 生成的概念/解释性插图？”

| Format | Advantages to tell the user | Limitations to tell the user |
|---|---|---|
| DOCX | Word/WPS 可视化编辑方便，适合学校 Word 模板与协作修改 | 跨软件字体、分页和目录可能变化，复杂公式与交叉引用需要额外维护 |
| LaTeX | 公式、编号、引用与长文档排版强，PDF 版式稳定，源码可复现 | 需要语法和编译环境，初学编辑成本较高，与 Word 模板不能直接互换 |
| Typst | 语法较简洁，编译预览方便，适合公式与结构化报告 | 模板与插件生态相对较小，不直接兼容 Word/LaTeX 源文件，仍需检查字体与编译环境 |

LaTeX/Typst deliver PDF **and editable source**, not DOCX. If a format is already specified, do not ask again or repeat the full comparison; mention only a constraint that affects the task. AI illustrations: **No / Yes**, for concepts and explanations only, never experimental proof.

At first report use, include the verified subagent model/effort and concurrency notice from [multi-agent-workflow.md](multi-agent-workflow.md), with the option to adjust or disable collaboration. Reuse recorded preferences and disclosure instead of asking on every turn. This optional adjustment does not block work or turn silence into explicit consent; required format/AI answers still need a response. Check host restrictions before dispatch. A small edit does not need workers merely because settings were disclosed.

## Conditional follow-up: only if AI is enabled

Ask the final insertion count (positive integer) and this question together, unless already answered:

> 是否需要将 AI 插图用 PPT 原生文字、形状和线条复现，保留可编辑 PPTX，再导出 PDF 并插入报告？
>
> - **不需要，直接使用 AI 图片**：步骤少，保留原图效果；图片仍是位图，不能逐个编辑其中的文字和图形。
> - **需要，PPT 可编辑复现**：适合架构图、流程图等，可编辑重建对象；需额外复现与核验，照片/纹理不一定能完全矢量化。保留 PPTX 和 PDF，Word 内的矢量保留情况需要验证。

The PPT question is required after AI opt-in, not inferred from an editable-report request. No default selection or silence counts as an answer. While it is pending, continue independent source/research work but do not generate/reconstruct the affected figures. If AI is disabled, ask neither count nor PPT question. User-requested reconstruction of an existing non-AI image can still use the same workflow without enabling AI generation. Details only for the selected route: [ppt-figure-reconstruction.md](ppt-figure-reconstruction.md).

Reuse explicit AI choices; do not treat silence or preselection as an answer. Only missing essential task information should block drafting. Inspect supplied materials while awaiting answers. Respect an explicit no-cover or blank-document request. Resolve conflicts between the requested format and assignment before building.

Keep one short record (file or work notes), not parallel plans/checklists/transcripts:

```markdown
# Report run
- Assignment / requested format / answer source:
- Authoritative source / template / required deliverables:
- Cover metadata and missing inputs:
- Mandatory requirements → report locations / supporting evidence / acceptance checks:
- Selected companion skills and purpose (only if used):
- Subagent preferences: enabled/disabled; model/effort by role; concurrency; setting source and disclosure state:
- Worker tasks used: scope / owned files / requested settings / observed settings or unknown / completion status:
- AI enabled / insertion count / attempts:
- PPT reconstruction: yes/no/not applicable; answer source:
- If reconstructed: PPTX / exported PDF / inserted vector asset / residual raster parts / target-app verification:
- Environment / build command / tool versions:
- Evidence paths and verified facts:
- Key claims: source passage/table/raw-result locator, conditions, calculation and support status (reuse evidence entries):
- Reference Metadata Ledger: verified metadata/source links (reuse bibliography where sufficient):
- Figures: source, role, caption, visible-text check (only if used):
- Build ID or artifact hash:
- Checks performed / reviewed pages:
- Repair rounds used (0–2) / findings and fixes:
- Pending limitations / final artifact paths:
```

Citation rules and reference-quality checks live in SKILL.md and [report-qa-checklist.md](report-qa-checklist.md); record their results without duplicating the checklist.

Add only applicable detail: template-fidelity notes for supplied DOCX, runtime/logs for experiments, screenshot identities for visual proof, prompt cards for AI images. Record independent review only if actually performed; distinguish self-review and unavailable checks. Never label an unavailable check as passed. The two-round budget in SKILL.md applies across all reviewers. Quality measurements, when useful, reuse the gate results in [report-qa-checklist.md](report-qa-checklist.md) rather than a separate scorecard.
