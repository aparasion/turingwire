---
title: "UniPool: A Globally Shared Expert Pool for Mixture-of-Experts"
date: 2026-05-07 17:59:44 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06665v1"
arxiv_id: "2605.06665"
authors: ["Minbin Huang", "Han Shi", "Chuanyang Zheng", "Yimeng Wu", "Guoxuan Chen", "Xintong Yu"]
slug: unipool-a-globally-shared-expert-pool-for-mixture-of-experts
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional Mixture-of-Experts (MoE) architectures, which allocate expert capacity on a per-layer basis, leading to linear growth in expert parameters with model depth. The authors argue that this rigid allocation is inefficient, as it assumes that each layer requires isolated expert capacity. Their analysis reveals that replacing learned top-k routers with uniform random routing results in only a minor drop in accuracy (1.0-1.6 points) across various production MoE models. This suggests redundancy in expert allocation that can be optimized. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose UniPool, a novel MoE architecture that utilizes a globally shared expert pool instead of the conventional per-layer expert ownership. This architecture allows independent per-layer routers to access a common pool of experts, thereby optimizing expert utilization. To facilitate stable training and balanced expert usage, they introduce a pool-level auxiliary loss that encourages equitable expert utilization across the shared pool. Additionally, they implement NormRouter, which provides sparse and scale-stable routing into the shared expert pool. The models are evaluated across five scales of the LLaMA architecture (182M, 469M, 650M, 830M, and 978M parameters) trained on a dataset of 30 billion tokens from the Pile.

**Results**  
UniPool demonstrates consistent improvements over matched vanilla MoE baselines in terms of validation loss and perplexity. Specifically, it achieves a reduction in validation loss by up to 0.0386 relative to vanilla MoE across the tested scales. Notably, reduced-pool variants of UniPool, utilizing only 41.6%-66.7% of the expert-parameter budget of vanilla MoE, either match or outperform the layer-wise MoE configurations. This indicates that expert parameters can grow sublinearly with depth in a shared-pool design, enhancing both efficiency and effectiveness compared to traditional MoE architectures.

**Limitations**  
The authors acknowledge that their approach may not generalize to all types of tasks or datasets, as the experiments are primarily conducted on a specific dataset (Pile) and architecture (LLaMA). They do not address potential challenges in routing efficiency or the impact of varying expert pool sizes on model performance in different contexts. Additionally, the reliance on a shared pool may introduce complexities in expert specialization that are not fully explored.

**Why it matters**  
The implications of UniPool extend to the design of future MoE architectures, suggesting that expert capacity can be managed more flexibly and efficiently. By decoupling expert allocation from model depth, this work opens avenues for more scalable and resource-efficient models, potentially leading to advancements in large-scale language models and other applications requiring adaptive capacity management. The findings encourage further exploration of shared expert pools and their integration with finer-grained expert decomposition strategies.

Authors: Minbin Huang, Han Shi, Chuanyang Zheng, Yimeng Wu, Guoxuan Chen, Xintong Yu, Yichun Yin, Hong Cheng  
Source: arXiv:2605.06665  
URL: https://arxiv.org/abs/2605.06665v1
