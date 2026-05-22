---
title: "DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback"
date: 2026-05-21 17:36:17 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22781v1"
arxiv_id: "2605.22781"
authors: ["Yunpeng Dong", "Jingkai He", "Yuze Hou", "Dong Du", "Zhonghu Xu", "Si Yu"]
slug: deltabox-scaling-stateful-ai-agents-with-millisecond-level-s
summary_word_count: 453
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the latency bottleneck in stateful AI agents, particularly those utilizing large language models (LLMs) for high-frequency state exploration, such as test-time tree search and reinforcement learning. Existing checkpoint and rollback (C/R) mechanisms incur significant delays (hundreds of milliseconds to seconds) due to the full duplication of the agent's state, which includes files and process states. The authors propose a solution to this problem by introducing a novel OS-level abstraction that allows for efficient change-based C/R, which is crucial for enhancing the performance of AI agents. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of DeltaBox, which leverages two co-designed OS mechanisms: DeltaFS and DeltaCR. DeltaFS implements change-based filesystem C/R by organizing file states into layers, allowing for a copy-on-write approach that minimizes the overhead of file updates. During a checkpoint, the writable layer is frozen, and a new layer is created, enabling efficient rollback through a simple layer switch. DeltaCR focuses on process state C/R, utilizing incremental dumps to capture only the changes in process memory. This mechanism accelerates rollback by directly forking from a frozen template process, bypassing traditional C/R pipelines. The combination of these mechanisms allows DeltaBox to achieve millisecond-level C/R latencies, specifically 14ms for checkpointing and 5ms for rollback.

**Results**  
DeltaBox was evaluated against standard benchmarks, including SWE-bench and RL micro-benchmarks. The results demonstrate that DeltaBox significantly reduces C/R latency compared to existing methods, enabling AI agents to explore a substantially larger number of nodes within fixed time budgets. While specific baseline comparisons are not detailed in the abstract, the performance improvements suggest a marked enhancement in operational efficiency for stateful AI agents, facilitating more extensive exploration and decision-making capabilities.

**Limitations**  
The authors acknowledge that the proposed DeltaBox system relies on specific OS-level support, which may limit its applicability across different operating systems or environments lacking these features. Additionally, the paper does not address potential security implications of the change-based C/R mechanism, such as the risks associated with incremental state exposure. Furthermore, the scalability of DeltaBox in highly dynamic environments with frequent state changes remains an open question.

**Why it matters**  
The implications of this work are significant for the development of more efficient AI agents capable of real-time decision-making and exploration. By reducing the latency associated with state management, DeltaBox enables more complex and responsive AI applications, particularly in domains requiring rapid state transitions, such as robotics, gaming, and interactive systems. This advancement could lead to broader adoption of stateful AI agents in practical applications, enhancing their performance and utility.

Authors: Yunpeng Dong, Jingkai He, Yuze Hou, Dong Du, Zhonghu Xu, Si Yu, Yubin Xia, Haibo Chen  
Source: arXiv:2605.22781  
URL: [https://arxiv.org/abs/2605.22781v1](https://arxiv.org/abs/2605.22781v1)
