---
title: "NetKV: Network-Aware Decode Instance Selection for Disaggregated LLM Inference"
date: 2026-06-02 17:06:57 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.03910v1"
arxiv_id: "2606.03910"
authors: ["Mubarak Adetunji Ojewale"]
slug: netkv-network-aware-decode-instance-selection-for-disaggrega
summary_word_count: 407
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces NetKV, a network-aware scheduling method that optimizes Time to First Token in disaggregated LLM inference by considering network costs."
---

**Problem**  
The paper addresses the inefficiencies in disaggregated large language model (LLM) inference, specifically the impact of network latency on Time to First Token (TTFT). Current scheduling methods primarily focus on compute load and prefix-cache locality, neglecting the network topology and dynamic congestion that can significantly affect performance. This gap in capability is critical, as it can lead to suboptimal scheduling decisions, particularly as context lengths increase. The work is presented as a preprint and has not undergone peer review.

**Method**  
The authors propose a novel scheduling framework called NetKV, which integrates a network cost oracle into the scheduling process. This oracle provides real-time network cost estimates, allowing the scheduler to make informed decisions based on both compute and network metrics. NetKV employs a greedy algorithm with a complexity of O(|D|) per request, where |D| represents the number of decode instances. The architecture is designed to be lightweight, requiring no modifications to existing transport protocols, inference engines, or hardware setups. The authors demonstrate that ignoring network costs can lead to arbitrarily suboptimal scheduling, particularly as context length increases, thus justifying the need for their approach.

**Results**  
In experiments conducted on a simulated environment with a 64-GPU four-tier fat-tree architecture using Mooncake traces, NetKV achieved a mean TTFT reduction of up to 21.2% compared to a round-robin scheduler and 17.6% compared to a tuned cache and load-aware scheduler. Additionally, NetKV improved Service Level Objective (SLO) attainment by as much as 20.1 percentage points. The method maintained a Time Between Tokens overhead below 0.5 ms across all tested conditions, showcasing its robustness and efficiency in real-world scenarios.

**Limitations**  
The authors acknowledge that their approach relies on the accuracy of the network cost oracle, which may be affected by stale telemetry data. While they claim that NetKV's tier rankings are robust to such staleness, the potential for inaccuracies in network measurements could still impact performance. Furthermore, the study is limited to a simulated environment, and real-world deployment may introduce additional complexities not accounted for in the simulation.

**Why it matters**  
The introduction of NetKV has significant implications for optimizing LLM inference in distributed systems, particularly in environments where network latency is a critical factor. By incorporating network awareness into scheduling decisions, this work paves the way for more efficient resource utilization and improved user experience in applications relying on LLMs. The findings contribute to the growing body of literature on optimizing distributed machine learning systems, as published in [arXiv cs.AI](https://arxiv.org/abs/2606.03910v1).
