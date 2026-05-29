---
title: "VPG: Visual Prefix Guidance for Autoregressive Image and Video Generation"
date: 2026-05-28 17:55:06 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.30317v1"
arxiv_id: "2605.30317"
authors: ["Xinyao Liao", "Qiyuan He", "Yicong Li", "Jiayin Zhu", "Xiaoye Qu", "Wei Wei"]
slug: vpg-visual-prefix-guidance-for-autoregressive-image-and-vide
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of autoregressive image and video generation models, specifically the issues of exposure bias and prefix drift that arise during inference. These models are typically trained using teacher-forced histories, which do not reflect the sampling process during inference where they must rely on their own generated prefixes. Existing solutions either modify the training process or apply external semantic guidance (e.g., class labels or text prompts) without adequately ensuring that the next-step predictions reinforce the generated prefix. This work presents a novel approach, Visual Prefix Guidance (VPG), as a training-free inference-time method to enhance the quality of predictions.

**Method**  
VPG operates by contrasting the model's output when conditioned on the generated prefix against its output when conditioned on a corrupted version of that prefix. This contrastive approach allows the model to identify and amplify logits that provide stronger posterior support for the generated prefix. The method does not require any retraining of the base model, making it computationally efficient. The authors evaluate VPG across various tasks, including class-conditional image generation with the VAR model, text-to-image generation with Infinity, and text-to-video generation with InfinityStar. The implementation details regarding the architecture and specific training compute are not disclosed, but the focus remains on the inference-time application of VPG.

**Results**  
VPG demonstrates significant improvements in generation quality across multiple benchmarks. Specifically, it achieves an average reduction in Fréchet Inception Distance (FID) of 0.36 on the VAR dataset. Additionally, VPG enhances performance metrics on both image and video generation tasks when compared to baseline models. The paper does not provide specific numerical results for all benchmarks, but the qualitative improvements suggest a robust enhancement in the generated outputs.

**Limitations**  
The authors acknowledge that VPG is a training-free method, which may limit its applicability in scenarios where model retraining could yield better performance. They do not address potential limitations related to the generalizability of VPG across different model architectures or datasets beyond those tested. Furthermore, the reliance on the quality of the corrupted prefix could introduce variability in performance, which is not explored in depth.

**Why it matters**  
The introduction of VPG has significant implications for the field of generative modeling, particularly in mitigating common issues associated with autoregressive models. By providing a method that enhances inference without the need for retraining, VPG opens avenues for more robust and efficient generation processes. This could lead to advancements in applications requiring high-quality image and video synthesis, such as content creation, virtual reality, and interactive media. The approach also sets a precedent for future research to explore inference-time enhancements that do not necessitate extensive retraining, potentially accelerating the deployment of generative models in real-world applications.

Authors: Xinyao Liao, Qiyuan He, Yicong Li, Jiayin Zhu, Xiaoye Qu, Wei Wei, Angela Yao  
Source: arXiv:2605.30317  
URL: [https://arxiv.org/abs/2605.30317v1](https://arxiv.org/abs/2605.30317v1)
