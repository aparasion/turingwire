---
title: "On Adaptivity in Zeroth-Order Optimization"
date: 2026-05-05 15:29:11 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03869v1"
arxiv_id: "2605.03869"
authors: ["Hassan Dbouk", "Nidham Gazagnadou", "Matthias Reisser", "Christos Louizos"]
slug: on-adaptivity-in-zeroth-order-optimization
summary_word_count: 427
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the effectiveness of adaptive zeroth-order (ZO) optimization methods for fine-tuning large language models (LLMs) under memory constraints. The authors challenge prior assertions that adaptive methods, such as ZO-Adam, provide superior convergence properties compared to traditional ZO stochastic gradient descent (ZO-SGD). They highlight that adaptive methods incur significant memory overhead without offering convergence advantages, particularly in high-dimensional spaces where ZO gradients exhibit a lack of coordinate-wise heterogeneity. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of MEAZO, a memory-efficient adaptive ZO optimizer. MEAZO simplifies the adaptation process by tracking only a single scalar for global step size adjustment, thereby reducing memory usage compared to existing adaptive methods. The authors provide theoretical convergence guarantees for MEAZO under standard assumptions, ensuring that it maintains performance while being memory-efficient. The experiments conducted utilize various LLM families and tasks, comparing MEAZO against ZO-Adam and ZO-SGD to validate its efficacy.

**Results**  
MEAZO demonstrates performance parity with ZO-Adam while maintaining a memory footprint comparable to ZO-SGD. In experiments across multiple LLMs, MEAZO achieves similar convergence rates and final performance metrics as ZO-Adam, but with significantly reduced memory requirements. The authors also report that MEAZO exhibits enhanced robustness to step size variations, particularly in scenarios involving grouped or block-structured optimization. Specific numerical results are not disclosed in the abstract, but the paper indicates that MEAZO's performance is consistent across diverse tasks and model architectures.

**Limitations**  
The authors acknowledge that while MEAZO offers memory efficiency and competitive performance, it may not outperform ZO-Adam in all scenarios, particularly those where adaptive mechanisms are beneficial. They do not address potential limitations related to the scalability of MEAZO in extremely high-dimensional optimization problems or its performance in non-quadratic loss landscapes. Additionally, the theoretical guarantees provided are based on standard assumptions, which may not hold in all practical applications.

**Why it matters**  
This work has significant implications for the field of large-scale machine learning, particularly in the context of fine-tuning LLMs where memory constraints are a critical concern. By demonstrating that adaptive ZO methods may not provide the expected advantages, the authors encourage a reevaluation of existing optimization strategies. MEAZO's design could inspire further research into memory-efficient optimization techniques, potentially leading to more scalable solutions for training large models in resource-constrained environments. The findings also suggest that practitioners should carefully consider the trade-offs between memory usage and convergence performance when selecting optimization algorithms for LLM fine-tuning.

Authors: Hassan Dbouk, Nidham Gazagnadou, Matthias Reisser, Christos Louizos  
Source: arXiv:2605.03869  
URL: [https://arxiv.org/abs/2605.03869v1](https://arxiv.org/abs/2605.03869v1)
