---
title: "LLM Zeroth-Order Fine-Tuning is an Inference Workload"
date: 2026-05-27 17:19:19 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28760v1"
arxiv_id: "2605.28760"
authors: ["Zelin Li", "Caiwen Ding"]
slug: llm-zeroth-order-fine-tuning-is-an-inference-workload
summary_word_count: 429
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiency in existing implementations of zeroth-order (ZO) fine-tuning for large language models (LLMs), which typically operate within conventional training loops. The authors argue that this approach leads to a mismatch between the algorithm's requirements for structured inference-style scoring and the fragmented nature of training-loop execution. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel execution framework for ZO fine-tuning that treats the repeated scoring phase as an inference workload, utilizing a serving runtime instead of a traditional training loop. They implement this approach using the vLLM execution path on the OPT-13B model, specifically targeting the SST-2 benchmark. The core technical contribution includes the reorganization of the runtime to optimize the scoring process, which is inherently more aligned with inference tasks. The authors also explore a MeZO-style high-rank factorization method to demonstrate that this runtime paradigm can effectively track a MeZO-like loss trajectory while achieving significant speed improvements.

**Results**  
The proposed method achieves an 8.13x speedup over the official LoZO baseline, completing a 20k-step LoZO run in 0.51 estimated training hours compared to 4.15 hours for the baseline under a matched LoRA-only setting. The final evaluation accuracy reached 0.922, with a full-validation accuracy of 0.931. In core-step scaling experiments across models ranging from OPT-1.3B to OPT-13B, the authors report speedups between 2.34x and 7.72x. The MeZO-style experiment further demonstrates that the new runtime can operate up to 2.55x faster while maintaining effective loss tracking.

**Limitations**  
The authors acknowledge that their approach is contingent on the specific architecture of the OPT models and may not generalize to all LLMs. They do not discuss potential limitations related to the scalability of the serving runtime across different hardware configurations or the implications of using dynamic adapter states for various model architectures. Additionally, the reliance on a serving runtime may introduce overheads not present in traditional training loops, which could affect performance in certain scenarios.

**Why it matters**  
This work has significant implications for the future of fine-tuning large language models, particularly in contexts where computational efficiency is critical. By framing ZO fine-tuning as an inference workload, the authors open avenues for lightweight adaptation strategies that can be integrated into real-time applications. This paradigm shift could facilitate more efficient model updates in production environments, enabling faster deployment of state-of-the-art models without the overhead of traditional training processes. The insights gained from this research may also inform the design of future training algorithms that leverage inference-like workloads for model adaptation.

Authors: Zelin Li, Caiwen Ding  
Source: arXiv:2605.28760  
URL: [https://arxiv.org/abs/2605.28760v1](https://arxiv.org/abs/2605.28760v1)
