---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
---

> 从 86 条内容中筛选出 10 条重要资讯。

---

1. [英伟达加入 NSF 州与区域 AI 中心计划，扩大美国 AI 研究与教育](#item-1) ⭐️ 8.0/10
2. [高带宽闪存迎来首个开放规范：512GB 堆栈与高达 3.0TB/s 速度](#item-2) ⭐️ 8.0/10
3. [英伟达 SCADA 将存储控制卸载到 GPU，cuFile 实现开源](#item-3) ⭐️ 8.0/10
4. [FCC 扩大覆盖清单禁止进口超 2 公斤外国机器人](#item-4) ⭐️ 8.0/10
5. [英伟达开放自动驾驶开源模型 Alpamayo 2 Super 商用](#item-5) ⭐️ 7.0/10
6. [混合计算框架超越 TOPS/W 峰值，提升 AI 能效](#item-6) ⭐️ 7.0/10
7. [仿真速度成为芯粒设计的关键瓶颈](#item-7) ⭐️ 7.0/10
8. [芯片行业技术论文周报：8 月 4 日](#item-8) ⭐️ 7.0/10
9. [三星发布 zHBM 芯片堆叠内存，宣称 HBM5 八倍速度并推出 V10 NAND](#item-9) ⭐️ 7.0/10
10. [南方公司签约大型负载量增至 17 吉瓦](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [英伟达加入 NSF 州与区域 AI 中心计划，扩大美国 AI 研究与教育](https://blogs.nvidia.com/blog/nsf-state-regional-ai-hub-program/) ⭐️ 8.0/10

英伟达加入 NSF 州与区域 AI 中心计划，旨在拓宽美国各地获取 AI 计算、数据和专业知识的渠道。

rss · NVIDIA Blog · 8月4日 16:00

**标签**: `#AI`, `#NVIDIA`, `#NSF`, `#Research Infrastructure`, `#Education`

---

<a id="item-2"></a>
## [高带宽闪存迎来首个开放规范：512GB 堆栈与高达 3.0TB/s 速度](https://www.storagereview.com/news/high-bandwidth-flash-gets-its-first-open-spec-512gb-stacks-and-up-to-3-0tb-s) ⭐️ 8.0/10

闪迪和 SK 海力士通过开放计算项目发布了首个开放的高带宽闪存（HBF）规范，支持 512GB 堆栈和高达 3.0TB/s 的速度，适用于 AI 推理系统。

rss · StorageReview · 8月4日 21:03

**标签**: `#storage`, `#flash memory`, `#AI inference`, `#open compute project`, `#hardware`

---

<a id="item-3"></a>
## [英伟达 SCADA 将存储控制卸载到 GPU，cuFile 实现开源](https://www.storagereview.com/news/nvidia-scada-puts-storage-control-on-the-gpu-as-cufile-goes-open-source) ⭐️ 8.0/10

英伟达在 FMS 2026 上发布了 SCADA 系统，将存储控制卸载到 GPU，并开源 cuFile 以提升小块 I/O 性能。SCADA 采用 NVSHMEM 模型，让 GPU 直接发起和管理存储 I/O。 这可以减少 GPU 加速存储场景下的 CPU 开销，支持每秒数百万次小块 I/O，对 AI 和高性能计算负载至关重要。cuFile 开源可能加速 GPUDirect Storage 的采用并扩大生态。 SCADA 全称是 Scaled Accelerated Data Access，采用 NVSHMEM 模型让 GPU 直接发起和管理存储 I/O。它基于 NVIDIA 与 IBM 等在 ASPLOS 2023 发表的 BaM 研究；cuFile 是 GPUDirect Storage 库的一部分，仅支持 Linux。

rss · StorageReview · 8月4日 19:32

**背景**: 传统 GPU 存储访问中，主机 CPU 需要管理文件系统并下发 I/O 命令，对小块传输来说开销很大。SCADA 将控制路径卸载到 GPU，使其直接管理存储。cuFile 为 GPU 直通数据传输提供高级 API，开源旨在鼓励其在存储环境中的更广泛应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blocksandfiles.com/2025/11/25/scada-nvidia/">Nvidia SCADA offloads storage control path to the GPU</a></li>
<li><a href="https://www.tomshardware.com/pc-components/ssds/nvidias-high-speed-ai-data-center-storage-servers-break-cover-touting-2-9-petabytes-of-storage-and-extreme-pcie-6-0-performance-wiwynn-shows-off-scada-server-with-gpu-accelerated-storage">Nvidia's high-speed AI data center storage servers break cover, touting 2.9 petabytes of storage and extreme PCIe 6.0 performance — Wiwynn shows off SCADA server with GPU-accelerated storage | Tom's Hardware</a></li>

</ul>
</details>

**发生了什么**: 英伟达在 FMS 2026 宣布 SCADA（Scaled Accelerated Data Access）技术，将存储控制路径卸载到 GPU，并将 cuFile 开源。目前仅为技术发布和软件开源，没有披露具体订单或客户采购。
**为什么重要**: 该技术有潜力降低 GPU 存储小 I/O 的 CPU 开销，提升 AI/HPC 工作负载的存储吞吐，可能推动 GPUDirect Storage 生态发展，并间接影响 GPU 存储相关产业链。
**影响产业链**: 暂无直接订单或财务数据，供应链影响主要体现在 NVIDIA 软件生态的增强，以及对存储设备、GPU 服务器需求的间接促进。但缺乏可见的产能、价格或收入证据。
**可能相关公司**: NVIDIA (NVDA), Wiwynn, IBM
**可信度**: 中等偏高：多个科技媒体（Blocks & Files、Tom's Hardware）报道，但未见 NVIDIA 官方新闻稿或正式财务指引。
**投研价值评分**: 23 / 100
**是否需要继续追踪**: 是
**投研理由**: 缺少订单/客户/收入/产能/价格验证，本次仅为技术发布和开源，暂无明确商业落地与财务影响。评分保守，仅反映 NVIDIA 生态绑定（platform_binding=8）和技术新颖性（novelty=4），其余子项均因证据不足而低分。

**标签**: `#NVIDIA`, `#GPU storage`, `#cuFile`, `#open source`, `#HPC`

---

<a id="item-4"></a>
## [FCC 扩大覆盖清单禁止进口超 2 公斤外国机器人](https://spectrum.ieee.org/fcc-covered-list-mobile-robots) ⭐️ 8.0/10

2026 年 7 月 28 日，美国联邦通信委员会（FCC）将重量超过 2 公斤的移动通信机器人和功率逆变器加入“覆盖清单”，禁止进口这些类别的新外国制造设备。此举由国防部推动，旨在应对国家安全风险，但也影响了盟国的机器人产业。 这一监管变化为外国机器人制造商，尤其是像宇树科技这样的中国公司，设置了重大障碍，影响美国机器人供应链和全球市场。这标志着美国在关键基础设施和军事相关领域对外国技术的限制进一步升级。 该规则仅适用于新设备；已认证设备仍然可以合法销售和使用。例外情况包括重量低于 2 公斤的机器人、通信速率低于 200 kbps 的设备、无人机、联网车辆和医疗设备。FCC 声称此举“国家中立”，但其理由引用了中国机器人的安全漏洞。

rss · IEEE Spectrum Robotics · 8月4日 11:00

**背景**: FCC“覆盖清单”创建于 2021 年，用于识别被视为国家安全风险的通信设备。被列入清单的设备无法获得 FCC 授权，实际上禁止其在美国进口和销售。此次扩展将先进机器人设备纳入清单，反映了对数据安全和机器人供应链独立的日益担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.fcc.gov/public/attachments/DOC-423682A1.pdf">FACT SHEET: FCC Updates Covered List to Include Foreign-Produced</a></li>
<li><a href="https://www.pcmag.com/news/us-drone-ban-2026-explained-the-fcc-rules-on-dji-autel-and-whats-still">US Drone Ban 2026 Explained: The FCC Rules on DJI, Autel... | PCMag</a></li>

</ul>
</details>

**发生了什么**: 美国 FCC 将外国制造的移动机器人（重量>2 公斤）和功率逆变器加入“覆盖清单”，禁止进口和销售新产品，自 2026 年 7 月 28 日起生效。
**为什么重要**: 这标志着美国对机器人技术进口的首次广泛限制，影响所有外国机器人制造商，尤其中国公司，可能重塑全球机器人供应链，并促使美国国内产能建设。
**影响产业链**: 影响机器人产业链的进口环节，导致外国设备进入美国市场受阻。可能影响美国机器人应用企业的采购成本，长期可能推动美国本土制造和替代供应链，但短期内对已认证设备无影响，因此对现有收入冲击有限。
**可能相关公司**: Unitree (宇树科技), DJI (大疆), Boston Dynamics, Agility Robotics
**可信度**: 高，因为依据官方 FCC 文件和知名科技媒体 IEEE Spectrum 的报道，信息可靠。
**投研价值评分**: 22 / 100
**是否需要继续追踪**: 是
**投研理由**: 缺少订单/客户/收入/产能/价格验证，监管政策变化虽影响进口和市场准入，但未见具体商业合同或财务数据，故总分保守为 22。

**标签**: `#robotics`, `#FCC`, `#regulation`, `#national security`, `#import ban`

---

<a id="item-5"></a>
## [英伟达开放自动驾驶开源模型 Alpamayo 2 Super 商用](https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/) ⭐️ 7.0/10

英伟达发布了面向自动驾驶的 340 亿参数开源基础模型 Alpamayo 2 Super，现已可商用。该模型将 320 亿参数视觉语言主干与 20 亿参数扩散专家结合。 Alpamayo 2 Super 针对自动驾驶最难处理的“长尾事件”（罕见且复杂的驾驶场景）。作为 Hugging Face 上被采用最多的自动驾驶开放推理模型之一，它可能加速整个行业的自动驾驶开发。 该模型属于 Alpamayo 系列，该系列被描述为 Hugging Face 上采用最多的自动驾驶开放推理模型。它在一个基础模型中支持多种自动驾驶相关能力。

rss · NVIDIA Blog · 8月4日 15:00

**背景**: 自动驾驶汽车不仅要处理常规场景，还要应对难以预料的罕见长尾事件。传统的端到端驾驶模型往往因为这些罕见输入超出训练分布而失效。像 Alpamayo 2 Super 这样的开放基础模型旨在帮助自动驾驶系统理解上下文、推理因果关系并选择合适的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/">NVIDIA Alpamayo 2 Super , the Frontier Open Model ... | NVIDIA Blog</a></li>
<li><a href="https://huggingface.co/nvidia/Alpamayo2-Super">nvidia / Alpamayo 2 - Super · Hugging Face</a></li>
<li><a href="https://github.com/NVlabs/alpamayo2">GitHub - NVlabs/ alpamayo 2 : NVIDIA Alpamayo 2 Super is an open...</a></li>

</ul>
</details>

**发生了什么**: 英伟达正式发布并开放商用 Alpamayo 2 Super 模型，这是一个面向自动驾驶的 340 亿参数开源基础模型。目前没有披露具体客户或订单。
**为什么重要**: 该模型针对自动驾驶长尾场景，可能提升行业开发效率，但尚无商业落地或收入贡献证据。
**影响产业链**: 短期内不会对产业链收入、利润或现金流产生直接可量化影响；可能影响自动驾驶软件工具链和英伟达 AI 平台生态，但需跟踪后续采用情况。
**可能相关公司**: NVIDIA (NVDA), Hugging Face（未上市）
**可信度**: 信源可信度高（官方博客），但缺乏商业验证，整体投资信号中等偏低。
**投研价值评分**: 29 / 100
**是否需要继续追踪**: 是
**投研理由**: 缺少订单/客户/收入/产能/价格验证；仅凭模型发布不足以给出高投资评分。

**标签**: `#autonomous vehicles`, `#AI model`, `#NVIDIA`, `#robotics`, `#open source`

---

<a id="item-6"></a>
## [混合计算框架超越 TOPS/W 峰值，提升 AI 能效](https://semiengineering.com/hybrid-computing-framework-looks-beyond-peak-tops-w-for-ai-efficiency-nottingham-trent-icl-aston/) ⭐️ 7.0/10

诺丁汉特伦特大学、伦敦帝国理工学院和阿斯顿大学的研究人员发表了一篇技术论文，提出一种系统级的混合数字-模拟计算框架。论文认为，将数字计算与模拟、光子、存内或神经形态引擎相结合，是实现更高能效人工智能的一条可行路径。 TOPS/W 被广泛用作 AI 加速器的能效指标，但它忽略了内存吞吐、数据搬运和负载相关的效率。这个系统级框架可能改变 AI 硬件的设计与评估方式，从而影响未来边缘和数据中心中低功耗 AI 的部署。 论文标题为《超越峰值 TOPS/W：混合数字、模拟与神经形态计算的系统级视角》。混合引擎可以采用模拟电子、光子、存内或神经形态原理，每种引擎分别负责最适合自己的计算任务。

rss · SemiEngineering · 8月5日 03:09

**背景**: TOPS（每秒万亿次运算）衡量 AI 推理的峰值性能，而 TOPS/W 衡量处理器每瓦功耗执行多少次运算。然而，实际推理性能还取决于内存带宽、模型优化和数据流水线效率。神经形态计算利用人工神经元模仿大脑的结构和功能，通常优先考虑能效和事件驱动处理。混合数字-模拟计算将快速的模拟器件与通用的数字处理器相结合，以实现更好的整体效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.03514">Beyond Peak TOPS/W: A System-Level Perspective on Hybrid Digital ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Analog_computer">Analog computer - Wikipedia</a></li>
<li><a href="https://www.qualcomm.com/news/onq/2024/04/a-guide-to-ai-tops-and-npu-performance-metrics">A guide to AI TOPS and NPU performance metrics | Qualcomm</a></li>

</ul>
</details>

**发生了什么**: 英国诺丁汉特伦特大学、帝国理工学院和阿斯顿大学的研究者发表了一篇论文，提出应超越峰值 TOPS/W 指标，从系统层面评估混合数字-模拟、光子、存内及神经形态计算在 AI 能效中的价值。目前只是学术研究，没有任何商业部署或订单信息。
**为什么重要**: 若该框架被工业界采纳，可能影响 AI 加速器的设计思路和评测标准，进而改变低功耗 AI 硬件市场的竞争格局。但现阶段距离产品化还很远，不会直接影响近期收入或利润。
**影响产业链**: 暂无明确的产业链影响。可能的间接影响在于推动混合信号芯片、存内计算、光子计算等上游技术获得更多研发关注，但缺少订单和产量证据，不能据此推断对收入或现金流的影响。
**可信度**: 中。来源为半导体行业媒体 Semiconductor Engineering，论文可在 arXiv 上查到，属于学术研究报道，可信度中等。
**投研价值评分**: 14 / 100
**是否需要继续追踪**: 是
**投研理由**: 该新闻为纯学术研究，缺少订单/客户/收入/产能/价格验证。根据保守原则，投资评分定为 14 分：capex_impact 2（无具体资本支出变化），order_evidence 0（无订单证据），supply_demand_impact 2（无供需失衡证据，仅潜在方向），platform_binding 0（无绑定大客户平台），earnings_elasticity 0（无盈利影响），source_confidence 7（行业媒体+arXiv，可信度中等），novelty 3（系统级视角有一定新颖性）。总分未超过论文类新闻 40 分上限。

**标签**: `#AI`, `#hardware`, `#energy efficiency`, `#hybrid computing`, `#neuromorphic`

---

<a id="item-7"></a>
## [仿真速度成为芯粒设计的关键瓶颈](https://semiengineering.com/why-simulation-speed-is-holding-chiplets-back/) ⭐️ 7.0/10

《半导体工程》报道称，在异构芯粒设计中，工具链能力已不再是限制因素；跨 2.5D 和 3D 堆叠的多物理场协同仿真的计算成本才是主要瓶颈。 这一转变凸显了先进封装和异构集成面临的关键挑战，设计团队现在必须加大对仿真基础设施和算法效率的投入，才能跟上芯粒复杂度的步伐。这可能会影响 EDA 工具的开发优先级以及 AI 和高性能计算芯片的设计成本。 文章指出，跨芯粒耦合热、机械和电域的多物理场协同仿真，随着裸片数量和堆叠层数的增加，计算成本变得难以承受。文中未点名具体厂商或工具，但讨论强调仿真速度现已落后于设计工具能力。

rss · SemiEngineering · 8月4日 07:02

**背景**: 芯粒是小型集成电路，可以组合在中介层或 3D 堆叠上以创建更大的处理器，从而实现不同工艺节点和功能的异构集成。多物理场协同仿真将热、电磁和机械等多个仿真域耦合到单一工作流中，以准确预测系统行为。然而，随着 2.5D 和 3D 集成规模扩大，这种协同仿真的计算负担呈指数级增长，使其成为新的瓶颈，尽管 EDA 工具已经取得了进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chiplet">Chiplet - Wikipedia</a></li>
<li><a href="https://www.keysight.com/blogs/en/tech/sim-des/what-is-a-chiplet-and-why-should-you-care">What is a Chiplet, and Why Should You Care? | Keysight Blogs</a></li>
<li><a href="https://hexagon.com/solutions/multiphysics-co-simulation">Co - simulation for coupled physics | Hexagon</a></li>

</ul>
</details>

**发生了什么**: 行业媒体撰文指出，芯粒设计的主要瓶颈已从工具链能力转向多物理场协同仿真的计算成本。
**为什么重要**: 这可能会推动 EDA 厂商和半导体设计团队加大对仿真算法和高性能计算资源的投入，但文章仅为行业观点，未涉及具体订单或资本开支变化。
**影响产业链**: 可能影响 EDA 工具、仿真软件及先进封装设计服务的市场需求，但短期无直接收入或利润变动证据。
**可能相关公司**: Synopsys, Cadence, Siemens EDA
**可信度**: 中低。来源为行业媒体，内容可信但缺乏一手商业数据。
**投研价值评分**: 16 / 100
**是否需要继续追踪**: 是
**投研理由**: 缺少订单/客户/收入/产能/价格验证，仅为技术瓶颈讨论，投资信号弱。

**标签**: `#chiplets`, `#simulation`, `#multi-physics`, `#2.5D/3D integration`, `#semiconductor design`

---

<a id="item-8"></a>
## [芯片行业技术论文周报：8 月 4 日](https://semiengineering.com/chip-industry-technical-paper-roundup-aug-4/) ⭐️ 7.0/10

《半导体工程》于 8 月 4 日发布了每周技术论文摘要，涵盖存储、神经形态计算、硬件安全、氧化物电子学和基于 LLM 的设计流程等进展。具体主题包括混合 NAND 闪存-DRAM 存储、多核神经形态计算和前硅功耗侧信道分析。 该摘要帮助芯片专业人士快速了解前沿半导体研究，这些研究可能影响未来芯片架构、安全验证方法和材料选择。它突出了神经形态计算和氧化物电子学等领域中持续活跃的研究，最终可能影响更广泛的产业链。 论文还涉及模块化硬件-软件泄漏验证、用 2D 半导体填补氧化物电子学中的 p 型空白以实现互补 BEOL CMOS，以及面向 Verilog 设计流程的 LLM 基准测试。这些均属研究级成果，未提及商业化部署。

rss · SemiEngineering · 8月4日 07:01

**背景**: 《半导体工程》每周汇集来自各学术会议和期刊的技术论文。神经形态计算旨在模仿神经结构以实现更高效的 AI 处理，而氧化物电子学被探索用于后端（BEOL）CMOS 集成，其中 p 型材料仍然是一个难题。前硅功耗侧信道分析旨在流片之前检测加密硬件中的漏洞，以降低安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neuromorphic_computing">Neuromorphic computing - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/s44172-026-00723-3?error=cookies_not_supported&code=7175eb69-ffb4-48ab-80fd-bb767c31bafd">Bridging the p - type gap in oxide electronics with 2D semiconductors</a></li>
<li><a href="https://www.mdpi.com/2674-0729/3/4/16">PreSCAN: A Comprehensive Review of Pre-Silicon Physical Side-Channel Vulnerability Assessment Methodologies</a></li>

</ul>
</details>

**发生了什么**: 《半导体工程》发布了 8 月 4 日当周的芯片行业技术论文摘要，汇总了存储、神经形态计算、硬件安全、氧化物电子学和 LLM 设计流程等多个研究方向的最新论文。
**为什么重要**: 该内容属于研究综述，缺乏具体的商业订单、客户采购、量产部署或财务指引，短期对产业链收入和利润无直接影响。但其中涉及的技术方向（如神经形态计算、BEOL 氧化物 CMOS、前硅安全验证）值得长期跟踪。
**影响产业链**: 目前未观察到对具体产业链环节收入、利润或现金流的直接冲击。论文中提及的技术如混合 NAND-DRAM、氧化物 p 型半导体等仍处于研究阶段，距离商业化较远，不会立即改变供需格局。
**可能相关公司**: Intel (INTC), IBM (IBM)
**可信度**: 中
**投研价值评分**: 10 / 100
**是否需要继续追踪**: 否
**投研理由**: 这是技术论文周报，不包含订单、客户、收入、产能、价格或供应链影响等硬投资信号，因此按规则保守评分。缺少订单/客户/收入/产能/价格验证。来源为行业媒体，可信度中等；技术方向有一定新颖性，但无商业化证据。

**标签**: `#semiconductors`, `#chip design`, `#hardware security`, `#neuromorphic computing`, `#memory technology`

---

<a id="item-9"></a>
## [三星发布 zHBM 芯片堆叠内存，宣称 HBM5 八倍速度并推出 V10 NAND](https://news.google.com/rss/articles/CBMijgFBVV95cUxOdFhNVEdIZjJmN0JhSDZfRmw1bG1nU0hMdE1BMHFRMmRzV01uNWFCemJBcE91d1lUTlFPOGdtZ2VFT0NDQTEtOXBpemFNWFc2c2tDTV91aEl2U1R5cmFXTkZ3V1owd2U5aGtuZmVnQURHRkJ2OFdtUWJjWUtrQmlUdlpYSUpiblVIcTRoQUln0gGOAUFVX3lxTE50WE1UR0hmMmY3QmFINl9GbDVsbWdTSEx0TUEwcVEyZHNXTW41YUJ6YkFwT3V3WVROUU84Z21nZUVPQ0NBMS05cGl6YU1YVzZza0NNX3VoSXZTVHlyYVdORndXWjB3ZTloa25mZWdBREdGQnY4V21RYmNZS2tCaVR2WlhJSmJuVUhxNGhBSWc?oc=5) ⭐️ 7.0/10

三星发布了 zHBM 概念架构，将高带宽内存垂直堆叠在 AI 加速器芯片之上，而非并排放置，并宣称其速度可达 HBM5 的 8 倍。该公司还推出了 V10 NAND，即超过 400 层的下一代 3D NAND。 这可能通过取消硅中介层从根本上改变 AI 加速器封装方式，有望缓解严重的 HBM 供应短缺。若实现商业化，将增强三星在 AI 内存市场对 SK 海力士和美光的竞争力。 据媒体报道，zHBM 被定位为 HBM4 之后的新架构，性能约为当前英伟达最新 AI 芯片所用 HBM 的 4 倍。V10 BV-NAND 据报道超过 400 层，标志着三星 3D NAND 堆叠路线图的重要一步。

rss · Google News - HBM Memory · 8月5日 00:15

**背景**: 高带宽内存（HBM）是一种为超高带宽和能效设计的 3D 堆叠 DRAM 技术，广泛用于 AI 加速器。2025 年开始的全球 HBM 和内存短缺源于产能向 AI 产品转移，预计将持续到 2027 年或更晚。三星的 zHBM 概念将内存直接堆叠在 AI 芯片顶部，取消硅中介层，有望提升性能、能效并降低成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.sedaily.com/finance/2026/02/11/samsung-unveils-zhbm-technology-to-stack-memory-on-gpus">Samsung Unveils zHBM Technology to Stack Memory on GPUs - Seoul Economic Daily</a></li>
<li><a href="https://www.trendforce.com/news/2026/02/18/news-breaking-hbm-barriers-samsungs-zhbm-vs-intels-z-angle-memory/">[News] Breaking HBM Barriers: Samsung’s zHBM vs. Intel’s Z-Angle Memory</a></li>
<li><a href="https://www.techtimes.com/articles/323062/20260804/samsungs-zhbm-places-memory-top-ai-chips-bv-nand-shatters-400-layer-barrier.htm">Samsung's zHBM Places Memory on Top of AI Chips; BV-NAND Shatters 400-Layer Barrier</a></li>

</ul>
</details>

**发生了什么**: 三星在公开场合发布了 zHBM 概念，即把 HBM 垂直堆叠在 AI 加速器芯片上，以替代传统硅中介层方案；同时公布了超过 400 层的 V10 NAND 技术。
**为什么重要**: 该技术若落地，可能改变 HBM/逻辑芯片的封装产业格局，影响 AI 加速器成本与性能，并在 HBM 短缺背景下提供新方案，但目前仅是概念发布，无客户或订单。
**影响产业链**: 短期不改变量产、价格或供应链；长期可能影响 HBM 封装设备（TSV、键合设备）、硅中介层供应商、以及三星与 SK 海力士/美光的竞争格局，但缺乏收入或利润弹性验证。
**可能相关公司**: Samsung Electronics (005930.KS), SK hynix (000660.KS), Micron (MU), NVIDIA (NVDA)
**可信度**: 中：多家科技媒体（TrendForce、TechTimes、首尔经济等）交叉报道，但三星官方尚未发布正式新闻稿或技术白皮书。
**投研价值评分**: 20 / 100
**是否需要继续追踪**: 是
**投研理由**: 缺少订单/客户/收入/产能/价格验证，属于概念架构发布；未披露量产计划或具体客户采用，capex、订单、供需、盈利弹性证据不足，故总分保守取 20 分。

**标签**: `#HBM`, `#Samsung`, `#semiconductor`, `#memory`, `#NAND`

---

<a id="item-10"></a>
## [南方公司签约大型负载量增至 17 吉瓦](https://www.utilitydive.com/news/southern-co-contracted-large-load-data-centers/826919/) ⭐️ 6.0/10

南方公司报告其签约的大型负载组合已增长至 17 吉瓦，其中包括一个 3.2 吉瓦的 OpenAI 数据中心，并包含一项首创的灵活需求响应协议。

rss · Utility Dive · 8月4日 13:20

**标签**: `#data centers`, `#energy demand`, `#OpenAI`, `#grid reliability`, `#AI infrastructure`

---