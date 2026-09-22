---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> 从 82 条内容中筛选出 10 条重要资讯。

---

1. [BOOST 运行时实现 HBM 与主机内存并发访问以加速 LLM 推理](#item-1) ⭐️ 7.0/10
2. [当使用 HLS 在更高抽象层次上操作时，智能体能否设计出更好的芯片？(UCLA)](#item-2) ⭐️ 7.0/10
3. [ABB 推出 Infinitus 800 VDC 端到端供电方案，瞄准 1MW 机架](#item-3) ⭐️ 7.0/10
4. [AI 加速服务器销售再度加速，GPU 系统占服务器支出过半](#item-4) ⭐️ 7.0/10
5. [波士顿动力开设超级工厂应用中心，训练 Atlas 执行制造任务](#item-5) ⭐️ 7.0/10
6. [Imec 发布 100 GHz Ge/Si 雪崩光电二极管，5V 下实现 400 Gbps 接收](#item-6) ⭐️ 7.0/10
7. [NVIDIA 推出 DSX Ready，为 AI 工厂认证电源和冷却产品](#item-7) ⭐️ 6.0/10
8. [威斯康星大学麦迪逊分校与 Marist 提出 LoRD 启发式方法，定位门级网表中的 RTL 硬件木马](#item-8) ⭐️ 6.0/10
9. [Blocks & Files 评测大普微 SLC 与 QLC 混合企业级 SSD](#item-9) ⭐️ 6.0/10
10. [FCIA 发布 FC-SP-3 光纤通道安全标准，面向后量子计算时代](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [BOOST 运行时实现 HBM 与主机内存并发访问以加速 LLM 推理](https://semiengineering.com/concurrent-hbm-and-host-memory-access-improves-llm-inference-throughput-georgia-tech-nvidia-stanford/) ⭐️ 7.0/10

佐治理工学院、英伟达研究院与斯坦福大学的研究人员联合发表了题为《BOOST: Concurrent Access to Host Memory and HBM to Accelerate LLM Inference》的技术论文，提出了首个可对 GPU 两级内存（主机内存与 HBM）进行并发、按比例访问的运行时系统。BOOST 不再把主机内存仅当作 HBM 的暂存区，而是聚合主机内存与 HBM 的带宽来提升 LLM 推理吞吐。 大模型解码阶段通常受内存带宽制约，因此在不依赖下一代 HBM 容量的前提下，把主机内存与 HBM 的带宽叠加利用，有望提升推理吞吐并降低单位推理成本。由于英伟达研究院参与其中，相关技术可能影响未来 GPU 内存管理软件，并改变现有 AI 加速卡的价值释放方式。 摘要强调的是"并发且按比例"的访问，而非简单地把张量卸载到 CPU 内存，即运行时按两级内存的相对带宽决定流量分配比例。目前该消息仅为论文摘要片段，具体基准数据、支持的硬件平台以及潜在的开销与延迟代价尚未披露。

rss · SemiEngineering · 9月21日 23:13

**背景**: HBM 是一种三维堆叠的 DRAM 接口，紧邻 GPU 裸片布置，可提供极高带宽，因此成为英伟达数据中心 GPU 等 AI 加速卡的标准配置。但单卡 HBM 容量有限且成本高昂，主机（CPU）内存容量大、价格低，历史上从 GPU 访问却较慢。大模型推理尤其是自回归逐 token 生成，每个 token 都要搬运大量权重与 KV 缓存张量，内存带宽因而成为主要瓶颈；此前的方案要么全部放在 HBM，要么把数据卸载到主机内存但付出高昂传输代价。BOOST 的思路是同时使用两级内存，把带宽叠加起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.13592v1">Concurrent Access to Host Memory and HBM to Accelerate LLM Inference</a></li>
<li><a href="https://www.alphaxiv.org/abs/2609.13592">BOOST: Concurrent Access to Host Memory and HBM to Accelerate ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**发生了什么**: 佐治理工学院、英伟达研究院与斯坦福大学联合发表技术论文，提出 BOOST 运行时系统，可对 GPU HBM 与主机内存进行并发、按比例访问，从而聚合两级内存带宽以提升大模型推理吞吐。该消息目前只是论文摘要片段，尚无完整基准与落地信息。
**为什么重要**: 大模型推理的解码阶段普遍是内存带宽瓶颈，若能把主机内存带宽也纳入推理数据通路，现有 AI 服务器在不增加 HBM 容量的情况下即可获得更高吞吐，潜在影响推理单位成本、GPU 利用率以及 HBM 与主机内存的配置比例。英伟达研究院的参与使该技术存在向产品级软件栈渗透的可能，但当前仍属研究阶段。
**影响产业链**: 短期不改变任何环节的收入、利润或现金流：论文未涉及订单、量产部署或采购。中期若被英伟达软件栈采纳，可能轻微降低对 HBM 容量扩张的边际需求压力，同时提升主机 DRAM 在 AI 服务器中的配置价值，利好 DRAM 与内存接口环节，但对 HBM 厂商而言是需求结构而非需求总量的变化；以上均为推演，缺少订单/客户/收入/产能/价格验证。
**可能相关公司**: NVDA (英伟达), 000660.KS (SK 海力士), 005930.KS (三星电子), MU (美光科技), TSM (台积电)
**可信度**: 中：论文有 arXiv 预印本与半导体工程媒体转载，来源可交叉验证，但内容公开程度有限（仅摘要片段），且无任何商用落地证据。
**投研价值评分**: 19 / 100
**是否需要继续追踪**: 是
**投研理由**: 该消息属于学术论文与运行时系统研究，缺少订单、客户采购、量产部署、产能扩张、价格变化或财务指引等硬性投资信号，按规则此类研究默认 10-35 分。capex_impact 仅 1 分（未涉及超大规模或运营商资本开支变化）；order_evidence 为 0（无任何订单或客户证据）；supply_demand_impact 1 分（可能间接影响 HBM 与主机 DRAM 的配置比例，但无价格或供需验证）；platform_binding 5 分（英伟达研究院为共同作者，属研究合作而非产品绑定）；earnings_elasticity 1 分（无可推断的营收或毛利影响）；source_confidence 7 分（arXiv 预印本加行业媒体转载，可交叉验证但信息不完整）；novelty 4 分（首个并发利用两级 GPU 内存的运行时系统，具备一定新颖性）。合计 19 分，未突破研究类 40 分上限。后续应跟踪该工作是否进入 CUDA/推理框架的正式版本，以及是否有云厂商或芯片厂商公布实测吞吐与部署情况。

**标签**: `#LLM Inference`, `#GPU Memory`, `#Systems Research`, `#HBM`, `#Performance Optimization`

---

<a id="item-2"></a>
## [当使用 HLS 在更高抽象层次上操作时，智能体能否设计出更好的芯片？(UCLA)](https://semiengineering.com/can-agents-design-better-chips-when-operating-at-a-higher-level-of-abstraction-using-hls-ucla/) ⭐️ 7.0/10

加州大学洛杉矶分校的研究人员调查了 LLM 智能体是否可以通过使用 HLS 在更高抽象层次上操作（而不是直接使用 RTL）来设计出更好的芯片。

rss · SemiEngineering · 9月21日 22:59

**标签**: `#AI/ML`, `#EDA`, `#LLM agents`, `#HLS`, `#chip design`

---

<a id="item-3"></a>
## [ABB 推出 Infinitus 800 VDC 端到端供电方案，瞄准 1MW 机架](https://www.storagereview.com/news/abb-infinitus-brings-a-source-to-rack-800-vdc-portfolio-to-ai-data-centers) ⭐️ 7.0/10

ABB 正式推出 Infinitus，这是一套面向 AI 数据中心的端到端（source-to-rack）直流供电技术产品组合，核心是 800 VDC 配电架构。ABB 表示该方案瞄准未来将达到并超过 1 MW 的单机架功耗，并宣称可实现最高约 5%的效率提升。 这一发布表明，随着 AI 机架功耗逼近 1 MW，行业正从当前主流的 48-54 VDC 机架配电转向更高电压的 800 VDC，这将带动新型电源转换、母线（busbar）和整流器等硬件需求。若超大规模云厂商采纳该架构，可能在下代 GPU 机架到来前重塑数据中心供电供应链。 ABB 指出，当前 AI 机架功耗已接近 200 kW，并认为下一代芯片将需要一种能够消除低压大电流配电损耗与体积负担的电气架构。该产品组合被描述为覆盖从电源侧到机架的完整路径，而非单一部件。

rss · StorageReview · 9月21日 17:03

**背景**: 数据中心历来在机架层面采用 48-54 VDC 等低压直流配电，但在如此低的电压下输送数百千瓦电力需要极粗的铜母排，并会产生大量转换损耗。NVIDIA 已为其未来机架提出 800 VDC 高压直流（HVDC）参考架构，多家电源厂商正竞相供应整流器、sidecar 辅助电源和母排。计划用于 Kyber 机架的 Vera Rubin Ultra 等 GPU 推动机架功耗迈向 1 MW，正是这一趋势使更高电压直流供电成为必需。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/">NVIDIA 800 VDC Architecture Will Power the Next Generation of AI ...</a></li>
<li><a href="https://blog.se.com/datacenter/2025/10/16/the-1-mw-ai-it-rack-is-coming-and-it-needs-800-vdc-power/">The 1 MW AI IT rack is coming, and it needs 800 VDC power - Schneider Electric Blog</a></li>
<li><a href="https://www.abb.com/global/en/industries/data-centers">Global Data Center Solutions Powering Advanced AI ... - ABB</a></li>

</ul>
</details>

**发生了什么**: ABB 发布 Infinitus 端到端 800 VDC 直流供电产品组合，面向 AI 数据中心，目标支持 1 MW 及以上的单机架功耗，并宣称最高约 5%的效率提升，涵盖从电源侧到机架的完整供电链路。
**为什么重要**: 该发布顺应了 NVIDIA 推动的 800 VDC 高压直流参考架构趋势，随着 AI 机架功耗从当前近 200 kW 迈向 1 MW，数据中心供电将从 48-54 VDC 向 800 VDC 迁移，可能带动整流器、母线、sidecar 等新型电力硬件需求。
**影响产业链**: 潜在影响数据中心电力设备产业链，包括高压直流电源、整流器、固态变压器、母排/连接器及机架级供电模块。但本次仅为厂商产品组合发布，缺少订单、客户、收入与产能验证，尚无法确认对收入、利润或现金流的实际拉动。
**可能相关公司**: ABB (ABBN.SW / ABB), NVIDIA (NVDA), Vertiv (VRT), Schneider Electric (SU.PA), Eaton (ETN), Delta Electronics (2308.TW), Lite-On (2301.TW)
**可信度**: 中。来源为 StorageReview 对 ABB 官方产品组合发布的报道，事件本身可信，且与 NVIDIA 800 VDC 架构及多家电源厂商路线图相互印证；但缺少订单金额、客户名称、量产时间表与财务指引，商业落地确定性不足。
**投研价值评分**: 34 / 100
**是否需要继续追踪**: 是
**投研理由**: 本次为厂商产品组合/平台级发布，绑定 NVIDIA 主导的 800 VDC 参考架构，具备一定平台绑定价值（platform_binding 11）与数据中心供电资本开支趋势相关性（capex_impact 7），但缺少订单/客户/收入/产能/价格验证（order_evidence 0、earnings_elasticity 3、supply_demand_impact 4），故按规则保守评分，source_confidence 6、novelty 3，合计 34 分，未达到高置信投研信号门槛。

**标签**: `#AI data centers`, `#data center power`, `#800 VDC`, `#high-density computing`, `#infrastructure`

---

<a id="item-4"></a>
## [AI 加速服务器销售再度加速，GPU 系统占服务器支出过半](https://www.nextplatform.com/compute/2026/09/21/accelerated-server-sales-are-themselves-accelerating/5297993) ⭐️ 7.0/10

The Next Platform 报道称，2026 年第二季度全球在服务器节点与整机柜系统上的支出为 1623.2 亿美元，其中 52.5%（约 874 亿美元）用于 GPU 加速系统，也就是说加速服务器的销售额不仅在增长，而且增速本身还在加快。 这表明 AI 基础设施支出已从小众项目变成服务器市场的主体，直接决定数据中心内 GPU、高带宽内存、供电散热与网络设备的需求规模，因此对整条算力硬件产业链具有方向性意义。 该数字属于季度市场规模统计，而非某家公司的订单或业绩指引，反映的是超大规模云厂商与云服务商的总体支出趋势；同类报道还指出，2023 至 2028 年间 GPU 加速服务器在收入和出货量两方面的增速均快于普通服务器。

rss · The Next Platform · 9月21日 19:21

**背景**: 加速服务器是指以专用芯片（GPU、NPU 等 AI 加速器）为核心的服务器，用它们来加速深度学习所需的矩阵运算，而不再只依赖 CPU。IDC 等市场研究机构会按季度统计超大规模云厂商和企业在这类系统上的支出，这一支出已成为衡量 AI 基建投入的主要指标。当 GPU 加速系统占据服务器总收入的一半以上，说明驱动数据中心资本预算的已经是 AI 训练与推理负载，而非通用计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nextplatform.com/compute/2026/09/21/accelerated-server-sales-are-themselves-accelerating/5297993">Accelerated Server Sales Are Themselves Accelerating</a></li>
<li><a href="https://www.datacenterknowledge.com/servers/ai-accelerated-servers-fuel-growth-in-data-center-spending?trk=article-ssr-frontend-pulse_little-text-block">AI Accelerated Servers Fuel Growth in Data Center Spending</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_accelerator">AI accelerator</a></li>

</ul>
</details>

**发生了什么**: The Next Platform 引用市场统计数据指出，2026 年第二季度服务器节点与整机柜系统支出达 1623.2 亿美元，其中 GPU 加速系统占 52.5%、约 874 亿美元，加速服务器收入增速本身正在加快。
**为什么重要**: 这说明 AI 算力硬件已占服务器市场收入过半，是数据中心资本开支结构变化的直接证据，指向 GPU、HBM、电源散热、交换网络等环节的持续需求。
**影响产业链**: 对上游 GPU 与 AI 加速芯片、HBM 存储、先进封装、服务器整机 ODM、液冷与电源、数据中心网络（以太网/InfiniBand）等环节构成需求侧支撑；但本条是行业总量数据，未给出任何单一厂商的收入、毛利或现金流增量。
**可能相关公司**: NVIDIA (NVDA), AMD (AMD), Broadcom (AVGO), Marvell (MRVL), Vertiv (VRT), Dell (DELL), Super Micro (SMCI), 台积电 (TSM)
**可信度**: 中：来源为 The Next Platform 这类专业服务器行业媒体，数据基于第三方市场统计，可信度尚可，但属于二手汇总且缺少官方公告与公司层面验证。
**投研价值评分**: 40 / 100
**是否需要继续追踪**: 是
**投研理由**: capex_impact 12 分（反映超大规模数据中心服务器支出规模数据，但并非新增资本开支公告）；order_evidence 3 分（无订单或具名客户采购，仅总量出货/支出统计）；supply_demand_impact 5 分（体现强劲需求，但无涨价、缺货或产能瓶颈的直接证据）；platform_binding 5 分（GPU 加速系统隐含 Nvidia 等平台，但未点名客户或平台）；earnings_elasticity 5 分（缺少订单/客户/收入/产能/价格验证，无法测算上市公司业绩弹性）；source_confidence 8 分（专业行业媒体且引用市场数据）；novelty 2 分（属既有趋势的延续确认）。总分 40，符合缺少硬性投资信号时不超过 45 的约束。

**标签**: `#AI infrastructure`, `#server market`, `#GPUs`, `#data centers`, `#hardware trends`

---

<a id="item-5"></a>
## [波士顿动力开设超级工厂应用中心，训练 Atlas 执行制造任务](http://www.roboticstomorrow.com/news/2026/09/21/boston-dynamics-opens-robotics-metaplant-application-center-to-train-humanoid-robots-for-manufacturing-tasks/27129) ⭐️ 7.0/10

2026 年 9 月 21 日，波士顿动力宣布成立“机器人超级工厂应用中心”（RMAC），该设施位于佐治亚州萨凡纳附近的现代汽车集团美国超级工厂（HMGMA）内部，Atlas 人形机器人目前正在此接受制造任务训练。此举标志着 Atlas 从实验室演示走向其母公司现代汽车集团旗下真实的汽车生产园区。 这是人形机器人从摆拍式演示走向真实汽车工厂车间的最明确信号之一，而且机器人供应商与最终客户同属一个母公司。如果 Atlas 的训练能够转化为常态化生产作业，可能会重塑车企在重复性装配、检测与物料搬运环节的用工方式，并加大其他人形机器人开发商和工业自动化供应商的竞争压力。 该公告属于设施启用与训练里程碑，而非技术披露：波士顿动力并未公布参与训练的 Atlas 数量、具体承担的任务、节拍时间、稼动率或商业化部署时间表。据此前报道，HMGMA 是位于佐治亚州埃拉贝尔、投资额 76 亿美元的“软件定义工厂”，已在电动车与混合动力车生产中整合 AI 与机器人自动化。

rss · Robotics Tomorrow · 9月21日 14:42

**背景**: 波士顿动力是 Spot、Stretch 和 Atlas 等机器人背后的公司，现代汽车集团于 2021 年收购其控股权，因此双方是关联方而非独立合作方。Atlas 是一款人形机器人，波士顿动力将其从液压平台重新设计为全电动平台，新版本定位已从纯研究转向真实工业作业。现代汽车集团美国超级工厂（HMGMA）是现代在佐治亚州新建的大型整车工厂，“metaplant（超级工厂）”一词指的是其“软件定义工厂”理念，即在生产体系中整合 AI、数据与机器人技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bostondynamics.com/news/boston-dynamics-opens-robotics-metaplant-application-center-to-train-humanoid-robots-for-manufacturing-tasks/">Boston Dynamics Opens Robotics Metaplant Application Center to Train Humanoid Robots for Manufacturing Tasks | Boston Dynamics</a></li>
<li><a href="https://www.therobotreport.com/boston-dynamics-opens-metaplant-application-center-train-atlas-humanoid-robots/">Boston Dynamics opens Metaplant Application Center to train Atlas humanoid robots - The Robot Report</a></li>
<li><a href="https://www.automotivemanufacturingsolutions.com/smart-factory/hyundai-reshapes-vehicle-production-at-metaplant-america/2677700">Hyundai Metaplant America reshapes EV and hybrid production with smart factory automation</a></li>

</ul>
</details>

**发生了什么**: 2026 年 9 月 21 日，波士顿动力宣布在现代汽车集团美国超级工厂（HMGMA，位于佐治亚州埃拉贝尔/萨凡纳附近，投资额 76 亿美元）内设立“机器人超级工厂应用中心”（RMAC），并已开始在该中心训练 Atlas 人形机器人执行制造任务。
**为什么重要**: 这是人形机器人进入真实整车厂环境的官方落地节点，供应商（波士顿动力）与客户（现代汽车集团）同属一个集团，属于内部验证型部署，可作为人形机器人商业化节奏的观察样本，但当前仍处于“训练”阶段而非量产替代人工阶段。
**影响产业链**: 潜在影响两条链条：一是人形机器人本体与关键零部件（执行器、减速器、丝杠、力/触觉传感、电池与电控）的中长期需求，二是整车厂装配、物流搬运环节的自动化设备与人力成本结构。但本次公告未披露任何订单金额、采购数量、售价、产能规划或收入贡献，短期对相关上市公司收入、利润与现金流无可验证影响。
**可能相关公司**: Hyundai Motor Group（现代汽车，005380.KS）, Hyundai Mobis（现代摩比斯，012330.KS）, Hyundai AutoEver（现代 AutoEver，307950.KS）, Boston Dynamics（未上市，现代汽车集团控股）
**可信度**: 中高：消息来自波士顿动力官方新闻稿，并由 The Robot Report、Automotive Manufacturing Solutions 等媒体交叉报道，来源可信度较高；但内容为设施启用与训练阶段，缺少订单、产量、财务与时间表等商业硬证据。
**投研价值评分**: 48 / 100
**是否需要继续追踪**: 是
**投研理由**: 评分为 48 分，属于官方设施启用与平台内部署事件，按“官方合作/产品发布/生态协作且缺少订单金额、客户采购、收入指引与明确部署规模”一档给分。平台绑定得 14 分，因现代汽车集团既是母公司又是终端客户，属于顶级产业平台；capex_impact 仅 8 分，因未披露 RMAC 投资金额，仅可间接关联 HMGMA 的 76 亿美元厂区资本开支；order_evidence 仅 6 分，因 Atlas 处于训练阶段，无订单、合同或批量交付证据；supply_demand_impact 仅 3 分，因无涨价、缺货、产能瓶颈或交期数据；earnings_elasticity 仅 4 分，因缺少订单/客户/收入/产能/价格验证；source_confidence 9 分（官方公告+多源交叉报道）；novelty 4 分，因其为人形机器人专用应用中心的新形态但方向符合市场预期。

**标签**: `#Robotics`, `#Humanoid Robots`, `#Boston Dynamics`, `#Manufacturing Automation`, `#AI`

---

<a id="item-6"></a>
## [Imec 发布 100 GHz Ge/Si 雪崩光电二极管，5V 下实现 400 Gbps 接收](https://news.google.com/rss/articles/CBMi3wFBVV95cUxQdGcyVmMyQjBSUzN3LUZkTTNCQy1FRFA2UFVYY0dabU5IRjI1YnFDWUdNSnRaZnU5UlZETk5GODFPLWxoNjFpN281THQ4UXVsZW4xOGpWcWhRdkJfNm5WOFVUYjdIdWNNSWtaSW9naWRNc3NTbE5qMHJ5Vi1iSG9Idm1TZkllVjVCbnMwb2oydGhFQTNRQ0hEWnllMlJRTjk1S241a2RPdE4zcnBEVUtRVS14Q3NqZUttb0s4THFONGN0YzN3SzI2OU9lX0RIQ2lLY0JiazMtNFpuaW1tenhN?oc=5) ⭐️ 7.0/10

Imec 宣布推出一款锗-硅（Ge/Si）雪崩光电二极管（APD），同时具备 100 GHz 带宽、仅 5V 偏压的低压工作特性，以及在 O 波段和 C 波段均达到 1.8 A/W 的响应度。该器件据称可实现净 400 Gbps 的光数据接收，是下一代单通道 400G 数据中心链路和共封装光学的重要基础器件。 随着 AI 和云计算数据中心流量增长，更快、更低电压的光电探测器是扩展光互连的关键，因为单通道带宽和能效是主要瓶颈。一款可在 5V 偏压下支持单通道 400 Gbps 的 Ge/Si APD 将对硅光子和共封装光学路线图产生重要意义，并惠及系统与网络生态。 该 APD 采用 Ge-on-Si 结构，因与 CMOS 工艺兼容且成本低而具有吸引力，并在 O 波段和 C 波段均以 1.8 A/W 响应度工作。但作为新闻稿发布，该公告缺少同行评审的方法学、良率、可靠性或封装集成细节，因此实际可制造性仍待验证。

rss · Google News - Optical Interconnect CPO · 9月21日 17:46

**背景**: 硅光子利用标准半导体制造工艺，将波导、调制器和探测器等光学元件集成到硅衬底上，从而实现比纯电互连更快、更高效的数据传输。雪崩光电二极管（APD）是一种通过雪崩倍增放大微弱光信号的光电探测器，灵敏度高，但传统上需要较高偏压。共封装光学（CPO）是一种新兴方案，将光学引擎直接放置在交换 ASIC 旁，以降低功耗并提升带宽密度，它依赖于像本次这样高速、高效的光电探测器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.imec-int.com/en/press/imec-debuts-100-ghz-gesi-avalanche-photodiode-apd-enabling-net-400-gbps-data-reception-just-5">Imec debuts 100 GHz Ge/Si avalanche photodiode (APD ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Silicon_photonics">Silicon photonics</a></li>
<li><a href="https://www.linkedin.com/pulse/co-packaged-optics-market-outlook-from-ai-networking-jzhkc">Co - Packaged Optics Market Outlook: From AI Networking Demand to...</a></li>

</ul>
</details>

**发生了什么**: Imec 发布了一款 Ge/Si 雪崩光电二极管（APD），实现 100 GHz 带宽、5V 低偏压工作，以及在 O 波段和 C 波段 1.8 A/W 的响应度，据称可支持净 400 Gbps 光数据接收。
**为什么重要**: 该器件面向下一代单通道 400G 数据中心链路和共封装光学（CPO），若能量产将提升光互连带宽密度并降低功耗，对硅光子和数据中心网络生态具有技术意义。
**影响产业链**: 潜在影响硅光子、光模块与光探测器产业链，以及数据中心光互连与 CPO 供应链；但当前仅为研究机构的技术演示/新闻稿，缺少订单/客户/收入/产能/价格验证，对上市公司收入、利润或现金流暂无可见影响。
**可能相关公司**: Imec（非上市研究机构）, 硅光/光模块厂商（如 Intel、Cisco、Broadcom 等，未在文中点名）
**可信度**: 中：来源为 Imec 官方新闻稿，机构可信度高，但缺少同行评审方法、良率、可靠性数据，且无商业客户或量产信息，故可信度评为中等。
**投研价值评分**: 19 / 100
**是否需要继续追踪**: 是
**投研理由**: 本条目属于实验室/研究突破性质，无真实订单、客户采购、产能扩张或价格信号，按规则总分应落在 10-35 且不超过 40。各分项：capex_impact 2（无超算/电信/云资本开支变化）、order_evidence 0（无订单或部署证据）、supply_demand_impact 1（无价格/供需证据）、platform_binding 3（Imec 与主流半导体生态有联系但本器件无点名大客户）、earnings_elasticity 1（暂无营收/毛利影响）、source_confidence 7（官方来源但缺细节）、novelty 5（100 GHz、5V 的 APD 具有技术新意），合计 19。

**标签**: `#silicon-photonics`, `#optical-interconnects`, `#avalanche-photodiode`, `#co-packaged-optics`, `#data-center-networking`

---

<a id="item-7"></a>
## [NVIDIA 推出 DSX Ready，为 AI 工厂认证电源和冷却产品](https://blogs.nvidia.com/blog/dsx-ready-ai-factories-power-cooling/) ⭐️ 6.0/10

NVIDIA 推出了 DSX Ready，这是一个为 AI 工厂认证电源和冷却产品的项目。

rss · NVIDIA Blog · 9月21日 18:00

**标签**: `#NVIDIA`, `#AI infrastructure`, `#data center cooling`, `#power management`, `#hardware qualification`

---

<a id="item-8"></a>
## [威斯康星大学麦迪逊分校与 Marist 提出 LoRD 启发式方法，定位门级网表中的 RTL 硬件木马](https://semiengineering.com/detecting-hardware-trojans-in-synthesized-gate-level-netlists-uw-madison-marist/) ⭐️ 6.0/10

威斯康星大学麦迪逊分校与 Marist University 的研究人员发表了题为《Demystifying Gate-Level Localization of RTL Trojans》的技术论文，指出 RTL 木马在综合之后仍会保留稳定的结构和信号流模式。他们提出 LoRD——一种轻量级启发式方法，利用这些特有的子图特征在综合后的门级网表中检测并定位硬件木马，据称在竞赛测试用例上实现了接近完美的检测与定位效果。 硬件木马是供应链安全威胁，一旦设计被综合成门级电路就极难发现，因此一种能在综合后网表（而非原始 RTL）上工作的方案，可为验证与安全团队提供成本更低、可在流程后段使用的检测手段。若接近完美的结果能够在竞赛基准之外得到复现，它可能补充甚至挑战依赖繁重特征工程的机器学习木马检测方案。 核心论点是 RTL 木马在综合后会产生一致的子图与信号流特征，因此定向启发式方法比通用机器学习特征学习更有效，同时保持轻量。相关开源项目 Lord_Trojan_Detection 提供了一个自动化流水线，可分析 Verilog 网表并定位与所检出木马相关的门实例。但报告结果是基于竞赛测试用例，摘要未给出误报率/漏报率、运行时间或在大型工业设计上的扩展性数据。

rss · SemiEngineering · 9月21日 23:21

**背景**: 硬件木马是对芯片电路的恶意篡改，通常分为极少被激活的触发器和仅在特定条件下才生效的载荷，因而在正常工作状态下几乎不可见。芯片先用 RTL（寄存器传输级）代码设计，再由综合工具转换成门级网表——即逻辑门及其连接关系的文本描述，最终被制造为硅片。由于第三方 IP、EDA 工具和晶圆厂处于设计者与芯片之间，攻击者可在多个环节植入木马；检测通常在综合前的 RTL 阶段或制造后的物理硅片阶段进行，而本项工作瞄准的正是综合后网表这一中间环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://semiengineering.com/detecting-hardware-trojans-in-synthesized-gate-level-netlists-uw-madison-marist/">Detecting Hardware Trojans in Synthesized Gate-Level Netlists (UW-Madison, Marist)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hardware_Trojan">Hardware trojan - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2506.17894">TROJAN -GUARD: Hardware Trojans Detection Using GNN in RTL ...</a></li>

</ul>
</details>

**发生了什么**: 威斯康星大学麦迪逊分校与 Marist University 发表学术论文，提出 LoRD 启发式方法，利用综合后稳定的结构子图与信号流特征在门级网表中检测并定位 RTL 硬件木马，并在竞赛测试用例上报告接近完美的检测与定位结果。
**为什么重要**: 硬件木马是芯片供应链安全的关键风险点，若该方案在工业级设计上可复现，可能成为综合后阶段的安全检测能力，融入 EDA 验证流程，并影响芯片安全相关工具与 IP 的价值主张。但目前仅为学术成果，尚无产品化或商业部署证据。
**影响产业链**: 理论上与 EDA 工具链及芯片安全验证环节相关，可能影响 Synopsys、Cadence、Siemens EDA 等厂商安全类工具的功能竞争格局；但本文未涉及价格、产能、订单、收入或利润，对相关公司的营收、毛利率与现金流没有可验证的直接影响。
**可能相关公司**: Synopsys (SNPS), Cadence Design Systems (CDNS), Siemens EDA（西门子旗下，未单独上市）
**可信度**: 中：来源为 Semiconductor Engineering 对论文的报道，可被 arXiv 与 GitHub 开源项目交叉印证，但内容为学术研究，缺少商业验证。
**投研价值评分**: 10 / 100
**是否需要继续追踪**: 否
**投研理由**: 该新闻属于学术论文与启发式算法贡献，缺少订单/客户/收入/产能/价格验证，也未改变任何超大规模厂商或代工厂的资本开支。按照规则，论文类成果默认 10-35 分且不得高于 40 分。其中 capex_impact、order_evidence、supply_demand_impact、earnings_elasticity 均无硬证据，取 0 分；platform_binding 仅为 1 分（与 EDA/芯片安全生态有间接关联，但未绑定英伟达、云厂商或电信运营商等头部平台）；source_confidence 取 6 分（行业媒体报道+论文与开源项目可交叉验证）；novelty 取 3 分（以启发式取代通用 ML 特征学习有一定新意，但仍在既有木马检测研究框架内）。合计 10 分，符合学术论文类的保守评分区间。

**标签**: `#hardware-security`, `#hardware-trojans`, `#EDA`, `#gate-level-netlists`, `#RTL`

---

<a id="item-9"></a>
## [Blocks & Files 评测大普微 SLC 与 QLC 混合企业级 SSD](https://www.blocksandfiles.com/flash/2026/09/21/a-look-at-dapustors-combined-slc-and-qlc-ssd/5297708) ⭐️ 6.0/10

Blocks & Files 发布了一篇技术性评测，审视大普微电子（DapuStor）推出的一款企业级 SSD，该产品在同一块盘内同时使用 SLC 与 QLC NAND 颗粒，以在写入性能与存储容量之间取得平衡。文章将该产品定位为厂商层面的差异化设计，而非全行业突破，且报道形式更接近产品拆解式评测，并未披露新客户或出货量。 SLC/QLC 混合设计的价值在于：QLC NAND 成本低、密度高，但写入慢、寿命短；SLC 写入快、耐久度高，但成本昂贵，将两者结合可让厂商在不大幅牺牲写入性能的前提下销售大容量企业级 SSD。对存储工程师和数据中心采购方而言，这类设计对读密集与混合负载（如 AI 数据湖、内容分发、温数据层）有实际意义，但本条消息本身并未显示出广泛采用或市场格局变化。 在 SLC/QLC 混合架构中，SLC 区域通常充当 QLC 区块之前的写入缓存，先以高速度吸收热数据写入，再在空闲时段把数据迁移到 QLC；Sandisk 的 nCache 技术此前已将该思路商业化，学术界也有针对其数据放置策略的研究。QLC 的擦写寿命通常仅约 1000 次 P/E 循环，因此耐久度与持续写入表现是此类混合设计的关键限制，而本次提供的材料中并未给出独立基准测试数据。

rss · Blocks and Files · 9月21日 13:00

**背景**: NAND 闪存通过在存储单元中写入不同数量的电压电平来保存数据：SLC 每单元存 1 比特，速度和耐久度最高；QLC 每单元存 4 比特，每 GB 成本最低，但写入明显更慢、擦写寿命也少得多。因此企业级 SSD 厂商常把 QLC 盘中的一部分容量划为伪 SLC（pSLC）模式用作缓存。大普微电子（DapuStor）成立于 2016 年 4 月，是中国的高端企业级 SSD、主控 SoC 与边缘计算存储产品供应商，与 NAND 原厂及其他企业级 SSD 厂商形成竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.dapustor.com/">Dapustor | Data Center Best Enterprise SSD | NVMe SSD | DapuStor</a></li>
<li><a href="https://www.kingston.com/en/blog/pc-performance/difference-between-slc-mlc-tlc-3d-nand">2D vs 3D NAND: Differences Between SLC, MLC, TLC and QLC Flash Storage - Kingston Technology</a></li>
<li><a href="https://www.mdpi.com/2076-3417/14/4/1648">Data Placement Using a Classifier for SLC/QLC Hybrid SSDs</a></li>

</ul>
</details>

**发生了什么**: Blocks & Files 对大普微电子（DapuStor）的一款企业级 SSD 做了技术性评测，该产品在单盘内混合使用 SLC 与 QLC NAND，以兼顾写入性能与容量；报道属于厂商产品层面的设计解析，未披露订单、客户、出货量或收入数据。
**为什么重要**: SLC 作写缓存、QLC 作容量层的混合架构是提升大容量企业级 SSD 性价比的现实路线，对 AI 数据湖、温数据存储等读密集场景有参考价值，但此类设计此前已被 Sandisk nCache 等方案实现，单个厂商的评测稿不足以改变行业供需或竞争格局。
**影响产业链**: 潜在影响集中在企业级 SSD/NAND 存储产业链：若该类混合盘被数据中心规模采用，可能增加对 QLC NAND 颗粒与控制器的需求，并间接影响 NAND 原厂的产能结构；但本条消息缺少订单/客户/收入/产能/价格验证，无法量化对任何环节的收入、毛利率或现金流的影响。
**可能相关公司**: 大普微电子 DapuStor（未在搜索结果中确认证券代码）, Samsung 三星电子（NAND 原厂）, Kioxia 铠侠（NAND 原厂）, SK Hynix / Solidigm（NAND 原厂）, Micron 美光（NAND 原厂）, 长江存储 YMTC（NAND 原厂）
**可信度**: 中：Blocks & Files 是存储领域较专业的行业媒体，但本条为产品评测/介绍性质，且提供的正文内容为空，缺少官方公告、订单或财务数据交叉验证。
**投研价值评分**: 18 / 100
**是否需要继续追踪**: 否
**投研理由**: 该消息属于厂商特定存储硬件介绍，没有订单、客户采购、产能扩张、涨价或财务指引等硬信号，按规则只能给较低分数。capex_impact 2（未见超大规模云厂商或运营商资本开支变化）、order_evidence 0（无订单或批量交付证据）、supply_demand_impact 2（无价格或供需紧张证据）、platform_binding 3（属企业级 SSD 厂商产品，未绑定英伟达/头部云厂商等平台）、earnings_elasticity 2（无法推断收入或毛利影响）、source_confidence 6（行业媒体可信但缺乏官方与多源验证）、novelty 3（SLC/QLC 混合并非首创，但单盘混合设计仍具一定新意），合计 18 分。缺少订单/客户/收入/产能/价格验证，后续需等待客户导入、出货规模或财务披露才能上调评级。

**标签**: `#SSD`, `#NAND flash`, `#storage hardware`, `#QLC`, `#SLC`

---

<a id="item-10"></a>
## [FCIA 发布 FC-SP-3 光纤通道安全标准，面向后量子计算时代](https://www.storagereview.com/review/fcias-fc-sp-3-a-standard-ready-for-the-quantum-computing-world) ⭐️ 6.0/10

光纤通道行业协会（FCIA）与 INCITS 正式发布 FC-SP-3 标准（编号 INCITS 577-2026），这是一项新的光纤通道安全协议标准，定义了光纤通道实体之间的身份认证、会话密钥协商以及帧保护机制，为后量子密码学迁移做准备。该标准被定位为对监管与密码学时间表的主动响应，包括针对美国国家安全系统的 NSA CNSA 2.0 指南以及欧洲即将到来的合规要求。 光纤通道至今仍是银行、政府与国防等关键业务企业存储 SAN 的底层技术，因此一项抗量子的安全标准可以让存储阵列、HBA 与交换机厂商在合规截止日期到来前启动后量子密码学（PQC）迁移。若被广泛采纳，可能提前拉动企业存储网络的固件与硬件更新周期。 FC-SP-3（INCITS 577-2026）延续了此前的 FC-SP 工作，并在 Broadcom 的光纤通道标准跟踪清单中以“Fibre Channel Security Protocols - 3”出现，同时还有 SM-HBA-2 等相关项目。不过公开信息较为宏观：并未说明强制采用哪些后量子算法、会带来多少性能或延迟开销，也没有给出合规产品的上市时间表。

rss · StorageReview · 9月21日 15:14

**背景**: 光纤通道（Fibre Channel）是一种专用于存储区域网络（SAN）的协议，用于将服务器连接到企业级存储阵列；由于 SAN 通常在物理上隔离，长期被认为“设计即安全”，但新的威胁与监管正在迫使其加强网络内安全。FC-SP 是 INCITS/T11 制定的光纤通道安全标准族，FC-SP-3 是其第三代。CNSA 2.0 是美国国家安全局（NSA）于 2022 年发布的“商用国家安全算法套件 2.0”，规定国家安全系统必须迁移到抗量子算法，其背景是量子计算机最终可能破解当前的公钥密码体系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fibrechannel.org/storage-security-fibre-channel-security/">Storage Security - Fibre Channel Industry Association</a></li>
<li><a href="https://www.broadcom.com/support/fibre-channel-networking/san-standards/fc-standards">Fibre Channel Standards - Broadcom Inc.</a></li>
<li><a href="https://www.marvell.com/content/dam/marvell/en/public-collateral/fibre-channel/marvell-fibre-channel-storcryption-post-quantum-technology-brief.pdf">[PDF] Qlogic Enhances Fibre Channel Security with Post-Quantum ...</a></li>

</ul>
</details>

**发生了什么**: FCIA 与 INCITS 发布 FC-SP-3（INCITS 577-2026）光纤通道安全协议标准，定义光纤通道实体的认证、会话密钥建立与帧保护，目标是为后量子密码学迁移和 NSA CNSA 2.0 等监管截止日期做准备。
**为什么重要**: 光纤通道仍是金融、政府、国防等关键业务存储 SAN 的底层协议，标准层面的抗量子要求可能推动 HBA、交换机与存储阵列的固件/硬件升级，属于长期的结构性技术迁移信号，但短期没有可量化的商业影响。
**影响产业链**: 潜在影响企业存储与存储网络产业链，包括光纤通道 HBA、SAN 交换机、存储阵列及其安全固件；但目前没有证据表明会带来收入、毛利率、利润或现金流的实际变化，更多是未来合规驱动的更新换代可能性。
**可能相关公司**: Broadcom (AVGO), Marvell (MRVL), Cisco (CSCO), HPE (HPE), Dell (DELL), IBM (IBM)
**可信度**: 中。标准发布有 INCITS 官方委员会与 StorageReview 报道相互印证，可信度尚可；但缺少技术细节、客户名单、订单或出货数据，且内容偏宣传性。
**投研价值评分**: 24 / 100
**是否需要继续追踪**: 是
**投研理由**: 这是标准发布类事件，缺少订单/客户/收入/产能/价格验证，也未涉及超大规模数据中心或运营商资本开支变化，因此 capex_impact、order_evidence、supply_demand_impact 与 earnings_elasticity 均给低分；仅因绑定光纤通道生态（Broadcom、Marvell、Cisco 等）以及官方标准机构背书，给予有限的 platform_binding 与 source_confidence 分值。总分 24，属研究/标准类信号的保守区间，需持续跟踪是否有厂商产品落地与合规采购启动。

**标签**: `#Post-Quantum Cryptography`, `#Fibre Channel`, `#Security Standards`, `#Enterprise Storage`, `#Quantum Computing`

---