---
title: "LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation"
date: 2026-05-18 17:57:03 +0000
category: research
subcategory: efficiency_inference
company: "NVIDIA"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.18739v1"
arxiv_id: "2605.18739"
authors: ["Yukang Chen", "Luozhou Wang", "Wei Huang", "Shuai Yang", "Bohan Zhang", "Yicheng Xiao"]
slug: longlive-2-0-an-nvfp4-parallel-infrastructure-for-long-video
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
The paper presents LongLive-2.0, addressing the limitations in speed and memory efficiency in long video generation tasks. Existing methods, particularly those in the Self-Forcing series, rely on ODE initialization and distribution matching distillation (DMD), which can be inefficient for long sequences. This work is a preprint and has not undergone peer review.

**Method**  
LongLive-2.0 introduces a novel NVFP4-based parallel infrastructure that optimizes both training and inference workflows. The core technical contribution is the sequence-parallel autoregressive (AR) training method, termed Balanced SP. This method co-designs an efficient teacher-forcing layout by pairing clean-history and noisy-target temporal chunks across ranks, facilitating a SP-aware chunked VAE encoding. The use of NVFP4 precision significantly reduces GPU memory costs and accelerates General Matrix Multiplication (GEMM) computations, which become increasingly critical as video length increases. The architecture allows for a direct tuning of a diffusion model into a long, multi-shot, interactive AR diffusion model, which can be adapted for real-time generation with reduced denoising steps using standalone LoRA weights. For inference, the system employs W4A4 NVFP4 quantization on Blackwell GPUs, optimizing the KV cache for memory efficiency and enhancing throughput via asynchronous streaming VAE decoding. On non-Blackwell architectures, SP inference is utilized to maintain competitive speeds.

**Results**  
LongLive-2.0 demonstrates significant performance improvements, achieving up to 2.15x speedup in training and 1.84x in inference compared to baseline methods. The LongLive-2.0-5B model achieves an impressive 45.7 frames per second (FPS) during inference while maintaining strong performance on benchmark datasets, although specific benchmark names and comparative metrics are not detailed in the abstract.

**Limitations**  
The authors acknowledge that the reliance on NVFP4 may limit applicability to specific GPU architectures, particularly Blackwell GPUs. Additionally, the paper does not address potential challenges in generalizing the method to other types of video generation tasks or the scalability of the approach beyond the tested configurations. The lack of peer review may also imply that the findings should be interpreted with caution until validated by the community.

**Why it matters**  
The implications of LongLive-2.0 are significant for the field of long video generation, particularly in enhancing the efficiency of training and inference processes. By addressing memory and speed bottlenecks, this work paves the way for more scalable and practical applications of video generation models in real-time scenarios. The introduction of a robust infrastructure and training methodology could inspire further research into optimizing generative models for long sequences, potentially influencing downstream applications in areas such as content creation, virtual reality, and interactive media.

Authors: Yukang Chen, Luozhou Wang, Wei Huang, Shuai Yang, Bohan Zhang, Yicheng Xiao, Ruihang Chu, Weian Mao et al.  
Source: arXiv:2605.18739  
URL: https://arxiv.org/abs/2605.18739v1
