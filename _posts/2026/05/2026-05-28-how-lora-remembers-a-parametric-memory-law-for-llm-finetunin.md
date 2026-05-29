---
title: "How LoRA Remembers? A Parametric Memory Law for LLM Finetuning"
date: 2026-05-28 17:22:24 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30260v1"
arxiv_id: "2605.30260"
authors: ["Ziwen Xu", "Haiwen Hong", "Linsong Yu", "Benglei Cui", "Longtao Huang", "Hui Xue"]
slug: how-lora-remembers-a-parametric-memory-law-for-llm-finetunin
summary_word_count: 409
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the quantitative limits and dynamics of parametric memory in Large Language Models (LLMs) during fine-tuning, particularly in the context of Low-Rank Adaptation (LoRA). While LoRA is widely adopted for updating model knowledge, previous research has primarily focused on qualitative evaluations, lacking a systematic exploration of how memory capacity can be quantified and optimized.

**Method**  
The authors propose a novel framework termed the Parametric Memory Law, which establishes a power law relationship between loss reduction (ΔL), effective parameters, and sequence length. This law serves as a theoretical foundation for analyzing memory capacity in LLMs. The study employs a fine-grained token-level analysis to identify a deterministic phase transition, where a prediction probability exceeding 0.5 is identified as a sufficient condition for verbatim recall during greedy decoding. Building on these insights, the authors introduce MemFT, a threshold-guided optimization strategy that reallocates the training budget towards tokens that fall below a specified threshold, thereby enhancing memory fidelity. The implementation details, including architecture specifics and training compute, are not disclosed in the abstract.

**Results**  
Empirical evaluations demonstrate that MemFT significantly improves memory fidelity and efficiency compared to baseline methods. The authors report that models fine-tuned with MemFT achieve a notable increase in recall accuracy, although specific numerical results and comparisons against named baselines are not detailed in the abstract. The effectiveness of MemFT is illustrated through various benchmarks, although exact metrics and effect sizes are not provided.

**Limitations**  
The authors acknowledge that their approach primarily focuses on the theoretical aspects of memory capacity and may not fully account for all practical scenarios in LLM fine-tuning. Additionally, the lack of detailed quantitative results in the abstract limits the ability to assess the full impact of their proposed methods. Other potential limitations include the generalizability of the findings across different model architectures and the scalability of MemFT in larger, more complex datasets.

**Why it matters**  
This work has significant implications for the ongoing development of LLMs, particularly in dynamic environments where continuous learning is essential. By quantifying the memory capacity and introducing a systematic approach to optimize memory fidelity, the findings could inform future research on efficient fine-tuning strategies. The introduction of the Parametric Memory Law may also pave the way for further theoretical advancements in understanding the interplay between model architecture, training dynamics, and memory retention in LLMs.

Authors: Ziwen Xu, Haiwen Hong, Linsong Yu, Benglei Cui, Longtao Huang, Hui Xue, Ningyu Zhang  
Source: arXiv:2605.30260  
URL: https://arxiv.org/abs/2605.30260v1
