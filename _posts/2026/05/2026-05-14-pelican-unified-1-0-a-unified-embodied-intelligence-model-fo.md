---
title: "Pelican-Unified 1.0: A Unified Embodied Intelligence Model for Understanding, Reasoning, Imagination and Action"
date: 2026-05-14 17:50:42 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.15153v1"
arxiv_id: "2605.15153"
authors: ["Yi Zhang", "Yinda Chen", "Che Liu", "Zeyuan Ding", "Jin Xu", "Shilong Zou"]
slug: pelican-unified-1-0-a-unified-embodied-intelligence-model-fo
summary_word_count: 463
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of a unified framework for embodied intelligence that integrates understanding, reasoning, imagination, and action within a single model. Existing approaches typically rely on separate systems for each capability, leading to inefficiencies and suboptimal performance. Pelican-Unified 1.0 is presented as the first embodied foundation model trained under the principle of unification, aiming to bridge this gap. The work is a preprint and has not yet undergone peer review.

**Method**  
Pelican-Unified 1.0 employs a single Vision-Language Model (VLM) that serves as both a unified understanding and reasoning module. The architecture maps scenes, instructions, visual contexts, and action histories into a shared semantic space. It utilizes an autoregressive approach to generate task-, action-, and future-oriented thought chains in a single forward pass, projecting the final hidden state into a dense latent variable. The Unified Future Generator (UFG) conditions on this latent variable to jointly produce future videos and actions through modality-specific output heads, all within a denoising framework. The model optimizes three loss functions—language, video, and action—backpropagating them into the shared representation, thus enabling simultaneous training of all capabilities rather than treating them as isolated expert systems.

**Results**  
Pelican-Unified 1.0 demonstrates superior performance across multiple benchmarks. It achieves a score of 64.7 on eight VLM benchmarks, outperforming comparable-scale models. On the WorldArena benchmark, it scores 66.03, securing the top rank. Additionally, it achieves a score of 93.5 on RoboTwin, marking it as the second-best average among the compared action methods. These results indicate that the unified approach effectively maintains the strengths of specialized models while integrating multiple capabilities into a single framework.

**Limitations**  
The authors acknowledge that while the unified model shows strong performance, it may still face challenges in scalability and generalization to more complex tasks that require deeper specialization. They do not address potential issues related to the computational efficiency of training such a large model or the implications of the denoising process on the quality of generated outputs. Furthermore, the reliance on a single VLM may limit the model's adaptability to diverse tasks that could benefit from specialized architectures.

**Why it matters**  
The implications of Pelican-Unified 1.0 are significant for the field of embodied intelligence. By demonstrating that a unified model can achieve high performance across multiple capabilities, this work paves the way for future research into integrated systems that can handle complex tasks more efficiently. It challenges the prevailing notion that specialization is necessary for optimal performance, suggesting that unification may lead to more versatile and capable AI systems. This could influence the design of future models in robotics, interactive AI, and other domains requiring a synthesis of understanding, reasoning, imagination, and action.

Authors: Yi Zhang, Yinda Chen, Che Liu, Zeyuan Ding, Jin Xu, Shilong Zou, Junwei Liao, Jiayu Hu et al.  
Source: arXiv:2605.15153  
URL: [https://arxiv.org/abs/2605.15153v1](https://arxiv.org/abs/2605.15153v1)
