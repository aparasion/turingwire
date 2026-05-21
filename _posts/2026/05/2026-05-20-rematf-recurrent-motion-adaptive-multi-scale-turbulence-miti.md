---
title: "ReMATF: Recurrent Motion-Adaptive Multi-scale Turbulence Mitigation for Dynamic Scenes"
date: 2026-05-20 17:28:49 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.21440v1"
arxiv_id: "2605.21440"
authors: ["Zhiming Liu", "Zhicheng Zou", "Nantheera Anantrasirichai"]
slug: rematf-recurrent-motion-adaptive-multi-scale-turbulence-miti
summary_word_count: 453
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of atmospheric turbulence in video sequences, which introduces distortions such as geometric warping, blur, and temporal flickering. These distortions significantly degrade visual quality and temporal consistency, complicating tasks in computer vision and video processing. Existing state-of-the-art methods predominantly utilize transformer and 3D architectures that require multi-frame inputs, leading to high computational costs and memory usage. This work presents ReMATF, a lightweight solution that operates effectively with only two frames, making it particularly relevant for real-time applications in resource-constrained environments. Notably, this is a preprint and has not yet undergone peer review.

**Method**  
ReMATF employs a recurrent architecture that integrates a multi-scale encoder-decoder framework with a motion-adaptive temporal fusion module. The encoder-decoder processes the input frames to extract spatial features at multiple scales, while the temporal fusion module performs per-pixel fusion between the warped previous output and the current frame prediction. This design allows for enhanced temporal coherence without the need for an expanded temporal window, effectively mitigating flicker and improving detail sharpness. The model's lightweight nature is achieved by limiting the input to two frames, which reduces the overall computational burden. The authors do not disclose specific training compute or dataset sizes, but they evaluate the model on both synthetic and real turbulence datasets.

**Results**  
ReMATF demonstrates significant performance improvements over existing multi-frame transformer baselines. The model achieves higher Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index Measure (SSIM) scores, alongside improved perceptual quality as measured by the Learned Perceptual Image Patch Similarity (LPIPS) metric. The paper reports that ReMATF not only enhances visual quality but also provides substantially faster inference times, making it a viable option for real-time turbulence mitigation. Specific numerical results are not provided in the abstract, but the qualitative improvements are emphasized.

**Limitations**  
The authors acknowledge that while ReMATF is effective for turbulence mitigation, it may not generalize well to all types of video distortions beyond atmospheric turbulence. Additionally, the reliance on only two frames may limit performance in scenarios where more temporal context is beneficial. The paper does not discuss potential limitations related to the model's robustness against varying levels of turbulence intensity or its performance on diverse video content types.

**Why it matters**  
The development of ReMATF has significant implications for real-time video processing applications, particularly in fields such as surveillance, autonomous driving, and remote sensing, where maintaining visual clarity under adverse conditions is crucial. By providing a lightweight and efficient solution for turbulence mitigation, this work opens avenues for further research into adaptive video restoration techniques that balance performance and computational efficiency. The approach could also inspire future architectures that leverage recurrent mechanisms for other types of temporal distortions.

Authors: Zhiming Liu, Zhicheng Zou, Nantheera Anantrasirichai  
Source: arXiv:2605.21440  
URL: https://arxiv.org/abs/2605.21440v1
