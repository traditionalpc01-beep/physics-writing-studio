# physics-writing-studio

把物理/材料/QLED 领域科学文本（中文或英文）改写成 Nature Portfolio 风格英文的写作 skill。由 [mumdark/nature-writing-studio](https://github.com/mumdark/nature-writing-studio) v2.x 转向而来：**v3.0.0 起整体转为纯物理领域**（QLED / 量子点 / PeLED / micro-LED / OLED / 半导体 / NiOx 空穴注入层），生物领域数据已全部清理，知识库基于 **189 篇 Nature 系开放获取物理论文**重新蒸馏。

当前版本：**v3.3.0**（2026-09-01）。

## 功能

- Nature 风格润色、中译英、去 AI 味
- 按章节改写：摘要 / 前言 / 方法 / 结果 / 讨论 / 图例 / 单句
- 整稿 `multi_section` 多节编排（自动选 SP 版式、跨节审计 X001-X010）
- 器件统计规范（average ± s.d. over N devices）与指标验证词表（EQE / luminance / LT50/LT95 / turn-on voltage / FWHM / CIE）强制证据锚定
- 改写后扫描 144 条 anti-AI 黑名单（critical/high），命中即替换或删除

## 知识库规模（v3.3.0）

| 文件 | 行数 | 说明 |
| --- | --- | --- |
| writing_rules.tsv | 97 | 含 R2000 器件规则、R3100-R3105 溅射工艺规则（本地 PDF 种子） |
| phrase_bank.tsv | 57 | 含 P2000 器件短语、P3100-P3105 溅射工艺短语 |
| anti_ai_patterns.tsv | 144 | A2000 按 189 篇语料实测校准 |
| opener_distribution.tsv | 5942 | 31.4 句开头/篇，口径 `occ>=2 ∪ 每篇每节 top5` |
| results_discussion_openers.tsv | 2002 | 10.6 首句模板/篇 |
| gap_transitions.tsv | 1532 | 按 (section, pivot_word) 索引 |
| cross_section_linkers.tsv | 725 | 节间衔接模板 |
| hedge_verbs.tsv | 134 | causal / associative / speculative 三档 |

全部蒸馏行的 DOI 溯源记录见 `skill/knowledge/PROVENANCE.md` 与 `provenance.json`。

## 语料与方法

189 篇 Nature Portfolio 开放获取论文（Nature Communications / Light: Science & Applications / Nature Electronics / Nature Materials / Communications Materials / Communications Physics 等），分 7 轮子 agent 定向采集：QLED/器件 → NiOx-HIL/SAM/功函数 → TMO 物理/掺杂 → 倒置 QLED/QD 界面 → 颜色/钙钛矿 NC/QD 物理 → 15 项指标关键词扩充 → 寿命/电流效率/NiOx 表征补漏。

蒸馏流水线：子 agent 采集（OA/付费墙校验）→ DOI 去重 → `scripts/distill_physics_corpus.py` → `merge_physics.py`（计数递增合并 + DOI manifest）→ `rebuild_openers.py`（口径重建）→ `run_e2e_sanity.py validate`。新增行 100% 可溯源到论文原文。

## 目录结构

```
skill/
  SKILL.md            调用契约
  CHANGELOG.md        版本历史
  agents/openai.yaml  agent 配置与 knowledge_summary
  prompts/            system_writer + style_guide + sections/<target>
  knowledge/          14 个 TSV 知识库 + PROVENANCE
  scripts/            蒸馏/合并/重建/校验脚本
  docs/               ROADMAP_v3
  fixtures/           测试样例
```

## 与上游的关系

- 保留上游 v2.x 的 Verification Layer（Rule 1a 硬溯源 / Rule 1b 通用知识 / Rule 2 em-dash 零容忍 / Rule 3 删改）、hedge 三档与多节编排架构
- prompt 中的示例实体全部换成器件物理（EQE、载流子、量子点、界面能级）
- 上游生物领域数据 18,863 行已删除；v3 语料全部为物理方向论文

## License

沿用上游仓库许可（见上游 README）。
