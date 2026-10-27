# 多智能体协作研究综述 · 三格式实测

本例来自2026-10-27的真实产出测试：约5,138个中文字、5章、15小节、14条参考文献，覆盖引言、已有工作、当前热点、未来研究和个人思考。三路使用同一正文与文献，分别构建；不是把同一个PDF改名复制。检索是选择性综述，未开展新的模型性能实验。

| 格式 | 报告 | 编辑入口 | 已验证范围 |
|---|---|---|---|
| DOCX | [文档](report.docx) · [10页LO预览](report-docx-preview.pdf) | Word/WPS编辑 | 正文、图、引文与分页检查通过；第2页自动目录未更新，**不是提交定稿** |
| LaTeX | [11页PDF](report-latex.pdf) | [main.tex](latex/main.tex)及相邻文献/资产 | 原生编译、自动一致性及独立逐页审查通过 |
| Typst | [10页修订PDF](report-typst.pdf) | [main.typ](typst/main.typ)及相邻文献/资产 | 按用户密排反馈修订；正文实测行距12.02→17.00pt，全部10页布局自查及回归检查通过 |

## 同一段正文的实际渲染

| DOCX（LibreOffice预览） | LaTeX | Typst（间距修订后） |
|---|---|---|
| [![DOCX正文](previews/docx-body.png)](report-docx-preview.pdf) | [![LaTeX正文](previews/latex-body.png)](report-latex.pdf) | [![Typst正文](previews/typst-body.png)](report-typst.pdf) |

旧Typst版的密排不是已经被用户接受的风格偏好；本次反馈已转为默认模板和实际PDF行距回归测试。参考文献与标题间距也已放宽。修订前后对照：[旧版正文](previews/typst-before.png) / [修订正文](previews/typst-body.png)。

## 可编辑插图

[原生PPTX](figures/collaboration.pptx) · [矢量PDF](figures/collaboration.pdf) · [SVG](figures/collaboration.svg)

最终正文仅插入1张概念图。AI生成参考后进行一次关系结构编辑，再重建为14个文本框、11个流程框、8条连接线；PPT没有图片对象，图PDF含29条矢量绘制路径且没有嵌入位图。图是文献综合，不代表新实验或普遍有效的统一算法。字体与箭头度量略有差别，轻微渐变改为纯色。

## 复建与证据

在latex目录执行 `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`；在typst目录执行 `typst compile main.typ report.pdf`。本机使用TeX Live 2026与Typst 0.15.1；Typst依赖Songti SC、Heiti SC、Times New Roman等已配置字体，跨主机可能需要明确替换并复核。

[引用台账](references-ledger.json)、[排版验证](checks/typst-layout.json)、[图结构检查](checks/figure-structure.json)、[发布文件哈希](checks/published-files.json)随样例保存。写作子代理与首轮独立终审均请求gpt-6.1-sol/high；请求参数不等于宿主另行证明了实际运行型号。最新Typst是用户反馈后的主agent布局自查，未冒称重复独立终审。

DOCX预览PDF清理了遗留的标题/作者元数据，并逐页比较渲染像素哈希确认页面未变。发布DOCX仅移除了模板遗留的作者/修改者等核心元数据，正文XML、关系、样式、媒体等其他ZIP部件逐字节保持一致。没有上传原论文全文、运行凭据、环境或缓存。

WPS操作工具失败，LibreOffice宏也未成功更新目录；使用DOCX前仍须更新整个目录、保存并重新导出检查。示例封面没有虚构个人信息，正式提交须按课程要求填写。
