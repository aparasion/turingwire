---
title: "Attention Once Is All You Need: Efficient Streaming Inference with Stateful Transformers"
date: 2026-05-13 17:06:15 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13784v1"
arxiv_id: "2605.13784"
authors: ["Victor Norgren"]
slug: attention-once-is-all-you-need-efficient-streaming-inference
summary_word_count: 397
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies of conventional transformer inference engines in streaming workloads, where data arrives continuously and queries require access to an ever-growing context. Traditional request-driven models incur an O(n) prefill cost for each query, which becomes prohibitive as the context size increases. The authors propose a novel approach to mitigate this issue, presenting a preprint that has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of a stateful session model that utilizes a persistent key-value (KV) cache, which is incrementally updated as new data arrives. This design allows the prefill operation to be decoupled from the query processing path, reducing query latency to O(|q|), where |q| is the length of the query, and is independent of the accumulated context size. The authors also introduce "Flash Queries," which leverage idle GPU cycles to pre-evaluate registered questions and return cached answers proactively, a capability not feasible in stateless engines that discard intermediate states. Additionally, a multi-tenant continuous-batching scheduler is implemented, featuring cell-budget admission and prefix-aware grouped prefill, enabling multiple stateful sessions to coexist on a single GPU while maintaining full quadratic self-attention.

**Results**  
The reference implementation of the proposed method demonstrates significant performance improvements on streaming market-data benchmarks. Specifically, it achieves up to a 5.9x speedup over conventional inference engines, including vLLM, SGLang, TensorRT-LLM, and llama.cpp, while maintaining constant query latency as the context size increases. This performance enhancement is particularly relevant for applications requiring real-time processing of streaming data.

**Limitations**  
The authors acknowledge that their approach may introduce complexity in managing stateful sessions, particularly in multi-tenant environments. They do not discuss potential limitations related to the scalability of the KV cache or the implications of session management on memory usage. Additionally, the reliance on GPU resources may limit applicability in environments where such hardware is not available or is constrained.

**Why it matters**  
This work has significant implications for real-time data processing applications, particularly in domains such as finance, telecommunications, and online services, where low-latency responses to streaming queries are critical. By enabling efficient stateful inference, the proposed model can enhance the performance of transformer-based architectures in scenarios that require continuous data ingestion and immediate query responses. This advancement could pave the way for more sophisticated applications of transformers in dynamic environments, potentially influencing future research on stateful architectures and streaming inference methodologies.

Authors: Victor Norgren  
Source: arXiv:2605.13784  
URL: [https://arxiv.org/abs/2605.13784v1](https://arxiv.org/abs/2605.13784v1)
