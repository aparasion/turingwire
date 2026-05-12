---
title: "Shepherd: A Runtime Substrate Empowering Meta-Agents with a Formalized Execution Trace"
date: 2026-05-11 17:50:51 +0000
category: research
subcategory: agents_robotics
company: "Meta"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10913v1"
arxiv_id: "2605.10913"
authors: ["Simon Yu", "Derek Chong", "Ananjan Nandi", "Dilara Soylu", "Jiuding Sun", "Christopher D Manning"]
slug: shepherd-a-runtime-substrate-empowering-meta-agents-with-a-f
summary_word_count: 440
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper presents Shepherd, a preprint work that addresses the lack of a formalized runtime substrate for meta-agents, which are agents that can manipulate other agents. Existing frameworks do not adequately support the complex interactions and state management required for effective meta-agent operations. Shepherd aims to fill this gap by providing a functional programming model that formalizes these operations and records interactions in a structured manner.

**Method**  
Shepherd employs a functional programming paradigm to define meta-agent operations as functions, with core operations mechanized in the Lean theorem prover. The system captures every interaction between agents and their environments as typed events in a Git-like execution trace, allowing for efficient state management and replay capabilities. Notably, Shepherd achieves a forking and filesystem operation speed that is five times faster than Docker, with over 95% prompt-cache reuse during replay. The authors demonstrate the utility of Shepherd through three applications: (1) runtime intervention, (2) counterfactual meta-optimization, and (3) Tree-RL training. Each application leverages the execution trace to enhance performance and efficiency.

**Results**  
In the runtime intervention application, a live supervisor using Shepherd increased pair coding pass rates from 28.8% to 54.7% on the CooperBench benchmark. For counterfactual meta-optimization, the system's branching exploration outperformed baseline methods across four benchmarks, achieving improvements of up to 11 points while reducing wall-clock time by as much as 58%. In the Tree-RL training application, forking rollouts at selected turns led to a performance increase on TerminalBench-2 from 34.2% to 39.4%. These results demonstrate Shepherd's effectiveness as a runtime infrastructure for programming meta-agents.

**Limitations**  
The authors acknowledge that while Shepherd significantly enhances the efficiency of meta-agent operations, it may not be universally applicable to all types of agents or environments. The reliance on the Lean theorem prover may introduce a learning curve for practitioners unfamiliar with formal methods. Additionally, the performance gains are benchmark-specific, and the generalizability of results across diverse tasks remains to be validated. The paper does not address potential scalability issues when applied to larger systems or more complex agent interactions.

**Why it matters**  
Shepherd represents a significant advancement in the infrastructure available for developing meta-agents, providing a formalized approach to managing agent interactions and state. The ability to efficiently fork and replay agent states opens new avenues for research in meta-learning, reinforcement learning, and agent-based systems. By enabling more sophisticated interventions and optimizations, Shepherd could lead to improved performance in collaborative and competitive environments. The open-source release of the system encourages further exploration and development in this area, potentially accelerating advancements in meta-agent capabilities.

Authors: Simon Yu, Derek Chong, Ananjan Nandi, Dilara Soylu, Jiuding Sun, Christopher D Manning, Weiyan Shi  
Source: arXiv:2605.10913  
URL: [https://arxiv.org/abs/2605.10913v1](https://arxiv.org/abs/2605.10913v1)
