---
layout: default
title: "Horizon Summary: 2026-10-09 (ZH)"
date: 2026-10-09
lang: zh
---

> 从 69 条内容中筛选出 9 条重要资讯。

---

1. [ETH Zurich 让机械手用指尖行走，成为独立机器人](#item-1) ⭐️ 7.0/10
2. [格芯与台积电达成 20 亿美元协议，用于美国 AI 芯片封装组件](#item-2) ⭐️ 7.0/10
3. [三星预测季度利润达 800 亿美元，因 AI 内存需求挤压 PC 和手机制造商 - news.lavx.hu](#item-3) ⭐️ 7.0/10
4. [铠侠称其高性能闪存驱动器速度翻倍](#item-4) ⭐️ 6.0/10
5. [Scality 推出 AI Inference Factory，通过 RDMA 从对象存储提供 KV 缓存](#item-5) ⭐️ 6.0/10
6. [美国近全部 94 座核反应堆已获得 AI 工具接入机会](#item-6) ⭐️ 6.0/10
7. [碳感知调度成为削减数据中心范围二排放的实用手段](#item-7) ⭐️ 6.0/10
8. [Sesterce 拟在芬兰旧造纸厂址建 100 亿欧元 AI 数据中心](#item-8) ⭐️ 6.0/10
9. [共封装光学能否解决数据中心互连瓶颈？](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [ETH Zurich 让机械手用指尖行走，成为独立机器人](https://spectrum.ieee.org/walking-robotic-hand) ⭐️ 7.0/10

苏黎世联邦理工学院（ETH Zurich）软体机器人实验室的研究者、博士生 Amirhossein Kazemipour 带领团队，把 Wuji Technology 的一款商用机械手改造成完全独立的机器人：它用五根指尖行走，随后再用同样的手指去操作物体。这只手背着一个 80 克的“背包”，内含电池、惯性测量单元（IMU）和一块 Raspberry Pi Zero，其行走步态是在仿真中通过强化学习训练出来的。 这项工作指向一种模块化机器人思路：身体部件不再被固定在单一功能上，机器人可以把手掌分离出去，在整条手臂或整个身体无法进入的狭窄、危险空间中操作开关和抓取物体。它可能应用于精细的工业维护以及搜救场景，同时把足式运动的形态设计空间拓展到传统左右对称的双足和四足之外。 团队刻意选择商用成品手而不是定制硬件，以免牺牲操作能力，但这也让步态学习更难，因为手的几何形状是为抓握而非爬行优化的；与左右对称的双足、四足机器人不同，手的手指长度不一且带有对生拇指，因此无法直接套用常规足式机器人的训练方法。文章节选未给出行走速度、负载、能耗或续航等数据，且该工作属于实验室研究，并非已部署产品。

rss · IEEE Spectrum Robotics · 10月8日 12:00

**背景**: 强化学习是一种训练方式：模型通过大量试错来学习技能，向目标行为靠近时获得奖励，偏离时受到惩罚；它被广泛用于教足式机器人行走，通常先在物理仿真器中训练，再迁移到真实硬件上。IMU 是一类测量加速度和旋转的传感器组件，可让机器人估计自身姿态与平衡；Raspberry Pi Zero 则是一块极小、低成本的单板计算机，常用于轻量化的板载控制。机械手通常安装在手臂末端并为抓握而优化，因此把它单独当作行走兼操作的机器人相当少见；此前的“会走路的机械手”多依赖专门设计的硬件，而非市售成品部件。

**发生了什么**: 苏黎世联邦理工学院软体机器人实验室把 Wuji Technology 的市售机械手改造成独立机器人，用五根指尖行走并完成操作，靠 80 克背包内的电池、IMU 和 Raspberry Pi Zero 供电与控制，步态通过仿真强化学习训练得到。
**为什么重要**: 它展示了一种“部件不限于单一功能”的模块化机器人方向，未来机械手可脱离本体进入狭窄空间执行维护或搜救任务，对足式运动与灵巧操作的形态设计有启发意义，但目前仍属实验室阶段。
**影响产业链**: 短期对产业链收入和利润几乎没有直接拉动：缺少订单、客户采购、量产部署、产能与价格验证，也未涉及数据中心、运营商或国家级算力平台的资本开支。可能被关注的方向是灵巧手/机器人末端执行器与低价嵌入式控制板（如 Raspberry Pi 类单板计算机）的长期需求，但本条新闻不构成订单证据。
**可能相关公司**: Wuji Technology（舞肌科技，未上市）, Raspberry Pi Holdings（RPI.L）, 灵巧手/机器人末端执行器相关厂商（作为观察方向，非订单证据）
**可信度**: 中：信息来自 IEEE Spectrum 对 ETH Zurich 团队工作的报道，来源可信度较高，但属于实验室研究报道，无官方订单、客户、财务或产能数据可交叉验证。
**投研价值评分**: 16 / 100
**是否需要继续追踪**: 否
**投研理由**: 本研究属于论文/实验室技术演示类信号，缺少订单/客户/收入/产能/价格验证，按规则总分应落在 10-35 区间并不得超过 40。capex_impact 与 earnings_elasticity 给极低分，order_evidence 与 supply_demand_impact 为 0；platform_binding 仅因使用市售机械手与 Raspberry Pi Zero 这类通用平台给 3 分，不构成头部客户绑定；source_confidence 7 分来自 IEEE Spectrum 的可靠报道；novelty 4 分体现“用市售手而非定制硬件实现指尖行走”的新意，但新颖性不计入资本开支、订单、供需与盈利弹性等子项。

**标签**: `#robotics`, `#manipulation`, `#locomotion`, `#ETH Zurich`, `#bio-inspired robotics`

---

<a id="item-2"></a>
## [格芯与台积电达成 20 亿美元协议，用于美国 AI 芯片封装组件](https://www.semiconductor-digest.com/globalfoundries-tsmc-strike-2b-deal-for-u-s-ai-chip-packaging-components/?utm_source=rss&utm_medium=rss&utm_campaign=globalfoundries-tsmc-strike-2b-deal-for-u-s-ai-chip-packaging-components) ⭐️ 7.0/10

格芯和台积电宣布了一项多年期 20 亿美元协议，以扩大美国先进 AI 芯片封装组件的产能。

rss · Semiconductor Digest · 10月8日 21:10

**标签**: `#semiconductors`, `#AI chips`, `#advanced packaging`, `#TSMC`, `#supply chain`

---

<a id="item-3"></a>
## [三星预测季度利润达 800 亿美元，因 AI 内存需求挤压 PC 和手机制造商 - news.lavx.hu](https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVVVXR05ITGFyV3JYOTdQRjJfd284dWZncFdIWkZoNDlGb1laVm9fRzlpRlNBS3k2VzZiSlE2WUNNc19KMGxNSmcxREpKUlI2SVdKLThQWmZZaUM4MW40bUM3bHJkeGtFaFBJMHdvWnozcGJXWHdJWHB6TWNMeDJkc3ZIZmhKeFlNOUh1TG5iUVdObjdOWnkwelVoeTkyVkNoQWx5a3JUbTd3WS1FaGE0X0FfNkw2SE81bUxCOEtveE0?oc=5) ⭐️ 7.0/10

三星预测，受人工智能内存需求推动，其季度利润将大幅增长，而这正给个人电脑和手机制造商带来压力。

rss · Google News - HBM Memory · 10月8日 12:20

**标签**: `#Samsung`, `#AI memory`, `#HBM`, `#semiconductor industry`, `#PC market`

---

<a id="item-4"></a>
## [铠侠称其高性能闪存驱动器速度翻倍](https://www.blocksandfiles.com/flash/2026/10/08/kioxia-doubles-super-fast-flash-drive-speed/5301892) ⭐️ 6.0/10

据 Blocks & Files 报道，铠侠（Kioxia）宣布已将其高性能闪存驱动器技术的速度提升了一倍。不过在现有材料中，铠侠并未公布具体的产品名称、接口规格、吞吐量或延迟指标，也没有给出上市时间表。 铠侠是全球最大的 NAND 闪存与 SSD 供应商之一，因此其高性能存储速度若出现实质性跃升，会直接关系到它在数据中心 SSD 领域相对三星、SK 海力士/Solidigm、美光、西部数据等竞争对手的地位。但由于没有公开的基准测试或产品路线图，这一说法目前更像是技术里程碑，而非能立刻改变市场格局的事件。 现有报道没有说明涉及哪一产品系列、采用何种接口或协议、原有速度为多少，也没有说明这一提升属于已量产产品还是实验室演示。在第三方基准测试或官方规格书公布之前，读者应把“速度翻倍”视为厂商单方面说法，尚未得到验证。

rss · Blocks and Files · 10月8日 15:00

**背景**: NAND 闪存是一种非易失性存储技术，断电后仍能保留数据，是 SSD、U 盘和手机存储的基础。铠侠是一家总部位于东京的日本存储企业，最初由东芝存储业务分拆而来，以 BiCS FLASH 三维闪存技术闻名，并向数据中心、消费端和汽车市场供应 SSD。在存储行业中，所谓“高性能闪存驱动器”通常指低延迟、高耐久度的一类高端 SSD，被用作 DRAM 与传统 TLC/QLC SSD 之间的缓存或分层存储层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kioxia">Kioxia - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Flash_memory">Flash memory - Wikipedia</a></li>

</ul>
</details>

**发生了什么**: 铠侠对外宣称其高性能闪存驱动器技术的速度提升了一倍，但未公布具体产品型号、接口协议、基准测试数据、量产状态与时间表，属于技术层面的单方面性能声明。
**为什么重要**: 铠侠是全球主要 NAND 闪存与 SSD 供应商之一，若该提速可落地到数据中心 SSD 产品线，将影响其在企业级存储市场相对三星、SK 海力士/Solidigm、美光、西部数据的竞争地位；但由于缺少实测数据与产品化信息，目前难以判断实际商业影响。
**影响产业链**: 可能影响 NAND 闪存—主控—企业级 SSD 模组—数据中心存储这一产业链，但本次公告未披露任何订单、客户、产能扩张、价格变动或收入结构变化，因此对相关公司收入、利润率与现金流的可推断影响极为有限，缺少订单/客户/收入/产能/价格验证。
**可能相关公司**: Kioxia Holdings (285A.T), Samsung Electronics (005930.KS), SK Hynix (000660.KS), Micron (MU), Western Digital (WDC), SanDisk (SNDK)
**可信度**: 低至中：消息来自行业媒体 Blocks & Files 的简短报道，内容为厂商性能声明，缺少官方产品文档、规格书、基准测试或客户部署信息，无法交叉验证。
**投研价值评分**: 15 / 100
**是否需要继续追踪**: 否
**投研理由**: 本次消息属于厂商性能宣称，既无订单与客户采购证据，也无产能、价格或供需变化，更无收入与毛利指引。按证据上限规则，缺少硬性投资信号的技术类宣称总分应控制在 45 分以内；其中 capex_impact、order_evidence、supply_demand_impact、earnings_elasticity 均按 0-5 的下限保守打分，novelty 仅因“速度翻倍”这一提法给予象征性分值。后续若出现官方产品发布、规格书、量产时间表或客户采用证据，应重新评估。

**标签**: `#Kioxia`, `#flash storage`, `#NAND`, `#SSD performance`, `#storage hardware`

---

<a id="item-5"></a>
## [Scality 推出 AI Inference Factory，通过 RDMA 从对象存储提供 KV 缓存](https://www.storagereview.com/news/scality-ai-inference-factory-kv-cache-object-storage-rdma) ⭐️ 6.0/10

Scality 发布了 Scality AI Inference Factory，这是一套开源代码（open-code）软件栈，用于在客户自有基础设施上运行开放权重模型，并由 Scality 负责验证、交付与维护。该软件栈把 Scality 的 AI Data Infrastructure（ADI）对象存储放在推理层之下，作为通过 RDMA 访问的共享键值（KV）缓存，Scality 声称相比重新计算缓存可实现 14 倍加速，目标客户为企业和政府机构。 KV 缓存是 LLM 推理中最大的内存消耗者，因此把它从 GPU 显存中移出、放入共享的解耦存储，是一个有意义的架构方向，有望缓解容量瓶颈并让缓存的上下文在多个推理副本之间复用。如果该方案在生产环境中得到验证，AI 基础设施的投入与设计重点将部分从单纯的 HBM 转向网络化存储和低延迟互联结构。 14 倍这一数字是厂商相对“重新计算”得出的宣称值，并非独立第三方基准测试，且未披露延迟、吞吐或成本数据。RDMA 之所以快，是因为绕过了 CPU 和操作系统，但这需要支持 RDMA 的网卡以及 RoCE 或 InfiniBand 等无损网络；同时对象存储相比本地 DRAM 天然会带来额外延迟，因此实际收益很大程度上取决于缓存命中率和以预填充（prefill）为主的工作负载。

rss · StorageReview · 10月8日 16:32

**背景**: 大语言模型逐 token 生成文本，为避免对已生成的每个 token 重复计算注意力，会把已处理 token 的键和值缓存下来，这就是 KV 缓存；缓存随上下文长度增长，是 GPU 显存的主要占用者。远程直接内存访问（RDMA）允许一台机器通过网络读写另一台机器的注册内存，几乎不需要远端 CPU 和操作系统参与，从而提供低延迟和高吞吐。Scality 是一家横向扩展对象存储厂商（其 RING 产品线），其 ADI 产品是试图把对象存储定位为 AI 工作负载的数据层，而不仅仅是归档存储。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://martinlwx.github.io/en/llm-inference-optimization-kv-cache/">LLM inference optimization (1): KV Cache - MartinLwx's Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Remote_direct_memory_access">Remote direct memory access - Wikipedia</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms">Understanding and Coding the KV Cache in LLMs from Scratch</a></li>

</ul>
</details>

**发生了什么**: Scality 发布 AI Inference Factory 开源软件栈，把自家 ADI 对象存储作为共享 KV 缓存，通过 RDMA 供 LLM 推理使用，厂商声称相比重新计算缓存有 14 倍加速，面向企业和政府机构自有基础设施。
**为什么重要**: KV 缓存是 LLM 推理最大的内存瓶颈，若能通过 RDMA 在共享对象存储上解耦，可能改变 AI 推理服务器的内存与存储配比，让网络化存储和低延迟互联在 AI 基础设施中的权重上升。但本次仅为厂商产品发布，缺少独立基准测试与客户验证。
**影响产业链**: 理论上利好 AI 推理侧的存储与网络产业链，包括支持 RDMA 的网卡/交换机与对象存储软件，但本次公告未披露任何实际采购、部署规模或收入贡献，对相关上市公司的收入、利润率与现金流无可量化影响。
**可能相关公司**: Scality（未上市，私营公司）, NVIDIA（NVDA，RDMA/RoCE 与 GPU 推理平台间接相关）, Pure Storage（PSTG，对象/并行存储间接相关）, 博通（AVGO，RDMA 网卡与交换芯片间接相关）
**可信度**: 中：消息来自厂商官方发布并经 StorageReview 报道，属可核实的公司公告，但仅有单一来源、无独立基准测试、无客户名单与部署数据。
**投研价值评分**: 24 / 100
**是否需要继续追踪**: 否
**投研理由**: 属厂商产品发布与生态合作型新闻，缺少订单/客户/收入/产能/价格验证，因此按证据上限压低评分。capex_impact 仅 4 分，因为没有任何超大规模厂商、电信或国家算力平台的资本开支变化；order_evidence 1 分，无订单、合同或量产交付证据；supply_demand_impact 3 分，无涨价、缺货或产能瓶颈证据；platform_binding 5 分，未绑定英伟达、云厂商或头部客户，仅适配开放权重模型；earnings_elasticity 2 分，Scality 未上市且无财务影响可推算；source_confidence 5 分，官方发布但单一来源且无独立验证；novelty 4 分，把对象存储作为 RDMA 共享 KV 缓存具有一定新意。合计 24 分。

**标签**: `#KV cache`, `#object storage`, `#RDMA`, `#LLM inference`, `#AI infrastructure`

---

<a id="item-6"></a>
## [美国近全部 94 座核反应堆已获得 AI 工具接入机会](https://spectrum.ieee.org/ai-assistants-nuclear-power-plant) ⭐️ 6.0/10

据 IEEE Spectrum 报道，今年美国近全部 94 座核反应堆都获得了在电厂运营中接入 AI 的机会，且大多数已采用。Atomic Canyon 于 8 月推出 NIVA，此前已在 Constellation Energy 旗下核电站试点；初创公司 Nuclearn 称已与超过 65 家美国合作伙伴开展业务，其中包括与 NuScale Power 的集成；微软与英伟达也已联手推进一个覆盖核电站全生命周期的 AI 项目。 核电是全球最厌恶风险、最不容出错的安全关键行业之一，因此 AI 能在整个机组群中迅速铺开，说明机器智能已在受监管的工业场景中跨过了可信度门槛。这也把两大趋势捆绑在一起：AI 数据中心需要更多稳定、零碳的电力，而核电行业需要 AI 来应对繁复的监管、老化的设备和不断萎缩的劳动力。 近期的核心用例是文档与监管文书工作，而非直接控制反应堆，因为许可、维护与合规这类语言和流程密集型任务正是当前 AI 所擅长的；Constellation 拒绝接受采访，因此其旗下机组的部署细节无法核实。值得注意的是，报道中点名的参与者——Atomic Canyon、Nuclearn、Constellation、NuScale——属于合作方，报道并未披露合同金额或收入数据。

rss · IEEE Spectrum Artificial Intelligence · 10月8日 14:28

**背景**: 美国运营着 94 座商业核反应堆，供应全国约五分之一的电力，该行业由美国核管理委员会监管，其规则建立在“失效可能造成严重伤害”的安全关键系统理念之上。这样的风险特征长期以来促使核电站采用保守的、以人为主导的运营方式，并对新技术的引入十分谨慎。如今两股压力正在改变这一格局：超大规模数据中心需要全天候的零碳电力，从而推动了核电复兴；同时行业面临大批退休潮，让本就专业化的劳动力更加紧张。NuScale 等公司研发的小型模块化反应堆也希望从设计、许可到运营一开始就借助 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Safety-critical_system">Safety-critical system</a></li>
<li><a href="https://www.energy.gov/supercomputing-and-exascale">Supercomputing and Exascale | Department of Energy</a></li>

</ul>
</details>

**发生了什么**: IEEE Spectrum 报道称，美国近全部 94 座核反应堆今年都获得了接入 AI 运营工具的机会，多数已采用；Atomic Canyon 推出 NIVA 并在 Constellation Energy 电站试点，Nuclearn 称已服务超过 65 家美国合作伙伴并集成 NuScale，微软与英伟达合作推进覆盖核电站全生命周期的 AI 项目。
**为什么重要**: 核电站运营的 AI 化意味着 AI 正进入受强监管的安全关键工业场景，同时把“AI 数据中心用电需求—核电复兴—核电数字化”三条链条串起来，可能带动核电运营软件、文档合规自动化和相关算力投入。
**影响产业链**: 直接受益方向是核电运营软件与 AI 助手、工程文档与合规自动化服务，以及为核电场景提供算力和模型能力的厂商；对 Constellation、NuScale 等运营与设备方更多是运营效率和许可证流程改善，而非短期收入变化。报道未披露任何合同金额、收入或毛利影响，因此对产业链收入和现金流的弹性目前难以量化。
**可能相关公司**: Constellation Energy (CEG), NuScale Power (SMR), Microsoft (MSFT), Nvidia (NVDA), Atomic Canyon（未上市）, Nuclearn（未上市）
**可信度**: 中：来源为 IEEE Spectrum 这一专业媒体，并交叉引用世界核新闻及企业官网，可信度较高；但缺少订单金额、客户采购合同、收入指引等硬性财务证据，且 Constellation 拒访使部署细节无法二次核实。
**投研价值评分**: 32 / 100
**是否需要继续追踪**: 是
**投研理由**: 该新闻属于行业应用与采用度报道，确有部署规模信号（近 94 座反应堆获接入、65 家以上合作伙伴、微软与英伟达合作），因此 order_evidence 给了 8 分；但与英伟达和微软的平台关联属于生态合作而非算力资本开支变化，capex_impact 仅 3 分；没有价格、产能、短缺或交付周期证据，supply_demand_impact 给 2 分；参与方多为未上市公司，无收入结构、毛利或自由现金流数据，earnings_elasticity 给 3 分；来源可信度较高给 7 分；事件本身较新但非共识突破，novelty 给 3 分。合计 32 分，符合“缺少订单/客户/收入/产能/价格验证”下应保守评分的要求，若后续出现明确的核电站采购金额或微软、英伟达等平台的 AI 数据中心配套核电资本开支指引，需上调评分。

**标签**: `#AI`, `#nuclear power`, `#energy`, `#industrial AI`, `#safety-critical systems`

---

<a id="item-7"></a>
## [碳感知调度成为削减数据中心范围二排放的实用手段](https://www.datacenterknowledge.com/sustainability/how-carbon-aware-scheduling-can-cut-data-center-emissions) ⭐️ 6.0/10

Data Center Knowledge 的一篇分析文章指出，碳感知调度（即在电网碳强度更低的时段和区域运行灵活、可延迟的工作负载）可将可再生能源的波动性转化为可测量的范围二排放下降。文章把这一做法定位为一种可落地的运营手段，而非硬件层面的新技术突破，并强调只有真正具备时间弹性的工作负载才能受益。 在监管机构、客户以及企业自身净零承诺的压力下，数据中心必须报告并削减范围二排放（即外购电力产生的间接排放），而 AI 带来的算力需求又不断推高用电量。如果碳感知调度无需新增资本开支即可减排，它将成为购电协议与自建可再生能源之外对运营商颇具吸引力的补充手段，帮助其同时应对成本与合规压力。 该方法依赖准确的电网碳强度预测，并结合用户设定的截止时间，使可延迟的批处理任务、模型训练等非交互式工作负载得以推迟或迁移至更清洁的区域。文章也指出其局限：对延迟敏感的服务、有状态应用以及受司法辖区约束的工作负载无法随意迁移，而减排效果最终取决于底层碳数据的质量。

rss · Data Center Knowledge · 10月8日 09:00

**背景**: 范围二排放是企业因外购电力、热力或制冷而产生的间接温室气体排放，对数据中心而言通常占其碳足迹的最大部分，且 GHG Protocol 要求同时披露基于地点和基于市场的两类数据。碳感知调度的思路借鉴了需求响应与云上竞价容量管理：调度器追求的不是最便宜的算力，而是最低的碳强度，依靠电网碳强度预测与可放宽的截止时间来实现。超大规模云厂商已在此领域试验多年，但由于需要工作负载具备弹性、碳数据可靠，并且要对 Kubernetes 之类的编排调度器进行改造，实际普及程度仍不均衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dcpulse.com/article/scope-1-2-3-data-centers">Scope 1, 2, and 3 Emissions in Data Centers Explained</a></li>
<li><a href="https://www.decarbonops.com/blog/carbon-footprint-data-centres">Carbon Footprint Data Centres: PUE, Scope 2, and IT Emissions ...</a></li>
<li><a href="https://luiscruz.github.io/course_sustainableSE/2026/papers/g15_carbon_scheduler.pdf">Carbon-Aware Scheduling</a></li>

</ul>
</details>

**发生了什么**: 行业媒体 Data Center Knowledge 发表分析文章，指出碳感知调度可通过将可延迟的灵活工作负载迁移到电网碳强度更低的时段和地区，帮助数据中心降低范围二排放，属于方法论与运营实践层面的讨论，未涉及任何具体产品或商业发布。
**为什么重要**: 该话题契合数据中心可持续运营与 ESG 披露趋势，长期看有利于调度软件、碳数据与能效管理类需求，但本文并未给出可量化的减排规模、客户案例或采购安排，短期对产业链营收与利润的直接推动有限。
**影响产业链**: 理论上影响数据中心能效与碳管理软件、电力调度与碳强度数据服务，以及可再生能源采购与储能调峰等环节；但文章中没有任何收入、利润率、资本开支或现金流变化的证据，缺少订单/客户/收入/产能/价格验证。
**可能相关公司**: 数据中心运营商与 REITs（如 Equinix、Digital Realty）, 超大规模云厂商（如 Microsoft、Google、Amazon）, 数据中心能效与碳管理软件供应商, 电网碳强度数据与电力交易服务商
**可信度**: 中：来源为专业行业媒体，议题真实且可交叉验证，但内容属于趋势性评论，缺少官方公告、具体客户或量化数据支撑。
**投研价值评分**: 18 / 100
**是否需要继续追踪**: 否
**投研理由**: 本文为行业分析型文章，仅描述碳感知调度的减排潜力，无订单、无指定客户采购、无资本开支调整、无价格或供需紧张信号，也未给出可推断的收入或利润率影响，因此资本开支、订单、供需与盈利弹性四项均按保守下限给分；仅来源可信度与议题新颖性略有加分，合计 18 分，属于弱投资信号。

**标签**: `#carbon-aware scheduling`, `#data centers`, `#sustainability`, `#green computing`, `#energy efficiency`

---

<a id="item-8"></a>
## [Sesterce 拟在芬兰旧造纸厂址建 100 亿欧元 AI 数据中心](https://news.google.com/rss/articles/CBMivwFBVV95cUxQRml4NWlLd0pnaW9JaVlMMVgydS1BZzY2ZXhqd0dBdXNneVFMRE5EYjN5d2d3RGMzbWttcFZCbWEtZmM5UnR0NzF2UWNJcTA2TWU2ZjJBRXZ1T01FS0Y5QUxoeHJFeE4wRlBXYV9aTS1VR2ZpWHRZU2dqUUw2dTYwWkw2SVU5RTF0dnRSZHlubnE1MlpiVXhIanNraXlocGxrZ21fcHhnX1paRFV0YklXUEdhaTlJOUhVNGN1QkJBQQ?oc=5) ⭐️ 6.0/10

法国 AI 与超级计算基础设施公司 Sesterce 宣布，计划在芬兰耶姆塞（Jämsä）原 Kaipola 造纸厂旧址建设一个投资约 100 亿美元（约 100 亿欧元）、容量 600MW 的 AI 数据中心园区，并计划于今年开工。 这是欧洲正在快速涌现的吉瓦级 AI 数据中心投资浪潮的一部分，凸显出对 AI 算力、供电与散热基础设施的持续需求，同时也把新的工业投资引入曾经的林业工业地区。 该园区规划容量为 600MW，选址于改造后的 Kaipola 造纸厂地块；此外 Sesterce 还单独与软银集团成立合资企业，在法国 Bosquel 开发 1GW 的 AI 数据中心，显示其正在欧洲多点布局；不过芬兰项目的公告并未披露客户、融资或供电细节。

rss · Google News - Data Center Liquid Cooling · 10月8日 17:24

**背景**: Sesterce 是一家法国公司，主要建设并运营超级计算与 AI 基础设施。AI 数据中心与传统数据中心不同，其内部密集部署大量高耗电的 GPU，因此容量通常以电力负荷（兆瓦）而非占地面积来衡量。芬兰等北欧国家因气候寒冷便于散热、电价相对低廉且低碳、且拥有可用工业用地而颇具吸引力——像 Kaipola 这样的旧造纸厂可提供现成的电力接入和可再利用的基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacenterdynamics.com/en/news/sesterce-to-invest-10bn-in-600mw-ai-data-center-campus-in-jämsä-finland/">Sesterce to invest $10bn in 600MW AI data center campus in ...</a></li>
<li><a href="https://www.sesterce.com/newsroom/softbank-group-sesterce-1gw-ai-data-center-bosquel-france">SoftBank Group and Sesterce to Develop 1 GW AI Data Center in ...</a></li>

</ul>
</details>

**发生了什么**: Sesterce 宣布在芬兰耶姆塞原 Kaipola 造纸厂旧址建设 600MW、约 100 亿美元的 AI 数据中心园区，计划今年开工，属于欧洲吉瓦级 AI 数据中心建设浪潮中的又一新增项目。
**为什么重要**: 该消息体现了 AI 算力基础设施资本开支持续扩张，将带动数据中心供电、散热、机电设备以及 GPU 等上游环节的需求，同时为芬兰当地带来工业投资。
**影响产业链**: 理论上利好数据中心电力设备、散热（液冷）、服务器与 GPU、以及建筑工程等产业链，但公告未披露客户、订单、融资方案或收入指引，对上市公司收入、利润和现金流的直接可验证影响有限。
**可能相关公司**: Sesterce（未上市）, SoftBank Group (9984.T), NVIDIA (NVDA), Vertiv (VRT), Schneider Electric (SU.PA)
**可信度**: 中：消息来源为 Sesterce 官方与 DataCenterDynamics 等行业媒体报道，可信度较好；但缺少客户、订单、融资与供电协议等硬性证据。
**投研价值评分**: 45 / 100
**是否需要继续追踪**: 是
**投研理由**: 投研评分 45：capex_impact 16（600MW、100 亿美元属明确的数据中心资本开支信号）；order_evidence 3（无订单或客户采购证据）；supply_demand_impact 6（新增算力与电力需求，但无价格、缺货或产能瓶颈数据）；platform_binding 7（与软银集团的合资关系提供一定平台绑定，但本项目未明确客户）；earnings_elasticity 3（对上市公司的收入/利润影响不可直接推断）；source_confidence 8（官方与行业媒体佐证）；novelty 2（属行业常规扩张）。整体缺少订单/客户/收入/产能/价格验证，故分数保守。

**标签**: `#AI infrastructure`, `#data centers`, `#Finland`, `#investment`, `#industry news`

---

<a id="item-9"></a>
## [共封装光学能否解决数据中心互连瓶颈？](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNSVYyRnZTcFRrMzByalVJWXpSZUs4OGpORnZSVThnTDRqZ0lkZVZIeTNRWlBNTTRnQUY3dWhPSE9zOXdnQXdKdFRTWXRxMWZSUXV0VzI0cDhaNWNKQkxvc19aVzZCU0NQQThWU09fODkxZU5SYWNfN056dGhPUGhXM2F1NUUxLUFrVWVJdU5aMGUtSnVoSXpiSW5QaVowYmtjSU9MMWFVNGRRU2t4NFFkVWRSNXc2cDViaURHYmowTzRneEYwYTMxUElCMEtaUGY3bWZaR0NOYWVxanM?oc=5) ⭐️ 6.0/10

Data Center Dynamics 发表了一篇分析文章，探讨共封装光学（CPO）能否解决数据中心行业即将面临的互连带宽和功耗挑战。该条目仅为标题/链接，没有正文，因此并未宣布新产品、订单或技术里程碑。 随着 AI 集群规模扩大，铜缆和可插拔光模块正接近传输距离和功耗极限，使 CPO 成为光互连领域潜在的长期重要架构。它可能重塑交换 ASIC、光引擎、激光器和数据中心基础设施的供应链。 CPO 将光发射和接收组件（光引擎）与交换 ASIC 集成在单个封装中，取代电路板边缘的可插拔光收发模块。关键挑战包括热管理、激光器可靠性、制造良率以及现场可维护性。

rss · Google News - Optical Interconnect CPO · 10月8日 16:04

**背景**: 共封装光学是一种半导体封装技术，将光学组件与电子 ASIC 集成在同一封装内，主要用于在 AI 加速器之间传输大量数据的数据中心。光互连使用光而非电信号，相比金属互连可降低功耗、延迟和串扰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Co-packaged_optics">Co-packaged optics</a></li>
<li><a href="https://www.corning.com/oem-solutions/worldwide/en/home/products-solutions/optical-communication-components/co-packaged-optics.html">What is Co-Packaged Optics (CPO) Technology? | Corning</a></li>
<li><a href="https://www.nature.com/articles/s41928-026-01681-6">Co-packaged optics for high-performance computing and ...</a></li>

</ul>
</details>

**发生了什么**: Data Center Dynamics 发布分析文章，讨论共封装光学（CPO）能否解决数据中心互连带宽与功耗瓶颈；该条目无正文，无具体产品、订单或客户信息。
**为什么重要**: 若 CPO 逐步替代可插拔光模块，可能影响交换 ASIC、光引擎、激光器及数据中心互连产业链，但当前仅为技术趋势讨论，尚无商业落地证据。
**影响产业链**: 潜在影响光通信器件、光引擎、激光器、交换芯片及先进封装环节；但缺少订单、客户、收入、产能或价格验证，无法量化收入与利润影响。
**可能相关公司**: Broadcom (AVGO), Marvell (MRVL), NVIDIA (NVDA), Corning (GLW), Coherent (COHR), Lumentum (LITE), TSMC (TSM)
**可信度**: 低。新闻仅为标题/链接，无正文和社区讨论，且无官方公告或订单数据；搜索资料可辅助背景理解，但不足以支撑高置信度判断。
**投研价值评分**: 15 / 100
**是否需要继续追踪**: 是
**投研理由**: 该新闻为行业分析文章，缺少订单/客户/收入/产能/价格验证，CPO 尚处技术导入早期，因此投研评分保守，总分 15。

**标签**: `#co-packaged-optics`, `#data-center`, `#optical-interconnect`, `#hardware`, `#networking`

---