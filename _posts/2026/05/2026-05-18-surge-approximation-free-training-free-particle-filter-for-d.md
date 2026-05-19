---
title: "SURGE: Approximation-free Training Free Particle Filter for Diffusion Surrogate"
date: 2026-05-18 17:59:00 +0000
category: research
subcategory: training_methods
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.18745v1"
arxiv_id: "2605.18745"
authors: ["Lifu Wei", "Yinuo Ren", "Naichen Shi", "Yiping Lu"]
slug: surge-approximation-free-training-free-particle-filter-for-d
summary_word_count: 387
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing inference-time guidance techniques in diffusion-based generative models, which often require repeated score or gradient evaluations. These methods introduce bias and high computational overhead, making them less efficient for practical applications. The authors propose a novel approach, URGE (Unbiased Resampling via Girsanov Estimation), which is a preprint and has not yet undergone peer review.

**Method**  
URGE introduces a derivative-free inference-time scaling algorithm that utilizes path-wise importance reweighting through a Girsanov change of measure. Unlike traditional methods that compute gradient-based particle weights, URGE employs a simple multiplicative weight for each simulated trajectory and incorporates periodic resampling. The authors establish an equivalence between path-wise and particle-wise Sequential Monte Carlo (SMC) methods, demonstrating that the Girsanov path weight can be expressed as a backward conditional expectation that recovers the particle-level weights. This guarantees that both approaches yield the same unbiased terminal law. The method is designed to be simpler to implement, requiring no score, Hessian, or partial differential equation (PDE) evaluations.

**Results**  
URGE was empirically evaluated against existing inference-time guidance baselines on synthetic datasets and diffusion-model benchmarks. The results indicate that URGE significantly outperforms these baselines in terms of generation quality. While specific numerical results are not detailed in the abstract, the authors claim that URGE achieves better performance metrics, suggesting a substantial improvement in sample quality without the computational burden associated with gradient-based methods.

**Limitations**  
The authors acknowledge that while URGE simplifies the implementation of inference-time guidance, it may still be sensitive to the choice of resampling frequency and the multiplicative weight strategy. Additionally, the paper does not address potential limitations related to the scalability of URGE in high-dimensional spaces or its performance in more complex, real-world scenarios. The lack of peer review also raises questions about the robustness of the findings.

**Why it matters**  
The introduction of URGE has significant implications for the field of generative modeling, particularly in enhancing the efficiency and effectiveness of diffusion-based models. By eliminating the need for gradient evaluations, URGE opens avenues for real-time applications and reduces computational costs, making it more accessible for practical deployment. This work could inspire further research into derivative-free methods in generative modeling and encourage the exploration of alternative resampling techniques that maintain unbiasedness while improving sample quality.

Authors: Lifu Wei, Yinuo Ren, Naichen Shi, Yiping Lu  
Source: arXiv:2605.18745  
URL: [https://arxiv.org/abs/2605.18745v1](https://arxiv.org/abs/2605.18745v1)
