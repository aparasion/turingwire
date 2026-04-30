---
title: "FaaSMoE: A Serverless Framework for Multi-Tenant Mixture-of-Experts Serving"
date: 2026-04-29 16:47:48 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.26881v1"
arxiv_id: "2604.26881"
authors: ["Minghe Wang", "Trever Schirmer", "Mohammadreza Malekabbasi", "David Bermbach"]
slug: faasmoe-a-serverless-framework-for-multi-tenant-mixture-of-e
summary_word_count: 412
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of deploying Mixture-of-Experts (MoE) models in multi-tenant environments, where the resource utilization is inefficient due to the requirement that all experts reside in memory, regardless of their activation status. This leads to significant underutilization of resources, particularly in scenarios where multiple tenants share the same infrastructure. The authors propose FaaSMoE, a serverless framework that leverages Function-as-a-Service (FaaS) platforms to mitigate these issues. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
FaaSMoE introduces a novel architecture that decouples the control and execution planes of MoE models by deploying experts as stateless FaaS functions. This allows for on-demand invocation of experts, enabling a scale-to-zero capability that conserves resources when experts are not in use. The framework supports configurable expert granularity, allowing users to adjust the trade-off between per-expert elasticity and invocation overhead. The authors implemented a prototype using an open-source edge-oriented FaaS platform and evaluated it with the Qwen1.5-moe-2.7B model under multi-tenant workloads. The architecture is designed to optimize resource allocation dynamically based on demand, thus enhancing the efficiency of MoE serving.

**Results**  
FaaSMoE demonstrated a significant reduction in resource usage, consuming less than one-third of the resources compared to a full-model baseline. This was evaluated under multi-tenant workloads, showcasing the framework's ability to efficiently manage resources while maintaining performance. The specific metrics of performance improvement and resource savings were not disclosed in the abstract, but the authors emphasize the practical implications of their approach in real-world scenarios.

**Limitations**  
The authors acknowledge that while FaaSMoE improves resource efficiency, it may introduce latency due to the overhead of invoking FaaS functions, particularly in scenarios with high-frequency requests. Additionally, the configurable granularity may complicate the deployment process, requiring careful tuning to achieve optimal performance. The paper does not address potential issues related to cold start times inherent in serverless architectures, which could impact the responsiveness of the system under certain conditions.

**Why it matters**  
The implications of FaaSMoE are significant for the deployment of large-scale MoE models in cloud environments, particularly in multi-tenant scenarios where resource efficiency is critical. By enabling on-demand expert invocation, FaaSMoE provides a scalable solution that can adapt to varying workloads, potentially lowering operational costs and improving the accessibility of high-capacity models. This work paves the way for future research into serverless architectures for machine learning, particularly in optimizing resource utilization and performance in shared environments.

Authors: Minghe Wang, Trever Schirmer, Mohammadreza Malekabbasi, David Bermbach  
Source: arXiv:2604.26881  
URL: [https://arxiv.org/abs/2604.26881v1](https://arxiv.org/abs/2604.26881v1)
