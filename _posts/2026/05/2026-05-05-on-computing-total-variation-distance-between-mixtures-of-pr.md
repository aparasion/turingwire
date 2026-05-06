---
title: "On Computing Total Variation Distance Between Mixtures of Product Distributions"
date: 2026-05-05 15:05:49 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03839v1"
arxiv_id: "2605.03839"
authors: ["Weiming Feng", "Yucheng Fu", "Minji Yang", "Anqi Zhang"]
slug: on-computing-total-variation-distance-between-mixtures-of-pr
summary_word_count: 462
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the computational challenge of approximating the total variation distance (TVD) between two mixtures of product distributions over an \( n \)-dimensional discrete domain. The authors identify a gap in existing literature regarding efficient algorithms for this problem, particularly in the context of high-dimensional spaces and mixtures with multiple components. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a randomized algorithm that approximates the total variation distance \( d_{\mathrm{TV}}(\mathbb{P}, \mathbb{Q}) \) between two mixtures \( \mathbb{P} \) and \( \mathbb{Q} \), where \( \mathbb{P} \) consists of \( k_1 \) product distributions and \( \mathbb{Q} \) consists of \( k_2 \) product distributions over the discrete domain \([q]^n\). The algorithm achieves a multiplicative error of \( (1 \pm \varepsilon) \) and operates in time complexity \( \mathrm{poly}((nq)^{k_1+k_2}, 1/\varepsilon) \). Additionally, the authors explore a special case involving mixtures of Boolean subcubes over \( \{0,1\}^n \). For this scenario, they provide a deterministic algorithm that computes the exact total variation distance in time \( \mathrm{poly}(n, 2^{O(k_1+k_2)}) \). They also establish that exact computation of TVD is \( \#\mathsf{P} \)-hard when \( k_1 + k_2 = \Theta(n) \).

**Results**  
The proposed randomized algorithm demonstrates significant efficiency, particularly for large \( k_1 \) and \( k_2 \). While specific numerical results are not provided in the abstract, the algorithm's performance is characterized by its polynomial time complexity relative to the number of distributions and the dimension of the space. The deterministic algorithm for the Boolean subcube case is notable for its exact computation capability, although it is limited by the exponential factor in \( k_1 + k_2 \). The authors do not provide direct comparisons to existing baselines in the abstract, which limits the ability to quantify effect sizes or improvements over prior methods.

**Limitations**  
The authors acknowledge that their randomized algorithm provides an approximation rather than an exact solution, which may not be suitable for applications requiring precise distance metrics. Furthermore, the deterministic algorithm's exponential time complexity in the number of distributions poses scalability issues for large \( k_1 \) and \( k_2 \). The paper does not address potential practical implementations or empirical evaluations of the algorithms, which could provide insights into their real-world applicability.

**Why it matters**  
This work has significant implications for fields that rely on measuring the divergence between probability distributions, such as machine learning, statistics, and information theory. The ability to efficiently approximate total variation distance in high-dimensional spaces can enhance model evaluation, anomaly detection, and generative modeling. Furthermore, the exploration of the complexity of exact computation in the Boolean subcube case contributes to the theoretical understanding of computational limits in probabilistic modeling.

Authors: Weiming Feng, Yucheng Fu, Minji Yang, Anqi Zhang  
Source: arXiv:2605.03839  
URL: [https://arxiv.org/abs/2605.03839v1](https://arxiv.org/abs/2605.03839v1)
