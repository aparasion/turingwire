---
title: "Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation"
date: 2026-05-05 15:15:30 +0000
category: research
subcategory: efficiency_inference
company: "Perplexity"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.03849v1"
arxiv_id: "2605.03849"
authors: ["Bin Wu", "Mengqi Huang", "Shaojin Wu", "Weinan Jia", "Yuxin Wang", "Zhendong Mao"]
slug: stream-r1-reliability-perplexity-aware-reward-distillation-f
summary_word_count: 466
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing distillation methods in autoregressive streaming video diffusion models, specifically focusing on Distribution Matching Distillation (DMD). The authors argue that current approaches treat all rollouts, frames, and pixels as equally reliable, which constrains the quality of the distilled output. They identify two critical axes of variance that are overlooked: Inter-Reliability, which pertains to the reliability of supervision across different student rollouts, and Intra-Perplexity, which concerns the varying contributions of spatial regions and temporal frames to overall quality. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose Stream-R1, a Reliability-Perplexity Aware Reward Distillation framework that adaptively reweights the distillation objective at both the rollout and spatiotemporal levels. The method employs a shared reward-guided mechanism to achieve this. At the Inter-Reliability level, the loss for each rollout is rescaled using an exponential function of a pretrained video reward score, ensuring that rollouts with more reliable supervision have a greater influence on optimization. For the Intra-Perplexity level, the reward model is back-propagated to derive per-pixel gradient saliency, which is then used to assign spatial and temporal weights. This allows the model to focus optimization efforts on regions and frames that are expected to yield the most significant quality improvements. An adaptive balancing mechanism is also integrated to ensure that no single quality axis—visual quality, motion quality, or text alignment—dominates the optimization process.

**Results**  
Stream-R1 demonstrates consistent improvements over existing distillation baselines across multiple dimensions of video generation quality. The authors report enhanced performance on standard streaming video generation benchmarks, although specific numerical results and effect sizes are not detailed in the abstract. The improvements are achieved without any modifications to the underlying architecture or additional inference costs, indicating the efficiency of the proposed method.

**Limitations**  
The authors acknowledge that their approach relies on the quality of the pretrained video reward model, which may introduce biases if the model is not sufficiently robust. Additionally, the paper does not address the potential computational overhead associated with the adaptive reweighting mechanism, which could impact scalability in real-world applications. Another limitation not discussed is the generalizability of the method across different types of video content or genres, which may vary in complexity and dynamics.

**Why it matters**  
The implications of Stream-R1 are significant for the field of video generation, particularly in enhancing the quality of outputs from autoregressive models. By addressing the shortcomings of existing distillation techniques, this work paves the way for more reliable and efficient streaming video generation. The adaptive reweighting strategy could be applied to other generative tasks, potentially leading to broader advancements in model training and performance optimization across various domains in machine learning.

Authors: Bin Wu, Mengqi Huang, Shaojin Wu, Weinan Jia, Yuxin Wang, Zhendong Mao, Yongdong Zhang  
Source: arXiv:2605.03849  
URL: [https://arxiv.org/abs/2605.03849v1](https://arxiv.org/abs/2605.03849v1)
