---
title: "When to Vote, When to Rewrite: Disagreement-Guided Strategy Routing for Test-Time Scaling"
date: 2026-04-29 13:11:39 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26644v1"
arxiv_id: "2604.26644"
authors: ["Zhimin Lin", "Yixin Ji", "Jinpeng Li", "Yu Luo", "Dong Li", "Junhua Fang"]
slug: when-to-vote-when-to-rewrite-disagreement-guided-strategy-ro
summary_word_count: 428
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing test-time scaling methods for Large Reasoning Models (LRMs) in mathematical reasoning tasks, particularly their inefficiency and diminishing returns on challenging instances. The authors highlight that current strategies, such as repeated sampling and self-correction, often lead to increased computational costs without significantly improving accuracy. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework that reformulates test-time scaling as an instance-level routing problem, leveraging output disagreement as a key signal for strategy selection. The framework operates without requiring additional training and employs three distinct strategies based on the level of disagreement observed in model outputs: 
1. **Lightweight resolution** for consistent outputs, where the model is confident in its prediction.
2. **Majority voting** for cases of moderate disagreement, aggregating predictions from multiple outputs to enhance reliability.
3. **Rewriting-based reformulation** for highly ambiguous instances, where the model generates alternative formulations to clarify the problem. This dynamic selection process allows for more efficient allocation of computational resources, adapting to the specific characteristics of each instance.

**Results**  
The proposed method was evaluated across seven mathematical benchmarks using three different models. The results indicate a notable improvement in accuracy, achieving gains of 3% to 7% over baseline methods. Specifically, the framework outperformed traditional test-time scaling techniques, demonstrating both enhanced accuracy and reduced sampling costs. The authors provide detailed comparisons against named baselines, although specific baseline performance metrics are not disclosed in the summary.

**Limitations**  
The authors acknowledge that their approach may not generalize well to all types of reasoning tasks beyond mathematical problems, as the reliance on output disagreement may vary in effectiveness across different domains. Additionally, the framework's performance is contingent on the quality of the underlying LRM; if the model's initial predictions are poor, the disagreement signal may not be reliable. The paper does not address potential computational overhead introduced by the rewriting strategy, which could negate some efficiency gains in certain scenarios.

**Why it matters**  
This work has significant implications for the development of more efficient reasoning models, particularly in scenarios where computational resources are limited. By introducing a method that intelligently routes strategies based on output disagreement, the authors provide a pathway for enhancing model reliability without incurring prohibitive costs. This approach could inspire further research into adaptive computation strategies in AI, potentially leading to more robust models capable of handling a wider range of reasoning tasks with improved efficiency.

Authors: Zhimin Lin, Yixin Ji, Jinpeng Li, Yu Luo, Dong Li, Junhua Fang, Juntao Li, Min Zhang  
Source: arXiv:2604.26644  
URL: https://arxiv.org/abs/2604.26644v1
