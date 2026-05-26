---
title: "Everything at Every Scale: Scale-Invariant Diffusion with Continuous Super-Resolution"
date: 2026-05-25 17:01:21 +0000
category: research
subcategory: efficiency_inference
company: "null"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26032v1"
arxiv_id: "2605.26032"
authors: ["Zixin Jessie Chen", "Zhuo Chen", "Archer Wang", "Jeff Gore", "William T. Freeman", "Congyue Deng"]
slug: everything-at-every-scale-scale-invariant-diffusion-with-con
summary_word_count: 427
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the integration of image generation and super-resolution tasks within a unified framework. Traditional approaches often require distinct architectures and retraining for different scales, which limits efficiency and scalability. The authors propose a novel model that leverages scale invariance to unify these tasks, thereby simplifying the process of generating high-quality images from noise and reconstructing fine details from coarse inputs.

**Method**  
The core technical contribution is the SKILD (Scale-invariant K-Space Image Learning Diffusion) model, which employs a diffusion process that explicitly incorporates scale as a coordinate in its dynamics. The forward process systematically attenuates image content from fine to coarse scales while injecting spectrum-matched Gaussian noise. The reverse process, trained on this framework, is capable of performing both image generation and continuous super-resolution without the need for task-specific architectures, conditioning branches, classifier-free guidance, or retraining for different scale factors. The model operates on a single unconditional checkpoint, which enhances its versatility and efficiency.

**Results**  
SKILD achieves a Fréchet Inception Distance (FID) of 2.65 and an Inception Score of 9.63 on the unconditional CIFAR-10 benchmark, outperforming existing models. For super-resolution tasks on ImageNet, it demonstrates performance improvements of 2× to 8×, surpassing conditional models across various perceptual metrics. Additionally, the model successfully reconstructs critical Ising models, with connected four-point correlations closely tracking ground truth values, indicating its effectiveness in handling complex physical systems.

**Limitations**  
The authors acknowledge that while SKILD unifies generation and super-resolution, it may still be limited by the quality of the training data and the inherent challenges of diffusion models, such as computational efficiency during inference. They do not address potential issues related to the model's performance on highly diverse datasets or its generalizability to other domains outside of image processing. Furthermore, the reliance on a single unconditional checkpoint may limit the model's adaptability to specific tasks that could benefit from tailored architectures.

**Why it matters**  
The implications of this work are significant for downstream applications in computer vision and generative modeling. By providing a unified framework for image generation and super-resolution, SKILD simplifies the workflow for practitioners and researchers, potentially accelerating advancements in related fields. The model's ability to operate across scales without retraining could lead to more efficient deployment in real-world applications, such as image enhancement in medical imaging, satellite imagery, and other domains where high-resolution reconstructions are critical. This research paves the way for further exploration of scale-invariant approaches in machine learning.

Authors: Zixin Jessie Chen, Zhuo Chen, Archer Wang, Jeff Gore, William T. Freeman, Congyue Deng, Marin Soljačić  
Source: arXiv:2605.26032  
URL: [https://arxiv.org/abs/2605.26032v1](https://arxiv.org/abs/2605.26032v1)
