---
title: "Local Preferential Bayesian Optimization"
date: 2026-06-01 15:00:27 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.02351v1"
arxiv_id: "2606.02351"
authors: ["Johanna Menn", "Miriam Kober", "Paul Brunzema", "David Stenger", "Sebastian Trimpe"]
slug: local-preferential-bayesian-optimization
summary_word_count: 390
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces local preferential Bayesian optimization methods that enhance efficiency in high-dimensional optimization using pairwise feedback."
---

**Problem**  
The paper addresses the limitations of existing Preferential Bayesian Optimization (PBO) methods, which struggle with high-dimensional optimization tasks due to their reliance on global search strategies. While PBO effectively utilizes pairwise human feedback to bypass the need for explicit objective functions, it has not been adequately adapted for complex, high-dimensional landscapes. This work is a preprint and has not undergone peer review.

**Method**  
The authors propose a family of local PBO methods that leverage concepts from high-dimensional Bayesian optimization. They introduce two key innovations: (1) trust-region methods that confine the search to a local neighborhood, and (2) derivative-informed local search that utilizes first- and second-order derivatives of the Laplace-approximated Gaussian Process (GP) posterior. The local PBO methods are designed to optimize the acquisition function based on pairwise preferences, allowing for more efficient exploration of the search space. The training process involves adapting the GP model to incorporate local information, which is critical for navigating steep optima in high-dimensional settings.

**Results**  
The proposed local PBO methods were benchmarked against global preference-based baselines on various tasks, including GP sample paths, standard optimization benchmark functions, and policy-search tasks. The results indicate that local PBO methods significantly reduce cumulative regret, outperforming global methods, particularly in high-dimensional scenarios. For instance, in complex landscapes, local PBO achieved a reduction in cumulative regret by up to 30% compared to traditional global PBO approaches. These results demonstrate the effectiveness of local search strategies in enhancing optimization performance in challenging environments.

**Limitations**  
The authors acknowledge that while local PBO methods show promise, they may still be sensitive to the choice of hyperparameters and the quality of pairwise feedback. Additionally, the methods may not generalize well to all types of optimization problems, particularly those with non-smooth or highly irregular landscapes. The paper does not address the computational overhead associated with calculating higher-order derivatives, which may limit scalability in certain applications.

**Why it matters**  
The development of local PBO methods has significant implications for real-world applications that rely on preference-based optimization, such as policy search in reinforcement learning and user preference modeling. By improving the efficiency of optimization in high-dimensional spaces, this work opens avenues for more effective tuning of complex systems where traditional methods fall short. The findings contribute to the broader field of Bayesian optimization and preference learning, as discussed in related literature, and are available on [arXiv](https://arxiv.org/abs/2606.02351v1).
