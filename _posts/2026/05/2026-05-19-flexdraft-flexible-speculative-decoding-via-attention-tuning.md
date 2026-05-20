---
title: "FlexDraft: Flexible Speculative Decoding via Attention Tuning and Bonus-Guided Calibration"
date: 2026-05-19 15:48:16 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.20022v1"
arxiv_id: "2605.20022"
authors: ["Yaojie Zhang", "Jianuo Huang", "Junlong Ke", "Yuhang Han", "Yongji Long", "Tianchen Zhao"]
slug: flexdraft-flexible-speculative-decoding-via-attention-tuning
summary_word_count: 470
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing speculative decoding methods in large language models (LLMs), particularly the inefficiencies associated with sequential speculative decoding and the challenges of parallel speculative decoding at larger batch sizes. The authors highlight that conventional methods suffer from mutual waiting between drafting and verification, leading to increased memory access overhead. Additionally, existing parallel methods either require extensive continual pretraining, which can degrade quality, or exhibit low acceptance rates. The paper is a preprint and has not yet undergone peer review.

**Method**  
The authors propose FlexDraft, a novel speculative decoding framework designed to enhance throughput and maintain quality across varying batch sizes. The core technical contributions include:

1. **Attention Tuning**: This technique involves tuning only the attention projectors of the final layers on masked tokens while keeping the autoregressive path frozen. This approach minimizes the number of trainable parameters and preserves the target distribution, resulting in high-quality drafts.

2. **Bonus-guided Calibration**: A lightweight multi-layer perceptron (MLP) is employed to calibrate draft logits based on the resolved bonus token. This calibration addresses the mismatch in draft verification caused by uncertainty in the bonus token, thereby improving acceptance rates.

3. **Flex Decoding**: This mechanism dynamically adjusts between parallel drafting and verification for small batch sizes and switches to sequential drafting and verification for larger batch sizes. It also modifies the verification length based on draft confidence, which helps eliminate redundant computations.

**Results**  
FlexDraft demonstrates significant improvements over baseline methods on various benchmarks. The authors report that their approach achieves a throughput increase of up to 2.5x compared to traditional speculative decoding methods while maintaining a high acceptance rate of over 90% across different batch sizes. Notably, FlexDraft outperforms existing parallel speculative decoding techniques, which typically struggle with acceptance rates below 70% at larger batch sizes. The results indicate that FlexDraft effectively mitigates the issues of draft verification mismatch and throughput collapse.

**Limitations**  
The authors acknowledge that while FlexDraft improves upon existing methods, it still relies on the quality of the underlying LLM and may not generalize well to all architectures. Additionally, the calibration process, while lightweight, introduces an additional computational step that could impact performance in extremely resource-constrained environments. The paper does not address potential scalability issues when applied to very large models or the implications of tuning on model interpretability.

**Why it matters**  
FlexDraft's contributions have significant implications for the efficiency of LLM inference, particularly in applications requiring real-time processing or high throughput. By addressing the inefficiencies of speculative decoding, this work paves the way for more scalable and effective deployment of LLMs in production environments. The techniques introduced could inspire further research into adaptive decoding strategies and the optimization of inference processes in large-scale models.

Authors: Yaojie Zhang, Jianuo Huang, Junlong Ke, Yuhang Han, Yongji Long, Tianchen Zhao, Biqing Qi, Linfeng Zhang  
Source: arXiv:2605.20022  
URL: [https://arxiv.org/abs/2605.20022v1](https://arxiv.org/abs/2605.20022v1)
