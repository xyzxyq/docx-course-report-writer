<p align="center">
  <img src="assets/icon.png" width="112" alt="DOCX Course Report Writer icon">
</p>

<h1 align="center">DOCX Course Report Writer</h1>

<p align="center">
  面向中文课程报告、实验报告、课程论文与 LaTeX 转 Word 的 Codex 技能。
  <br>
  从材料、证据、图表、模板到 DOCX/PDF 交付，按工程化流程生成可检查、可复现、可提交的报告。
</p>

<p align="center">
  语言 / Language:
  <a href="#zh-cn">简体中文</a> |
  <a href="#english">English</a>
</p>

<p align="center">
  <a href="#quick-start"><img src="https://img.shields.io/badge/Codex-Skill-111827" alt="Codex Skill"></a>
  <a href="#quality-gates"><img src="https://img.shields.io/badge/output-DOCX%20%2B%20PDF-2563eb" alt="DOCX and PDF"></a>
  <a href="#superpowers-workflow"><img src="https://img.shields.io/badge/workflow-Superpowers-7c3aed" alt="Superpowers"></a>
  <a href="#word-toc-pdf"><img src="https://img.shields.io/badge/Word-COM%20field%20update-0f766e" alt="Word COM"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License"></a>
</p>

<p align="center">
  <img src="assets/poster.png" width="820" alt="DOCX Course Report Writer poster">
</p>

---

<a id="zh-cn"></a>

## 简体中文

### 这是什么

`docx-course-report-writer` 是一个本地 Codex skill，用于创建、修复、迁移和验收中文课程类 DOCX 报告。它适用于课程报告、实验报告、课程论文、读书报告、文献综述、LaTeX 转 DOCX、模板迁移、图表密集型报告和用户反馈后的返修。

它不是单纯的“润色文字”工具，而是把报告当作一个可验证交付物处理：

- 先锁定任务书、模板、证据和交付物
- 再生成或迁移正文、表格、图、引用和目录
- 最后检查 DOCX 包、Word TOC、PDF 页面渲染、图表可读性和事实口径

### 它解决的问题

真实课程报告经常不是“写得不够通顺”，而是这些地方出问题：

- 模板里的旧主题、静态目录、占位正文残留
- Word 目录不是自动 TOC，或导出 PDF 后目录没有更新
- 图表、截图、AI 图片、TikZ 图在最终页面里不可读
- 流程图箭头交叉、遮挡、指错或与模块重叠
- 图中文字贴边、压线、与箭头或其他标签碰撞
- 实验结果、分数、文件名、模型名和用户最新修正不一致
- AI 生成图里出现错误校名、公司名、数字或伪造证据
- 只检查 DOCX 文本，没有检查最终 PDF 页面

### 核心亮点

| 能力 | 说明 |
|---|---|
| Source-first 工作区 | 推荐维护 `report-draft.md`、`references.md`、`image-attributions.md`、日志、截图、图源、脚本、DOCX 和 PDF，便于返修和复现 |
| 默认 DOCX 模板 | 用户未提供模板时自动使用 `skill-assets/default-course-report-template.docx`；用户提供模板时永远优先使用用户模板 |
| Superpowers 工作流 | 安装了 Superpowers 时必须先调用对应流程技能，例如规划、调试、执行、验证 |
| Actor/Critic 双智能体 | 每次使用必须创建或激活 Actor 与 Critic，至少两轮 `Actor -> Critic`，无迭代上限 |
| Fact ledger | 分数、文件名、模型名、数据集大小、日期、最终/中间结果口径都要有来源和验证记录 |
| Figure ledger | 每张图记录角色、来源、制作方式、归因和 Review And Revise 状态 |
| 文生图边界 | 使用 AI 文生图前必须询问用户是否开启，以及最多生成/插入几张；默认最多 3 张 |
| 严格图形 QA | TikZ、流程图、架构图、时间线和机制图必须审查箭头、文字排版、最终缩放效果 |
| Word 目录与 PDF | Windows 下优先通过 Word COM 更新字段、目录和页码，再导出 PDF |

<a id="quick-start"></a>

### 快速开始

将仓库复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse . "$env:USERPROFILE\.codex\skills\docx-course-report-writer"
```

然后在 Codex 中使用：

```text
请使用 docx-course-report-writer，把我的课程报告材料整理成可提交 DOCX，并导出 PDF 做最终检查。
```

推荐准备的源文件：

```text
report-draft.md
references.md
image-attributions.md
raw logs 或 screenshots
figure sources
assignment/template/rubric
```

运行内置样例：

```powershell
python scripts/build_report.py `
  --draft examples\sample-report\report-draft.md `
  --refs examples\sample-report\references.md `
  --output output\sample-report.docx `
  --root examples\sample-report
```

如果没有传入 `--template`，脚本会自动使用 `skill-assets/default-course-report-template.docx` 作为样式和页面设置模板，并默认清空模板正文，避免旧目录、`XXXX`、示例章节等残留。

用户提供模板时使用：

```powershell
python scripts/build_report.py `
  --template path\to\user-template.docx `
  --draft path\to\report-draft.md `
  --refs path\to\references.md `
  --output path\to\report.docx `
  --root path\to\working-folder
```

只有明确想从空白文档开始时才使用：

```powershell
python scripts/build_report.py --no-default-template ...
```

### DOCX QA

```powershell
python scripts/qa_docx_report.py `
  --docx output\sample-report.docx `
  --require-toc `
  --min-images 1 `
  --min-tables 2 `
  --min-heading1 1
```

<a id="word-toc-pdf"></a>

### Word 目录与 PDF

Windows 上推荐用 Word COM 更新目录、字段和页码，并导出 PDF：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File scripts/update_word_fields.ps1 `
  -DocxPath output\sample-report.docx `
  -ExportPdf `
  -UseAsciiTemp
```

`-UseAsciiTemp` 用于规避中文路径和 Word COM 自动化中的编码问题。

### 工作流

1. 检查并调用 Superpowers。
2. 读取任务书、模板、源文件和用户约束。
3. 询问 AI 文生图是否开启，以及最多生成/插入几张。
4. 建立 run record、fact ledger、figure ledger。
5. 创建或激活 Actor 与 Critic。
6. Actor 生成或修复报告源文件、图表和 DOCX。
7. Critic 审查真实产物，而不是只审查计划。
8. 至少完成两轮 `Actor -> Critic`。
9. 更新 Word 字段和 TOC，导出 PDF。
10. 检查最终 DOCX/PDF、图表页、目录页、表格页和代码块页。

<a id="superpowers-workflow"></a>

### Superpowers 工作流

| 场景 | Superpowers skill |
|---|---|
| 多步骤报告任务需要规划 | `superpowers:writing-plans` |
| 执行已有计划 | `superpowers:subagent-driven-development` 或 `superpowers:executing-plans` |
| 修复坏 DOCX/PDF、坏目录、坏图、旧事实口径 | `superpowers:systematic-debugging` |
| 修改生成脚本或修复脚本 bug | `superpowers:test-driven-development` |
| 声称完成前 | `superpowers:verification-before-completion` |

如果 Superpowers 不可用，使用 `references/superpowers-adapter.md` 中的降级流程，并在 run record 中记录。

<a id="quality-gates"></a>

### 质量门

交付前必须通过或明确说明限制：

- 证据真实性：实验结果、截图、日志和数据不能编造
- 文件归属：最终 DOCX/PDF 和生成脚本由 Orchestrator 统一集成
- 模板残留：没有旧主题、旧截图、旧目录、占位符、无关媒体
- Word 字段：标题样式、TOC 字段、页码和目录经过更新
- 事实口径：分数、文件名、模型名、日期和最终结果一致
- 图形语义：TikZ/流程图/架构图含义正确
- 箭头审查：箭头不交叉、不遮挡、不指错、不贴近到影响阅读
- 文字排版审查：标签不贴边、不压线、不碰撞箭头/模块/其他标签
- PDF 渲染：目录页、图表页、表格页、代码块页经过最终检查

### 图形审验规则

TikZ、流程图、pipeline、架构图、时间线和机制图必须在渲染后、插入 DOCX/PDF 后各做一次 `Review And Revise`。

这些情况一律拒收：

- 箭头穿过模块、文字、图例、caption 或证据区域
- 箭头头部被裁剪、被边框盖住、太小、指错对象
- 多条箭头距离太近，读者无法分辨路径
- 文本标签贴边、压线、碰撞箭头、碰撞模块或碰撞其他标签
- 节点文字过长导致行距、留白和视觉重心失衡
- 图只在源文件里看起来还行，但缩放到 Word/PDF 后变得拥挤

修复顺序：

1. 增加留白、节点距离、节点宽度和内边距。
2. 缩短标签，把解释性文字移到 caption、表格或正文。
3. 使用显式 anchors、正交路径、中间坐标、`shorten >=` 和 `shorten <=`。
4. 拆成多张小图。
5. 两次源级修复仍不清晰时，重画更简单的结构。

### 目录结构

```text
.
├── SKILL.md
├── references/
├── scripts/
├── skill-assets/
│   ├── default-course-report-template.docx
│   ├── report-draft-template.md
│   ├── references-template.md
│   └── image-attributions-template.md
├── assets/
│   ├── icon.png
│   └── poster.png
├── examples/
│   └── sample-report/
└── docs/
    ├── testing-report.md
    ├── historical-failures.md
    ├── audit-notes.md
    ├── sample-report.docx
    ├── sample-report.pdf
    ├── sample-rendered-page-1.png
    └── sample-rendered-page-2.png
```

### 已验证内容

本仓库包含可复现样例和测试记录：

- [docs/testing-report.md](docs/testing-report.md)
- [docs/sample-report.docx](docs/sample-report.docx)
- [docs/sample-report.pdf](docs/sample-report.pdf)
- [docs/sample-rendered-page-1.png](docs/sample-rendered-page-1.png)
- [docs/sample-rendered-page-2.png](docs/sample-rendered-page-2.png)

验证覆盖：

- Python 脚本编译
- 默认模板构建
- 缺失 `Heading 2/3` 时自动补齐 Word 标题样式
- DOCX package/text QA
- 自动 TOC 字段
- 表格、图片、标题统计
- Word COM 字段更新
- PDF 导出
- PDF 关键事实口径检查
- 首屏非空检查
- TikZ/流程图箭头与文字排版审验规则

### 设计来源

README 首屏结构参考了 [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) 的方式：顶部集中展示 logo、标题、徽章、语言入口和一句话定位，再在正文展开问题、解决方案、快速开始和验证证据。

工作流思想参考 [obra/superpowers](https://github.com/obra/superpowers)：先澄清和规划，再分阶段执行；遇到问题先定位根因；完成前必须用真实产物和命令结果验证。

---

## English

### What It Is

`docx-course-report-writer` is a local Codex skill for creating, repairing, migrating, and verifying Chinese coursework DOCX reports. It is designed for course reports, lab reports, course papers, reading reports, literature reviews, LaTeX-to-DOCX conversion, template migration, figure-heavy Word reports, and submission-ready report packages.

It treats a report as an engineering deliverable, not just a writing task: source files, evidence, figures, citations, Word fields, DOCX output, PDF rendering, and final QA all stay traceable.

### Highlights

| Capability | Description |
|---|---|
| Source-first workspace | Keep draft, references, image attribution, logs, screenshots, figure sources, scripts, DOCX, and PDF reproducible |
| Default DOCX template | Uses `skill-assets/default-course-report-template.docx` when no user template is supplied; user templates always take precedence |
| Superpowers workflow | Invokes relevant Superpowers skills for planning, debugging, execution, and verification when installed |
| Actor/Critic loop | Requires at least two complete `Actor -> Critic` cycles; no maximum iteration count |
| Fact ledger | Tracks scores, filenames, model names, dataset sizes, dates, and final/intermediate claims |
| Figure ledger | Tracks every figure's role, source, method, attribution, and Review And Revise status |
| AI-image safety | Requires user opt-in and a maximum generation/insertion count; default maximum is 3 |
| Strict diagram QA | Rejects unclear arrows, arrow overlaps, label collisions, cramped nodes, and bad final-scale rendering |
| Word COM export | Updates Word fields/TOC and exports PDF on Windows |

### Quick Start

Copy this repository into your Codex skills folder:

```powershell
Copy-Item -Recurse . "$env:USERPROFILE\.codex\skills\docx-course-report-writer"
```

Run the included sample:

```powershell
python scripts/build_report.py `
  --draft examples\sample-report\report-draft.md `
  --refs examples\sample-report\references.md `
  --output output\sample-report.docx `
  --root examples\sample-report
```

Run DOCX QA:

```powershell
python scripts/qa_docx_report.py `
  --docx output\sample-report.docx `
  --require-toc `
  --min-images 1 `
  --min-tables 2 `
  --min-heading1 1
```

Update fields and export PDF with Microsoft Word:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File scripts/update_word_fields.ps1 `
  -DocxPath output\sample-report.docx `
  -ExportPdf `
  -UseAsciiTemp
```

### Workflow

1. Invoke Superpowers when installed.
2. Read assignment, template, source files, and user constraints.
3. Ask whether AI text-to-image is enabled and how many images may be generated/inserted.
4. Create run record, fact ledger, and figure ledger.
5. Create or activate Actor and Critic.
6. Complete at least two `Actor -> Critic` cycles.
7. Update Word fields/TOC and export PDF.
8. Inspect the actual DOCX/PDF before delivery.

### Quality Gates

The skill blocks delivery unless these are satisfied or explicitly documented:

- evidence authenticity
- file ownership
- template residue removal
- Word field / TOC update
- fact ledger consistency
- figure semantics
- arrow audit
- text-layout audit
- rendered visual QA

### Repository Structure

```text
.
├── SKILL.md
├── references/
├── scripts/
├── skill-assets/
├── assets/
├── examples/
└── docs/
```

### Verification

See [docs/testing-report.md](docs/testing-report.md). The checked sample covers script compilation, default template behavior, Word heading/TOC handling, DOCX QA, Word COM PDF export, PDF text checks, rendered-page inspection, and stricter TikZ/diagram QA rules.

---

## License

MIT. See [LICENSE](LICENSE).
