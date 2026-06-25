---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 103 条内容中筛选出 10 条重要资讯。

---

1. [AI 设计出人类无法想象的射频芯片](#item-1) ⭐️ 9.0/10
2. [Google DeepMind 为 Gemini 3.5 Flash 加入计算机使用能力](#item-2) ⭐️ 9.0/10
3. [AMD 驱动 TOP500 前十中四台，中国 LineShine 登顶](#item-3) ⭐️ 8.0/10
4. [英伟达领跑数据中心以太网交换市场，IDC 报告](#item-4) ⭐️ 8.0/10
5. [高通以约 40 亿美元收购 Modular，强化 AI 软件能力](#item-5) ⭐️ 8.0/10
6. [Agility Robotics 通过 25 亿美元 SPAC 合并上市](#item-6) ⭐️ 8.0/10
7. [SK 海力士凭 HBM AI 内存超越三星市值](#item-7) ⭐️ 8.0/10
8. [美光预测 AI 需求将导致 2027 年后内存短缺](#item-8) ⭐️ 8.0/10
9. [提出基于基础模型的连续物理推理](#item-9) ⭐️ 7.0/10
10. [UCIe 与 BoW：实用芯片互连标准对比](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI 设计出人类无法想象的射频芯片](https://spectrum.ieee.org/ai-radio-chip-design) ⭐️ 9.0/10

普林斯顿大学的研究人员利用强化学习和逆向设计方法，生成了新颖的射频集成电路（RFIC）布局，实现了创纪录的性能并大幅缩短了设计时间。 这一突破有望加速 5G、6G、自动驾驶和卫星通信等无线技术的发展，因为它克服了传统上依赖人类多年经验的 RFIC 设计'暗艺术'。 研究团队使用扩散模型快速生成新颖或可解释的布局，并在 130 纳米 SiGe BiCMOS 工艺中制造原型以验证性能。该方法可以设计任意形状的多端口电磁结构，并与有源电路协同设计。

rss · IEEE Spectrum Artificial Intelligence · 6月24日 13:00

**背景**: 射频集成电路（RFIC）对于无线通信至关重要，但设计难度极大，通常需要多年的经验。传统设计方法依赖人类直觉和迭代优化。AI 驱动的逆向设计和强化学习提供了一种自动化优化这一过程的途径，类似于 AlphaGo 处理围棋的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41467-024-54178-1">Deep-learning enabled generalized inverse design of multi ...</a></li>
<li><a href="https://collaborate.princeton.edu/en/publications/deep-learning-enabled-generalized-inverse-design-of-multi-port-ra/">Deep-learning enabled generalized inverse design of multi ... Intelligent Inverse Designs of Impedance Matching Circuits ... Inverse Design of Multilayered Pixelated mm-Wave Power ... AI Is Designing Radio Chips That Humans Couldn’t Even Imagine AI is designing radio chips that humans couldn’t even imagine</a></li>

</ul>
</details>

**发生了什么**: 普林斯顿大学团队发表论文，证明用强化学习和逆向设计可自动生成高性能射频芯片布局，并在自然通讯期刊发表。
**为什么重要**: AI 方法可能改变射频芯片设计范式，但当前仅停留在学术研究阶段，无商业订单或量产计划。
**影响产业链**: 暂无实质影响，但如果未来商业化，可能影响射频芯片设计工具 EDA 市场及芯片制造。
**可能相关公司**: Cadence Design Systems, Synopsys, Ansys
**可信度**: 中（来源可靠但研究尚处早期，无订单证据）
**投研价值评分**: 12 / 100
**是否需要继续追踪**: 是
**投研理由**: 缺少订单/客户/收入/产能/价格验证。研究论文属学术突破，但无商业化证据，投资信号极弱。

**标签**: `#AI`, `#chip design`, `#RFIC`, `#reinforcement learning`, `#inverse design`

---

<a id="item-2"></a>
## [Google DeepMind 为 Gemini 3.5 Flash 加入计算机使用能力](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/) ⭐️ 9.0/10

Google DeepMind 在 Gemini 3.5 Flash 模型中引入了内置的计算机使用能力，使开发者能够构建可以跨浏览器、移动和桌面环境进行观察、推理和采取行动的智能体。 这标志着向能够自主与任何软件界面交互的 AI 智能体迈出了重要一步，可能大规模改变自动化、机器人技术和数字工作流程。 Gemini 3.5 Flash 是一个原生多模态推理模型，针对速度和成本进行了优化，现在内置了计算机使用能力。该模型可以点击、打字、滚动和检查屏幕截图，类似于 OpenAI 和微软的竞争产品。

rss · Google DeepMind Blog · 6月24日 16:30

**背景**: 计算机使用能力允许 AI 模型通过控制鼠标和键盘与图形用户界面（GUI）交互，从而实现数据输入和发票处理等任务的自动化。OpenAI 和微软已经探索了这一能力，Google 的加入为这一新兴的 AI 智能体范式带来了竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/">Introducing computer use in Gemini 3.5 Flash - The Keyword</a></li>

</ul>
</details>

**发生了什么**: Google DeepMind 发布了 Gemini 3.5 Flash 的内置计算机使用功能，允许模型操控浏览器和桌面界面。
**为什么重要**: 该功能标志着 AI 智能体能力的重大进展，可能推动自动化应用生态发展，并加剧与 OpenAI、微软在 agent 领域的竞争。
**影响产业链**: 主要影响 AI 模型服务、云计算和自动化软件产业链。短期内可能增加 Google Cloud API 调用量，但缺乏具体客户和收入数据。
**可能相关公司**: Alphabet (GOOGL)
**可信度**: 高，来源为 Google DeepMind 官方博客和 Google 开发者文档。
**投研价值评分**: 32 / 100
**是否需要继续追踪**: 是
**投研理由**: 产品发布，但缺少订单、客户采购、收入指引或部署规模等硬信号。依据规则，总分不超过 45。平台绑定中等（Google 生态），来源可信度高，但无直接财务影响。

**标签**: `#AI`, `#Gemini`, `#Google DeepMind`, `#computer use`, `#model capability`

---

<a id="item-3"></a>
## [AMD 驱动 TOP500 前十中四台，中国 LineShine 登顶](https://www.storagereview.com/news/amd-powers-4-of-the-top-10-on-the-june-2026-top500-as-chinas-lineshine-takes-no-1) ⭐️ 8.0/10

2026 年 6 月 TOP500 榜单中，AMD 技术驱动的系统达 191 台（同比增长 11%），占比 41%，前十名中有 4 台使用 AMD 处理器或加速器。中国基于华为 LingKun 架构的百亿亿次超算 LineShine 首次亮相即夺得第一，取代 El Capitan。 AMD 在 TOP500 中份额增长凸显其在 HPC 领域对抗 Intel 和 NVIDIA 的竞争力增强，而中国 LineShine 以自主架构进入百亿亿次时代，可能影响全球超算采购和基础设施投资方向。 LineShine 位于深圳国家超级计算中心，于 2026 年上半年投入使用，采用华为 LingKun 架构和 LX2 CPU。AMD Instinct MI350X 和 MI355X 加速器（CDNA 4 架构）被部分顶级系统采用。

rss · StorageReview · 6月24日 15:19

**背景**: TOP500 榜单每年两次基于 HPL 基准测试排名全球最强超算。AMD EPYC CPU 和 Instinct GPU 是现代 HPC 系统的关键组件。LineShine 是中国继神威·太湖之光后续型号后的第二台百亿亿次超算，体现了国家对自主研发 HPC 技术的持续投入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LineShine_(supercomputer)">LineShine (supercomputer) - Wikipedia</a></li>
<li><a href="https://www.top500.org/news/lineshine-debuts-no-1-top500-enters-new-global-exascale-era/">LineShine Debuts at No. 1 as the TOP500 Enters a New Global ...</a></li>

</ul>
</details>

**发生了什么**: 2026 年 6 月 TOP500 榜单发布，AMD 驱动的系统占比提升至 41%，中国 LineShine 首次上榜即获第一。
**为什么重要**: AMD 在 HPC 市场份额扩大可能影响其数据中心业务收入，LineShine 的国产架构显示中国超算自主化进展，但缺乏直接订单或财务数据。
**影响产业链**: AMD 的 EPYC 和 Instinct 出货量可能随超算部署增加，但新闻未披露具体采购量或合同。
**可能相关公司**: AMD, NVIDIA
**可信度**: 中等，新闻来自存储媒体，但 TOP500 数据公开可信，无官方收入或订单确认。
**投研价值评分**: 26 / 100
**是否需要继续追踪**: 是
**投研理由**: 缺少订单/客户/收入/产能/价格验证，仅榜单排名变化，投资信号弱。

**标签**: `#HPC`, `#AMD`, `#TOP500`, `#supercomputing`, `#LineShine`

---

<a id="item-4"></a>
## [英伟达领跑数据中心以太网交换市场，IDC 报告](https://www.datacenterknowledge.com/infrastructure/nvidia-overtakes-rivals-in-data-center-ethernet-switching-idc-says) ⭐️ 8.0/10

根据 IDC 报告，英伟达通过将其 Spectrum 以太网交换机作为 GPU 核心 AI 平台的一部分进行销售，已跃居数据中心以太网交换市场首位。 这标志着英伟达从 GPU 扩展至网络领域的战略，构建端到端 AI 基础设施生态，可能对思科、Arista 等传统网络厂商构成挑战。 IDC 报告强调英伟达成功将其 Spectrum-X 以太网平台与 GPU 系统捆绑销售，为 AI 工作负载提供优化性能。这与传统独立销售交换机的模式形成对比。

rss · Data Center Knowledge · 6月24日 13:41

**背景**: 数据中心以太网交换历来由思科、Arista 等厂商主导，但 AI 工作负载要求极高的带宽和低延迟。英伟达的 Spectrum-X 平台专为 AI 网络设计，与 InfiniBand 竞争。通过将网络与 GPU 和 CUDA 生态集成，英伟达提供了紧密耦合的解决方案，简化了 AI 数据中心的部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/networking/ethernet-switching/">Ethernet Switching for AI and the Cloud | NVIDIA</a></li>
<li><a href="https://drivenets.com/blog/why-infiniband-falls-short-of-ethernet-for-ai-networking/">InfiniBand vs Ethernet - Why Ethernet fits AI Networking needs</a></li>

</ul>
</details>

**发生了什么**: IDC 报告显示英伟达在数据中心以太网交换市场跃居第一，通过将其 Spectrum 以太网交换机作为 GPU AI 平台一体化的部分进行销售。
**为什么重要**: 这表明英伟达正从 GPU 计算扩展到网络基础设施，实现端到端 AI 平台整合，可能对传统网络厂商构成竞争压力。
**影响产业链**: 主要影响数据中心网络设备供应链，特别是以太网交换芯片和交换机厂商。英伟达的份额增长可能挤压思科、Arista 等传统厂商的市场空间。但缺乏具体订单或收入数据，影响程度待确认。
**可能相关公司**: NVDA, CSCO, ANET
**可信度**: 中 - IDC 为知名第三方研究机构，但新闻未提供详细报告数据，且缺乏英伟达官方确认或具体市场份额数字。
**投研价值评分**: 14 / 100
**是否需要继续追踪**: 是
**投研理由**: 缺少订单/客户/收入/产能/价格验证。新闻仅为 IDC 市场排名报道，无硬财务信号。平台绑定给予一定分数，但整体证据不足，总分保守为 14 分。

**标签**: `#Nvidia`, `#data center networking`, `#AI infrastructure`, `#Ethernet switching`, `#GPU computing`

---

<a id="item-5"></a>
## [高通以约 40 亿美元收购 Modular，强化 AI 软件能力](https://www.semiconductor-digest.com/qualcomm-to-acquire-modular/?utm_source=rss&utm_medium=rss&utm_campaign=qualcomm-to-acquire-modular) ⭐️ 8.0/10

高通宣布以约 39.2 亿美元收购专注于 AI 基础设施软件的初创公司 Modular Inc。该交易旨在加强高通在数据中心和边缘环境中生成式 AI 与代理式 AI 的软件基础。 此次收购使高通能够整合 Modular 开放的、可移植的 AI 软件栈，在快速增长的 AI 市场中获得更强竞争力。这标志着高通从硬件向更高价值软件层的战略延伸，可能影响边缘 AI 和数据中心计算格局。 Modular 以其 Mojo 编程语言和 MAX 引擎闻名，旨在提升 AI 模型的可移植性和性能。据报道，这笔收购价值近 40 亿美元，预计在未来几个月内完成，尚需监管批准。

rss · Semiconductor Digest · 6月24日 21:13

**背景**: 生成式 AI 指能创造新内容的 AI 系统，而代理式 AI 涉及能够自主采取行动实现目标的智能体。Modular 的软件旨在让 AI 工作负载在不同硬件（包括高通的骁龙处理器）上高效运行，解决规模化部署 AI 的关键挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-to-Acquire-Modular/default.aspx">Qualcomm to Acquire Modular</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/qualcomm-ai-chip-modular-software.html">Qualcomm inks deal for AI startup Modular to bolster software ...</a></li>

</ul>
</details>

**发生了什么**: 高通宣布以约 39.2 亿美元收购 AI 软件公司 Modular，官方已确认，预计近期完成。
**为什么重要**: 收购增强了高通在 AI 软件栈（特别是生成式 AI 和代理式 AI）的能力，有助于其在边缘和云端与英伟达等对手竞争。
**影响产业链**: 对硬件供应链直接影响有限，但可能带动高通 AI 芯片（如 Snapdragon、Cloud AI 100）的软件生态和采用率，间接影响营收。
**可能相关公司**: QCOM (Qualcomm), NVDA (Nvidia), AMD (Advanced Micro Devices)
**可信度**: 高：官方新闻稿和 CNBC 确认收购金额，来源可信。
**投研价值评分**: 44 / 100
**是否需要继续追踪**: 是
**投研理由**: 收购金额明确但无具体订单或客户合同；软件层面收购对硬件 capex 和供需影响小；高通平台绑定加分；盈利弹性待观察；来源可信度极高。总分 44 符合无硬信号的收购估值范围。

**标签**: `#Acquisition`, `#Qualcomm`, `#Modular`, `#AI`, `#Edge Computing`

---

<a id="item-6"></a>
## [Agility Robotics 通过 25 亿美元 SPAC 合并上市](http://www.roboticstomorrow.com/news/2026/06/24/agility-robotics-to-go-public-through-25-billion-merger-with-churchill-capital-corp-xi/26773) ⭐️ 8.0/10

Agility Robotics 宣布与 SPAC 公司 Churchill Capital Corp XI 合并，估值 25 亿美元，成为美国首家上市纯类人机器人公司，且已有商业部署。 这标志着人形机器人领域的重大财务里程碑，为 Agility 提供资金以扩大生产和商业运营，并显示投资者对该行业信心增强。 合并预计于 2026 年完成，需获得监管和股东批准。Agility 的 Digit 机器人已部署于物流和仓储场景。

rss · Robotics Tomorrow · 6月25日 01:46

**背景**: SPAC 是一家通过 IPO 筹集资金以收购私营公司的空壳公司，上市流程监管较少。纯类公司专注于单一行业，让投资者可精准投资特定领域。Agility Robotics 以其双足机器人 Digit 闻名，正与 Tesla、Figure Robotics 等公司竞争新兴人形机器人市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SPAC_(merger)">SPAC (merger)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pure_play">Pure play - Wikipedia</a></li>

</ul>
</details>

**发生了什么**: Agility Robotics 宣布与 SPAC 公司 Churchill Capital Corp XI 合并，估值 25 亿美元，成为美国首家上市纯类人机器人公司。
**为什么重要**: 这是人形机器人领域的重大融资事件，为 Agility 提供扩张资本，并提升行业关注度。
**影响产业链**: 直接影响有限，主要影响 Agility 自身融资及产能扩张计划，间接利好机器人零部件供应商。
**可能相关公司**: Agility Robotics, Churchill Capital Corp XI, Tesla (TSLA), Figure Robotics, Boston Dynamics
**可信度**: 中，来源为行业新闻网站，未引用官方公告或 SEC 文件。
**投研价值评分**: 23 / 100
**是否需要继续追踪**: 是
**投研理由**: 缺少订单/客户/收入/产能/价格验证，仅涉及 SPAC 合并融资，无商业部署规模及客户采购细节。

**标签**: `#humanoid robotics`, `#SPAC`, `#IPO`, `#robotics industry`, `#Agility Robotics`

---

<a id="item-7"></a>
## [SK 海力士凭 HBM AI 内存超越三星市值](https://news.google.com/rss/articles/CBMi4wFBVV95cUxOSTN6aWNYOWdLN29BQTliVmRyOGJwU0pJZDFFeUZRWTJxSmVMUVlyUnJEYUxla0xOM1VzYW1rczBaZlM0WVZkSjEwWW9lT0FPbDdBM3NCcEhUMG5ZMF95Zi03WlJ2SWZHRHVGdlhkZHl2RVg0RXpPNGRQdWVWMTdPMFBtM3czVjlVT09KdFRuVVRMekRrLUNaX2l6dkI0X2xBNmExRGhNb1BfOHNISGJaZEtZaUFkX0x4ampNMGZwWlBFRnRXdWl0MTR0MUhFUHRwcFAwNW14cUMwMVRDX2xEZ2NrRdIB4wFBVV95cUxOSTN6aWNYOWdLN29BQTliVmRyOGJwU0pJZDFFeUZRWTJxSmVMUVlyUnJEYUxla0xOM1VzYW1rczBaZlM0WVZkSjEwWW9lT0FPbDdBM3NCcEhUMG5ZMF95Zi03WlJ2SWZHRHVGdlhkZHl2RVg0RXpPNGRQdWVWMTdPMFBtM3czVjlVT09KdFRuVVRMekRrLUNaX2l6dkI0X2xBNmExRGhNb1BfOHNISGJaZEtZaUFkX0x4ampNMGZwWlBFRnRXdWl0MTR0MUhFUHRwcFAwNW14cUMwMVRDX2xEZ2NrRQ?oc=5) ⭐️ 8.0/10

SK 海力士的市值 26 年来首次超越三星电子，这得益于其在面向 AI 应用的高带宽内存（HBM）芯片上的早期和大规模投资。 这一半导体领导地位的历史性转变凸显了专用 AI 内存相比传统 DRAM 和 NAND 的日益增长的价值，并表明 HBM 正成为关键的竞争差异化因素。 SK 海力士占据 HBM 市场 90%以上的份额，英伟达是其主要客户，并优先开发 HBM3E 和 HBM4，而三星仍在努力提高其 HBM 产能。

rss · Google News - HBM Memory · 6月24日 09:03

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，通过垂直堆叠内存芯片并通过宽接口连接，提供极高的数据带宽。它对于英伟达 GPU 等 AI 加速器至关重要，可实现训练大型语言模型和其他计算密集型任务的快速数据传输。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.computetape.com/learn/what-is-high-bandwidth-memory-hbm/">What Is HBM ? | High - Bandwidth Memory for AI</a></li>

</ul>
</details>

**发生了什么**: SK 海力士的市值首次超越三星电子，主要因其在 HBM 内存上的领先地位和 AI 芯片需求驱动。
**为什么重要**: 这标志着半导体行业领导权的重大转变，显示 HBM 作为 AI 关键组件的价值正在重塑市场格局。
**影响产业链**: 直接影响 HBM 供应链（DRAM 堆叠、封装、测试），提升 SK 海力士的营收和利润，同时可能挤压三星的 DRAM 业务份额。
**可能相关公司**: SK Hynix (000660.KS), Samsung Electronics (005930.KS), NVIDIA (NVDA), AMD (AMD)
**可信度**: 高，多家权威媒体报道且与已知市场份额数据一致。
**投研价值评分**: 88 / 100
**是否需要继续追踪**: 是
**投研理由**: 拥有明确客户（英伟达）、订单证据（90%市场份额）、供应紧张以及估值变化，满足强投资信号条件，总评分 88 分。

**标签**: `#HBM`, `#SK Hynix`, `#Samsung`, `#AI memory`, `#semiconductor`

---

<a id="item-8"></a>
## [美光预测 AI 需求将导致 2027 年后内存短缺](https://news.google.com/rss/articles/CBMiekFVX3lxTE9fM2N1OGxMU2dWZHpxZlQ5c0w5YnptUXdKejZ4dkZTeDRZLTRfZUQ2bEduVzBZN1NZdXNvZ1RlWllhMDNqUUNCLXVwVmdXeG1ISXlZa1NpRDBTN1p0YVVfa2hmQnFvWm44RVFVaDFXZVhEdFhRcWNEZ1Fn0gGOAUFVX3lxTFA5d19rVk9wVWZseTJKZ0ZhSzZkWkRTamFPWWxpN3FlRWNEVlFRd0F5WGtUT29UclhkZUNJdmdQSXh0UlRmRGpiVnRFeDFYbHVGcHNJeFdxS1ZEdm9PVXZPbWxDZE5aTTE1Q0QzV0N6WkFfWFBPa3hiNUxnTjNoSkc0dVhwTkR5S2JxckUtV1E?oc=5) ⭐️ 8.0/10

领先内存芯片制造商美光（Micron）预测，由于 AI 应用对内存的需求激增，重塑了传统内存周期，内存行业可能在 2027 年后出现供应短缺。 这一预测标志着内存需求的结构性转变，可能导致内存价格持续走高，并增加对内存生产能力的投资，凸显了内存对 AI 工作负载日益增长的重要性。 短缺预计在 2027 年之后发生，这意味着这是长期需求趋势而非短期供应紧张。美光的预测表明，当前和规划中的产能可能不足以满足 AI 驱动的需求。

rss · Google News - HBM Memory · 6月25日 01:59

**背景**: 内存行业历来遵循周期性的繁荣-萧条模式，受过度投资和供应过剩阶段驱动。然而，AI 对高带宽内存（HBM）和先进内存产品的需求正在创造结构性的需求增长。美光与三星、SK 海力士一起，是内存芯片领域的主要参与者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.idc.com/resource-center/blog/semiconductor-market-to-surge-past-the-trillion-dollar-threshold-ai-infrastructure-drives-market-growth/">Semiconductor Market Forecast 2026: The AI Supercycle Arrives - IDC</a></li>
<li><a href="https://www.uncoveralpha.com/p/every-memory-cycle-ends-the-same">Every Memory Cycle Ends the Same. Until It Doesn't.</a></li>

</ul>
</details>

**发生了什么**: 美光预测 2027 年后因 AI 需求导致内存短缺，暗示长期需求趋势变化。
**为什么重要**: 这可能引发内存行业的结构性投资，影响价格和供应链，但对即期订单和收入没有直接证据。
**影响产业链**: 影响内存产业链，包括 HBM、DRAM 和 NAND；可能推动美光及同业增加资本支出，但尚未确认。
**可能相关公司**: MU（美光）, 三星电子, SK 海力士
**可信度**: 中（基于新闻报道，非美光官方公告原文）
**投研价值评分**: 44 / 100
**是否需要继续追踪**: 是
**投研理由**: 缺少订单/客户/收入/产能/价格验证，属于远期预测，评分保守。

**标签**: `#AI`, `#memory`, `#Micron`, `#hardware`, `#industry analysis`

---

<a id="item-9"></a>
## [提出基于基础模型的连续物理推理](https://semiengineering.com/continuous-physics-reasoning-definition-minimum-criteria-and-the-role-of-foundation-models-for-physics/) ⭐️ 7.0/10

提出了一种通用的连续物理推理系统，通过将基础模型与原生物理结构推理相结合，旨在以制造分辨率实现确定性的、求解器级通用性。 这种方法可能弥合 AI 与传统工程仿真之间的差距，实现设计迭代过程中的实时物理分析，从而加速产品开发并减少对手动仿真设置的依赖。 该系统被描述为“连续”，因为它使物理推理与设计变更的步伐保持一致，而不是将物理处理为设计后的独立步骤。基础模型是架构，而连续物理推理是它们所支持的工作流程。

rss · SemiEngineering · 6月24日 07:04

**背景**: 传统仿真通常在设计冻结后运行，这引入延迟并限制了探索空间。物理基础模型旨在提供“一次训练，随处部署”的能力，类似于 NLP 中的大语言模型。连续物理推理是利用这类模型、使物理洞察更贴近工程变更的工作流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://semiengineering.com/from-simulation-checkpoints-to-continuous-physics/">From Simulation Checkpoints To Continuous Physics</a></li>
<li><a href="https://semiengineering.com/foundation-model-for-physics-the-next-layer-of-intelligence-for-engineering/">Foundation Model For Physics: The Next Layer Of Intelligence For ...</a></li>

</ul>
</details>

**发生了什么**: SemiEngineering 发布文章，提出了一个结合基础模型进行连续物理推理的通用系统概念，尚未进入商业部署或产品阶段。
**为什么重要**: 该概念如果实现，可能改变工程设计仿真工作流，降低仿真成本并加速迭代，但目前仅为学术/概念研究，无客户或订单验证。
**影响产业链**: 目前无直接产业链影响，可能间接利好 EDA/CAE 软件厂商（如 Synopsys、Ansys）及 AI 芯片平台（如 NVIDIA），但无具体收入或利润影响。
**可能相关公司**: NVDA, SNPS, ANSS, Dassault Systèmes
**可信度**: 中（来源权威，但内容为概念讨论，无商业验证）
**投研价值评分**: 28 / 100
**是否需要继续追踪**: 是
**投研理由**: 论文/概念研究，缺少订单、客户、收入、产能或价格验证；source_confidence 较高但其他子项低，总评分≤40。

**标签**: `#physics reasoning`, `#foundation models`, `#AI for science`, `#continuous reasoning`

---

<a id="item-10"></a>
## [UCIe 与 BoW：实用芯片互连标准对比](https://semiengineering.com/ucie-vs-bow-practical-insights-for-choosing-the-right-chiplet-standards/) ⭐️ 7.0/10

《半导体工程》发布了一份详细的白皮书，对比了 UCIe 和 BoW 两种芯片互连标准，为根据应用需求选择标准提供了工程指导。 随着基于芯片的设计在高端和成本敏感市场中普及，理解 UCIe 与 BoW 之间的权衡有助于工程师优化系统性能、功耗和成本。 UCIe 由英特尔、AMD、台积电等主要行业参与者支持，旨在实现高带宽、低延迟的片间连接。BoW 在开放计算项目下开发，专注于对性能要求较低的应用的简单性和成本效益。

rss · SemiEngineering · 6月24日 07:03

**背景**: 芯片（Chiplet）是较小的裸片，集成后形成更大的系统，实现异构集成并提高良率。UCIe（通用芯片互连标准）和 BoW（Bunch of Wires）等互连标准定义了芯片间通信的物理层和协议层。UCIe 是一个由联盟驱动、获得广泛行业支持的标准；而 BoW 是开放计算项目下的开放规范，常用于不太复杂的设计中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://semiengineering.com/ucie-vs-bow-practical-insights-for-choosing-the-right-chiplet-standards/">UCIe vs. BoW: Practical Insights For Choosing The Right Chiplet Standards</a></li>
<li><a href="https://en.wikipedia.org/wiki/UCIe">UCIe - Wikipedia</a></li>

</ul>
</details>

**发生了什么**: 《半导体工程》发布了一篇技术白皮书，比较 UCIe 和 BoW 芯片互连标准，提供工程选择指导。
**为什么重要**: 该比较有助于工程师根据应用需求选择标准，但缺乏具体商业部署或财务影响信息。
**影响产业链**: 该内容不涉及具体供应链收入、利润或现金流变化。
**可能相关公司**: Intel, AMD, TSMC, Qualcomm, Google
**可信度**: 中（来源权威但仅为技术分析，无商业验证）
**投研价值评分**: 15 / 100
**是否需要继续追踪**: 否
**投研理由**: 缺少订单/客户/收入/产能/价格验证，仅为技术标准比较，投资信号弱。

**标签**: `#chiplet`, `#UCIe`, `#BoW`, `#interconnect`, `#semiconductor`

---