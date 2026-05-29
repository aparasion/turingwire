---
title: "VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion"
date: 2026-05-28 17:59:57 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30351v1"
arxiv_id: "2605.30351"
authors: ["Hidir Yesiltepe", "Jiazhen Hu", "Tuna Han Salih Meral", "Adil Kaan Akan", "Kaan Oktay", "Hoda Eldardiry"]
slug: videomla-low-rank-latent-kv-cache-for-minute-scale-autoregre
summary_word_count: 471
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing causal video diffusion models that utilize a fixed-size sliding-window key-value (KV) cache. While recent advancements have focused on optimizing token selection and positional encoding within this framework, the per-head KV layout—significantly impacting memory usage and latency—has remained largely unchanged. The authors present a novel approach, Multi-Head Latent Attention (MLA), to improve the efficiency of KV caching in video diffusion. This work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this paper is the introduction of the Multi-Head Latent Attention (MLA) mechanism, which substitutes the traditional per-head keys and values with a shared low-rank content latent representation and a decoupled 3D-RoPE positional key. This architecture reduces the per-token KV memory usage by 92.7% across all cached layers. The authors explore the effectiveness of MLA in video diffusion, noting that the spectral assumptions typically applied in language models do not hold for video data, where pretrained video attention exhibits a high effective rank. Despite this, VideoMLA maintains quality at high compression ratios, where traditional spectral approximations would predict significant reconstruction errors. The authors argue that the MLA bottleneck, rather than the pretrained spectrum, dictates the effective rank, with both spectral and random initializations utilizing nearly the full rank budget from the outset, and training effectively adapts within this budget.

**Results**  
On the VBench benchmark, VideoMLA demonstrates competitive performance, matching short-horizon streaming video diffusion baselines. Notably, it achieves the highest overall score for long-horizon tasks among the evaluated methods. Additionally, VideoMLA improves throughput by 1.23x on a single B200 compared to existing approaches. These results indicate that the proposed method not only enhances memory efficiency but also maintains or improves performance metrics across various temporal horizons.

**Limitations**  
The authors acknowledge that while VideoMLA shows promise, it operates under the assumption that the latent representation can effectively capture the necessary information for video diffusion, which may not hold universally across all video datasets. They do not address potential limitations related to the generalizability of the model to diverse video types or the implications of the low-rank assumption in different contexts. Furthermore, the reliance on a specific architecture may limit flexibility in adapting to other diffusion tasks.

**Why it matters**  
The introduction of VideoMLA has significant implications for the field of video generation and diffusion, particularly in scenarios requiring efficient memory usage and low latency. By demonstrating that a low-rank latent representation can effectively replace traditional per-head KV caches, this work opens avenues for further research into optimizing attention mechanisms in video processing. The findings could influence the design of future models, potentially leading to more scalable and efficient video generation systems that can operate in real-time applications.

Authors: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag  
Source: arXiv:2605.30351  
URL: [https://arxiv.org/abs/2605.30351v1](https://arxiv.org/abs/2605.30351v1)
