---
title: "An adaptive wavelet-based PINN for problems with localized high-magnitude source"
date: 2026-04-30 17:57:22 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.28180v1"
arxiv_id: "2604.28180"
authors: ["Himanshu Pandey", "Ratikanta Behera"]
slug: an-adaptive-wavelet-based-pinn-for-problems-with-localized-h
summary_word_count: 427
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing physics-informed neural networks (PINNs) in solving differential equations characterized by localized high-magnitude source terms. Specifically, it tackles the issues of spectral bias and loss imbalance that arise in multiscale phenomena, which are prevalent in applications such as thermal processing, electromagnetics, impact mechanics, and fluid dynamics. The work is presented as a preprint and has not undergone peer review.

**Method**  
The authors introduce an adaptive wavelet-based PINN (AW-PINN) that dynamically adjusts the wavelet basis functions based on the residual and supervised loss during training. This adaptive mechanism allows AW-PINN to effectively manage high-scale features without incurring significant memory overhead. The training process is divided into two stages: an initial short pre-training phase where fixed wavelet bases are used to identify relevant wavelet families, followed by an adaptive refinement phase that modifies scales and translations without requiring high-resolution bases across the entire domain. Notably, AW-PINN does not utilize automatic differentiation for computing derivatives in the loss function, which enhances training speed. The theoretical foundation includes a Gaussian process limit and the derivation of its associated neural tangent kernel (NTK) structure under specific assumptions.

**Results**  
AW-PINN was evaluated on several challenging partial differential equations (PDEs) with localized high-magnitude source terms, exhibiting extreme loss imbalances with ratios as high as \(10^{10}:1\). The benchmarks included transient heat conduction, localized Poisson problems, oscillatory flow equations, and Maxwell equations with a point charge source. AW-PINN consistently outperformed existing methods in its class, demonstrating superior performance metrics across these PDEs, although specific numerical results and comparisons to named baselines were not detailed in the abstract.

**Limitations**  
The authors acknowledge that while AW-PINN effectively addresses loss imbalance and spectral bias, its performance may still be sensitive to the choice of wavelet families and the initial conditions set during the pre-training phase. Additionally, the theoretical guarantees provided are contingent on certain assumptions that may not hold in all practical scenarios. The paper does not discuss the scalability of AW-PINN to higher-dimensional problems or its computational efficiency relative to other state-of-the-art methods in extensive detail.

**Why it matters**  
The development of AW-PINN has significant implications for the field of scientific computing and machine learning, particularly in applications requiring the solution of complex PDEs with localized phenomena. By effectively managing loss imbalance and enhancing training efficiency, AW-PINN could facilitate more accurate and faster simulations in various engineering and physical sciences domains. This work opens avenues for further research into adaptive methods in PINNs and their potential integration with other machine learning frameworks.

Authors: Himanshu Pandey, Ratikanta Behera  
Source: arXiv:2604.28180  
URL: [https://arxiv.org/abs/2604.28180v1](https://arxiv.org/abs/2604.28180v1)
