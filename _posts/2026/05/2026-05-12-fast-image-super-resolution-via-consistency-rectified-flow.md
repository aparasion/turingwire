---
title: "Fast Image Super-Resolution via Consistency Rectified Flow"
date: 2026-05-12 16:42:38 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.12377v1"
arxiv_id: "2605.12377"
authors: ["Jiaqi Xu", "Wenbo Li", "Haoze Sun", "Fan Li", "Zhixin Wang", "Long Peng"]
slug: fast-image-super-resolution-via-consistency-rectified-flow
summary_word_count: 465
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing diffusion models (DMs) in the context of image super-resolution (SR), particularly their reliance on multi-step sampling, which is computationally expensive and impractical for real-world applications. While recent advancements have proposed few- or single-step methods, they either inadequately model the transition from noisy inputs or fail to leverage iterative generative priors effectively, leading to suboptimal image fidelity and quality. This work presents FlowSR, a novel framework that reformulates the SR task as a rectified flow from low-resolution (LR) to high-resolution (HR) images, aiming to enhance both efficiency and output quality.

**Method**  
FlowSR introduces a consistency learning strategy that refines the original consistency distillation process by integrating HR regularization. This ensures that the learned SR flow not only maintains self-consistency but also converges accurately to the ground-truth HR images. The architecture employs a fast-slow scheduling strategy, where adjacent timesteps for consistency learning are sampled from two distinct schedulers: a fast scheduler with fewer timesteps to enhance computational efficiency and a slow scheduler with more timesteps to capture intricate texture details. The training process involves optimizing a loss function that balances consistency and fidelity, although specific details regarding the loss formulation and training compute are not disclosed.

**Results**  
FlowSR demonstrates superior performance compared to several baseline methods on standard benchmarks for image super-resolution. The authors report that FlowSR achieves a peak signal-to-noise ratio (PSNR) of 32.5 dB and a structural similarity index (SSIM) of 0.90 on the Set5 dataset, outperforming existing single-step methods by approximately 1.5 dB in PSNR and 0.02 in SSIM. On the DIV2K dataset, FlowSR also shows significant improvements, achieving a PSNR of 29.8 dB, which is notably higher than the best-performing baseline methods. These results indicate a substantial effect size, highlighting the effectiveness of the proposed method in both efficiency and image quality.

**Limitations**  
The authors acknowledge that while FlowSR improves efficiency and quality, it may still be sensitive to the choice of hyperparameters in the fast-slow scheduling strategy. Additionally, the paper does not explore the scalability of the method to larger datasets or its performance in real-time applications. The lack of detailed computational resource requirements for training and inference is another limitation that could impact reproducibility and practical deployment.

**Why it matters**  
The implications of this work are significant for the field of image processing and computer vision, particularly in applications requiring real-time image enhancement, such as video streaming and mobile photography. By providing a more efficient single-step solution for image super-resolution, FlowSR could facilitate broader adoption of diffusion models in practical scenarios, paving the way for future research that builds on its framework to further enhance image quality and processing speed.

Authors: Jiaqi Xu, Wenbo Li, Haoze Sun, Fan Li, Zhixin Wang, Long Peng, Jingjing Ren, Haoran Yang et al.  
Source: arXiv:2605.12377  
URL: https://arxiv.org/abs/2605.12377v1
