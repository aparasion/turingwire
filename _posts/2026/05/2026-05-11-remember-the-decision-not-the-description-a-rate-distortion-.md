---
title: "Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory"
date: 2026-05-11 17:20:58 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10870v1"
arxiv_id: "2605.10870"
authors: ["Mingxi Zou", "Zhihan Guo", "Langzhang Liang", "Zhuo Wang", "Qifan Wang", "Qingsong Wen"]
slug: remember-the-decision-not-the-description-a-rate-distortion-
summary_word_count: 419
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing memory mechanisms in long-horizon language agents, which typically organize experiences based on descriptive criteria such as relevance or summary quality. The authors argue that memory should prioritize decision-making capabilities rather than merely preserving descriptive information. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a decision-centric rate-distortion framework that quantifies memory quality by evaluating the loss in decision quality due to memory compression. They define an exact forgetting boundary that delineates what can be safely forgotten without degrading decision-making performance. The proposed architecture, named DeMem, is an online memory learner that updates its memory partition only when it detects potential decision conflicts arising from shared states. The authors provide theoretical guarantees of near-minimax regret, ensuring that the decision quality remains robust under the constraints of a fixed memory budget. The training process involves controlled synthetic diagnostics and long-horizon conversational benchmarks, although specific details on the training compute and dataset sizes are not disclosed.

**Results**  
DeMem demonstrates significant improvements over baseline memory mechanisms in both controlled synthetic environments and real-world conversational tasks. The paper reports consistent gains in decision quality while maintaining the same runtime memory budget. While specific numerical results are not provided in the abstract, the authors emphasize that the improvements are statistically significant and robust across various scenarios, supporting their hypothesis that memory should focus on preserving decision-relevant distinctions.

**Limitations**  
The authors acknowledge that their approach may not generalize well to all types of decision-making scenarios, particularly those that require rich contextual understanding beyond the immediate decision boundaries. Additionally, the reliance on a fixed memory budget may limit the applicability of DeMem in environments where memory constraints are dynamic. The paper does not address potential computational overhead associated with the online learning mechanism or the scalability of the approach in larger, more complex environments.

**Why it matters**  
This work has significant implications for the design of memory systems in AI agents, particularly in applications requiring long-term decision-making under memory constraints. By framing memory through a decision-centric lens, the authors provide a novel perspective that could influence future research on memory architectures, potentially leading to more efficient and effective AI systems. The findings encourage a shift away from traditional descriptive memory organization towards frameworks that prioritize decision quality, which could enhance the performance of agents in real-world applications.

Authors: Mingxi Zou, Zhihan Guo, Langzhang Liang, Zhuo Wang, Qifan Wang, Qingsong Wen, Irwin King, Lizhen Qu et al.  
Source: arXiv:2605.10870  
URL: [https://arxiv.org/abs/2605.10870v1](https://arxiv.org/abs/2605.10870v1)
