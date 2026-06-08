# DOCX Course Report Writer

[![Skill](https://img.shields.io/badge/Codex-Skill-111827)](#quick-start)
[![DOCX](https://img.shields.io/badge/output-DOCX%20%2B%20PDF-2563eb)](#quality-gates)
[![Superpowers](https://img.shields.io/badge/workflow-Superpowers-7c3aed)](#superpowers-mapping)
[![Windows Word](https://img.shields.io/badge/Word-COM%20field%20update-0f766e)](#quick-start)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

![DOCX Course Report Writer Poster](assets/poster.png)

<div align="center">

![Skill Icon](assets/icon.png)

**A Codex skill for building, repairing, and verifying Chinese coursework DOCX reports with source-first evidence, Word TOC handling, figure QA, and Actor/Critic review.**

**面向中文课程报告、实验报告、课程论文与模板迁移的 Codex 技能：强调真实证据、自动目录、图表审查、文生图边界与 Actor/Critic 双智能体迭代。**

</div>

---

## English

### What This Skill Is

`docx-course-report-writer` is a local Codex skill for end-to-end Chinese academic report work. It helps an agent turn assignments, templates, LaTeX reports, source code, screenshots, experiment logs, citations, and figure assets into a formal `.docx` report package.

The skill is designed for situations where a simple text draft is not enough. It focuses on the things that usually break real course-report deliverables:

- stale template content
- fake or weak evidence
- broken Word table of contents
- incorrect score/result claims
- AI-generated images with wrong text
- TikZ/flowchart arrows that overlap or point incorrectly
- screenshots that show error pages rather than real evidence
- DOCX files that pass text checks but fail rendered-page QA

The workflow is intentionally inspired by [obra/superpowers](https://github.com/obra/superpowers): clarify the target, write a concrete plan, execute in bounded phases, debug from root cause, review the actual artifact, and verify before claiming completion. This skill adapts that discipline to Chinese DOCX report production.

### Highlights

- **Source-first workflow**: draft, references, image attribution, logs, screenshots, scripts, DOCX, and PDF stay traceable.
- **Mandatory Actor/Critic loop**: every use requires at least two full `Actor -> Critic` cycles; there is no maximum iteration count.
- **Superpowers integration**: if `superpowers:*` skills are installed, the skill requires invoking the relevant Superpowers workflow before acting.
- **Fact ledger**: final scores, filenames, model names, dataset sizes, dates, and result boundaries are tracked before writing claims.
- **Figure ledger**: every figure records role, method, source/evidence, attribution, and Review And Revise status.
- **AI-image safety**: the user must be asked whether to enable text-to-image and how many images to generate; default maximum is 3.
- **Arrow audit**: TikZ, flowcharts, pipelines, architecture diagrams, timelines, and mechanism diagrams must be reviewed after rendering, especially arrows.
- **Word COM field update**: on Windows, the helper script can update TOC/fields and export PDF through Microsoft Word.
- **Rendered QA**: final checks include DOCX package/text checks and rendered PDF/page inspection when possible.

### Repository Structure

```text
.
├── SKILL.md                         # Main skill entrypoint
├── references/                      # Detailed workflow, QA, style, figures, sources, Superpowers adapter
├── scripts/                         # Reusable build, Word-field, QA, and screenshot annotation helpers
├── skill-assets/                    # Original skill templates/assets
├── assets/
│   ├── icon.png                     # Generated README icon
│   └── poster.png                   # Generated README poster
├── examples/
│   └── sample-report/               # Reproducible source fixture for the checked DOCX/PDF sample
└── docs/
    ├── testing-report.md            # Local verification evidence
    ├── historical-failures.md       # Failure scenarios mined from recent usage
    ├── audit-notes.md               # Actor/Critic audit notes
    ├── sample-report.docx           # Generated sample DOCX
    ├── sample-report.pdf            # Word-exported PDF
    ├── sample-rendered-page-1.png   # Rendered TOC page
    └── sample-rendered-page-2.png   # Rendered body/figure page
```

### When To Use

Use this skill when Codex handles:

- Chinese course reports
- experiment reports
- course papers
- reading reports
- literature reviews
- LaTeX-to-DOCX conversion
- DOCX template migration
- report repair after user feedback
- figure-heavy academic reports
- submission-ready report folders

Do not use it for legal drafting, arbitrary OOXML surgery, generic forms, or tracked-change review pipelines unrelated to course reports.

### Quick Start

Install or copy this folder into your Codex skills directory:

```powershell
Copy-Item -Recurse . "$env:USERPROFILE\.codex\skills\docx-course-report-writer"
```

Then ask Codex to use the skill:

```text
请使用 docx-course-report-writer，把我的课程报告材料整理成可提交 DOCX，并导出 PDF 做最终检查。
```

For a source-first report, prepare:

```text
report-draft.md
references.md
image-attributions.md
raw logs or screenshots
figure sources
```

Run the included reproducible sample:

```powershell
python scripts/build_report.py `
  --draft examples\sample-report\report-draft.md `
  --refs examples\sample-report\references.md `
  --output output\sample-report.docx `
  --root examples\sample-report
```

Run DOCX package QA:

```powershell
python scripts/qa_docx_report.py `
  --docx output\sample-report.docx `
  --require-toc `
  --min-images 1 `
  --min-tables 2 `
  --min-heading1 1
```

Update Word fields and export PDF on Windows:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File scripts/update_word_fields.ps1 `
  -DocxPath path\to\report.docx `
  -ExportPdf `
  -UseAsciiTemp
```

### Workflow

The main run card is:

1. Check and invoke Superpowers when installed.
2. Lock scope, deliverables, evidence, template constraints, and AI-image permission/count.
3. Create a fact ledger and requirement-to-evidence checklist.
4. Create or activate `Actor` and `Critic`.
5. Run `Actor -> Critic` cycle 1.
6. Fix source-level defects.
7. Run `Actor -> Critic` cycle 2.
8. Continue iterating while blocking defects remain.
9. Update Word fields/TOC and export PDF.
10. Inspect actual DOCX/PDF artifacts before final delivery.

### Superpowers Mapping

When Superpowers is available, this skill routes work as follows:

| Situation | Superpowers skill |
|---|---|
| Need to plan multi-step report work | `superpowers:writing-plans` |
| Execute an existing plan | `superpowers:subagent-driven-development` or `superpowers:executing-plans` |
| Fix a failed report, bad DOCX/PDF, broken TOC, bad diagram, or stale result | `superpowers:systematic-debugging` |
| Implement report-generation scripts or bug fixes | `superpowers:test-driven-development` when tests are feasible |
| Claim the work is complete | `superpowers:verification-before-completion` |

If Superpowers is not installed, use `references/superpowers-adapter.md` as a fallback.

### Quality Gates

The skill blocks delivery unless these are satisfied or explicitly documented:

- Evidence authenticity gate
- File ownership gate
- Template residue gate
- Word field / TOC gate
- Fact ledger gate
- Figure semantics gate
- External screenshot gate
- Analysis depth gate
- Rendered visual QA gate

The generated sample in `docs/` was checked with:

- Python compile checks for helper scripts
- DOCX package/text QA
- Word COM field update
- Word PDF export through an ASCII temp path
- PDF text extraction for result values and forbidden stale score tokens
- PDF page rendering through `pdftoppm`
- Visual inspection of TOC and figure pages

See `docs/testing-report.md`.

### Included Sample

The repository contains both source inputs and generated outputs:

| Path | Role |
|---|---|
| `examples/sample-report/report-draft.md` | Source-first report draft |
| `examples/sample-report/references.md` | Reference ledger |
| `examples/sample-report/image-attributions.md` | Figure attribution ledger |
| `examples/sample-report/assets/skill-flow.png` | Reviewed diagram used by the sample |
| `docs/sample-report.docx` | Generated DOCX artifact |
| `docs/sample-report.pdf` | Word-exported PDF artifact |
| `docs/sample-rendered-page-1.png` | Rendered page inspection evidence |
| `docs/sample-rendered-page-2.png` | Rendered page inspection evidence |

---

## 中文说明

### 这个 Skill 是什么

`docx-course-report-writer` 是一个面向 Codex 的本地技能包，用于完成中文课程报告、实验报告、课程论文、读书报告、综述、LaTeX 转 DOCX、模板替换和报告返修等任务。

它不是单纯“润色文字”的技能，而是把课程报告当成一个可验证的工程交付：读取任务书、锁定证据、生成或迁移内容、插入图表、更新 Word 目录、导出 PDF，并检查最终页面。

### 核心特点

- **源文件优先**：先维护 `report-draft.md`、引用、图像归因、日志、截图、图源和脚本，再生成 DOCX/PDF。
- **强制 Actor/Critic 双智能体**：每次使用至少两轮 `Actor -> Critic`，没有迭代上限。
- **强制 Superpowers 调用门**：如果安装了 Superpowers 插件或技能，必须先调用对应流程技能。
- **事实台账**：分数、数据集大小、模型名、文件名、日期、最终/中间结果口径都要进入 fact ledger。
- **图像台账**：每张图都记录角色、来源、制作方式、归因和审查状态。
- **文生图边界**：使用 AI 文生图前必须询问用户是否开启，以及最多生成/插入几张；默认最多 3 张。
- **箭头审查**：TikZ、流程图、架构图、时间线、机制图必须进入 Review And Revise，重点检查箭头是否交叉、遮挡、指错或与模块重叠。
- **Word 自动目录**：使用真实 Word Heading 样式和 TOC 字段；Windows 下优先通过 Word COM 更新字段并导出 PDF。
- **渲染级 QA**：不仅检查 DOCX 文本，还要检查 PDF 或页面渲染，避免目录、表格、图片、代码块在最终页面出问题。

### 适用场景

适合：

- 中文课程报告
- 实验报告
- 课程论文
- 文献综述
- 读书报告
- LaTeX 报告迁移到 Word 模板
- 旧 DOCX 模板替换
- 带大量截图、图表、代码块的报告
- 用户指出问题后的报告返修

不适合：

- 法律文书
- 与报告无关的复杂 OOXML 手术
- 表单/内容控件工作流
- 通用文档审阅流水线

### 使用方式

将仓库复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse . "$env:USERPROFILE\.codex\skills\docx-course-report-writer"
```

然后在 Codex 中说明任务，例如：

```text
请使用 docx-course-report-writer，将我的课程报告材料整理成正式 DOCX，并检查 PDF 页面效果。
```

推荐的工作目录材料：

```text
report-draft.md
references.md
image-attributions.md
原始日志
真实截图
图源文件
生成脚本
```

### 最重要的强制规则

1. 不允许编造实验结果。
2. 要求真实截图时，必须截取真实终端或应用窗口。
3. AI 图片不能替代真实证据。
4. AI 图片中如果包含事实文字，必须先写白名单，生成后再检查。
5. 目录必须是真实 Word TOC 字段，不允许用静态文字假装目录。
6. 每次使用必须创建或激活 Actor 与 Critic。
7. 至少两轮 Actor/Critic，发现阻塞问题继续迭代。
8. 所有流程图、架构图、TikZ 图和时间线必须做最终图像审查，重点检查箭头。
9. 用户反馈就是新的失败测试，必须回到源文件、脚本或图源修复。
10. 交付前必须检查实际 DOCX/PDF，而不是只检查计划。

### 脚本说明

| Script | Purpose |
|---|---|
| `scripts/build_report.py` | 从轻量 Markdown 草稿构建 DOCX |
| `scripts/qa_docx_report.py` | 检查 DOCX 文本、TOC、图片、表格、标题和残留内容 |
| `scripts/update_word_fields.ps1` | 通过 Word COM 更新 TOC/字段并导出 PDF |
| `scripts/annotate_screenshot.py` | 给真实截图添加红框和透明红色标签 |

### 已验证内容

本仓库包含一个测试样例：

- [sample-report.docx](docs/sample-report.docx)
- [sample-report.pdf](docs/sample-report.pdf)
- [sample-rendered-page-1.png](docs/sample-rendered-page-1.png)
- [sample-rendered-page-2.png](docs/sample-rendered-page-2.png)

该样例覆盖：

- 自动目录字段
- Word Heading 样式
- 表格
- 插图与图注来源
- 代码块
- `99.69% / 99.61%` 事实口径
- 禁止残留 `100%` 结果口径
- PDF 页面渲染检查
- 首页非空检查
- 箭头 Review And Revise

详情见 [docs/testing-report.md](docs/testing-report.md)。

### 设计理念

这个技能参考了高星 agent skill 项目的组织方式：主 `SKILL.md` 保持短入口，复杂细节放到 `references/`；执行时不是靠“记住规则”，而是通过 run record、fact ledger、figure ledger、Actor/Critic loop 和 QA checklist 强制落地。

它尤其强调：报告质量不是语言流畅度，而是证据、结构、图表、引用、目录、事实口径和最终渲染共同通过检查。

它也吸收了 [Superpowers](https://github.com/obra/superpowers) 的任务执行思想：先澄清和规划，再分阶段执行；遇到问题先定位根因；完成前必须用真实产物和命令结果验证，而不是只给出主观判断。

---

## License

MIT. See [LICENSE](LICENSE).
