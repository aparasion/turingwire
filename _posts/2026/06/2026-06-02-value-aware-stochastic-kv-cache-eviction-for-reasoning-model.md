---
title: "Value-Aware Stochastic KV Cache Eviction for Reasoning Models"
date: 2026-06-02 17:16:33 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.03928v1"
arxiv_id: "2606.03928"
authors: ["Ting-Yun Chang", "Harvey Yiyun Fu", "Deqing Fu", "Chenghao Yang", "Jesse Thomason", "Robin Jia"]
slug: value-aware-stochastic-kv-cache-eviction-for-reasoning-model
summary_word_count: 383
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces Value-aware Stochastic KV Cache Eviction (VaSE), enhancing reasoning model efficiency while maintaining accuracy through improved cache management."
---

**Problem**  
The paper addresses the limitations of existing key-value (KV) cache eviction methods in reasoning models, which often lead to reduced accuracy compared to selection-based sparse attention mechanisms. The authors highlight that current eviction strategies can result in catastrophic failures due to the eviction of high-magnitude value states, leading to repetitive reasoning loops. This work is particularly relevant as it is a preprint and has not undergone peer review, indicating the need for further validation of its findings.

**Method**  
The core contribution is the Value-aware Stochastic KV Cache Eviction (VaSE) method, which operates without requiring additional training. VaSE identifies and protects value states with large magnitudes during the eviction process, thereby preventing accuracy degradation. The method introduces stochasticity in the eviction decisions, which enhances cache diversity and mitigates the risk of catastrophic failures. The authors implement VaSE in conjunction with the Qwen3 model, utilizing a 4x compression of the KV cache. The architecture supports FlashAttention2, allowing for a static memory footprint while maintaining operational efficiency.

**Results**  
VaSE demonstrates significant improvements in accuracy across six reasoning tasks when compared to state-of-the-art (SOTA) selection methods at equivalent sparsity levels. Specifically, Qwen3 models employing VaSE achieve higher average accuracies than the best-performing selection-based method, with an improvement margin exceeding 4% over the strongest existing eviction method. These results indicate that VaSE effectively balances the trade-off between computational efficiency and model performance.

**Limitations**  
The authors acknowledge that while VaSE improves accuracy and efficiency, it may not be universally applicable across all reasoning tasks or model architectures. The method's reliance on stochastic eviction decisions could introduce variability in performance, which may not be desirable in all contexts. Additionally, the paper does not explore the long-term effects of using VaSE in dynamic environments where the nature of reasoning tasks may evolve.

**Why it matters**  
The introduction of VaSE has significant implications for the development of more efficient reasoning models, particularly in scenarios where memory and computational resources are constrained. By bridging the gap between efficiency and accuracy, this method paves the way for future research into advanced cache management techniques in large language models and other AI systems. The findings contribute to the ongoing discourse on optimizing model performance while managing resource limitations, as discussed in related works on sparse attention mechanisms and memory management strategies, available on [arXiv](https://arxiv.org/abs/2606.03928v1).
