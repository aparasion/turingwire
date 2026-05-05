---
title: "Active Sampling for Ultra-Low-Bit-Rate Video Compression via Conditional Controlled Diffusion"
date: 2026-05-04 17:25:14 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.02849v1"
arxiv_id: "2605.02849"
authors: ["Amirhosein Javadi", "Shirin Saeedi Bidokhti", "Tara Javidi"]
slug: active-sampling-for-ultra-low-bit-rate-video-compression-via
summary_word_count: 383
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of video compression at ultra-low bitrates, a critical gap in the literature where existing methods often fail to maintain perceptual quality under severe rate constraints. The authors propose a novel approach, ActDiff-VC, which leverages diffusion models to enhance video compression efficiency. Notably, this work is presented as a preprint and has not undergone peer review.

**Method**  
ActDiff-VC employs a conditional diffusion model for video compression, partitioning videos into variable-length segments. The framework selectively transmits keyframes based on content, utilizing a mechanism for content-adaptive keyframe selection. Additionally, it incorporates budget-aware sparse trajectory selection to summarize temporal dynamics through a compact set of tracked point trajectories. The conditional diffusion decoder synthesizes the remaining frames based on these sparse signals, enabling perceptually realistic reconstructions. The architecture's training details, including compute requirements, are not disclosed, but the focus on conditioning signals is a key technical contribution.

**Results**  
The authors evaluate ActDiff-VC on the UVG and MCL-JCV benchmarks, reporting significant performance improvements over established learned codecs. Specifically, ActDiff-VC achieves up to 64.6% bitrate reduction while maintaining matched NIQE scores. Furthermore, it improves Kernel Inception Distance (KID) by up to 64.6% and Fréchet Inception Distance (FID) by up to 37.7% at comparable bitrates. These results indicate a favorable perceptual rate-distortion trade-off, outperforming both learned and diffusion-based baselines in the ultra-low-bitrate regime.

**Limitations**  
The authors acknowledge that the reliance on keyframe selection and sparse trajectory representation may limit the method's applicability in scenarios with highly dynamic content. Additionally, the performance metrics are primarily focused on perceptual quality, and the computational efficiency of the proposed method in real-time applications is not thoroughly examined. The lack of peer review may also imply that the findings should be interpreted with caution until validated by the community.

**Why it matters**  
The implications of this work are significant for the field of video compression, particularly in applications where bandwidth is severely constrained, such as mobile streaming and IoT devices. By demonstrating that diffusion models can be effectively utilized for ultra-low-bitrate video compression, this research opens avenues for further exploration of generative models in practical compression scenarios. The proposed mechanisms for keyframe and trajectory selection could inspire future work on adaptive compression techniques that balance quality and efficiency.

Authors: Amirhosein Javadi, Shirin Saeedi Bidokhti, Tara Javidi  
Source: arXiv:2605.02849  
URL: [https://arxiv.org/abs/2605.02849v1](https://arxiv.org/abs/2605.02849v1)
