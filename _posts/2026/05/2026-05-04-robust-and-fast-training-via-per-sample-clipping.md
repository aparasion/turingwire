---
title: "Robust and Fast Training via Per-Sample Clipping"
date: 2026-05-04 15:11:36 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.02701v1"
arxiv_id: "2605.02701"
authors: ["Davide Nobile", "Philipp Grohs"]
slug: robust-and-fast-training-via-per-sample-clipping
summary_word_count: 431
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing gradient estimation techniques in the presence of heavy-tailed gradient noise, which can significantly hinder the convergence of stochastic optimization algorithms. The authors propose a novel approach, per-sample clipped SGD (PS-Clip-SGD), to improve robustness and convergence rates in non-convex optimization problems. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of PS-Clip-SGD, which employs per-sample gradient clipping to mitigate the effects of noise in gradient estimates. The method is theoretically analyzed, demonstrating optimal in-expectation convergence rates for non-convex problems under heavy-tailed noise conditions. The authors provide high-probability convergence guarantees that align with the in-expectation rates, differing only by polylogarithmic factors in the failure probability. The training process involves clipping gradients on a per-sample basis, which is shown to be effective even when gradient accumulation is employed. The authors also explore the implications of mini-batch level clipping, revealing that it can enhance training performance without incurring significant computational overhead.

**Results**  
Empirical evaluations demonstrate that PS-Clip-SGD outperforms both vanilla SGD with momentum and standard gradient clipping when training AlexNet on the CIFAR-100 dataset. Specifically, PS-Clip-SGD achieves a lower training loss and faster convergence compared to the baselines, despite the additional computational cost associated with per-sample clipping. The authors report that PS-Clip-SGD consistently improves performance metrics, although exact numerical results are not disclosed in the abstract. The findings suggest that the method is particularly effective in scenarios where gradient noise is prevalent, thus validating the theoretical claims made.

**Limitations**  
The authors acknowledge that while PS-Clip-SGD shows promise, its performance may vary depending on the specific characteristics of the dataset and the model architecture used. They do not address potential scalability issues when applied to larger datasets or more complex models beyond AlexNet. Additionally, the computational overhead introduced by per-sample clipping, although deemed manageable, could still be a concern in resource-constrained environments. The paper does not explore the impact of hyperparameter tuning on the performance of PS-Clip-SGD, which could be a critical factor in practical applications.

**Why it matters**  
The implications of this work are significant for the field of machine learning, particularly in the context of training deep neural networks under challenging conditions. By providing a robust gradient estimation technique that effectively handles heavy-tailed noise, PS-Clip-SGD could enhance the reliability and efficiency of training algorithms in various applications. This research opens avenues for further exploration into adaptive clipping strategies and their integration into existing optimization frameworks, potentially leading to more resilient models in real-world scenarios.

Authors: Davide Nobile, Philipp Grohs  
Source: arXiv:2605.02701  
URL: [https://arxiv.org/abs/2605.02701v1](https://arxiv.org/abs/2605.02701v1)
