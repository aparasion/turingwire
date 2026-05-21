---
title: "Stdlib or Third-Party? Empirical Performance and Correctness of LLM-Assisted Zero-Dependency Python Libraries"
date: 2026-05-20 17:02:54 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21405v1"
arxiv_id: "2605.21405"
authors: ["Peng Ding", "Rick Stevens"]
slug: stdlib-or-third-party-empirical-performance-and-correctness-
summary_word_count: 444
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the performance and correctness of Python's standard library (stdlib) as a substitute for third-party libraries, which often introduce dependency management overhead and supply chain risks. The authors empirically investigate whether a significant portion of the functionality provided by popular third-party libraries can be replicated using only the stdlib, and at what cost in terms of performance and correctness. The study is motivated by the need for lightweight, dependency-free software solutions, particularly in constrained environments.

**Method**  
The core technical contribution is the development of `zerodep`, a collection of single-file Python modules that reimplement popular third-party libraries using only the stdlib. The authors employed large language models (LLMs) to assist in generating these implementations under strict constraints: no external imports, single-file structure, drop-in API compatibility, and mandatory correctness validation against the reference libraries. The study spans over 40 modules across 12 categories, including serialization, networking, cryptography, agent protocols, and text processing. The authors conducted systematic benchmarking to evaluate performance and correctness, focusing on the ability of LLMs to generate code that meets the specified constraints.

**Results**  
The results indicate that stdlib-only implementations achieve performance parity (within a factor of 2) with their third-party counterparts in the majority of cases. Notably, the primary performance degradation occurs in areas reliant on C-extension-backed computations, such as image processing and low-level cryptography. In contrast, the LLM-generated stdlib implementations exhibit significant speedups—ranging from 5x to 115x—over many widely-used libraries due to the avoidance of architectural overhead. The authors provide detailed performance metrics across various categories, demonstrating that LLMs can effectively generate performant code under the imposed constraints.

**Limitations**  
The authors acknowledge several limitations, including the potential for LLMs to require iterative human correction in complex scenarios, particularly where the stdlib's capabilities are insufficient. They also note that the performance metrics may not generalize across all use cases, as the study focuses on specific library categories and may not account for all edge cases. Additionally, the reliance on LLMs raises questions about the reproducibility and maintainability of the generated code, which are not fully addressed in the paper.

**Why it matters**  
This work has significant implications for the future of software engineering, particularly in contexts where minimizing dependencies is critical. By demonstrating that a substantial portion of third-party library functionality can be effectively replicated using the stdlib, the authors provide a pathway for developing lightweight, secure applications that mitigate supply chain risks. Furthermore, the findings suggest that LLMs can be a valuable tool in the software development process, particularly for generating code that adheres to strict constraints, thereby enhancing productivity and correctness in dependency-free environments.

Authors: Peng Ding, Rick Stevens  
Source: arXiv:2605.21405  
URL: [https://arxiv.org/abs/2605.21405v1](https://arxiv.org/abs/2605.21405v1)
