---
title: "TriSearch: Learning to Optimize Triangulations via Bistellar Flips"
date: 2026-05-28 16:54:06 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30220v1"
arxiv_id: "2605.30220"
authors: ["Yiran Wang", "Guido Mont\u00fafar"]
slug: trisearch-learning-to-optimize-triangulations-via-bistellar-
summary_word_count: 425
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in optimization techniques for triangulations of polytopes, specifically through the lens of bistellar flips. Existing methods often rely on exhaustive enumeration of triangulations, which becomes computationally infeasible as the dimensionality and complexity of the polytopes increase. The authors propose TriSearch, a reinforcement learning framework that learns to optimize triangulations without the need for explicit enumeration, thus providing a more scalable solution. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
TriSearch employs a reinforcement learning approach to optimize triangulations via bistellar flips. The core technical contribution is the introduction of a circuit-supported subtriangulation action representation, where feasible flips are encoded by their supporting circuit and the corresponding local subtriangulation. This representation allows the learned policy to rank potential flips based on local geometric and combinatorial features, facilitating efficient navigation through the flip graph. The architecture is dimension-agnostic, enabling the model to generalize from smaller training instances to larger polytopes. The authors instantiate TriSearch in both 3D and 4D settings, utilizing a policy gradient method for training. The computational resources required for training are not explicitly disclosed.

**Results**  
TriSearch demonstrates superior performance on metric objectives in 3D triangulations, outperforming existing baselines. In 4D, it successfully discovers a greater number of distinct triangulations—specifically Fine, Regular, and Star triangulations of reflexive polytopes—compared to existing samplers, all while operating under a fixed computational budget. The authors report that TriSearch achieves a significant increase in the diversity of triangulations found, indicating an effective exploration of the search space. However, specific quantitative metrics (e.g., exact performance numbers or effect sizes) are not provided in the abstract.

**Limitations**  
The authors acknowledge that the performance of TriSearch may be sensitive to the choice of local geometric and combinatorial features used for ranking flips. Additionally, the framework's reliance on reinforcement learning introduces challenges related to sample efficiency and convergence, particularly in higher dimensions. The paper does not address potential limitations regarding the scalability of the approach to even higher dimensions or the robustness of the learned policy across varying polytope configurations.

**Why it matters**  
The implications of this work are significant for computational geometry and optimization in higher-dimensional spaces. By providing a scalable method for optimizing triangulations, TriSearch opens avenues for more efficient algorithms in applications such as mesh generation, computer graphics, and topological data analysis. The ability to generalize from smaller instances to larger polytopes suggests potential for broader applicability in various fields that require triangulation optimization, including robotics and machine learning.

Authors: Yiran Wang, Guido Montúfar  
Source: arXiv:2605.30220  
URL: https://arxiv.org/abs/2605.30220v1
