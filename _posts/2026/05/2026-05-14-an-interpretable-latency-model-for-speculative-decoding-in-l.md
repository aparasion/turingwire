---
title: "An Interpretable Latency Model for Speculative Decoding in LLM Serving"
date: 2026-05-14 16:45:28 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.15051v1"
arxiv_id: "2605.15051"
authors: ["Linghao Kong", "Megan Flynn", "Michael Peng", "Nir Shavit", "Mark Kurtz", "Alexandre Marques"]
slug: an-interpretable-latency-model-for-speculative-decoding-in-l
summary_word_count: 466
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in understanding the performance of speculative decoding (SD) in production serving systems for large language models (LLMs). While previous research has demonstrated significant speedups in controlled environments, the dynamics of request load and effective batch size in real-world applications remain poorly characterized. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel latency model for SD that is both simple and interpretable. The model infers effective batch size from the request rate using Little's Law, allowing for a decomposition of per-request demand into load-independent and load-dependent components across three phases: prefill, drafting, and verification. The model's parameters are validated through extensive empirical measurements from the vLLM framework, which includes variations in verifier and drafter model sizes, prefill and decode lengths, request rates, draft lengths, and acceptance probabilities. The authors also extend their framework to accommodate mixture of experts models, where sparse expert activation alters effective service costs under varying load conditions.

**Results**  
The proposed latency model demonstrates a high degree of accuracy in predicting observed latencies across different configurations. Key findings include that speedups from SD diminish as server load increases, which is quantitatively characterized by the model. The authors provide specific metrics on how draft length, acceptance rate, and the sizes of verifier and drafter models influence latency. For instance, they show that increasing draft length can lead to diminishing returns in latency reduction under high load, which is critical for optimizing SD in deployed systems. The model's predictions outperform baseline latency metrics derived from traditional queuing theory approaches, indicating a significant improvement in understanding LLM serving dynamics.

**Limitations**  
The authors acknowledge that their model is based on empirical measurements from a specific framework (vLLM), which may limit generalizability to other LLM architectures or serving environments. Additionally, the model does not account for all potential sources of latency, such as network delays or hardware-specific bottlenecks, which could affect real-world performance. The authors also note that while the model provides insights into SD behavior, it may require further refinement to capture more complex interactions in heterogeneous serving environments.

**Why it matters**  
This work has significant implications for the deployment of LLMs in production settings, particularly in optimizing the configuration of speculative decoding to enhance inference speed without sacrificing accuracy. By providing a structured framework for understanding the latency dynamics of SD, the authors enable engineers and researchers to make informed decisions about model serving strategies. This could lead to more efficient resource utilization and improved user experiences in applications relying on LLMs. Furthermore, the extension of the model to mixture of experts architectures opens avenues for future research in optimizing sparse model serving.

Authors: Linghao Kong, Megan Flynn, Michael Peng, Nir Shavit, Mark Kurtz, Alexandre Marques  
Source: arXiv:2605.15051  
URL: [https://arxiv.org/abs/2605.15051v1](https://arxiv.org/abs/2605.15051v1)
