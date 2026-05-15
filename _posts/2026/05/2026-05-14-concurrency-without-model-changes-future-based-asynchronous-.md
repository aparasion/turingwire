---
title: "Concurrency without Model Changes: Future-based Asynchronous Function Calling for LLMs"
date: 2026-05-14 17:02:28 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.15077v1"
arxiv_id: "2605.15077"
authors: ["Guangyu Feng", "Huanzhi Mao", "Prabal Dutta", "Joseph E. Gonzalez"]
slug: concurrency-without-model-changes-future-based-asynchronous-
summary_word_count: 402
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of synchronous execution semantics in function calling for large language models (LLMs), which leads to increased end-to-end latency during task execution. The authors highlight that existing frameworks do not allow for overlapping model decoding and function execution, thereby constraining the efficiency of LLMs in real-time applications. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of AsyncFC, an execution-layer framework that enables asynchronous function calling without requiring modifications to existing LLM architectures or function implementations. AsyncFC operates by decoupling the LLM decoding process from the execution of function calls, allowing for concurrent execution when dependencies allow. The framework leverages a future-based approach, where LLMs can reason over symbolic futures that represent unresolved execution results. The authors do not disclose specific details regarding the architecture of the LLMs used, the loss functions, or the exact compute resources required for training, focusing instead on the execution layer's capabilities.

**Results**  
AsyncFC demonstrates a significant reduction in end-to-end task completion time across standard function-calling benchmarks and adapted software engineering benchmarks. The authors report that AsyncFC achieves up to a 50% reduction in latency compared to synchronous function calling methods while maintaining task accuracy levels comparable to those of traditional approaches. The results indicate that LLMs can effectively manage asynchronous interactions with tools, showcasing their inherent capability to handle symbolic futures.

**Limitations**  
The authors acknowledge that AsyncFC's performance may be contingent on the nature of the functions being called, particularly in scenarios with complex dependencies that could limit parallel execution. They also note that while AsyncFC does not require changes to existing models, its effectiveness may vary based on the specific LLM architecture employed. An additional limitation not explicitly mentioned is the potential overhead introduced by managing asynchronous execution, which could offset some latency gains in certain contexts.

**Why it matters**  
The implications of this work are significant for the development of more efficient LLM agents capable of real-time decision-making and tool use. By enabling asynchronous function calling, AsyncFC paves the way for enhanced performance in applications requiring rapid responses, such as conversational agents, automated coding assistants, and interactive AI systems. This research opens avenues for further exploration into asynchronous paradigms in AI, potentially leading to more sophisticated interactions between models and external tools.

Authors: Guangyu Feng, Huanzhi Mao, Prabal Dutta, Joseph E. Gonzalez  
Source: arXiv:2605.15077  
URL: https://arxiv.org/abs/2605.15077v1
