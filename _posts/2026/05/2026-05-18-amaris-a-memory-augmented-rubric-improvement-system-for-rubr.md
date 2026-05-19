---
title: "AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning"
date: 2026-05-18 16:06:27 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18592v1"
arxiv_id: "2605.18592"
authors: ["Peilin Wu", "Xinlu Zhang", "Kun Wan", "Wentian Zhao", "Gang Wu", "Xinya Du"]
slug: amaris-a-memory-augmented-rubric-improvement-system-for-rubr
summary_word_count: 460
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing rubric-based reward shaping methods in reinforcement learning (RL), particularly those that adapt rubrics based on immediate local signals such as current rollouts or pairwise comparisons. These methods fail to retain diagnostic information from evaluations, leading to a lack of long-term knowledge accumulation and strategic reuse. Consequently, the system must repeatedly derive evaluation principles from scratch, which hinders its ability to recognize recurring suboptimal behaviors and limits the potential for a curriculum-like progression in training. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose AMARIS (A Memory-Augmented Rubric Improvement System), which enhances rubric modifications by leveraging long-term training history. AMARIS operates by analyzing individual rollouts at each training step and aggregating these findings into step-level summaries. It retrieves relevant historical context from a persistent evaluation memory using both static (recent steps) and dynamic (semantically matched) retrieval methods. The rubrics are then updated based on these accumulated analyses. The system runs asynchronously alongside the standard RL training loop, introducing minimal computational overhead. The architecture emphasizes the integration of memory retrieval mechanisms to facilitate evidence-driven updates to the rubrics.

**Results**  
AMARIS demonstrates consistent performance improvements over baseline methods across both closed and open-ended domains. The paper reports that the combination of static and dynamic memory retrieval significantly enhances performance, with moderate retrieval budgets yielding most of the gains. Specifically, the authors note that the entire AMARIS pipeline incurs only approximately 5% additional time overhead due to its asynchronous execution. While exact numerical results against specific baselines are not detailed in the abstract, the overall performance trend indicates a substantial enhancement in the efficacy of rubric-based reward shaping.

**Limitations**  
The authors acknowledge that the reliance on historical context may introduce biases if the evaluation memory is not managed effectively. They do not discuss potential scalability issues related to the size of the persistent evaluation memory or the computational costs associated with maintaining and querying this memory over extended training periods. Additionally, the impact of varying retrieval budgets on performance is not exhaustively explored, which could be a critical factor in practical applications.

**Why it matters**  
The introduction of AMARIS has significant implications for the field of reinforcement learning, particularly in the context of fine-tuning large language models (LLMs) through rubric-based reward shaping. By transforming the process from a stateless heuristic to an evidence-driven loop, AMARIS enables more effective learning from past evaluations, potentially leading to improved model performance and robustness. This work paves the way for future research into memory-augmented systems in RL, encouraging the exploration of long-term knowledge retention and its effects on learning efficiency and adaptability.

Authors: Peilin Wu, Xinlu Zhang, Kun Wan, Wentian Zhao, Gang Wu, Xinya Du, Zhiyu Chen  
Source: arXiv:2605.18592  
URL: [https://arxiv.org/abs/2605.18592v1](https://arxiv.org/abs/2605.18592v1)
