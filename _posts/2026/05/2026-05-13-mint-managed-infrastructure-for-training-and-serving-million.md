---
title: "MinT: Managed Infrastructure for Training and Serving Millions of LLMs"
date: 2026-05-13 16:59:08 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13779v1"
arxiv_id: "2605.13779"
authors: ["Mind Lab", ":", "Song Cao", "Vic Cao", "Andrew Chen", "Kaijie Chen"]
slug: mint-managed-infrastructure-for-training-and-serving-million
summary_word_count: 489
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper presents the MindLab Toolkit (MinT), addressing the challenge of efficiently managing and serving a large number of Low-Rank Adaptation (LoRA) policies derived from a limited set of expensive base models. The authors highlight the inefficiencies in traditional methods that require merging each policy into full checkpoints, which is resource-intensive and impractical at scale. This work is a preprint and has not yet undergone peer review.

**Method**  
MinT introduces a managed infrastructure that abstracts the complexities of distributed training, serving, scheduling, and data movement through a service interface. The architecture is designed to scale along three dimensions: 

1. **Scale Up**: MinT extends LoRA reinforcement learning to accommodate frontier-scale dense and mixture of experts (MoE) architectures, including MLA and DSA attention paths, validated for models exceeding 1 trillion parameters.
   
2. **Scale Down**: The system optimizes the transfer of only the exported LoRA adapters, which can be significantly smaller than the base model (under 1% in rank-1 settings). This approach results in substantial reductions in operational steps, achieving an 18.3x reduction on a 4B dense model and a 2.85x reduction on a 30B MoE model.

3. **Scale Out**: MinT separates policy addressability from CPU/GPU working sets, enabling tensor-parallel deployments that can manage catalogs of up to 1 million addressable policies. The system supports thousands of active adapter revisions simultaneously, with cold loading treated as scheduled service work. The use of packed MoE LoRA tensors enhances live engine loading efficiency by 8.5-8.7x.

**Results**  
MinT demonstrates significant performance improvements over traditional methods. The adapter-only handoff reduces operational steps by 18.3x for a 4B dense model and 2.85x for a 30B MoE model. Additionally, concurrent multi-policy GRPO reduces wall time by 1.77x and 1.45x, respectively, without increasing peak memory usage. The system's ability to handle 10^6-scale addressable catalogs and thousands of active adapters showcases its scalability and efficiency in managing large-scale LoRA policy catalogs.

**Limitations**  
The authors acknowledge that while MinT effectively manages large-scale LoRA policies, the reliance on a single base model may limit flexibility in adapting to diverse application requirements. Additionally, the performance metrics are primarily based on specific model architectures, and the generalizability of these results to other architectures or settings remains to be validated. The paper does not address potential challenges in maintaining model performance during rapid policy updates or the implications of cold loading on latency.

**Why it matters**  
MinT has significant implications for the deployment of large language models (LLMs) in production environments, particularly in scenarios requiring rapid adaptation and serving of multiple policies. By streamlining the management of LoRA policies, MinT enables more efficient use of computational resources, potentially lowering operational costs and improving response times in real-time applications. This work lays the groundwork for future research into scalable infrastructure solutions for LLMs, particularly in the context of dynamic policy adaptation and multi-task learning.

Authors: Mind Lab, Song Cao, Vic Cao, Andrew Chen, Kaijie Chen, Cleon Cheng, Steven Chiang et al.  
Source: arXiv:2605.13779  
URL: [https://arxiv.org/abs/2605.13779v1](https://arxiv.org/abs/2605.13779v1)
