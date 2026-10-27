# GitHub Skills 调研与吸收建议

日期：2026-10-27。对象：`docx-course-report-writer`。本地基线：`1e2f7bb`。

> 后续状态：本轮调研后，模板占位符缺陷已修复，引用与图表检查规则已做第一批适配；详见[实施与验证记录](verification-2026-10-27.md)。下文保留调研当时的结论，“尚未实施/修复”描述的是该历史阶段。

**结论：优先吸收局部编辑保真、引用身份核对、数据图语义检查和对照评估方法；不整包叠加高星技能。** 本轮是检索、取舍与缺陷验证，尚未修改运行中的 skill 或实现修复。

## 1. 检索边界与证据强度

- 使用 GitHub 连接器执行 12 组仓库检索，返回 192 条记录、去重 180 个候选。每组最多取首屏 20 条，采用连接器默认排序；不能宣称覆盖 GitHub 全部相关仓库或形成全站星数榜。
- 对 35 个候选通过 GitHub 公共 REST API 核对仓库星数、默认分支、更新时间、归档状态及许可证元数据；对其中 13 个仓库定向阅读相关 SKILL、流程说明、README 或许可文件。定向阅读不等于全部代码审计或执行验证。
- 通用方向优先查看 ≥1,000 星项目，中文 DOCX、Typst 等细分方向保留 100–999 星候选；9 星的中文 Typst 项目仅作为检索覆盖记录，未归为高星推荐。
- 星数属于整个仓库，不能当成单个 skill 的评分。检索命中是发现线索，仓库自述是作者主张，只有本地复现结果是本项目的实测证据。
- 本次没有安装、执行或整体复制外部技能，没有启用外部多 agent 流程，没有运行在线付费服务。维护任务不触发报告格式/AI 插图问询。

可复核记录：[检索词与原始候选名](github-skills-search-2026-10-27.json)、[35 个仓库的元数据快照](github-skills-metadata-2026-10-27.json)。星数快照日期为上述日期，后续会变化。`license: null` / `NOASSERTION` 表示 API 未识别出标准许可，不能推断为可自由复制。

## 2. 文档生成与模板保真

| 项目 / 仓库星数 | 已阅读来源 | 值得吸收 | 不采用 / 适配边界 |
|---|---|---|---|
| MiniMax-AI/skills · 13,728 | [minimax-docx](https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-docx/SKILL.md)、[编辑流程](https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-docx/references/scenario_b_edit_content.md) | 区分新建、局部填充和套模板；处理跨 run 占位符；编辑前后比较非目标内容 | 不迁移到 .NET；不把“清除所有直接格式”“所有章节奇数页开始”当作通用规则；自动修复和局部 XSD 检查也不能证明版式保真 |
| anthropics/skills · 184,077 | [DOCX skill](https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md)、[专项许可](https://github.com/anthropics/skills/blob/main/skills/docx/LICENSE.txt) | 将结构有效、修订标记完整和实际渲染区分开；跨 run 文本是重要测试场景 | 专项目录标注 proprietary 且许可含复制/衍生限制；本轮只记录对比结论，不引入其代码或提示词；不增加 docx-js 后端 |
| Gostyan/docx-skill-4-cn-paper · 461 | [中文 DOCX skill](https://github.com/Gostyan/docx-skill-4-cn-paper/blob/main/docx-editor-cn/SKILL.md)、[目录许可](https://github.com/Gostyan/docx-skill-4-cn-paper/blob/main/docx-editor-cn/LICENSE.txt) | 中文论文三线表、SEQ 图表编号、公式布局可作为以后专项测试的参照 | 与当前字体、引用和章节规则大量重合；不把单一论文格式覆盖所有课程模板。目录标 MIT，实际引入文件前仍需核对来源与第三方内容 |
| openai/skills · 28,332 | [PDF skill](https://github.com/openai/skills/blob/main/skills/.curated/pdf/SKILL.md) | 以渲染页核对视觉结果，文本提取只作辅助 | 当前已实现逐页检查，增量较小；不为此替换现有 pypdfium2 或追加 Poppler 安装要求。当前公开 curated 目录未列出 DOCX skill，不把旧印象当成现状 |

本项目已覆盖模板副本编辑、字段定稿、逐页检查及目标办公软件的保真边界。新增价值集中在**保留非目标 run、域与图片的行为测试**，不是再加一段“保持格式”的口号。

## 3. 文献与学术写作

| 项目 / 仓库星数 | 已阅读来源 | 值得吸收 | 不采用 / 适配边界 |
|---|---|---|---|
| K-Dense-AI/scientific-agent-skills · 54,843 | [citation-management](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/citation-management/SKILL.md)、[scientific-writing](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-writing/SKILL.md) | 标识符与书目信息去重；核对预印本/正式发表版本；补齐真实存在的缺失字段；区分元数据检查与正文证据核验 | 保留当前紧凑台账；不为所有课程报告引入逐行 claim hash、临床注册/投稿声明流程或最低文献数；不依赖 Scholar 抓取。当前宿主已有 citation-management，优先按需复用 |
| Imbad0202/academic-research-skills · 54,095 | [academic-paper](https://github.com/Imbad0202/academic-research-skills/blob/main/academic-paper/SKILL.md)、[许可](https://github.com/Imbad0202/academic-research-skills/blob/main/LICENSE) | 根据任务区分写作、修订、查引用；按需参考用户原稿风格 | 不引入 12-agent 管线、复杂路由和跨阶段强制澄清；许可文本为 CC BY-NC 4.0，本轮不复制其实现或提示词 |
| zLanqing/codex-claude-academic-skills · 5,365 | [research-writing-skill](https://github.com/zLanqing/codex-claude-academic-skills/blob/main/research-writing-skill/SKILL.md) | 区分已有证据、用户确认、推断和建议；章节按论点、证据、解释、局限组织 | 当前入口与证据台账已基本覆盖；无需再新增平行写作工作流 |
| yunshenwuchuxun/latex-paper-skills · 271 | [README 与技能目录说明](https://github.com/yunshenwuchuxun/latex-paper-skills/blob/main/README.md) | 实验结果 planned / placeholder / verified 状态及结果回填思路 | 只读到框架/示例说明，未验证内部脚本；不迁入多模型 CLI、IEEE 默认模板或整套 issue 驱动流程 |
| serenakeyitan/citation-check-skill · 257 | [README](https://github.com/serenakeyitan/citation-check-skill/blob/main/README.md) | 先列关键断言再核验；区分仅给定材料与公开检索模式 | 不采纳“所有断言都必须有外部引用”“所有舍入差异都是错误”“相同输入必然相同输出”等绝对化主张。应区分精度要求、缺证据与已证伪；未验证其运行能力 |

拟吸收的引用规则必须保留以下限制：同 DOI 可以提示重复，但不同版本不能只凭相似标题静默合并；引用版本改变后要重新核对支撑段落；没有卷期页码的 online-first 记录不应凭空补齐。现有 GB/T 7714 格式和用户模板优先级继续适用。

## 4. 科研图表、Typst 与评估

| 项目 / 仓库星数 | 已阅读来源 | 值得吸收 | 不采用 / 适配边界 |
|---|---|---|---|
| Haojae/scipilot-figure-skill · 2,716 | [SKILL.md](https://github.com/Haojae/scipilot-figure-skill/blob/main/SKILL.md) | 先核对数据形态与图的论证目标；交代样本量和误差区间含义；使用颜色之外的区分方式；按最终插入尺寸检查 | 不照搬所有图型禁令、固定字号/期刊尺寸、强制期刊问询或无限回改；课程报告按实际需求裁剪 |
| apcamargo/typst-skills · 232 | [typst-author](https://github.com/apcamargo/typst-skills/blob/main/typst-author/SKILL.md) | 遇到不确定 API 时核对编译器版本和对应文档，再做最小验证；保留现有视觉风格 | 不复制整套语言手册；不把每次编辑都运行 formatter 变成门槛。未识别出仓库标准许可，不直接搬运文件 |
| obra/superpowers · 305,784 | [verification-before-completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | 完成声明需要对应实际成品和验证证据 | 当前已覆盖版本绑定与修复后检查；不引入整套 Superpowers，不机械要求每条消息重复所有检查 |
| benchflow-ai/skillsbench · 1,874 | [README](https://github.com/benchflow-ai/skillsbench/blob/main/README.md) | 用真实任务产物、可执行验收和有/无 skill 对照评价效果 | 属于评估框架，非报告写作 skill；不为本项目安装云沙箱或整套基准。可用本仓库现有 unittest 与固定小样例实现局部比较 |

另定向查看 [Anthropic skill-creator 的评估章节](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)：旧版/新版对照和区分客观验收与主观质量值得参考；不采用其固定并发启动方式，不以外部调研文档作为当前运行多 agent 的授权。

## 5. 本地已验证的首要缺陷

**Major：占位符替换会破坏同段非目标内容。** 位置：[build_report.py](../scripts/build_report.py) 的 `replace_paragraph_text()`（基线第 496 行），调用者为 `replace_text_placeholders()` 的正文和表格路径。

复现输入是一份内存中的合成文档，单段包含：加粗“姓名：”、分在两个 run 的 `{{STUDENT_NAME}}`、带下划线的“（请核对）”和一个内嵌图片。调用 `replace_text_placeholders(doc, {"STUDENT_NAME": "张三"})` 后：

| 检查 | 替换前 | 实际替换后 |
|---|---|---|
| 正文文字 | 姓名：`{{STUDENT_NAME}}`（请核对） | 姓名：张三（请核对），文字正确 |
| 非目标尾注下划线 | 存在 | 尾注被并入首个加粗 run，下划线不再作用于文字 |
| 段内 `w:drawing` 数量 | 1 | 0，内嵌图片被删除 |

原因来自本地源码：函数把每个 run 的 `.text` 设为空，再把整段文本放进第一个 run。保留了段落对象不等于保留段内内容。该问题可使学校模板中的同段标识图或局部格式丢失；本例不证明所有模板都受影响。

执行环境：现有 `output/vector-e2e/venv/bin/python`；使用 python-docx 创建合成段落和临时 PNG。断言确认上述文字、下划线和图片结果；未使用 Word/WPS 目视验证。完整观测保存在忽略目录 `output/github-skill-research-2026-10-27/placeholder-reproduction.json`。下面是不需要图片文件的最小格式复现：

```python
import sys
from docx import Document
sys.path.insert(0, "scripts")
from build_report import replace_text_placeholders

doc = Document()
p = doc.add_paragraph()
p.add_run("姓名：").bold = True
p.add_run("{{STUDENT_").italic = True
p.add_run("NAME}}").italic = True
p.add_run("（请核对）").underline = True
replace_text_placeholders(doc, {"STUDENT_NAME": "张三"})
assert p.text == "姓名：张三（请核对）"
assert not any(r.text == "（请核对）" and r.underline for r in p.runs)
```

最后一个断言记录**现有缺陷**，不是正确行为的验收。修复后的测试应反过来断言尾注内容及格式仍保留，并覆盖图片。

## 6. 最小实施队列（尚未实施）

| 顺序 | 改动与触达范围 | 为什么值得做 | 最小验收 |
|---|---|---|---|
| 1 · 必须修复 | `scripts/build_report.py` 的局部替换逻辑、全部正文/表格调用者、`tests/test_build_report_format.py` 和模板保真测试 | 已复现同段内容丢失；直接影响已承诺的模板保真 | 单 run/跨 run/多占位符正确；非目标格式、域、图片不变；正文与表格均覆盖；相同输入重跑不损坏成品。不把复杂超链接/修订跨界默认为普通文本 |
| 2 · 推荐 | `references/source-quality.md` 与现有引用 QA；优先复用已安装 citation-management 的适用能力 | 防止同文献多键重复、预印本与正式版混淆 | 两个同 DOI 条目能识别；版本不同先核实；更换版本后重新核对证据，不虚构缺失字段 |
| 3 · 推荐 | `references/figures-and-diagrams.md` 与对应 QA 项 | 现有图形检查偏重渲染和箭头，统计图语义仍可补足 | 含误差线的图交代 n 与 SD/SEM/CI；类别数据不暗示不存在的连续关系；颜色之外仍可区分；不虚构统计结果 |
| 4 · 评估方式 | 复用现有测试、运行记录与少量固定样例，不新增通用评估框架 | 验证新规则改变了实际输出，而不只增加提示词 | 旧版与新版使用相同材料、同模型/工具条件；记录成品缺陷、时间和可获得的 token 数据；没有基线就不声称提高准确率或效率 |

基线评估建议只设五个任务：混合格式占位符、重复/不同版本引用、含误差区间的数据图、Typst 原生工程修订、课程报告小改动。最后一项检查新规则是否造成额外安装、无关澄清或过量审阅。每个任务按实际问题比较，不能将通过五个样例解释成全场景正确率。

## 7. 已有能力与明确排除项

已有能力：任务要求映射、关键论点证据台账、GB/T 7714、三格式路由、模板副本编辑、实际渲染检查、有限修复预算、按需协作。只在发现真实缺口时修改这些机制。

排除：整包复制技能集合；扩建新的转换后端；强制安装所有工具；所有课程报告强制 IMRaD/PRISMA/期刊投稿流程；“降 AI 率”或文风诊断替代学术真实性；无上限审查循环；用目录站星数给收录技能背书。

ComposioHQ、VoltAgent、travisvn 等高星集合用于发现候选，不作为实现质量证据。OfficeCLI、Pandoc 模板等属于潜在工具/模板候选，未因其星数而迁移当前后端。其余仅完成元数据核对的候选保留在 JSON 中，不能描述为已完成源码评审。

## 8. 本轮交付与限制

交付为本报告、12 组检索记录和 35 个仓库元数据快照；本地缺陷复现是额外诊断证据。运行 skill、安装目录、依赖、配置、提交和发布均未改变。

尚未执行外部技能端到端测试、旧新版 A/B、Windows/Word/WPS 验证或项目全量回归；本轮没有功能修改，不能声称缺陷已经修复或 skill 质量已提高。下一实施项是第 1 项模板局部替换保真修复。
