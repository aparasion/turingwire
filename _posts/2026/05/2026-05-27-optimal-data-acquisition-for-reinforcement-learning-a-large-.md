---
title: "Optimal Data Acquisition for Reinforcement Learning: A Large Deviations Perspective"
date: 2026-05-27 16:08:56 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28675v1"
arxiv_id: "2605.28675"
authors: ["Mingjie Hu", "Jian-Qiang Hu", "Enlu Zhou"]
slug: optimal-data-acquisition-for-reinforcement-learning-a-large-
summary_word_count: 462
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiency of data acquisition in reinforcement learning (RL), particularly in contexts where interactions are costly and slow, such as business and healthcare operations. The authors identify a gap in the literature regarding principled metrics for evaluating data acquisition efficiency in infinite-horizon RL settings. They propose a novel framework based on large deviations theory to quantify and optimize data acquisition strategies. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a large deviations framework that characterizes the exponential decay rate of the policy-selection error probability as a metric for data acquisition efficiency. They derive a variational characterization of this decay rate for Markov chains, leading to a nested optimization problem that captures the optimality of data acquisition strategies. Due to the implicit and generally intractable nature of this problem, the authors propose a tractable convex relaxation with explicit constraints. To solve this relaxed problem, they develop a lazy one-step projected subgradient method, which generates iterates that inform an adaptive data acquisition policy. Additionally, the framework is extended to accommodate linear function approximation, enhancing scalability.

**Results**  
The proposed method demonstrates near-robust optimality under the defined efficiency criterion, with empirical evaluations indicating significant improvements in data acquisition efficiency compared to baseline methods. While specific numerical results are not detailed in the abstract, the authors suggest that their approach outperforms traditional data acquisition strategies in various scenarios, as evidenced by numerical experiments. The effectiveness of the proposed adaptive policy is highlighted, although exact performance metrics and comparisons to named baselines are not provided in the abstract.

**Limitations**  
The authors acknowledge that the nested optimization problem is generally intractable, which necessitates the use of a convex relaxation. While they provide a solution method, the performance of the lazy one-step projected subgradient method may be sensitive to hyperparameter choices and initialization. Additionally, the scalability improvements through linear function approximation may not generalize to all RL environments, particularly those with complex state-action spaces. The paper does not address potential limitations related to the robustness of the proposed method in highly stochastic environments or its applicability to non-Markovian settings.

**Why it matters**  
This work has significant implications for the deployment of reinforcement learning in real-world applications where data acquisition is a bottleneck. By providing a principled framework for optimizing data acquisition strategies, the authors contribute to the development of more efficient RL algorithms that can operate effectively in environments with costly interactions. The integration of large deviations theory into RL opens new avenues for research, particularly in understanding the trade-offs between exploration and exploitation in data-scarce scenarios. This framework could lead to advancements in adaptive learning systems across various domains, including healthcare and business operations.

Authors: Mingjie Hu, Jian-Qiang Hu, Enlu Zhou  
Source: arXiv:2605.28675  
URL: https://arxiv.org/abs/2605.28675v1
