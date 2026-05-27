---
title: "MRT: Masked Region Transformer for Layered Image Generation and Editing at Scale"
date: 2026-05-26 16:16:19 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.27235v1"
arxiv_id: "2605.27235"
authors: ["Zhicong Tang", "Zhao Zhang", "Jingye Chen", "Mohan Zhou", "Yifan Pu", "Yuchi Liu"]
slug: mrt-masked-region-transformer-for-layered-image-generation-a
summary_word_count: 397
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the underexplored area of layered image generation and editing at scale, which is crucial for enabling layer-wise reuse and composition of visual content. The authors present MRT, a preprint work that aims to fill this gap by providing a robust framework for multi-layer transparent image generation and editing, leveraging a large dataset of over 10 million multilingual design samples.

**Method**  
The core technical contribution of MRT is a 20B-parameter masked region diffusion model that integrates three tasks—text-to-layers, image-to-layers, and layers-to-layers—within a unified framework. The model employs selective token masking to facilitate flexible layer-wise generation and editing. A novel component, the overflow-aware canvas layer, is introduced to manage boundary inconsistencies and support semi-transparent background synthesis, allowing for the generation of editable layers that extend beyond the visible canvas. The authors also implement diffusion distillation, enabling real-time multi-layer generation in just 8 steps with minimal quality degradation. The training process utilizes a diverse dataset, although specific training compute details are not disclosed.

**Results**  
MRT demonstrates substantial improvements over existing state-of-the-art methods, including various commercial systems, across all three tasks. Notably, it significantly outperforms the Qwen-Image-Layered model in image-to-layers quality, as evidenced by user study results. The model achieves inference speeds that are 10-100 times faster than competitors while reducing activation GPU memory consumption by 50-90% during image-to-layer inference. These results establish a new benchmark for multi-layer transparent image generation.

**Limitations**  
The authors acknowledge that while MRT excels in layered image generation and editing, it may still face challenges in handling highly complex scenes or intricate layer interactions that were not fully explored in their experiments. Additionally, the reliance on a large dataset may limit the model's generalizability to niche applications or specific artistic styles. The paper does not discuss potential biases in the training data or the implications of using a large model in terms of environmental impact.

**Why it matters**  
The implications of this work are significant for downstream applications in graphic design, content creation, and augmented reality, where layered image manipulation is essential. By establishing a new benchmark in multi-layer image generation, MRT opens avenues for further research into efficient and scalable image editing tools, potentially influencing the development of future generative models that prioritize user interactivity and creative control.

Authors: Zhicong Tang, Zhao Zhang, Jingye Chen, Mohan Zhou, Yifan Pu, Yuchi Liu, Yalong Bai, Ethan Smith et al.  
Source: arXiv:2605.27235  
URL: [https://arxiv.org/abs/2605.27235v1](https://arxiv.org/abs/2605.27235v1)
