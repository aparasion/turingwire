---
title: "Edge-Efficient Image Restoration: Transformer Distillation into State-Space Models"
date: 2026-05-04 16:35:26 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.02794v1"
arxiv_id: "2605.02794"
authors: ["Srinivas Soumitri Miriyala", "Sowmya Vajrala", "Sravanth Kodavanti", "Vikram Nelvoy Rajendiran", "Sharan Kumar Allur"]
slug: edge-efficient-image-restoration-transformer-distillation-in
summary_word_count: 456
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in efficient image restoration techniques suitable for edge devices, particularly focusing on the limitations of transformer architectures in terms of runtime latency when processing high-resolution images. While transformers excel in global modeling through self-attention mechanisms, their computational demands hinder their deployment on mobile hardware. The authors propose a hybrid framework that combines the strengths of transformers and state-space models (SSMs) to enhance both performance and efficiency. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is a modular framework that integrates transformer and SSM blocks into a hybrid architecture, specifically a U-Net-style design. The authors employ lightweight SSMs as feature-distilled surrogates for transformer blocks, which allows for reduced computational overhead while preserving restoration quality. To optimize the architecture, they introduce Efficient Network Search (ENS), a multi-objective search strategy that identifies effective hybrid configurations tailored to specific restoration tasks. ENS penalizes the use of transformers to minimize latency, enabling the discovery of optimal block combinations without extensive hardware profiling. The training process and specific loss functions are not detailed in the abstract, but the focus is on balancing restoration quality with runtime efficiency.

**Results**  
The proposed hybrid architectures demonstrate significant improvements in inference speed compared to the Restormer baseline, which requires 10,119.52 ms for inference on a Snapdragon 8 Elite CPU. The results for the ENS-discovered hybrids are as follows:  
- ENS-Deblurring: 2,973 ms (3.4x faster than Restormer)  
- ENS-Deraining: 5,816 ms (1.74x faster)  
- ENS-Denoising: 8,666 ms (1.17x faster)  
Despite these reductions in runtime, the hybrid models maintain competitive restoration quality, although specific quantitative metrics (e.g., PSNR, SSIM) are not provided in the abstract.

**Limitations**  
The authors acknowledge that while the hybrid approach improves efficiency, the reliance on SSMs may lead to suboptimal performance on fine-grained restoration tasks compared to full transformer models. Additionally, the ENS methodology may not generalize across all types of image restoration tasks, and the search process could be computationally intensive in itself. The paper does not discuss the potential impact of varying input resolutions or the scalability of the proposed method to other edge devices.

**Why it matters**  
This work has significant implications for the deployment of image restoration algorithms on resource-constrained devices, such as smartphones and IoT devices. By effectively balancing the trade-off between computational efficiency and restoration quality, the proposed hybrid framework could enable real-time image processing applications in various domains, including mobile photography, augmented reality, and remote sensing. The introduction of ENS also opens avenues for further research into automated architecture search in the context of deep learning, particularly for applications requiring low-latency inference.

Authors: Srinivas Soumitri Miriyala, Sowmya Vajrala, Sravanth Kodavanti, Vikram Nelvoy Rajendiran, Sharan Kumar Allur  
Source: arXiv:2605.02794  
URL: [https://arxiv.org/abs/2605.02794v1](https://arxiv.org/abs/2605.02794v1)
