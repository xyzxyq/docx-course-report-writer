// Copy this folder and replace metadata/body/references before delivery.
// Use `typst fonts` to check the chosen CJK family; record any substitution.
#let cjk-font = "Songti SC" // Windows: "SimSun"; portable install: "Noto Serif CJK SC".
#let heading-font = "Heiti SC" // Windows: "SimHei"; portable install: "Noto Sans CJK SC".
#let latin-font = "Times New Roman"
#let course = "课程名称"
#let title = "报告题目"
#let college = "学院系别"
#let major = "专业名称"
#let student = "学生姓名"
#let student-id = "学生学号"
#let teacher = "任课教师"
#let date = "提交日期"

#set document(title: title, author: student)
#set page(paper: "a4", margin: 25.4mm, numbering: none)
#set text(font: (latin-font, cjk-font), size: 10.5pt, lang: "zh", top-edge: 0.88em, bottom-edge: -0.12em)
#set par(first-line-indent: (amount: 2em, all: true), leading: 6.5pt, spacing: 12.5pt, justify: true)
#set heading(numbering: (..nums) => {
  let ns = nums.pos()
  if ns.len() == 1 { numbering("第一章", ns.first()) }
  else { ns.map(str).join(".") }
})
#show heading: set block(above: 24pt, below: 12pt)
#show heading: set text(font: (heading-font, cjk-font), weight: "bold")
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  align(center, text(size: 16pt, it))
}
#show heading.where(level: 2): set text(size: 14pt)
#show heading.where(level: 3): set text(size: 12pt)
#set math.equation(numbering: "(1)")
#set figure.caption(position: bottom)
#set figure(numbering: n => context {
  numbering("1.1", counter(heading).get().first(), n)
})
// Resolve chapter numbers at the target, including references from later chapters.
#show ref: it => context {
  let el = it.element
  if el != none and el.func() == figure and it.form == "normal" {
    let prefix = if it.supplement == auto { el.supplement }
      else if type(it.supplement) == function { it.supplement(el) }
      else { it.supplement }
    link(el.location(), [#prefix #numbering("1.1", counter(heading).at(el.location()).first(), counter(figure.where(kind: el.kind)).at(el.location()).first())])
  } else { it }
}
// Reset figure and table counters only at numbered body chapters.
#show heading.where(level: 1): it => {
  if it.numbering != none {
    counter(figure.where(kind: image)).update(0)
    counter(figure.where(kind: table)).update(0)
  }
  it
}

#align(center)[
  #v(22mm)
  #text(font: heading-font, size: 18pt, weight: "bold")[《#course》]
  #v(12mm)
  #text(font: heading-font, size: 22pt, weight: "bold")[课程报告]
  #v(22mm)
  #set text(size: 13pt)
  #set par(first-line-indent: 0pt)
  #table(
    columns: (24mm, 90mm), stroke: none, inset: (y: 3mm), row-gutter: 3mm,
    align: (right, center),
    [实验题目], table.cell(stroke: (bottom: 0.5pt))[#title],
    [学院系别], table.cell(stroke: (bottom: 0.5pt))[#college],
    [专业名称], table.cell(stroke: (bottom: 0.5pt))[#major],
    [学生姓名], table.cell(stroke: (bottom: 0.5pt))[#student],
    [学生学号], table.cell(stroke: (bottom: 0.5pt))[#student-id],
    [任课教师], table.cell(stroke: (bottom: 0.5pt))[#teacher],
  )
  #v(1fr)
  #text(size: 10.5pt)[#date]
  #v(10mm)
]
#pagebreak()
#outline(title: [目 录], depth: 3)
#pagebreak()
#set page(numbering: "1", number-align: center)
#counter(page).update(1)

= 研究目的
本文为课程报告模板示例。正式报告应说明研究问题、任务要求和评价标准，所有结果须有可核验的来源。
== 任务与范围
围绕课程要求组织正文，区分已观察结果、解释和待验证假设。在线技术文档可作为工具使用说明的来源@typst-docs。

= 方法与结果
== 方法说明
公式示例：
$ macron(x) = 1/n sum_(i=1)^n x_i $ <eq-mean>
@eq-mean 表示算术平均值；实际分析应说明数据来源和适用条件。
#figure(
  box(stroke: 0.5pt, inset: 12pt, width: 80%)[
    #align(center)[研究问题 $arrow.r$ 方法设计 $arrow.r$ 证据分析]
  ],
  kind: image, supplement: [图], caption: [研究过程示意],
) <fig-process>
如 @fig-process 所示，结论应由证据支持。
#figure(
  table(columns: (1fr, 2fr), stroke: 0.5pt,
    table.header([项目], [记录要求]),
    [输入], [保留数据来源], [输出], [保存实际结果],
  ),
  supplement: [表], caption: [证据记录要求],
) <tab-evidence>

= 讨论与结论
结合实际结果说明限制，避免将模板示例作为实验结论。@tab-evidence 仅展示记录结构。

#pagebreak()
#show bibliography: set text(size: 10pt)
#show bibliography: set par(leading: 4pt, spacing: 10pt)
#bibliography("references.bib", title: [参考文献], style: "gb-7714-2015-numeric")
