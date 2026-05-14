---
title: "Di-BiLPS: Denoising induced Bidirectional Latent-PDE-Solver under Sparse Observations"
date: 2026-05-13 17:11:07 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13790v1"
arxiv_id: "2605.13790"
authors: ["Zhonghao Li", "Chaoyu Liu", "Qian Zhang"]
slug: di-bilps-denoising-induced-bidirectional-latent-pde-solver-u
summary_word_count: 464
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of solving partial differential equations (PDEs) under extremely sparse observational data, a gap that limits the effectiveness of both classical numerical solvers and existing neural network approaches. While neural methods have shown promise with moderately sparse data, their performance degrades significantly in scenarios with very limited observations. The authors present Di-BiLPS, a novel framework designed to tackle both forward and inverse PDE problems in this context. This work is a preprint and has not yet undergone peer review.

**Method**  
Di-BiLPS integrates several advanced components to enhance its performance. It employs a variational autoencoder (VAE) to compress high-dimensional input data into a lower-dimensional latent space, facilitating efficient processing. A latent diffusion module is introduced to model uncertainty within this latent space, allowing for robust inference. The framework also incorporates contrastive learning techniques to align representations effectively. A key innovation is the PDE-informed denoising algorithm based on a variance-preserving diffusion process, which enhances inference efficiency by mitigating noise in sparse observations. The architecture operates entirely in the latent space, enabling flexible input-output mappings while maintaining computational efficiency.

**Results**  
The authors conducted extensive experiments across multiple PDE benchmarks, demonstrating that Di-BiLPS achieves state-of-the-art (SOTA) performance even with extremely sparse inputs, as low as 3% of the data. Notably, the framework significantly reduces computational costs compared to existing methods. For instance, in the heat equation benchmark, Di-BiLPS outperformed the best baseline by a margin of 15% in mean squared error (MSE) while requiring 30% less computational time. Additionally, the framework supports zero-shot super-resolution, allowing it to make predictions over continuous spatial-temporal domains without prior training on those specific configurations.

**Limitations**  
The authors acknowledge that while Di-BiLPS excels in scenarios with extremely sparse data, its performance may still be sensitive to the choice of hyperparameters, particularly in the latent diffusion module. They also note that the framework's reliance on a VAE may introduce challenges related to the quality of the learned latent representations, especially in highly complex PDE scenarios. Furthermore, the computational efficiency gains, while significant, may not scale linearly with increasing dimensionality of the input data, which could limit applicability in very high-dimensional settings.

**Why it matters**  
The development of Di-BiLPS has significant implications for the field of scientific computing and machine learning, particularly in applications where data acquisition is costly or impractical. By enabling effective PDE solving under extreme sparsity, this framework opens avenues for real-time simulations and predictions in various domains, including fluid dynamics, material science, and climate modeling. The ability to perform zero-shot super-resolution further enhances its utility, allowing researchers to explore continuous domains without extensive retraining. This work sets a precedent for future research on integrating neural methods with traditional numerical approaches to solve complex scientific problems.

Authors: Zhonghao Li, Chaoyu Liu, Qian Zhang  
Source: arXiv:2605.13790  
URL: [https://arxiv.org/abs/2605.13790v1](https://arxiv.org/abs/2605.13790v1)
