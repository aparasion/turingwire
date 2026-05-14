---
title: "OSDN: Improving Delta Rule with Provable Online Preconditioning in Linear Attention"
date: 2026-05-13 12:59:26 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13473v1"
arxiv_id: "2605.13473"
authors: ["Chenyu Zhou", "Hongpei Li", "Yuerou Liu", "Jianghao Lin", "Dongdong Ge", "Yinyu Ye"]
slug: osdn-improving-delta-rule-with-provable-online-preconditioni
summary_word_count: 406
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of linear attention mechanisms and state-space models in achieving effective in-context associative recall. Specifically, it critiques the Delta Rule, which employs a single scalar gate for step size determination, leading to suboptimal performance due to its neglect of feature-wise curvature in the objective function. The work is presented as a preprint and has not undergone peer review.

**Method**  
The authors introduce Online Scaled DeltaNet (OSDN), which enhances the Delta Rule by incorporating a diagonal preconditioner that is updated online through hypergradient feedback. This preconditioning is mathematically equivalent to scaling the write-side key on a per-feature basis, allowing OSDN to maintain the efficient chunkwise parallel processing of DeltaNet without incurring the overhead associated with high-dimensional states. The theoretical foundation of OSDN is built on the exact-quadratic structure of the inner regression loss, which enables super-geometric convergence when compared to a right-Newton method. Additionally, the authors propose Adaptive Preconditioner Forgetting (APF) to address non-stationary contexts by dynamically refreshing the preconditioner calibration.

**Results**  
Empirical evaluations demonstrate that OSDN significantly enhances in-context recall performance. At the 340M-parameter scale, OSDN achieves a 32% improvement in JRT-style in-context recall compared to DeltaNet. When scaled to 1.3B parameters, OSDN realizes a 39% reduction in the recall residual ratio while maintaining competitive performance on general downstream tasks, such as perplexity and LongBench benchmarks. These results indicate that the online preconditioning mechanism effectively scales and amplifies performance in large models.

**Limitations**  
The authors acknowledge that while OSDN improves recall performance, it may still be sensitive to the choice of hyperparameters for the preconditioner and the forgetting mechanism. Additionally, the paper does not explore the computational overhead introduced by the hypergradient updates in detail, which could impact real-time applications. The generalizability of the findings across different architectures and tasks remains to be fully validated.

**Why it matters**  
The introduction of OSDN has significant implications for the development of more efficient attention mechanisms in large-scale models. By addressing the shortcomings of the Delta Rule and enhancing in-context recall, OSDN paves the way for improved performance in applications requiring associative memory, such as natural language processing and reinforcement learning. The theoretical advancements in convergence and the practical improvements in recall performance suggest that online preconditioning could become a standard technique in future model architectures, particularly as the field moves towards larger and more complex models.

Authors: Chenyu Zhou, Hongpei Li, Yuerou Liu, Jianghao Lin, Dongdong Ge, Yinyu Ye  
Source: arXiv:2605.13473  
URL: https://arxiv.org/abs/2605.13473v1
