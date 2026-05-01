---
title: "Cost-Aware Learning"
date: 2026-04-30 15:39:09 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.28020v1"
arxiv_id: "2604.28020"
authors: ["Clara Mohri", "Amir Globerson", "Haim Kaplan", "Tomer Koren", "Yishay Mansour"]
slug: cost-aware-learning
summary_word_count: 399
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding Cost-Aware Learning, specifically in scenarios where different components of a finite-sum objective incur varying costs. The authors highlight the need for algorithms that not only minimize error but also consider the associated costs of sampling different functions. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce the Cost-Aware Stochastic Gradient Descent (C-SGD) algorithm tailored for convex functions. C-SGD incorporates a cost complexity analysis to achieve a target error of ε, providing a theoretical framework for understanding the trade-offs between cost and performance. Additionally, they establish a lower bound for the cost in this learning setting. To further optimize costs, a subset selection algorithm is proposed, which strategically selects components to minimize training expenses. The theoretical insights are applied to reinforcement learning, particularly in the context of language models, leading to the development of Cost-Aware Generalized Policy Optimization (Cost-Aware GRPO). This algorithm is designed to optimize policy gradients while accounting for the computational costs that vary with sequence length.

**Results**  
Empirical evaluations demonstrate that Cost-Aware GRPO significantly reduces the number of tokens used in policy optimization by approximately 30% compared to baseline methods, while maintaining or even exceeding baseline accuracy. The experiments were conducted on large language models (LLMs) with 1.5 billion and 8 billion parameters, showcasing the effectiveness of the proposed methods in practical scenarios.

**Limitations**  
The authors acknowledge that their approach primarily focuses on convex functions and may not generalize well to non-convex settings, which are prevalent in many real-world applications. Additionally, while the empirical results are promising, they are limited to specific architectures and may not reflect performance across all types of language models or reinforcement learning tasks. The paper does not address the scalability of the proposed algorithms in terms of larger datasets or more complex environments.

**Why it matters**  
This work has significant implications for the field of machine learning, particularly in resource-constrained environments where computational costs are a critical factor. By integrating cost considerations into the learning process, the proposed algorithms enable more efficient training of models, which is essential for deploying AI systems in real-world applications. The insights gained from this research could inform future work on cost-sensitive learning and optimization strategies, potentially leading to more sustainable AI practices.

Authors: Clara Mohri, Amir Globerson, Haim Kaplan, Tomer Koren, Yishay Mansour  
Source: arXiv:2604.28020  
URL: [https://arxiv.org/abs/2604.28020v1](https://arxiv.org/abs/2604.28020v1)
