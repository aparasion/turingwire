---
title: "AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation"
date: 2026-05-13 16:06:34 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13724v1"
arxiv_id: "2605.13724"
authors: ["Yuchao Gu", "Guian Fang", "Yuxin Jiang", "Weijia Mao", "Song Han", "Han Cai"]
slug: anyflow-any-step-video-diffusion-model-with-on-policy-flow-m
summary_word_count: 440
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing consistency-distilled models in few-step video generation, particularly their performance degradation when increasing the number of sampling steps during inference. The authors highlight that current methods replace the original probability-flow ODE trajectory with a consistency-sampling trajectory, which hampers the scaling behavior desirable for any-step video diffusion. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core contribution of this work is the AnyFlow framework, which introduces a novel approach to video diffusion distillation by optimizing the entire ODE sampling trajectory rather than a fixed number of steps. The authors shift the focus from endpoint consistency mapping (i.e., mapping from latent variable \( z_t \) to \( z_0 \)) to flow-map transition learning (i.e., mapping from \( z_t \) to \( z_r \) over arbitrary time intervals). This is achieved through the proposed Flow Map Backward Simulation technique, which decomposes a full Euler rollout into shortcut flow-map transitions. This method allows for efficient on-policy distillation, effectively reducing test-time errors such as discretization error in few-step sampling and exposure bias in causal generation. The framework is evaluated across various architectures, including both bidirectional and causal models, with parameter scales ranging from 1.3 billion to 14 billion.

**Results**  
Extensive experiments demonstrate that AnyFlow matches or surpasses the performance of consistency-based models in the few-step regime while maintaining scalability with respect to sampling step budgets. Specific performance metrics are not disclosed in the abstract, but the authors indicate that their method achieves significant improvements over baseline models, suggesting a robust enhancement in video generation quality across different sampling scenarios.

**Limitations**  
The authors acknowledge that while AnyFlow improves upon existing methods, it may still be constrained by the inherent challenges of video generation, such as the complexity of modeling long-term dependencies and the potential for artifacts in generated videos. Additionally, the scalability of the method to even larger models or more complex datasets is not fully explored. The paper does not address the computational overhead introduced by the flow-map transition learning process, which could impact practical deployment.

**Why it matters**  
The implications of this work are significant for the field of video generation, particularly in applications requiring flexible sampling strategies. By enabling effective any-step video diffusion, AnyFlow could enhance the usability of generative models in real-time applications, such as video synthesis and interactive media. The framework's ability to maintain performance across varying sampling steps opens avenues for further research into adaptive sampling techniques and more efficient training paradigms in generative modeling.

Authors: Yuchao Gu, Guian Fang, Yuxin Jiang, Weijia Mao, Song Han, Han Cai, Mike Zheng Shou  
Source: arXiv:2605.13724  
URL: https://arxiv.org/abs/2605.13724v1
