---
title: "When Hidden States Drift: Can KV Caches Rescue Long-Range Speculative Decoding?"
date: 2026-04-29 08:25:01 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26412v1"
arxiv_id: "2604.26412"
authors: ["Tianyu Liu", "Yuhao Shen", "Xinyi Hu", "Baolin Zhang", "Hengxin Zhang", "Jun Dai"]
slug: when-hidden-states-drift-can-kv-caches-rescue-long-range-spe
summary_word_count: 438
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the persistent issue of long-range decay in speculative decoding for large language models (LLMs). While speculative decoding accelerates inference, existing hidden-state-based drafters exhibit degraded accuracy as the speculative step increases. Previous research has attributed this decay to train-inference mismatch and proposed test-time training (TTT) as a solution. However, the authors demonstrate that long-range decay persists even with TTT-trained models, indicating a gap in understanding the underlying mechanisms of context information preservation during hidden-state reuse.

**Method**  
The authors introduce the KV-Reuse Hypothesis, positing that reusing the key-value (KV) cache from the target model can enhance long-range drafting by providing richer contextual signals. They propose a diagnostic framework called KVShot, which evaluates three paradigms of context reuse: hidden-only, KV-only, and hybrid. The experiments are conducted using the Qwen3-8B model, focusing on the impact of KV cache reuse on long-range acceptance rates. The authors identify two structural bottlenecks: (1) shallow drafters struggle with accurate target query estimation, and (2) draft-side KV projections receive sparse gradient signals. These insights suggest that to fully leverage KV-aware decoding, a shift from TTT to block-wise training paradigms is necessary.

**Results**  
The results indicate that KV cache reuse significantly improves long-range acceptance rates compared to hidden-only and hybrid paradigms. However, the end-to-end speedups remain marginal under the current training pipelines. The authors provide quantitative metrics demonstrating that KV-only approaches outperform hidden-only methods in long-range scenarios, although specific numerical results are not disclosed in the abstract. The findings highlight the importance of KV cache in maintaining contextual integrity over extended speculative steps.

**Limitations**  
The authors acknowledge that while KV cache reuse improves long-range acceptance, the overall speedup in inference remains limited, suggesting that current training methodologies may not fully exploit the potential of KV-aware decoding. They also note that the shallow drafters' inability to accurately estimate target queries and the sparsity of gradient signals for KV projections are significant bottlenecks. However, the paper does not explore the implications of these limitations on broader model architectures or the potential for generalization across different LLMs.

**Why it matters**  
This work has significant implications for the design of next-generation inference architectures in LLMs. By elucidating the limitations of current speculative decoding methods and proposing a framework for KV cache reuse, the authors provide a roadmap for future research aimed at enhancing long-range contextual understanding in LLMs. The insights gained from KVShot could inform the development of more effective training paradigms, ultimately leading to improved performance in real-world applications where long-range dependencies are critical.

Authors: Tianyu Liu, Yuhao Shen, Xinyi Hu, Baolin Zhang, Hengxin Zhang, Jun Dai, Jun Zhang, Shuang Ge et al.  
Source: arXiv:2604.26412  
URL: [https://arxiv.org/abs/2604.26412v1](https://arxiv.org/abs/2604.26412v1)
