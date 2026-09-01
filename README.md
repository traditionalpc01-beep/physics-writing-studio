<div align="center">

# 🔭 physics-writing-studio

**把物理 / 材料领域的中文草稿，改写成《Nature》顶刊风格的英文**

![Version](https://img.shields.io/badge/version-v3.3.0-2563eb)
![语料](https://img.shields.io/badge/语料-189%20篇%20Nature%20系论文-059669)
![知识库](https://img.shields.io/badge/知识库-14%20个%20TSV%20·%2010,700%2B%20行-7c3aed)
![平台](https://img.shields.io/badge/运行于-ZCode%20%2F%20Codex%20等%20AI%20助手-f59e0b)
![License](https://img.shields.io/badge/License-仅供研究%20·%20上游未声明-lightgrey)

由 [mumdark/nature-writing-studio](https://github.com/mumdark/nature-writing-studio) v2.x **转向纯物理领域**（QLED / 量子点）的衍生改版 · 知识库基于 189 篇 Nature 系开放获取物理论文重新蒸馏

[快速开始](#-快速开始) · [它能做什么](#-它能做什么) · [它是怎么工作的](#-它是怎么工作的通俗版) · [常见问题](#-常见问题) · [引用](#-引用) · [License](#-license)

</div>

---

## 🙏 致谢

- **[mumdark/nature-writing-studio](https://github.com/mumdark/nature-writing-studio)** —— 项目的起点。Verification Layer 校验体系（Rule 1a 硬溯源 / Rule 2 破折号零容忍 / Rule 3 删改）、hedge 三档证据分级、多节编排接口与整套蒸馏方法论，全部继承自其 v2.x 设计；
- **上游 v2.x 的原始蒸馏工作**——逐篇观察 412 篇 Nature 论文、LCS 引文校验 18/18 通过，本项目的物理知识库方法论直接受益于此；
- **189 篇开放获取论文的作者们**——没有你们把器件数据和方法细节写得清清楚楚，就没有这个素材库；
- **ZCode / OpenAI Codex 生态**——skill 的运行时与子代理采集流水线载体。

---

## 🤔 这是什么？（给第一次来的你）

一句话：**它是一位"顶刊文风润色师"，住在你的 AI 编程助手里。**

你把写好的中文（或英文）草稿交给它，它输出一段读起来像发表在 Nature 上的英文——不是机翻腔，也不是一眼假的"AI 味"。

打个比方：普通 AI 润色像"英语好的朋友帮你顺句子"；这个 skill 像一位**读过 189 篇量子点 LED 顶刊论文的老编辑**——他知道物理学家在摘要第一句习惯怎么开头、段落之间用什么句式承上启下、哪些浮夸词一出现就会被人识破是 AI 写的。

> 🎯 **方向聚焦**：QLED / 量子点 / 钙钛矿 / OLED / micro-LED / NiOₓ 空穴注入层。如果你的论文落在这个圈子里，它比通用润色工具更"懂行"。

**小词典**（后文出现的术语，30 秒看完）：

| 术语 | 通俗解释 |
| --- | --- |
| QLED | 量子点发光二极管：用纳米晶发光的新一代显示技术 |
| EQE（外量子效率） | 每 100 个注入电子最终发出多少个光子，LED 最核心的效率指标 |
| T₅₀ / T₉₅ | 器件亮度衰减到初始值 50% / 95% 所需的工作时长，即"寿命" |
| NiOₓ | 氧化镍薄膜，QLED 里常用的"空穴注入层"材料，也是本项目的用户侧研究方向 |
| TSV | 一张 Excel 式的素材表格，本项目的知识库就是 14 张这样的表 |

## ✨ 它能做什么

- ✍️ **全流程改写**：摘要 / 前言 / 方法 / 结果 / 讨论 / 图注 / 单句，或整稿多节一键编排
- 🇨🇳 → 🇬🇧 **中译英**、英文润色、去 AI 味，三种活都能干
- 🧪 **指标强制证据锚定**：EQE、亮度、寿命、起亮电压……草稿里没写的数字一律标 `[TBD]`，**绝不替你编数据、编引用**
- 🚫 **反 AI 味安检**：内置 144 条"AI 高频用词黑名单"（如空泛的 *excellent performance*、滥用破折号），改写完自动扫描，命中即替换
- 📐 **顶刊统计规范**：自动使用 *average ± s.d. over N devices* 这类 Nature 系标配表述

## 👀 一个例子（示意）

| 你写给它的 | 它输出的（Nature 风格，示意） |
| --- | --- |
| 我们做了一种掺锂的氧化镍薄膜，用来帮助量子点 LED 注入电荷。器件更亮了，效率也更高，寿命很长，综合性能非常出色。 | We fabricated a Li-doped NiOₓ hole-injection layer by RF magnetron sputtering. QLEDs based on this layer exhibited an EQE of 21.4% and a maximum luminance of 8.6 × 10⁴ cd m⁻², with T₉₅ of 1,240 h at an initial luminance of 100 cd m⁻². |

改动点：① 浮夸词"非常出色"→ 换成具体指标；② 补上制备方法关键词；③ 效率/亮度/寿命按顶刊惯用格式表述。
⚠️ 示例中的数字仅为演示——**实际输出只用你草稿里给出的数字，缺的标 `[TBD]`**。

## 🚀 快速开始

**第 1 步 · 安装**（让 AI 助手替你装）：

对 ZCode / Codex 说：

```text
请从 https://github.com/traditionalpc01-beep/physics-writing-studio 安装这个 skill
```

**第 2 步 · 使用**：把草稿发给助手，并说明目标章节，例如：

```text
用 physics-writing-studio 把下面这段改成 Nature 风格英文（target=abstract）：
<粘贴你的摘要>
```

**第 3 步 · 拿结果**：每次输出 = 改写正文 + 精简版 + 改写说明（告诉你它改了什么、为什么改）。

## ⚙️ 它是怎么工作的（通俗版）

三步流水线，全部本地规则、不联网：

1. **素材库**：14 张 TSV 表，存着从 189 篇论文里统计出来的"高频开头 / 承上启下 / 收尾句式"——写摘要时优先挑 Nature 作者最常用的那几种开头；
2. **写作规则**：97 条规则管结构（如方法节过去时被动语态带完整工艺参数），134 个动词分三档管"语气与证据匹配"（强证据用 *demonstrate*，推测才用 *may*）；
3. **反 AI 味安检**：改写结果过一遍 144 条黑名单，命中浮夸词、模板腔立即重写。

<details>
<summary><b>📦 知识库规模（点开看明细，v3.3.0）</b></summary>

| 文件 | 行数 | 内容 |
| --- | --- | --- |
| opener_distribution.tsv | 5,942 | 句开头素材（31.4 条/篇，口径 `occ≥2 ∪ 每篇每节 top5`） |
| results_discussion_openers.tsv | 2,002 | 结果/讨论节首句素材（10.6 条/篇） |
| gap_transitions.tsv | 1,532 | 转折/递进句式（按章节 + 转折词索引） |
| cross_section_linkers.tsv | 725 | 章节间衔接句式 |
| writing_rules.tsv | 97 | 写作规则（含 R3100-R3105 溅射工艺规则） |
| anti_ai_patterns.tsv | 144 | 反 AI 味黑名单（A2000 已按 189 篇实测校准） |
| hedge_verbs.tsv | 134 | 证据强度三档动词表 |
| phrase_bank.tsv | 57 | 器件/工艺短语模板 |
| 其余 6 张 | — | 领域指标词表、叙事模板、句长统计等 |

每条蒸馏行都带论文 DOI 溯源，见 [skill/knowledge/PROVENANCE.md](skill/knowledge/PROVENANCE.md)。版本历史见 [skill/CHANGELOG.md](skill/CHANGELOG.md)。

</details>

<details>
<summary><b>🔬 语料与方法（点开看）</b></summary>

- **189 篇** Nature Portfolio 开放获取论文（Nat. Commun. / Light Sci. Appl. / Nat. Electron. / Nat. Mater. / Commun. Mater. / Commun. Phys. 等），7 轮 AI 子代理定向采集：QLED 器件 → NiOx 空穴注入 / SAM / 功函数 → 过渡金属氧化物物理 → 倒置 QLED / 量子点界面 → 颜色 / 钙钛矿 NC → 15 项指标关键词扩充 → 寿命 / 效率 / 薄膜表征补漏；
- 每篇强制校验：OA 全文、章节完整、无付费墙、DOI 去重；
- 蒸馏流水线全部脚本化（`skill/scripts/`）：采集 → 去重 → 蒸馏 → 合并 → 口径重建 → 一致性校验；新增行 100% 可回溯到论文原句；
- 另有 1 篇论文被"扣下"从未入库，专门用作盲测复核（holdout 验证）。

</details>

## ❓ 常见问题

**Q：我不是物理专业的，能用吗？**
能。把中文草稿交给它就行；但专业内容对不对仍需你自己把关——它管"怎么说得像顶刊"，不管"结论是否成立"。

**Q：它会编数据吗？**
规则上禁止。没写的数字标 `[TBD]`，引用一律 `[1] [2]` 占位，最终成稿由你填真实值。

**Q：和直接让 ChatGPT 润色有什么区别？**
区别在"先验"：它的每个句式选择都有 189 篇真实论文的出现频率统计撑腰，且有对抗黑名单压制 AI 味——相当于把老编辑的"手感"做成了可复用的规则库。

## 📄 引用

如果本项目帮到了你的论文或研究，欢迎引用：

```bibtex
@software{physics_writing_studio_2026,
  author = {traditionalpc01-beep},
  title  = {physics-writing-studio: Nature-style English rewriting skill
            for QLED / quantum-dot physics},
  year   = {2026},
  url    = {https://github.com/traditionalpc01-beep/physics-writing-studio},
  note   = {Physics-domain derivative of mumdark/nature-writing-studio (v3.3.0)}
}
```

上游项目（本项目的架构与方法论来源）：

```bibtex
@software{nature_writing_studio_2026,
  author = {mumdark},
  title  = {nature-writing-studio},
  year   = {2026},
  url    = {https://github.com/mumdark/nature-writing-studio},
  note   = {Upstream project: Verification Layer, hedge tiers,
            multi-section orchestration and distillation methodology}
}
```

> 📚 **语料说明**：知识库引文均溯源至 189 篇开放获取论文（逐行 DOI 见 `skill/knowledge/provenance.json`）。论文全文受出版社版权保护，**本仓库不存储、不再分发任何论文全文**，仅包含句式级引文摘录。

## 📜 License

⚠️ **请先读这一段再复用本仓库**：

1. **上游未声明开源许可**。上游仓库 [mumdark/nature-writing-studio](https://github.com/mumdark/nature-writing-studio) 截至 2026-09-01 未附带 LICENSE 文件，依默认版权条款保留所有权利。本仓库是在其 v2.x 基础上的衍生改版，沿用了其架构、部分通用写作规则与反 AI 黑名单行，因此**仓库整体仅供学习与研究使用，不授予再分发或商业许可**；
2. **新增内容归属**：物理领域蒸馏数据（knowledge/ 中物理方向行）、`skill/scripts/` 蒸馏脚本与文档为仓库作者（traditionalpc01-beep）新增；若上游日后声明开源许可，本仓库将跟进对齐；
3. **异议通道**：如你是上游作者，对本仓库的任何内容有异议，请提 issue，我们会及时调整或移除相关内容；
4. **第三方语料**：论文全文版权归属各自出版社与作者，本仓库仅含句式级引文摘录与 DOI 溯源（见 `skill/knowledge/PROVENANCE.md`）。
