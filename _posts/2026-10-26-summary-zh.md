---
layout: default
title: "Horizon Summary: 2026-10-26 (ZH)"
date: 2026-10-26
lang: zh
---

> 从 36 条内容中筛选出 3 条重要资讯。

---

1. [硅光调制器借内置电光均衡器实现 200 Gb/s PAM4](#item-1) ⭐️ 7.0/10
2. [Imec 探索垂直 3D DRAM 堆叠以改善 GPU 散热](#item-2) ⭐️ 6.0/10
3. [慕尼黑工大与 IIT 坎普尔指出多层 CFET 的自热与寄生限制](#item-3) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [硅光调制器借内置电光均衡器实现 200 Gb/s PAM4](https://semiengineering.com/silicon-photonic-modulator-reaches-200-gb-s-pam4-with-reduced-dsp-science-tokyo-yokohama-aist-petra/) ⭐️ 7.0/10

来自东京科学大学（Institute of Science Tokyo）、横滨国立大学、产业技术综合研究所（AIST）与光电子技术研究协会（PETRA）的研究人员在《Nature Communications》发表论文，展示了一种低电压慢光硅光子晶体波导调制器，借助内置电光均衡器实现单波长 200 Gb/s 的 PAM4 传输，并显著降低了对 DSP 的依赖。该内置均衡器在光/模拟域补偿器件的频率响应，从而减少收发机中高功耗数字信号处理的工作量。 AI 数据中心的多太比特光互连正日益受制于 DSP 功耗，以及传统硅马赫-曾德尔调制器在效率与带宽之间的权衡；把一部分均衡功能转移到光子器件内部，有望降低单比特功耗并简化收发机设计。如果该方案能够实现可制造化，将为 AI 集群的 scale-up 与 scale-out 提供更廉价、更密集的 200G 每通道光链路。 该器件是一种硅光子晶体波导慢光调制器，通过慢光效应在极短的尺寸内增强电光相互作用，从而在保持低驱动电压的同时借助内置电光均衡器扩展带宽；论文报告的结果是单波长 200 Gb/s PAM4 且 DSP 负担降低。这仍属于同行评审论文中的研究性演示，成品率、长期可靠性、工作温度范围以及与 CMOS 代工工艺的兼容性等指标尚未形成量产数据。

rss · SemiEngineering · 10月25日 20:49

**背景**: PAM4 是一种四电平脉冲幅度调制格式，每个符号携带两比特信息，由于能在相同符号速率下把吞吐量翻倍，已成为 400G 与 800G 短距光链路的主流选择。硅光技术用标准 CMOS 兼容工艺制造光调制器，但硅的电光效应较弱，导致器件必须在“长器件效率高但速度慢”和“短器件速度快但电压高”之间取舍。慢光结构与片上均衡正是研究者试图打破这一权衡的两条路径，目标是满足 AI 数据中心内部所需的高速、低能耗收发机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41467-026-78128-1">Reduced-DSP 200G/λ low-voltage slow-light silicon modulator ...</a></li>
<li><a href="https://www.science.org/doi/10.1126/sciadv.adi5339">Slow-light silicon modulator with 110-GHz bandwidth - Science</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-67826-x">Ultracompact and large-bandwidth silicon modulator in a CMOS ...</a></li>

</ul>
</details>

**发生了什么**: 东京科学大学、横滨国立大学、AIST 与 PETRA 的研究团队发表论文，展示一种低电压慢光硅光子晶体波导调制器，通过内置电光均衡器实现单波长 200 Gb/s PAM4 传输并降低 DSP 负载，面向 AI 数据中心光互连。
**为什么重要**: 该成果针对硅光调制器效率与带宽难以兼得的长期痛点，若未来可量产，可能降低每比特功耗并简化高速光模块的 DSP 架构，从而影响 AI 数据中心光互连的成本结构。
**影响产业链**: 理论上涉及硅光调制器、光引擎/光模块、DSP 与交换芯片等环节的价值分配，DSP 负担下降可能削弱 DSP 在模块物料成本中的占比，同时提升硅光芯片与晶圆代工环节的重要性；但当前仅为论文级演示，尚无收入、毛利率或现金流层面的可验证影响。
**可能相关公司**: Institute of Science Tokyo / AIST / PETRA（研究机构，非上市）, 硅光与光模块相关 A 股/美股标的（如中际旭创、新易盛、光迅科技、Coherent、Lumentum）仅供参考, DSP/SerDes 相关厂商（如 Marvell、Broadcom）仅供参考
**可信度**: 中：核心结果发表于同行评审的 Nature Communications，并有 Science Advances 等慢光调制器工作作为技术脉络佐证，来源可信度较高；但内容属研究演示，缺少任何订单、客户、产能或价格验证。
**投研价值评分**: 19 / 100
**是否需要继续追踪**: 是
**投研理由**: 评分为 19 分：论文级技术突破，novelty 给 4 分、source_confidence 给 8 分；capex_impact 仅 2 分（未涉及任何超大规模厂商或电信资本开支变化），order_evidence 为 0 分（缺少订单/客户/合同/部署规模证据），supply_demand_impact 仅 1 分（无价格上涨、短缺或产能瓶颈证据），platform_binding 为 3 分（面向 AI 数据中心但未绑定英伟达、云厂商或电信运营商等顶级平台），earnings_elasticity 仅 1 分（缺少收入结构、毛利率、利润与自由现金流验证）。整体缺少订单/客户/收入/产能/价格验证，按论文类新闻保守给分，需持续跟踪其是否进入代工工艺与商用光模块。

**标签**: `#silicon photonics`, `#optical interconnects`, `#PAM4`, `#modulators`, `#AI data centers`

---

<a id="item-2"></a>
## [Imec 探索垂直 3D DRAM 堆叠以改善 GPU 散热](https://semiengineering.com/vertical-dram-stacking-expands-thermal-design-space-beyond-hbm-imec/) ⭐️ 6.0/10

Imec 研究人员发表了一项封装级热仿真研究，评估将 DRAM 裸片垂直旋转堆叠在 GPU 上方并在层间加入散热腔的 3D 体积式 DRAM-on-GPU 架构，并以堆叠高度、内存容量和组织方式作为设计变量。 该研究检验垂直 DRAM 堆叠能否缓解当前 2.5D HBM 以及新兴 HBM-on-GPU 设计所面临的热与带宽约束；随着内存功耗和容量持续上升，这对未来 AI 加速器的封装路线具有重要意义。 该研究基于仿真而非硅片验证，现有摘要未报告实测温度、带宽、良率、成本或制造就绪度；它明确将散热腔和垂直布局定位为扩大热设计空间的手段。

rss · SemiEngineering · 10月26日 07:02

**背景**: 高带宽内存（HBM）是由硅通孔连接的多层 DRAM 裸片堆栈，通常通过硅中介层放置在 GPU 旁边，这种 2.5D 封装方式已成为 AI 加速器的核心。HBM-on-GPU 进一步将内存直接堆叠在 GPU 裸片上方，可缩短连接距离，但由于逻辑和内存都在极小体积内发热，散热挑战非常严峻。Imec 是比利时纳米电子研究机构，经常发布早期封装与热管理研究，用于引导半导体产业的长期路线图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/hbm-on-gpu-imec-iedm">HBM on GPU : Thermal Challenges and Solutions - IEEE Spectrum</a></li>
<li><a href="https://www.techradar.com/pro/hbm-on-gpu-set-to-power-the-next-revolution-in-ai-accelerators-and-just-to-confirm-theres-no-way-this-will-come-to-your-video-card-anytime-soon">Imec’s 3D HBM - on - GPU technology has its pros and cons | TechRadar</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0026271425001957">A review in thermal management for advanced chip packaging ...</a></li>

</ul>
</details>

**发生了什么**: Imec 发布了一项封装级热仿真研究，提出将 DRAM 裸片垂直堆叠在 GPU 上方并在层间加入散热腔的 3D 体积式 DRAM-on-GPU 架构，用于探索超越传统 HBM-on-GPU 的热设计空间。
**为什么重要**: 该研究面向未来 AI 加速器的高带宽、高功耗内存封装难题，若后续被产业界采纳，可能影响先进封装、HBM/DRAM 堆叠和散热技术的长期路线。
**影响产业链**: 若该架构未来走向量产，可能影响先进封装、HBM/DRAM、散热材料与设备环节，但当前仅处于仿真研究阶段，尚无收入、利润或现金流影响。
**可能相关公司**: imec（非上市研究机构）, SK 海力士, 三星电子, 美光科技, 台积电, 英伟达
**可信度**: 中：来源为 Semiconductor Engineering 对 imec 论文的摘要报道，可信度尚可，但缺少论文全文、实测数据和产业验证。
**投研价值评分**: 12 / 100
**是否需要继续追踪**: 否
**投研理由**: 该新闻属于 imec 的封装级热仿真研究，提出垂直 3D DRAM-on-GPU 与散热腔设计，技术新颖但缺少订单/客户/收入/产能/价格验证；按论文/研究类默认区间打分，总分 12，需等待流片、客户合作或量产部署信号。

**标签**: `#3D DRAM`, `#HBM`, `#GPU`, `#thermal management`, `#semiconductor packaging`

---

<a id="item-3"></a>
## [慕尼黑工大与 IIT 坎普尔指出多层 CFET 的自热与寄生限制](https://semiengineering.com/self-heating-and-parasitics-challenge-multi-tier-cfet-scaling-tu-munich-iit-kanpur/) ⭐️ 6.0/10

慕尼黑工业大学与印度理工学院坎普尔分校的研究人员发表了题为《多层 CFET 设计中的自热与寄生效应》的论文，分析了自热效应（SHE）以及中段工艺（MOL）与后段工艺（BEOL）寄生对多层垂直堆叠纳米片器件设计的制约。该研究量化了多层互补场效应晶体管（CFET）架构中热学与寄生耦合带来的性能损失，而非提出新的器件结构。 CFET 被普遍视为 2 纳米以下节点取代环栅纳米片晶体管的主要候选方案，因此量化热学与寄生代价可以告诉产业界垂直堆叠在实际中能推进到什么程度。由于这些代价会随堆叠层数增加而放大，它们直接影响未来先进制程设计规则与金属互连预算的制定。 该分析聚焦于多层堆叠结构，即多个纳米片器件上下叠放，并把自热与 MOL/BEOL 寄生作为相互耦合的约束而非彼此独立的效应来处理。摘要较为简短，未披露具体节点目标、仿真温升数值或寄生电阻电容数据，因此仅凭摘要尚无法判断各项损失的量化幅度。

rss · SemiEngineering · 10月26日 07:01

**背景**: 互补场效应晶体管（CFET）把 n 型与 p 型器件垂直叠放在同一投影面积内，中间由介质隔离层隔开，而不是并排放置，被视为 2 纳米之后环栅纳米片晶体管的自然继任者。中段工艺（MOL）指晶体管与金属布线之间的接触与局部互连层，后段工艺（BEOL）指多层金属互连叠层，两者都会引入寄生电阻与电容，导致开关变慢并增加功耗。自热是指密集排布且热隔离的纳米片沟道中功耗引起的温升，随着器件向上堆叠，散热路径变长，该问题会进一步恶化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2603.21910v1">Self-Heating and Parasitic Effects in Multi-Tier CFET Design</a></li>
<li><a href="https://ieeexplore.ieee.org/document/10292591">Vertically Stacked Nanosheet Number Optimization Strategy for ...</a></li>
<li><a href="https://www.insidedeeptech.com/cfet-complementary-fet-full-guide/">CFET: A Full Guide to Stacked Nanosheet Transistors After GAAFET</a></li>

</ul>
</details>

**发生了什么**: 慕尼黑工业大学与印度理工学院坎普尔分校发表学术论文，研究多层 CFET 设计中自热效应与 MOL/BEOL 寄生对垂直堆叠纳米片器件的制约。
**为什么重要**: CFET 是 2 纳米以下先进节点最受关注的结构方向之一，该研究提示垂直堆叠层数增加会同时放大散热与寄生代价，可能影响未来制程的设计规则与互连方案选择。
**影响产业链**: 属于早期器件物理与设计层面的研究，短期不改变任何设备、材料或代工环节的订单、产能、价格与收入；长期仅在 CFET 路线推进时才可能间接影响先进制程设备与互连材料的资本开支节奏。
**可能相关公司**: TSMC (TSM), Samsung Electronics (005930.KS), Intel (INTC), Applied Materials (AMAT), ASML (ASML), Lam Research (LRCX)
**可信度**: 中：论文来自 arXiv 预印本并由 Semiconductor Engineering 报道，机构可信度高，但内容为学术分析，无任何商业或财务披露。
**投研价值评分**: 18 / 100
**是否需要继续追踪**: 否
**投研理由**: 该消息为学术论文研究，缺少订单/客户/收入/产能/价格验证，也不涉及任何厂商资本开支变化，因此按论文类证据上限保守评分；来源可信度较高、主题新颖性尚可，构成主要得分项。

**标签**: `#semiconductors`, `#CFET`, `#advanced-nodes`, `#device-physics`, `#thermal-effects`

---