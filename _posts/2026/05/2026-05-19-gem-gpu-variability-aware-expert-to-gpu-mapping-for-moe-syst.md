---
title: "GEM: GPU-Variability-Aware Expert to GPU Mapping for MoE Systems"
date: 2026-05-19 15:01:39 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.19945v1"
arxiv_id: "2605.19945"
authors: ["Sourish Wawdhane", "Avinash Kumar", "Poulami Das"]
slug: gem-gpu-variability-aware-expert-to-gpu-mapping-for-moe-syst
summary_word_count: 386
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in Mixture-of-Expert (MoE) models during inference, particularly the performance bottleneck caused by GPU stragglers. Existing methods for expert-to-GPU mapping do not account for GPU variability, leading to suboptimal placement of heavily utilized experts on slower GPUs. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce GEM (GPU-variability-aware Expert Mapping), a framework designed to optimize the mapping of experts to GPUs in MoE systems. GEM leverages two primary insights: (1) the need for non-uniform token load distribution across GPUs based on their performance variability, and (2) the strategic placement of consistent and temporal experts on different GPUs to minimize latency. The framework collects variability profiles for each GPU and analyzes token load distributions per task to inform expert placement. The authors do not disclose specific architectural details, loss functions, or training compute requirements, focusing instead on the mapping strategy.

**Results**  
GEM demonstrates a significant improvement in end-to-end latency, achieving an average reduction of 7.9% and a maximum reduction of 16.5% compared to baseline methods. The paper does not specify the exact baseline methods used for comparison, nor does it provide detailed metrics on the benchmarks employed. However, the results indicate a clear advantage in latency performance, suggesting that the proposed mapping strategy effectively mitigates the impact of GPU variability.

**Limitations**  
The authors acknowledge that their approach relies on accurate profiling of GPU variability, which may not be feasible in all deployment scenarios. Additionally, the paper does not address the potential overhead introduced by the variability profiling process itself. Other limitations include the lack of exploration into the scalability of GEM across larger MoE models or diverse hardware configurations, as well as the absence of a comprehensive evaluation on a wider range of tasks beyond those tested.

**Why it matters**  
The implications of GEM are significant for the deployment of MoE models in real-world applications, where latency is critical. By addressing GPU variability, GEM provides a more robust framework for expert mapping that can enhance the efficiency of MoE systems, potentially leading to faster inference times in production environments. This work opens avenues for further research into adaptive resource allocation strategies in distributed systems, particularly in the context of heterogeneous hardware setups.

Authors: Sourish Wawdhane, Avinash Kumar, Poulami Das  
Source: arXiv:2605.19945  
URL: [https://arxiv.org/abs/2605.19945v1](https://arxiv.org/abs/2605.19945v1)
