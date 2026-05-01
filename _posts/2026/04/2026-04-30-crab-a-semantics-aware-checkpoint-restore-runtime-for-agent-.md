---
title: "Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes"
date: 2026-04-30 17:20:19 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28138v1"
arxiv_id: "2604.28138"
authors: ["Tianyuan Wu", "Chaokun Chang", "Lunxi Cao", "Wei Gao", "Wei Wang"]
slug: crab-a-semantics-aware-checkpoint-restore-runtime-for-agent-
summary_word_count: 443
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing checkpoint and restore (C/R) mechanisms for autonomous agents operating within sandboxed environments and microVMs. Current approaches either focus on application-level recovery, which captures chat history but neglects OS-level effects, or employ full per-turn checkpointing, which incurs significant overhead due to dense co-location of agents. The authors identify a critical agent-OS semantic gap that obscures the relevance of state changes for recovery, leading to inefficiencies in checkpointing. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose Crab (Checkpoint-and-Restore for Agent SandBoxes), a runtime system that operates transparently at the host level to bridge the agent-OS semantic gap without requiring modifications to existing agents or C/R backends. Crab employs an eBPF-based inspector to classify OS-visible effects of each agent turn, allowing for intelligent decision-making regarding checkpoint granularity. A coordinator component aligns checkpoints with turn boundaries and optimizes the overlap of C/R operations with the wait time of large language models (LLMs). Additionally, a host-scoped engine manages checkpoint traffic across co-located sandboxes, ensuring efficient resource utilization. The architecture leverages existing OS capabilities while enhancing the granularity and relevance of checkpoints.

**Results**  
Crab significantly improves recovery correctness from 8% (using chat-only checkpoints) to 100% in scenarios involving shell-intensive and code-repair workloads. Furthermore, it reduces checkpoint traffic by up to 87%, demonstrating substantial efficiency gains. The execution time remains within 1.9% of fault-free execution, indicating that the overhead introduced by Crab is minimal compared to the benefits it provides in terms of recovery accuracy and resource management. These results were benchmarked against standard C/R methods, showcasing Crab's effectiveness in real-world applications.

**Limitations**  
The authors acknowledge that while Crab achieves high recovery correctness and efficiency, it may not account for all edge cases in agent behavior or OS interactions, particularly in highly dynamic environments. Additionally, the reliance on eBPF may introduce compatibility issues with certain OS configurations or versions. The paper does not explore the scalability of Crab in environments with a significantly larger number of co-located agents or the potential impact of varying workloads on its performance.

**Why it matters**  
The implications of this work are significant for the development of more efficient and reliable autonomous agents, particularly in applications requiring fault tolerance and rapid recovery. By addressing the agent-OS semantic gap, Crab enables more intelligent checkpointing strategies that can lead to reduced resource consumption and improved performance in multi-agent systems. This advancement opens avenues for further research into optimizing agent interactions with the OS, potentially influencing the design of future agent frameworks and C/R systems.

Authors: Tianyuan Wu, Chaokun Chang, Lunxi Cao, Wei Gao, Wei Wang  
Source: arXiv:2604.28138  
URL: https://arxiv.org/abs/2604.28138v1
