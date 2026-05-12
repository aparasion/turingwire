---
title: "Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents"
date: 2026-05-11 16:49:36 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10832v1"
arxiv_id: "2605.10832"
authors: ["Shijue Huang", "Hangyu Guo", "Chenxin Li", "Junting Lu", "Xinyu Geng", "Zhaochen Su"]
slug: towards-on-policy-data-evolution-for-visual-native-multimoda
summary_word_count: 442
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses significant limitations in multimodal deep search agents, specifically the inability to reuse intermediate visual evidence from tool outputs and the static nature of training data curation. Current systems treat images returned from searches or transformations as ephemeral, preventing their re-consumption in subsequent tasks. Additionally, existing training data is often curated without adapting to the evolving capabilities of the agent, leading to inefficiencies in learning. 

**Method**  
The authors propose a novel framework that integrates a visual-native agent harness with an On-policy Data Evolution (ODE) mechanism. The visual-native agent harness employs an image bank reference protocol, allowing every tool-returned image to be registered as an addressable reference. This enables the reuse of intermediate visual evidence across different tools. The ODE mechanism operates as a closed-loop data generator that iteratively refines the training data based on the agent's current policy needs. This refinement process occurs across multiple rounds, ensuring that each round's data is tailored to the specific learning requirements of the agent. The framework supports both supervised fine-tuning and policy-aware reinforcement learning, effectively covering the entire training lifecycle.

**Results**  
The implementation of ODE significantly enhances the performance of the Qwen3-VL-8B agent across eight multimodal deep search benchmarks. The average performance improved from 24.9% to 39.0%, surpassing the Gemini-2.5 Pro baseline, which achieved 37.9%. For the 30B model, the average score increased from 30.6% to 41.5%. These results indicate a substantial effect size, demonstrating the efficacy of the proposed method in improving agent performance in complex multimodal tasks.

**Limitations**  
The authors acknowledge that the proposed method may require extensive computational resources due to the iterative nature of the ODE process. Additionally, the reliance on an image bank may introduce challenges related to storage and retrieval efficiency. The paper does not address potential scalability issues when applied to larger datasets or more complex multimodal environments. Furthermore, the generalizability of the findings to other types of agents or tasks remains to be explored.

**Why it matters**  
This work has significant implications for the development of more capable multimodal agents that can effectively handle open-world problems. By enabling the reuse of visual evidence and dynamically curating training data, the proposed framework enhances the learning efficiency and adaptability of agents. This could lead to advancements in various applications, including robotics, interactive AI systems, and complex decision-making scenarios where visual reasoning is critical. The integration of ODE into the training lifecycle may set a new standard for how multimodal agents are developed and trained, paving the way for future research in this domain.

Authors: Shijue Huang, Hangyu Guo, Chenxin Li, Junting Lu, Xinyu Geng, Zhaochen Su, Zhenyu Li, Shuang Chen et al.  
Source: arXiv:2605.10832  
URL: [https://arxiv.org/abs/2605.10832v1](https://arxiv.org/abs/2605.10832v1)
