---
title: "PARE: Pruning and Adaptive Routing for Efficient Video Generation"
date: 2026-05-26 17:43:25 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.27336v1"
arxiv_id: "2605.27336"
authors: ["Yutong Wang", "Yunke Wang", "Tianfan Xue", "Yu Qiao", "Yaohui Wang", "Xinyuan Chen"]
slug: pare-pruning-and-adaptive-routing-for-efficient-video-genera
summary_word_count: 468
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in Video Diffusion Transformers (DiTs), which are known for generating high-quality videos but require significant computational resources due to their extensive architectures and iterative sampling processes. Existing methods have attempted to mitigate these costs by compressing model width, depth, or sampling steps; however, they typically employ a static architecture that lacks adaptability to varying inputs or denoising stages. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce PARE (Pruning and Adaptive Routing for Efficient video generation), which innovatively combines structure-aware pruning and input-adaptive routing to optimize both width and depth of DiTs. For width reduction, they analyze the specialization of attention heads into spatial and temporal roles, developing an importance scoring mechanism that prioritizes the retention of motion-critical temporal heads during pruning. For depth reduction, PARE employs a lightweight router that is conditioned on both the denoising timestep and the visual content, allowing for dynamic selection of which transformer blocks to execute at each timestep. This approach enables per-input computational adaptation rather than relying on a fixed block removal strategy. The training process involves a progressive pipeline where initial width-pruned quality is recovered through distillation, followed by joint optimization of the student model and the router to decouple the learning objectives.

**Results**  
PARE was evaluated on the Wan2.1-14B benchmark for both image-to-video and text-to-video generation tasks. The results demonstrate that PARE significantly reduces per-step computation while maintaining high-quality outputs across various VBench dimensions. Specifically, the method achieves a reduction in computational cost by up to 50% compared to baseline DiTs, while preserving video quality metrics such as FID and PSNR. Additionally, when combined with step distillation, PARE further accelerates the generation process, showcasing its effectiveness in enhancing efficiency without compromising quality.

**Limitations**  
The authors acknowledge that the performance of PARE may vary depending on the specific characteristics of the input data and the complexity of the video generation task. They also note that the reliance on a lightweight router introduces an additional layer of complexity that may require careful tuning. An obvious limitation not discussed is the potential impact of pruning on the model's generalization capabilities, particularly in scenarios with diverse or unseen input distributions.

**Why it matters**  
The implications of PARE are significant for the field of video generation, as it presents a novel approach to optimizing computational efficiency in DiTs without sacrificing output quality. This work paves the way for future research on adaptive architectures that can dynamically adjust to input characteristics, potentially leading to more scalable and resource-efficient video generation systems. Furthermore, the techniques developed in PARE could be applicable to other domains within deep learning where model efficiency is critical.

Authors: Yutong Wang, Yunke Wang, Tianfan Xue, Yu Qiao, Yaohui Wang, Xinyuan Chen, Chang Xu  
Source: arXiv:2605.27336  
URL: [https://arxiv.org/abs/2605.27336v1](https://arxiv.org/abs/2605.27336v1)
