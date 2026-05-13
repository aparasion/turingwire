---
title: "KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference"
date: 2026-05-12 17:53:47 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12471v1"
arxiv_id: "2605.12471"
authors: ["Alireza Nadali", "Patrick Cooper", "Ashutosh Trivedi", "Alvaro Velasquez"]
slug: kv-fold-one-step-kv-cache-recurrence-for-long-context-infere
summary_word_count: 406
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of long-context inference in transformer models, specifically the limitations of existing methods that either require retraining or compromise fidelity for memory efficiency. The authors propose KV-Fold, a training-free protocol that leverages the key-value (KV) cache for efficient long-context processing. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
KV-Fold introduces a novel inference protocol that utilizes the KV cache as an accumulator in a left fold operation over sequence chunks. The model processes each chunk sequentially, conditioning on the accumulated KV cache from previous chunks. This approach allows the model to append newly generated keys and values to the cache, effectively creating a recurrence mechanism without modifying the model's parameters. The authors demonstrate that this method is stable, with per-step drift initially rising before plateauing, and is robust to variations in numerical precision (up to 10,000x) and chunk sizes. The architecture remains unchanged, relying on the existing capabilities of frozen pretrained transformers.

**Results**  
KV-Fold achieves remarkable performance on a needle-in-a-haystack benchmark, attaining 100% exact-match retrieval across 152 trials with context lengths ranging from 16K to 128K tokens and chain depths up to 511 on the Llama-3.1-8B model. This performance is notable when compared to traditional streaming methods, which often sacrifice retrieval fidelity for memory constraints. KV-Fold operates efficiently within the memory limits of a single 40GB GPU, demonstrating its practicality for long-context inference.

**Limitations**  
The authors acknowledge that while KV-Fold is effective, it may not generalize to all types of tasks or models beyond those tested. The reliance on the existing KV cache structure may limit its applicability to architectures that do not utilize this mechanism. Additionally, the paper does not explore the potential impact of varying model sizes or the effects of different training datasets on the performance of KV-Fold.

**Why it matters**  
The implications of KV-Fold are significant for the field of natural language processing and transformer-based models. By providing a method for long-context inference that does not require retraining or architectural modifications, this work opens avenues for more efficient processing of extensive sequences in real-time applications. The stability and robustness of the KV-cache recurrence could lead to advancements in tasks requiring long-range dependencies, such as document retrieval, summarization, and dialogue systems. This research contributes to the ongoing exploration of optimizing transformer architectures for practical deployment in resource-constrained environments.

Authors: Alireza Nadali, Patrick Cooper, Ashutosh Trivedi, Alvaro Velasquez  
Source: arXiv:2605.12471  
URL: [https://arxiv.org/abs/2605.12471v1](https://arxiv.org/abs/2605.12471v1)
