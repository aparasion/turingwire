---
title: "LoKA: Low-precision Kernel Applications for Recommendation Models At Scale"
date: 2026-05-11 17:32:29 +0000
category: research
subcategory: efficiency_inference
company: "null"
secondary_companies: ["NVIDIA"]
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10886v1"
arxiv_id: "2605.10886"
authors: ["Liang Luo", "Yinbin Ma", "Quanyu Zhu", "Vasiliy Kuznetsov", "Yuxin Chen", "Jian Jiao"]
slug: loka-low-precision-kernel-applications-for-recommendation-mo
summary_word_count: 514
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limited adoption of low-precision arithmetic, specifically FP8, in large recommendation models (LRMs), despite its successful application in large language models (LLMs). The authors highlight that LRMs are numerically sensitive due to their reliance on small matrix multiplications (GEMMs) and normalization processes, which can lead to degraded model quality and extended training times when FP8 is applied directly. The challenges faced by LRMs necessitate a system-model co-design approach rather than merely improving FP8 kernels. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce LoKA (Low-precision Kernel Applications), a framework designed to make FP8 practical for LRMs through three core components:  
1. **LoKA Probe**: A statistically grounded online benchmarking method that profiles activation and weight statistics to quantify per-layer errors. This component identifies safe and unsafe regions for FP8 adoption, as well as fast and slow execution sites.  
2. **LoKA Mods**: A collection of reusable model adaptations that enhance numerical stability and execution efficiency when using FP8. These modifications are designed to work seamlessly with the existing architecture of LRMs.  
3. **LoKA Dispatch**: A runtime system that utilizes insights from LoKA Probe to dynamically select the most efficient FP8 kernel that meets the specified accuracy requirements during execution.  

The framework emphasizes a co-design approach, integrating model components with hardware capabilities to optimize performance while maintaining model integrity.

**Results**  
The authors demonstrate that LoKA significantly improves the performance of LRMs when using FP8. In experiments, they report a reduction in training time by up to 30% compared to traditional FP32 implementations while maintaining accuracy levels within 1% of baseline models. Specifically, on the MovieLens dataset, LoKA achieved a 15% improvement in recommendation accuracy over standard FP8 implementations, and a 20% reduction in memory usage. These results were benchmarked against established baselines, including traditional FP32 and naive FP8 approaches, showcasing the effectiveness of their framework.

**Limitations**  
The authors acknowledge that the effectiveness of LoKA is contingent on the specific architecture of the LRM and the characteristics of the dataset used. They also note that while LoKA improves numerical stability, it may not be universally applicable across all types of recommendation tasks. Additionally, the reliance on statistical profiling may introduce overhead that could offset some performance gains in certain scenarios. The paper does not address potential impacts on model interpretability or the generalizability of the proposed methods to other domains outside of recommendation systems.

**Why it matters**  
The implications of this work are significant for the deployment of large-scale recommendation systems, particularly in environments where computational resources are constrained. By enabling the use of low-precision arithmetic without sacrificing model quality, LoKA paves the way for more efficient training and inference processes. This could lead to broader adoption of FP8 in various applications, ultimately enhancing the scalability and performance of recommendation models in real-world scenarios. The framework also sets a precedent for future research on system-model co-design in other areas of machine learning.

Authors: Liang Luo, Yinbin Ma, Quanyu Zhu, Vasiliy Kuznetsov, Yuxin Chen, Jian Jiao, Jiecao Yu, Buyun Zhang et al.  
Source: arXiv:2605.10886  
URL: https://arxiv.org/abs/2605.10886v1
