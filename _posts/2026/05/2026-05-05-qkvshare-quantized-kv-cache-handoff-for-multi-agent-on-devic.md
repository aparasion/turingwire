---
title: "QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs"
date: 2026-05-05 15:44:29 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.03884v1"
arxiv_id: "2605.03884"
authors: ["Pratik Honavar", "Tejpratap GVSL"]
slug: qkvshare-quantized-kv-cache-handoff-for-multi-agent-on-devic
summary_word_count: 434
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in multi-agent large language model (LLM) systems on edge devices, specifically the costly processes of re-prefilling or transferring full-precision key-value (KV) caches during agent handoff. The authors propose a solution to improve the efficiency of KV-cache handoff, which is critical for maintaining context in real-time applications. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the QKVShare framework, which implements a quantized KV-cache handoff mechanism. This framework utilizes token-level mixed-precision allocation to optimize memory usage and performance. It introduces a self-contained CacheCard representation that facilitates efficient KV storage and retrieval. Additionally, QKVShare is designed to be compatible with HuggingFace's cache injection path, allowing for seamless integration with existing LLM architectures. The authors conducted experiments using the Llama-3.1-8B-Instruct model on 150 GSM8K problems, focusing on adaptive quantization strategies compared to uniform quantization. The training compute specifics are not disclosed, but the emphasis is on the efficiency of the handoff process rather than the training of the model itself.

**Results**  
The results demonstrate that adaptive quantization outperforms uniform quantization, particularly in scenarios involving deeper hops and higher budget settings. The QKVShare framework significantly reduces total time to first token (TTFT) latency during handoff. Specifically, at a nominal context of 1K, QKVShare achieves a TTFT of 130.7 ms compared to 150.2 ms for full re-prefill. At a nominal context of 8K, the TTFT is reduced to 397.1 ms versus 1029.7 ms for the baseline. These results indicate a clear advantage of the QKVShare method in terms of latency reduction across varying context sizes, with post-injection generation being the primary contributor to the observed latency.

**Limitations**  
The authors acknowledge the need for further exploration of controller ablations to optimize the handoff process. They also highlight the necessity for more rigorous apples-to-apples runtime comparisons to validate the performance gains of QKVShare against other state-of-the-art methods. An additional limitation not explicitly mentioned is the potential impact of quantization on model accuracy, which warrants further investigation.

**Why it matters**  
The implications of this work are significant for the deployment of multi-agent LLMs on resource-constrained edge devices. By demonstrating a viable method for efficient KV-cache handoff, QKVShare paves the way for more responsive and context-aware applications in real-time environments. This research could influence future designs of on-device LLM systems, particularly in scenarios where low latency and efficient memory usage are critical. The findings encourage further exploration of quantization techniques and their integration into existing frameworks, potentially leading to advancements in the performance of edge AI applications.

Authors: Pratik Honavar, Tejpratap GVSL  
Source: arXiv:2605.03884  
URL: [https://arxiv.org/abs/2605.03884v1](https://arxiv.org/abs/2605.03884v1)
