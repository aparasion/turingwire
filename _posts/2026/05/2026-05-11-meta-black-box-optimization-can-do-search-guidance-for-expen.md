---
title: "Meta-Black-Box Optimization Can Do Search Guidance for Expensive Constrained Multi-Objective Optimization"
date: 2026-05-11 09:25:35 +0000
category: research
subcategory: other
company: "Meta"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.10260v1"
arxiv_id: "2605.10260"
authors: ["Yukun Du", "Haiyue Yu", "Jiang Jiang", "Shuaiwen Tang", "Xiaotong Xie", "Haobo Liu"]
slug: meta-black-box-optimization-can-do-search-guidance-for-expen
summary_word_count: 390
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the existing literature on Meta-Black-Box Optimization (MetaBBO) methods, which primarily focus on optimizing the control of search algorithms but neglect the critical aspect of search guidance. Specifically, the authors propose a solution for expensive constrained multi-objective optimization problems (ECMOPs), which are prevalent in various engineering and scientific applications. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce MetaSG-SAEA, a bi-level framework that integrates a meta-policy for search guidance with a low-level Surrogate-Assisted Evolutionary Algorithm (SAEA). The core technical contribution is the Max-Min Constraint-Calibrated Inequality (MM-CCI), a novel region abstraction that effectively maps heterogeneous constraint evaluations into a scalar representation. This abstraction allows for a more structured approach to guiding the search process. The framework employs diffusion-based population initialization to convert the meta-policy's guidance into solution-level priors for the SAEA. To enhance scalability, an attention-based state representation is constructed, accommodating variations in problem dimensions, population sizes, and the number of objectives and constraints.

**Results**  
MetaSG-SAEA demonstrates superior performance compared to state-of-the-art baselines across multiple benchmark datasets. The authors report significant improvements in convergence speed and solution quality, although specific numerical results and effect sizes are not detailed in the abstract. The framework's ability to generalize across different problem distributions is also highlighted, indicating robustness in diverse optimization scenarios.

**Limitations**  
The authors acknowledge that while MetaSG-SAEA shows promise, it may still be limited by the assumptions inherent in the MM-CCI abstraction, which could affect its applicability to highly complex or non-standard ECMOPs. Additionally, the scalability of the attention-based representation may introduce computational overhead, particularly in high-dimensional settings. The paper does not address potential challenges related to the interpretability of the meta-policy or the implications of its deployment in real-world applications.

**Why it matters**  
This work has significant implications for the field of multi-objective optimization, particularly in contexts where computational resources are limited and evaluations are expensive. By providing a structured approach to search guidance, MetaSG-SAEA could enhance the efficiency of optimization processes in various domains, including engineering design, resource allocation, and machine learning hyperparameter tuning. The introduction of MM-CCI may also inspire further research into problem-agnostic abstractions that can facilitate more effective optimization strategies.

Authors: Yukun Du, Haiyue Yu, Jiang Jiang, Shuaiwen Tang, Xiaotong Xie, Haobo Liu, Chongshuang Hu, Shengkun Chang  
Source: arXiv:2605.10260  
URL: [https://arxiv.org/abs/2605.10260v1](https://arxiv.org/abs/2605.10260v1)
