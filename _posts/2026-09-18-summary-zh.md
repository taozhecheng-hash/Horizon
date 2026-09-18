---
layout: default
title: "Horizon Summary: 2026-09-18 (ZH)"
date: 2026-09-18
lang: zh
---

> 从 66 条内容中筛选出 5 条重要资讯。

---

1. [爱尔兰研究人员用 DNA 折纸构建分子计算机](#item-1) ⭐️ 7.0/10
2. [TrueNAS 发布原生 Proxmox VE 插件，自动以 zvol 形式提供 iSCSI/NVMe/TCP 存储](#item-2) ⭐️ 7.0/10
3. [CoreWeave 上线多机架 NVIDIA Vera Rubin NVL72 集群](#item-3) ⭐️ 7.0/10
4. [Bull/Eviden 击败 HPE，赢得下一代 LUMI AI 超算合同](#item-4) ⭐️ 7.0/10
5. [ASML 的 High-NA EUV 获得更广泛行业支持](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [爱尔兰研究人员用 DNA 折纸构建分子计算机](https://www.blocksandfiles.com/architecture/2026/09/17/irish-researchers-molecular-computer-uses-dna-origami/5297209) ⭐️ 7.0/10

据 Blocks & Files 于 2026 年 9 月 17 日的报道，爱尔兰研究人员建造了一台分子计算机，其计算基础是 DNA 折纸（DNA origami），即把 DNA 链在纳米尺度折叠成设计好的形状。报道没有提供论文链接、逻辑门数量、运算速度或其他工程细节。 这是“超越硅基计算”长期探索中的又一个进展，理论上可能走向纳米尺度、低功耗、可大规模并行并直接与生物体系接口的分子计算。但 DNA 计算机目前仍停留在实验室演示阶段，对主流计算产业和半导体供应链的近期影响可以忽略不计。 DNA 折纸由 Paul Rothemund 于 2006 年提出，方法是用一条长单链 DNA 作为支架，由数百条短“订书钉”链把它折叠成任意的二维或三维形状；而 DNA 计算本身可追溯到 Leonard Adleman 在 1994 年的演示。由于这条新闻没有任何技术内容，无法判断该器件的错误率、开关速度、可逆性或可扩展性，而这些正是分子计算的经典瓶颈。

rss · Blocks and Files · 9月17日 14:23

**背景**: DNA 折纸属于结构 DNA 纳米技术，利用碱基互补配对的高度特异性让 DNA 自组装成精确形状的纳米结构；自 2006 年以来，它已从一种“艺术形式”走向药物递送、等离激元电路等应用，但多数商业应用仍处于概念或测试阶段。DNA 计算则是非传统计算的一个分支，用 DNA、生物化学和分子生物学“硬件”替代电子电路，涵盖理论、实验与应用，包括数据存储、纳米尺度成像、合成控制器和反应网络等。因此这类分子计算机是研究阶段的器件而非产品，通常以速度换取并行度和分子尺度的密度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DNA_origami">DNA origami</a></li>
<li><a href="https://en.wikipedia.org/wiki/DNA_computing">DNA computing</a></li>

</ul>
</details>

**发生了什么**: 据 Blocks & Files 报道，爱尔兰研究人员构建了一台利用 DNA 折纸（DNA origami）进行计算的分子计算机，属于实验室层面的研究进展；报道未给出论文出处、算力规模、器件数量、运算速度或任何商业化细节，原文内容也为空。
**为什么重要**: 该事件代表生物分子计算这一非传统计算方向的持续探索，长期看可能影响超低功耗、纳米尺度与生物接口的计算范式；但短期内不改变主流半导体、服务器与算力基础设施的格局，也不构成可投资的产业信号。
**影响产业链**: 缺少订单/客户/收入/产能/价格验证，目前没有明确受益的产业链环节，对任何上市公司的收入、利润率或现金流都没有可验证的影响。若该方向长期成熟，理论上可能带动 DNA 合成、生物试剂、纳米加工与科研仪器等上游需求，但本新闻不提供任何规模或时间表。
**可能相关公司**: 暂无明确相关上市公司，可长期跟踪 DNA 合成、生物试剂与生物计算方向的企业
**可信度**: 中低：来源为 Blocks & Files 这类科技媒体的转述，未提供论文链接、研究机构名称或官方发布，且新闻正文缺失，无法交叉验证。
**投研价值评分**: 10 / 100
**是否需要继续追踪**: 否
**投研理由**: 该事件属于实验室研究/技术突破，没有订单、客户、产能、价格或财务数据支撑，按规则论文与实验室研究默认 10-35 分且无商业化证据时不得超过 40 分。因此订单证据 0、供应链供需影响 0、资本开支影响 0、盈利弹性 0、平台绑定 0，仅来源可信度 6 分、新颖性 4 分，合计 10 分。缺少订单/客户/收入/产能/价格验证。

**标签**: `#DNA computing`, `#molecular computing`, `#DNA origami`, `#nanotechnology`, `#biocomputing`

---

<a id="item-2"></a>
## [TrueNAS 发布原生 Proxmox VE 插件，自动以 zvol 形式提供 iSCSI/NVMe/TCP 存储](https://www.storagereview.com/news/truenas-proxmox-plugin-turns-every-vm-disk-request-into-an-automated-zvol-over-iscsi-or-nvme-tcp) ⭐️ 7.0/10

TrueNAS 发布了原生的 Proxmox VE 存储插件：在 Proxmox 中申请一块虚拟机磁盘后，系统会在 TrueNAS 25.10 或更高版本上自动创建对应的 OpenZFS zvol，并以 iSCSI LUN 或 NVMe/TCP namespace 的形式发布给虚拟化主机。该插件同时在 Proxmox 侧接管磁盘的全生命周期管理，包括快照、扩容、迁移和删除。 这一集成基本消除了把 TrueNAS 块存储接入 Proxmox VE 的手工配置工作，而 TrueNAS + Proxmox 正是家庭实验室、中小企业和中小型私有云中常见的组合，同时也为 Proxmox 用户提供了从传统 iSCSI 迁移到延迟更低的 NVMe/TCP 的顺畅路径。此举还有助于巩固 TrueNAS 作为 Proxmox 用户首选存储后端的地位，而不只是服务于 VMware 或 Hyper-V 环境。 该插件要求 TrueNAS 25.10 或更高版本，块传输层同时支持 iSCSI 和 NVMe/TCP，并可由 Proxmox 侧发起 zvol 的创建、快照、扩容、迁移与删除操作。目前 TrueNAS 与 StorageReview 均未给出吞吐、延迟或规模测试数据，实际选用哪种传输方式仍取决于部署环境的网络与网卡支持情况。

rss · StorageReview · 9月17日 16:19

**背景**: zvol 是一种表现得像裸块设备的 ZFS 数据集，因此可以像物理磁盘一样呈现给虚拟化主机，同时保留快照、校验等 ZFS 特性。iSCSI 是长期存在的标准，用于在普通 TCP/IP 网络上传输 SCSI 块命令；而 NVMe over TCP（NVMe/TCP）则通过 TCP 承载 NVMe 命令，对闪存存储而言通常延迟更低、效率更高。Proxmox VE 是开源虚拟化平台，其存储插件机制允许管理员定义虚拟机磁盘的实际存放位置，因此原生 TrueNAS 插件的意义在于：存储层现在可以直接在 Proxmox 内部配置，而不必在两端手工操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NVMe_over_TCP">NVMe over TCP - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ISCSI">iSCSI - Wikipedia</a></li>
<li><a href="https://forums.truenas.com/t/pool-vs-dataset-vs-partitions-vs-vdev-vs-zvol-vs-disks-or-afew-questions-about-terminology/27675">Pool vs dataset vs partitions vs vdev vs zvol vs disks: Or, afew questions about terminology</a></li>

</ul>
</details>

**发生了什么**: TrueNAS 发布原生 Proxmox VE 存储插件，可将 Proxmox 中的虚拟机磁盘请求自动转换为 TrueNAS 25.10 及以后版本上的 OpenZFS zvol，并以 iSCSI LUN 或 NVMe/TCP namespace 形式对外提供，同时支持创建、快照、扩容、迁移与删除。
**为什么重要**: 该插件把 TrueNAS 块存储与 Proxmox VE 的对接从手工配置变成自动化流程，降低了中小企业、家庭实验室和中小型私有云部署块存储的门槛，并为 Proxmox 用户从 iSCSI 向 NVMe/TCP 迁移提供了官方路径，有利于 TrueNAS 在 Proxmox 生态中的渗透。
**影响产业链**: 影响面主要在存储软件与私有云/虚拟化集成环节：可能小幅带动 TrueNAS 一体机与自建 ZFS 存储节点的采用，以及支持 NVMe/TCP 的网卡、交换机和全闪阵列需求。缺少订单/客户/收入/产能/价格验证，尚无证据显示会对任何上市公司的营收、毛利或现金流产生可量化影响。
**可能相关公司**: iXsystems（TrueNAS 母公司，未上市）, Proxmox Server Solutions GmbH（Proxmox VE 开发商，未上市）
**可信度**: 中：消息来自存储行业垂直媒体 StorageReview 对厂商官方产品发布的报道，版本号与功能描述具体可信；但缺少订单、客户、收入、产能与价格等商业硬证据，也无官方财报指引佐证。
**投研价值评分**: 40 / 100
**是否需要继续追踪**: 否
**投研理由**: 这是一次产品与生态集成发布，属于软件功能层面的合作，缺少订单、客户采购、收入指引或明确部署规模等硬投资信号。按规则，无硬信号时总分应不超过 45，故给予 40 分。其中平台绑定得分相对较高（TrueNAS 与 Proxmox 生态绑定，但并非 Nvidia、超大规模云厂商或运营商等顶级平台）；capex_impact、order_evidence、supply_demand_impact、earnings_elasticity 均按缺少验证的下限区间保守打分，novelty 认可其自动化 zvol 编排的新意，source_confidence 因官方产品发布加垂直媒体报道给予中等偏上。缺少订单/客户/收入/产能/价格验证。

**标签**: `#TrueNAS`, `#Proxmox`, `#ZFS`, `#NVMe/TCP`, `#iSCSI`

---

<a id="item-3"></a>
## [CoreWeave 上线多机架 NVIDIA Vera Rubin NVL72 集群](https://www.storagereview.com/news/coreweave-brings-up-a-multi-rack-vera-rubin-nvl72-cluster-hundreds-of-rubin-gpus-1-6-tb-s-per-gpu-and-a-no-fee-archive-tier) ⭐️ 7.0/10

CoreWeave 已在 CoreWeave Cloud 上部署多机架 NVIDIA Vera Rubin NVL72 集群，将数百颗 Rubin GPU 连接为面向智能体（agentic）AI 工作负载的单一横向扩展环境。每个由 Dell 制造的机架包含 72 颗 Rubin GPU、36 颗 Vera CPU，以 NVLink 6 作为纵向扩展（scale-up）互连，并配备 BlueField-4 DPU 以及每 GPU 两个 ConnectX-9 SuperNIC，实现每 GPU 1.6 Tb/s 网络带宽；CoreWeave 同时为该集群提供免手续费的归档存储层。 这是 NVIDIA 下一代 Vera Rubin 平台在专业 AI 云上最早的多机架部署之一，意味着 Blackwell 的后继产品正从发布阶段走向面向客户的生产算力。这也说明 AI 新云（neocloud）的竞争焦点已转向机架级系统和每 GPU 互连带宽，而不再只是 GPU 数量，对采购推理与智能体 AI 算力的用户意义重大。 每 GPU 1.6 Tb/s 的带宽来自为每颗 Rubin GPU 搭配两个 ConnectX-9 SuperNIC，机架内纵向扩展则由 NVLink 6 承担，并配有 BlueField-4 DPU。该消息未提供集群或免手续费归档层的容量、定价、跑分与可用时间等细节，目前也没有第三方验证或性能层面的技术深度解析。

rss · StorageReview · 9月17日 15:48

**背景**: NVIDIA 的 NVL72 是一种机架级系统设计，通过高速 NVLink 将 72 颗 GPU 连接起来，使其如同一个大型加速器；上一代是基于 Blackwell 的 GB200 NVL72。Vera Rubin 是 NVIDIA 的下一代平台，把 Rubin GPU 与 Vera CPU、NVLink 6 交换机、ConnectX-9 SuperNIC 和 BlueField-4 DPU 组合在一起，NVIDIA 表示该平台已进入全面量产并向大型云客户出货。CoreWeave 是一家上市的、专注于 AI 的云服务商（新云厂商），对外出租 GPU 算力，此次部署意味着它把这一新平台正式上线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">Rack-Scale Agentic AI Supercomputer | NVIDIA Vera Rubin NVL 72</a></li>
<li><a href="https://radiant.co/blog/a-deep-dive-into-nvidia-vera-rubin-nvl72">A Deep Dive into NVIDIA ’s Vera Rubin NVL72 Platform | Radiant Blog</a></li>

</ul>
</details>

**发生了什么**: CoreWeave 在 CoreWeave Cloud 上线多机架 NVIDIA Vera Rubin NVL72 集群，将数百颗 Rubin GPU 组成面向智能体 AI 的横向扩展环境；每个 Dell 机架含 72 颗 Rubin GPU、36 颗 Vera CPU、NVLink 6、BlueField-4 DPU，并为每颗 GPU 配两个 ConnectX-9 SuperNIC（1.6 Tb/s/GPU），同时提供免手续费归档存储层。
**为什么重要**: 这是 Vera Rubin 平台在专业 AI 云上较早的多机架落地案例，说明下一代英伟达机架级系统从发布走向实际算力供给，也强化了 AI 云围绕机架级系统与每 GPU 互连带宽竞争的趋势。
**影响产业链**: 潜在受益方向为 NVIDIA 的 Rubin GPU/Vera CPU/NVLink 6/ConnectX-9/BlueField-4 整机架供应链、整机与液冷机架集成商（本次为 Dell 制造），以及 CoreWeave 自身的 GPU 云租赁收入与资本开支；但本条消息未披露订单金额、采购数量上限、价格、交付节奏或利润率，缺少订单/客户/收入/产能/价格验证。
**可能相关公司**: NVIDIA (NVDA), CoreWeave (CRWV), Dell Technologies (DELL)
**可信度**: 中：信息来自 StorageReview 的简短新闻稿，属较可信的行业媒体，且与 NVIDIA 已宣布 Vera Rubin 平台量产、向大型云客户出货的公开信息方向一致；但缺少 NVIDIA 或 CoreWeave 官方公告、订单金额与部署规模细节，无法交叉验证具体配置与数量。
**投研价值评分**: 51 / 100
**是否需要继续追踪**: 是
**投研理由**: 本次为具名 AI 云厂商对新平台的实际部署，属于硬信号中的“商用部署”，故总分可高于 45，但仅为短讯、无订单金额与财务指引，故不宜给高。capex_impact 12 分（CoreWeave 部署数百颗 Rubin GPU 意味着实质资本开支，但未给出金额或资本开支指引）；order_evidence 8 分（存在真实部署与批量交付迹象，但无合同金额与客户采购细节）；supply_demand_impact 3 分（无涨价、缺货、产能瓶颈或交期数据）；platform_binding 14 分（深度绑定 NVIDIA 顶级机架级平台与 Dell 整机）；earnings_elasticity 4 分（未披露收入、毛利、现金流影响，仅为可推断的算力出租收入方向）；source_confidence 6 分（单一行业媒体报道，未获官方或多家权威来源确认）；novelty 4 分（Vera Rubin 多机架部署在公开信息中仍属较新事件）。合计 51 分。

**标签**: `#AI infrastructure`, `#NVIDIA`, `#CoreWeave`, `#GPUs`, `#Cloud Computing`

---

<a id="item-4"></a>
## [Bull/Eviden 击败 HPE，赢得下一代 LUMI AI 超算合同](https://www.nextplatform.com/hpc/2026/09/17/bull-beats-out-hpe-for-next-gen-lumi-ai-supercomputer/5297292) ⭐️ 7.0/10

Bull/Eviden 赢得下一代 LUMI AI 超算的承建合同，在 EuroHPC 的采购竞标中击败了现有供应商 HPE。这一中标让 Eviden 的 HPC 业务在公开竞争中拿下旗舰项目，而当前基于 Cray 架构的 LUMI 系统正是由 HPE 承建的。 这一决定将重塑欧洲主权 AI 与 HPC 供应链的一部分，因为它决定了 EuroHPC 后续面向 AI 能力机型的大额投入由哪家厂商承接。对 HPE 而言，这是在欧洲丢失的一个旗舰标杆客户；对 Eviden 而言，则是在超大规模与 AI 优化系统供应竞赛中一次重要的信誉加分。 该消息未披露合同金额、新机器的加速器或 CPU 供应商以及交付时间，因此这一中标的商业规模仍无法量化。现有 LUMI 部署在芬兰卡亚尼，在 2025 年 11 月的 TOP500 榜单中排名第九，并且仍是 LUMI AI Factory 的计算主力。

rss · The Next Platform · 9月17日 17:22

**背景**: LUMI 是 EuroHPC 联合执行体（EuroHPC JU）的旗舰超级计算机；EuroHPC 由欧盟与各国共同出资，2021—2027 年预算约 70 亿欧元，目标是在欧洲建设世界级超算能力。现有的 LUMI 由 HPE 的 Cray 产品线提供，曾一度是欧洲最快的机器，同时承载传统数值模拟与 AI 负载。Bull 是法国 Atos 旗下的 HPC 品牌，其计算业务现归属 Eviden，因此这次中标会直接增强该厂商在欧洲超算领域的项目组合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LUMI">LUMI - Wikipedia</a></li>
<li><a href="https://lumi-supercomputer.eu/lumi_supercomputer/">LUMI supercomputer - LUMI</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_High-Performance_Computing_Joint_Undertaking">European High-Performance Computing Joint Undertaking - Wikipedia</a></li>

</ul>
</details>

**发生了什么**: Bull/Eviden 在 EuroHPC 的采购中击败 HPE，赢得下一代 LUMI AI 超算的承建合同，成为欧洲旗舰超算后续机型的系统集成商。
**为什么重要**: 该合同属于国家/欧盟级算力平台的资本开支项目，中标方将获得硬件集成、软件栈与运维服务收入，同时改变欧洲 HPC 供应链的供应商格局；对于在超算领域有长期积累的 Eviden 而言，这是一次对 HPE 的正面替代，具备标杆意义。
**影响产业链**: 影响的是超算系统集成与 HPC 服务产业链，中长期可能带动服务器、互连、液冷与加速器等上游环节的采购；但由于公开信息未披露合同金额、加速器选型与交付批次，无法据此测算对 Eviden（Atos）收入、利润率或现金流的实际贡献，对 HPE 欧洲订单的负面影响也难以量化。
**可能相关公司**: Eviden / Atos (EPA: ATO), HPE (NYSE: HPE), EuroHPC JU（欧盟联合执行体，非上市）
**可信度**: 中高：消息来自专注 HPC 的行业媒体 The Next Platform，且 LUMI、EuroHPC JU 等背景可由维基百科与官方站点交叉验证；但缺少合同金额、交付规模、加速器供应商等官方细节，商业影响仍待官方公告确认。
**投研价值评分**: 56 / 100
**是否需要继续追踪**: 是
**投研理由**: 评分依据：这是有明确客户（EuroHPC/LUMI）的采购中标，属于真实订单信号，故 order_evidence 给 13；平台绑定 EuroHPC 这一国家/欧盟级算力平台，给 12；平台资本开支影响给 10；但缺少订单金额、交付批次、芯片选型与价格/产能信息，supply_demand_impact 仅 4，earnings_elasticity 仅 6；来源为行业媒体，source_confidence 8；事件为采购结果而非技术突破，novelty 3。合计 56，符合“有真实订单但缺少金额与规模验证”的区间。关键待验证项：缺少订单金额/客户收入/产能/价格验证。

**标签**: `#HPC`, `#AI supercomputers`, `#EuroHPC`, `#Eviden`, `#procurement`

---

<a id="item-5"></a>
## [ASML 的 High-NA EUV 获得更广泛行业支持](https://semiwiki.com/semiconductor-manufacturers/intel/373593-asml-has-high-na-and-chipmakers-cant-say-no/) ⭐️ 6.0/10

已垄断极紫外（EUV）光刻系统的 ASML，据报正在为其下一代高数值孔径（High-NA）EUV 技术赢得更广泛的行业支持，该技术旨在印制更小、更密集的电路图形。该消息来自 SemiWiki 的一篇简短摘要，并未披露具体有哪些芯片厂商新增承诺，也没有订单金额、数量或时间表。 High-NA EUV 决定了谁能以经济的方式量产最先进的逻辑与存储节点，因此芯片厂商在这一技术上的站队变化，会直接影响英特尔、台积电、三星及其设备供应链的竞争格局。由于 ASML 是 EUV 设备的垄断供应商，行业接受度提升将进一步强化其定价权，并拉大率先采用者与其他厂商之间的制程差距。 数值孔径描述光学系统可接收光线的角度范围，将其从 0.33 提升至 0.55 可获得更高分辨率；ASML 已于 2023 年 12 月交付首台 High-NA EUV 系统，预计 2025—2026 年进入大规模量产使用。但该文未提供任何技术基准、成本数据或具名客户承诺，因此“行业支持扩大”的说法尚未得到验证。

rss · SemiWiki · 9月17日 13:00

**背景**: 光刻是用光把电路图形转移到硅片上的工艺，EUV 光刻则使用由激光轰击锡等离子体产生的 13.5 纳米极紫外光，用于制造最先进的芯片。数值孔径（NA）是衡量光学系统聚光能力与分辨率极限的无量纲参数，数值越高可分辨的图形越小。目前 ASML 是全球唯一生产 EUV 光刻机的公司，因此主要芯片厂商对 High-NA 的采用决策，本质上就是对其技术路线的选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.asml.com/en/products/euv-lithography-systems">EUV lithography systems – Products - ASML</a></li>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">EUV lithography - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Numerical_aperture">Numerical aperture - Wikipedia</a></li>

</ul>
</details>

**发生了什么**: SemiWiki 发布一篇简短摘要，称 ASML 的下一代 High-NA EUV 光刻技术正在获得更广泛的行业支持，但全文为导流式短文，未披露具体客户、订单金额、交付数量或时间表。
**为什么重要**: High-NA EUV 是先进逻辑与存储制程的关键设备层，直接关系到英特尔、台积电、三星等厂商的制程竞争力以及 ASML 的设备垄断定价权；不过该消息本身缺乏增量信息，更像是对既有趋势的重述。
**影响产业链**: 潜在影响链条为 ASML 光刻设备—晶圆厂资本开支—先进制程代工与存储产能。但本条消息没有订单、价格、产能或资本开支数据，无法据此推导收入、毛利率或现金流变化；缺少订单/客户/收入/产能/价格验证。
**可能相关公司**: ASML (ASML.O / ASML.AS), Intel (INTC), TSMC (TSM / 2330.TW), Samsung Electronics (005930.KS), Applied Materials (AMAT), Lam Research (LRCX), Zeiss SMT（ASML 光学供应商，未上市）
**可信度**: 低：信息来源为行业博客 SemiWiki 的摘要式导流文章，无官方公告、无具名客户、无量化数据，也未提供可交叉验证的第三方报道；ASML 官方页面仅确认 2023 年 12 月首台 High-NA 系统交付及 2025—2026 年量产预期。
**投研价值评分**: 24 / 100
**是否需要继续追踪**: 否
**投研理由**: 该消息属于趋势性评论与摘要转载，没有硬性投资信号：无订单、无具名客户采购、无设备价格或产能瓶颈变化、无收入或利润率指引，因此除平台绑定（ASML 对顶尖晶圆厂的垄断地位，给 7 分）外，各项子分均按保守给分。source_confidence 偏低（4 分），总分为 4+2+2+7+3+4+2=24，落在低置信度对应的 40 分上限以内。后续需跟踪 ASML 财报、High-NA 设备的实际出货台数与客户装机公告，才能判断其收入弹性。

**标签**: `#ASML`, `#High-NA EUV`, `#semiconductor manufacturing`, `#lithography`, `#chip fabrication`

---