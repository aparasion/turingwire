---
title: "Optimization over the intersection of manifolds"
date: 2026-05-21 17:08:00 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.22736v1"
arxiv_id: "2605.22736"
authors: ["Yan Yang", "Bin Gao", "Ya-xiang Yuan"]
slug: optimization-over-the-intersection-of-manifolds
summary_word_count: 425
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of optimization over the intersection of two manifolds, a problem prevalent in various applications such as sparse and low-rank optimization. The existing literature lacks a comprehensive framework that effectively handles the coupled geometry of the feasible region formed by the intersection of manifolds. The authors present a novel approach to this problem, which is particularly relevant given that the work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is a geometric optimization method that leverages the properties of the manifolds involved. The authors establish that the conditions of clean intersection and intrinsic transversality are equivalent, which facilitates a tractable projection onto the tangent space of the intersection. The proposed method employs a retraction on one manifold while updating the iterate along two orthogonal directions: one direction maintains the iterate on the first manifold, while the other direction asymptotically approaches the second manifold and reduces the objective function. The convergence analysis is conducted under the assumption of intrinsic transversality, leading to derived rates for both feasibility and optimality measures. The authors demonstrate that every accumulation point of the iterates is first-order stationary.

**Results**  
The authors validate their method through numerical experiments on several optimization problems, including fitting spherical data, approximating hyperbolic embeddings on real datasets, and computing compressed modes. The results indicate that their method outperforms existing baselines in terms of convergence speed and solution quality. Specific performance metrics are not disclosed in the abstract, but the authors claim significant improvements over traditional methods, suggesting a robust effect size in practical applications.

**Limitations**  
The authors acknowledge that their method relies on the assumption of intrinsic transversality, which may not hold in all scenarios. Additionally, the paper does not address the computational complexity of the proposed method in detail, nor does it explore the scalability of the approach to higher-dimensional manifolds or more complex intersections. The lack of extensive empirical validation across diverse datasets may also limit the generalizability of the findings.

**Why it matters**  
This work has significant implications for optimization tasks that involve manifold constraints, particularly in fields such as machine learning, computer vision, and signal processing. By providing a new geometric perspective on manifold intersection optimization, the proposed method could enhance the efficiency and effectiveness of algorithms in applications requiring low-rank approximations and sparse representations. The findings may also inspire further research into the geometric properties of manifolds and their intersections, potentially leading to new optimization techniques and theoretical advancements.

Authors: Yan Yang, Bin Gao, Ya-xiang Yuan  
Source: arXiv:2605.22736  
URL: https://arxiv.org/abs/2605.22736v1
