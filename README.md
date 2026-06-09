<p align="center">
  <img src="assets/logo.png" width="116" alt="DOCX Course Report Writer logo">
</p>

<h1 align="center">DOCX Course Report Writer</h1>

<p align="center">
  <em>“没有什么比一件未完成的任务一直挂在那里更令人疲惫。”</em>
  <br>
  <sub>William James，1886。每个被课程报告追杀的大学生都懂。</sub>
</p>

<p align="center">
  面向大学生水课课程报告、实验报告、课程论文与综述写作的 Codex Skill。
  <br>
  这是一个被本学期过量课程报告逼出来的自动化工作流。
  <br>
  把“又要写 Word 报告”变成“可规划、可验证、可修复、可提交”的文档工程流程。
</p>

<p align="center">
  <a href="#quick-start"><img src="https://img.shields.io/badge/Codex-Skill-111827" alt="Codex Skill"></a>
  <a href="#demo"><img src="https://img.shields.io/badge/watercourse-report%20automation-f97316" alt="大学水课报告自动化"></a>
  <a href="#demo"><img src="https://img.shields.io/badge/demo-DOCX%20%2B%20PDF-2563eb" alt="DOCX and PDF demo"></a>
  <a href="#highlights"><img src="https://img.shields.io/badge/Word-TOC%20%2F%20PDF%20QA-0f766e" alt="Word TOC and PDF QA"></a>
  <a href="#workflow"><img src="https://img.shields.io/badge/workflow-Actor%20%2F%20Critic-7c3aed" alt="Actor Critic workflow"></a>
  <a href="README.en.md"><img src="https://img.shields.io/badge/README-English-64748b" alt="English README"></a>
</p>

<p align="center">
  <img src="assets/coursework-overload.jpg" width="390" alt="我怎么不记得有这么多作业">
  <img src="assets/coursework-done.jpg" width="390" alt="我作业写完了">
</p>

---

## 它解决什么问题？

大学水课很多，课程报告也很多。真正消耗人的不是某一篇报告，而是一学期里反复出现的“查资料、凑结构、配图、写格式、调目录、导 PDF、再返工”。这个 Skill 就是为这种场景做的：让重复性课程报告尽量自动化，让 Codex 不只是写正文，而是把 Word 交付链路一起跑完。

很多课程报告不是“写不出来”，而是交付前容易在这些地方翻车：

| 报告问题 | Skill 的处理方式 |
| --- | --- |
| 内容看似完整，但没有证据链 | 先建立事实台账，再写结论；运行日志、截图、引用和数据必须可追踪 |
| Word 目录、页码、字段没更新 | 使用真实 Word 标题样式，Windows 下优先 Word COM 更新字段并导出 PDF |
| 封面、模板、旧内容残留 | 使用模板优先策略，并检查占位符、旧主题、旧截图和乱码 |
| 图表插进去后不专业 | 强制正式图注、图号顺序、箭头/文字布局审查和 PDF 页面级 QA |
| AI 图片被误当证据 | AI 图只作概念解释；来源、prompt 和非证据属性写入旁路记录 |

`docx-course-report-writer` 的目标不是生成一份“能打开”的 DOCX，而是生成一份能经得住课程提交、教师检查和二次修订的报告包。它适合那些要求不一定难、但格式和交付细节非常烦的课程报告。

<a id="demo"></a>

## 示例展示：深度学习架构课程报告

下面的示例来自一次真实调试后的修订版 DOCX。它展示了这个 Skill 现在会强制关注的细节：封面只占第一页、目录页码右对齐、图注使用 `图x.x` 正式编号，正文不泄漏原始 `图片来源：` 元数据。

| 文件 | 说明 |
| --- | --- |
| [`deep-learning-architecture-report-demo.docx`](docs/deep-learning-architecture-report-demo.docx) | 已上传到 GitHub 的修订版 Word 示例产出 |
| [`deep-learning-architecture-report-demo.pdf`](docs/deep-learning-architecture-report-demo.pdf) | 已上传到 GitHub 的 Word COM 导出 PDF 示例产出 |
| [`deep-learning-demo-cover.png`](docs/deep-learning-demo-cover.png) | 封面页渲染预览 |
| [`deep-learning-demo-toc.png`](docs/deep-learning-demo-toc.png) | 目录页渲染预览 |
| [`deep-learning-demo-figure.png`](docs/deep-learning-demo-figure.png) | 第 11 页正式图注与页面级检查预览 |

### 封面：只占第一页

<p align="center">
  <img src="docs/deep-learning-demo-cover.png" width="680" alt="修订版报告封面预览">
</p>

### 目录：页码右对齐

<p align="center">
  <img src="docs/deep-learning-demo-toc.png" width="680" alt="修订版报告目录预览">
</p>

### 图表：正式图注与页面级检查（第 11 页）

<p align="center">
  <img src="docs/deep-learning-demo-figure.png" width="680" alt="修订版报告第 11 页正式图注与页面级检查预览">
</p>

<a id="highlights"></a>

## 亮点

### 1. Source-first，不凭空写结果

报告先做 evidence plan：任务要求、运行命令、日志、截图、数据、文件名、模型名、引用来源和最终结论都进入事实台账。没有真实证据的结论会被标成限制或推断。

### 2. Word-first，避免“看起来像目录”的假目录

生成器使用真实 Word 标题样式和自动目录字段；Windows 下通过 Word COM 更新目录、页码、字段并导出 PDF。目录页码右对齐、参考文献分页、封面单页都作为验收条件。

### 3. Actor/Critic 双角色审查

每次运行至少两轮：

```text
Actor 生成 / 修复 -> Critic 审查真实 DOCX/PDF/图片 -> Actor 再修复 -> Critic 复审
```

Critic 审查的不是计划，而是实际产物。只要封面、目录、图表、字段、事实或渲染仍有阻塞问题，就继续迭代。

### 4. 图表不是装饰，是可读性工程

流程图、架构图、时间线、TikZ 图、自绘图和 AI 概念图都要经过 Review And Revise。重点检查箭头、文字压框、图号、图注、缩放后的清晰度，以及是否误把概念图写成证据。

### 5. 对中文课程项目友好

默认中文报告结构、中文封面、中文图注、中文 QA 规则，并且针对 Windows、中文路径、Word COM、WSL、截图和 PDF 渲染等高频课程交付问题做了专门处理。

<a id="quick-start"></a>

## 快速开始

### 安装

将仓库放入 Codex skills 目录：

```powershell
C:\Users\<用户名>\.codex\skills\docx-course-report-writer
```

在 Codex 中点名使用：

```text
请使用 $docx-course-report-writer，根据 assignment.md、template.docx 和 src/ 生成中文实验报告。
需要真实运行、截图、导出 DOCX 和 PDF。
```

### 推荐输入

| 输入 | 为什么需要 |
| --- | --- |
| 课程要求 / rubric | 锁定评分点和报告结构 |
| DOCX 模板 | 保留学校或课程格式；未提供时使用内置默认模板 |
| 代码、日志、截图、数据 | 形成证据链，避免编造实验结果 |
| 参考文献或论文链接 | 支撑综述、课程论文和技术事实 |
| 姓名、学号、课程名、教师名 | 生成正式封面 |
| 是否允许 AI 图片及数量 | AI 图像是阻塞式 intake 问题，不能静默默认 |

<a id="workflow"></a>

## 工作流

```mermaid
flowchart LR
  A["Scope intake<br/>任务 / 模板 / AI 图片"] --> B["Evidence plan<br/>事实台账 / 截图计划"]
  B --> C["Actor cycle 1<br/>写作 / 绘图 / 生成 DOCX"]
  C --> D["Critic cycle 1<br/>审查真实产物"]
  D --> E["Actor cycle 2<br/>源头修复 / 重新导出"]
  E --> F["Critic cycle 2<br/>复审 DOCX/PDF"]
  F --> G{"阻塞问题清零?"}
  G -- "否" --> E
  G -- "是" --> H["Final gates<br/>Word 字段 / PDF / 页面渲染"]
  H --> I["交付报告包"]
```

完整流程见 [`references/workflow.md`](references/workflow.md)。

## 默认模板与生成器

模板优先级：

1. 用户提供的 DOCX 模板。
2. 内置默认模板：[`skill-assets/default-course-report-template.docx`](skill-assets/default-course-report-template.docx)。
3. 只有用户明确要求空白文档时，才使用无模板文档。

默认构建器会：

- 填充封面元信息，移除 `放置`、`校徽`、`《XXXX》` 等占位符。
- 将封面压缩到第一页，避免日期或空白封面内容溢出到第二页。
- 生成真实 Word Heading 和自动 TOC 字段。
- 使用 `图<章号>.<序号>` 形式生成正式图注。
- 默认不把 `图片来源：...` 渲染进正文，来源信息放入 sidecar 文件。
- 在 `参考文献` 前插入分页。

## QA 命令示例

```powershell
python scripts\qa_docx_report.py `
  --docx report.docx `
  --require-toc `
  --require-cover `
  --min-images 4 `
  --min-tables 3 `
  --min-heading1 6 `
  --require-reference-pagebreak `
  --require-formal-figure-captions `
  --forbid-image-source-lines
```

Word 字段更新与 PDF 导出：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
  -File scripts\update_word_fields.ps1 `
  -DocxPath report.docx `
  -ExportPdf `
  -UseAsciiTemp
```

<a id="quality-gates"></a>

## 质量门

交付前必须通过或明确说明限制：

- 真实证据：实验结果、截图、数据、日志和引用不能凭空编造。
- 模板卫生：无旧主题、旧截图、旧目录、占位符和乱码。
- 封面与目录：封面只占第一页，目录页码右对齐，字段已更新。
- 图注规范：所有插图都有正式 `图x.x 标题`。
- 图像语义：箭头、标签、布局、缩放后的可读性通过审查。
- 参考文献：单独分页，事实与引用一致。
- PDF 渲染：检查目录页、图页、表格页、代码块页和参考文献页。
- 分析深度：实验报告必须有结果分析、失败原因、局限和个人理解。

完整清单见 [`references/report-qa-checklist.md`](references/report-qa-checklist.md)。

## 项目结构

```text
docx-course-report-writer/
├─ SKILL.md
├─ README.md
├─ README.en.md
├─ assets/
│  └─ logo.png
├─ skill-assets/
│  ├─ default-course-report-template.docx
│  ├─ report-draft-template.md
│  ├─ references-template.md
│  └─ image-attributions-template.md
├─ references/
│  ├─ workflow.md
│  ├─ actor-critic-loop.md
│  ├─ figures-and-diagrams.md
│  ├─ windows-word-fields.md
│  └─ report-qa-checklist.md
├─ scripts/
│  ├─ build_report.py
│  ├─ qa_docx_report.py
│  ├─ update_word_fields.ps1
│  └─ annotate_screenshot.py
├─ examples/
│  └─ sample-report/
└─ docs/
   ├─ deep-learning-architecture-report-demo.docx
   ├─ deep-learning-architecture-report-demo.pdf
   ├─ deep-learning-demo-cover.png
   ├─ deep-learning-demo-toc.png
   └─ deep-learning-demo-figure.png
```

## 常见问题

### 没有课程模板怎么办？

使用内置默认模板。它会保留正式封面、页面设置、标题层级、表格样式和目录结构，同时清理模板残留。

### 可以插入 AI 图片吗？

可以，但必须先询问用户是否开启，以及最多生成几张。AI 图片只能作为概念图或解释性图片，不能替代真实实验截图、真实数据图或真实运行结果。

### 为什么要导出 PDF？

DOCX 包结构通过不等于页面排版通过。目录、图表、表格、代码块和封面是否真的好看，必须看 Word 更新后的 PDF 或页面渲染。

### 为什么强调双轮 Actor/Critic？

课程报告常见缺陷往往发生在“初稿完成之后”：目录没更新、图注不规范、图被压缩、表格溢出、引用不一致。双轮审查把这些问题前置到交付前。

## 参考

- [`SKILL.md`](SKILL.md)：Skill 入口和强制运行契约。
- [`references/workflow.md`](references/workflow.md)：端到端报告工作流。
- [`references/figures-and-diagrams.md`](references/figures-and-diagrams.md)：图表、AI 图片、箭头和图注规范。
- [`references/windows-word-fields.md`](references/windows-word-fields.md)：Word COM、目录字段和 PDF 导出。
- [`docs/testing-report.md`](docs/testing-report.md)：测试与验证记录。
