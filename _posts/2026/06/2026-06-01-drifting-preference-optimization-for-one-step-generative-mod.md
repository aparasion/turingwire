---
title: "Drifting Preference Optimization for One-Step Generative Models"
date: 2026-06-01 17:31:49 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.02521v1"
arxiv_id: "2606.02521"
authors: ["Zhou Jiang", "Yandong Wen", "Zhen Liu"]
slug: drifting-preference-optimization-for-one-step-generative-mod
summary_word_count: 405
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces Drifting Preference Optimization (DrPO), an innovative method for preference finetuning one-step text-to-image generators efficiently."
---

**Problem**  
The paper addresses the challenge of preference finetuning in one-step text-to-image generators, which are appealing for their efficiency but struggle with standard alignment methods. Existing techniques often depend on complex mechanisms such as policy likelihoods, denoising trajectories, differentiable reward gradients, or test-time optimization, which can be computationally intensive and impractical for real-time applications. This work is a preprint and has not undergone peer review.

**Method**  
The authors propose Drifting Preference Optimization (DrPO), an online finetuning method specifically designed for deterministic one-step generators. DrPO operates by sampling candidate images from the generator for each prompt and ranking them based on a target reward. The method synthesizes an update direction in feature space using high- and low-scoring samples, creating a non-parametric dipole preference field combined with a reference drift derived from a frozen base generator. This update is optimized through a detached feature-space regression target, allowing the method to utilize large, black-box, or non-differentiable rewards solely for ranking purposes. Consequently, inference remains efficient, requiring only a single generator call.

**Results**  
DrPO was evaluated on two models, SD-Turbo and SDXL-Turbo, across various target rewards and benchmarks, including HPSv3 and GenEval. The results indicate that DrPO significantly enhances alignment compared to reward-gradient-free one-step preference baselines. Notably, it achieves a reduction in HPSv3 training computation by a factor of 3.51 under matched effective-batch settings, primarily by eliminating the need for reward-model backpropagation. These improvements suggest that DrPO can effectively streamline the finetuning process while maintaining high-quality output.

**Limitations**  
The authors acknowledge that while DrPO shows promise, it is still reliant on the quality of the target reward for ranking, which may not always be optimal. Additionally, the method's performance in scenarios with highly variable or noisy rewards is not thoroughly explored. The paper does not address potential scalability issues when applied to larger datasets or more complex generative tasks, nor does it discuss the implications of using a frozen base generator for reference drift.

**Why it matters**  
DrPO represents a significant advancement in the field of generative modeling, particularly for applications requiring real-time image generation with high alignment to user preferences. By enabling efficient preference finetuning without the computational overhead of traditional methods, this approach could facilitate broader adoption of one-step generators in practical applications. The implications of this work extend to various domains, including content creation and interactive AI systems, where rapid and responsive image generation is critical. For further details, see the full paper available on [arXiv](https://arxiv.org/abs/2606.02521v1).
