---
title: "One-Step Distillation of Discrete Diffusion Image Generators via Fixed-Point Iteration"
date: 2026-05-20 17:59:10 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.21484v1"
arxiv_id: "2605.21484"
authors: ["Chaoyang Wang", "Yunhai Tong"]
slug: one-step-distillation-of-discrete-diffusion-image-generators
summary_word_count: 444
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in discrete diffusion models, which are known for their high-quality visual synthesis but suffer from slow, iterative decoding processes. Existing single-step distillation methods either require auxiliary score networks that effectively double the computational load or utilize complex parameterizations and multi-stage pipelines that complicate optimization. The authors propose a novel approach, Fixed-Point Distillation (FPD), to streamline this process. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core contribution of this paper is the Fixed-Point Distillation (FPD) framework, which enables end-to-end training of discrete diffusion models. FPD constructs local correction targets by partially corrupting the student's one-step draft and refining it with a single step from the teacher model. The authors introduce a multi-bandwidth drift loss that operates in a continuous feature space, allowing for the accumulation of corrections iteratively. To facilitate backpropagation through the discrete bottleneck, a straight-through estimator is employed, which allows the model to use hard-sampled tokens during the forward pass while routing continuous gradients back to the student logits. This ensures that both training and inference utilize the same codebook manifold. Additionally, an optional unconditional adversarial objective can be incorporated to enhance perceptual realism.

**Results**  
FPD demonstrates competitive performance in visual fidelity and structural alignment compared to multi-step teacher models, achieving significant improvements over existing discrete distillation baselines. The authors report that FPD narrows the performance gap to multi-step teachers while maintaining a single inference step. Specific quantitative results include improvements in metrics such as FID (Fréchet Inception Distance) and IS (Inception Score), although exact numbers and baseline comparisons are not detailed in the abstract. The evaluations encompass both class-conditional and text-conditional generation tasks, showcasing the versatility of the proposed method.

**Limitations**  
The authors acknowledge that while FPD improves upon existing methods, it may still be limited by the inherent challenges of discrete token representation and the potential for information loss during the corruption and refinement process. They do not discuss the scalability of the method to larger models or datasets, nor do they address the computational overhead introduced by the optional adversarial objective. Additionally, the reliance on a straight-through estimator may introduce biases that could affect gradient flow.

**Why it matters**  
The implications of this work are significant for the field of generative modeling, particularly in enhancing the efficiency of discrete diffusion models. By enabling single-step distillation without sacrificing visual quality, FPD could facilitate real-time applications of generative models in various domains, including image synthesis and editing. This approach may also inspire further research into optimizing other generative frameworks, potentially leading to more efficient architectures and training methodologies.

Authors: Chaoyang Wang, Yunhai Tong  
Source: arXiv:2605.21484  
URL: [https://arxiv.org/abs/2605.21484v1](https://arxiv.org/abs/2605.21484v1)
