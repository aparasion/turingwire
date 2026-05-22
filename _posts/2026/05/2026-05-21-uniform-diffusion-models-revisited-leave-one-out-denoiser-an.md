---
title: "Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State Reformulation"
date: 2026-05-21 17:27:19 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.22765v1"
arxiv_id: "2605.22765"
authors: ["Samson Gourevitch", "Yazid Janati", "Dario Shariatian", "Umut Simsekli", "Eric Moulines", "Eric P. Xing"]
slug: uniform-diffusion-models-revisited-leave-one-out-denoiser-an
summary_word_count: 416
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of Uniform Diffusion Models (UDM) in the context of discrete diffusion processes, particularly the mismatch between the standard plug-in bridge parameterization and the denoising posterior. The authors highlight that while Masked Diffusion Models (MDM) align the prediction and reverse dynamics, UDMs do not, leading to suboptimal performance. This work aims to refine the training objectives and parameterization of UDMs to enhance their generative capabilities.

**Method**  
The core technical contribution is the introduction of a leave-one-out (LOO) denoising posterior, which predicts each clean token without utilizing its corresponding noisy observation. This approach reveals that the conventional plug-in Evidence Lower Bound (ELBO) is not optimized for UDMs. The authors derive exact conversions between the denoiser, the LOO posterior, and the score function, allowing for a clearer separation of parameterization and training objectives. Additionally, they propose an absorbing-state reformulation of UDMs that maintains the joint law while enabling simpler denoising posteriors and a natural remasking mechanism. The training process leverages these insights to improve inference through an informed predictor-corrector sampler and enhanced temperature sampling based on the LOO predictor.

**Results**  
The authors report that the leave-one-out parameterization consistently improves UDM generation across various language modeling tasks. Specifically, they demonstrate that the absorbing-state construction either matches or surpasses the performance of MDMs on standard benchmarks. While exact numerical results are not disclosed in the abstract, the improvements suggest a significant effect size, indicating that the empirical gap between masked and uniform diffusion is primarily influenced by parameterization and sampling design rather than the choice of marginals.

**Limitations**  
The authors acknowledge that their findings are based on theoretical derivations and empirical evaluations that may not cover all potential scenarios in practical applications. They do not address the computational overhead introduced by the LOO approach or the absorbing-state reformulation, which may affect scalability. Additionally, the generalizability of their results to other domains beyond language modeling remains unexamined.

**Why it matters**  
This work has significant implications for the design and optimization of diffusion models in generative tasks. By clarifying the relationship between parameterization and training objectives, it opens avenues for more effective model architectures that can leverage the strengths of both UDMs and MDMs. The insights gained from the LOO denoising posterior and the absorbing-state reformulation could lead to advancements in generative modeling techniques, potentially influencing future research in areas such as natural language processing and beyond.

Authors: Samson Gourevitch, Yazid Janati, Dario Shariatian, Umut Simsekli, Eric Moulines, Eric P. Xing, Alain Durmus  
Source: arXiv:2605.22765  
URL: [https://arxiv.org/abs/2605.22765v1](https://arxiv.org/abs/2605.22765v1)
