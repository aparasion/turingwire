---
title: "PALS: Power-Aware LLM Serving for Mixture-of-Experts Models"
date: 2026-05-20 17:19:20 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21427v1"
arxiv_id: "2605.21427"
authors: ["Can Hankendi", "Rana Shahout", "Minlan Yu", "Ayse K. Coskun"]
slug: pals-power-aware-llm-serving-for-mixture-of-experts-models
summary_word_count: 376
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding the optimization of energy consumption in large language model (LLM) inference workloads within data centers. While existing systems focus on optimizing throughput and latency through batching and scheduling, they overlook the dynamic control of GPU power as a resource. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce PALS (Power-Aware LLM Serving), a runtime system that treats GPU power caps as a controllable parameter alongside software configurations like batch size. PALS employs a two-pronged approach: it utilizes lightweight offline power-performance models to predict the energy efficiency of various configurations and implements a feedback-driven controller to dynamically adjust these configurations in real-time. The system is integrated into the existing vLLM serving framework, ensuring compatibility without necessitating model retraining or API modifications. The training compute details are not disclosed, but the focus is on optimizing runtime configurations rather than model training.

**Results**  
PALS demonstrates significant improvements in energy efficiency and quality of service (QoS) across multi-GPU systems and both dense and mixture-of-experts (MoE) models. Specifically, it achieves up to a 26.3% increase in energy efficiency compared to baseline systems. Additionally, it reduces QoS violations by a factor of 4x to 7x when operating under power constraints. These results indicate that PALS effectively tracks and adapts to dynamic power budgets while maintaining throughput targets.

**Limitations**  
The authors acknowledge that PALS is designed for specific LLM serving frameworks and may require further adaptation for broader applicability across different architectures. Additionally, the reliance on offline power-performance models may limit the system's adaptability to unforeseen workload variations. The paper does not address potential impacts on model accuracy or inference latency due to the dynamic adjustments in power and batch size.

**Why it matters**  
The integration of power control into LLM inference runtimes has significant implications for the development of energy-efficient AI systems. By enabling energy-proportional and grid-interactive capabilities, PALS paves the way for more sustainable AI deployments in data centers, which are increasingly scrutinized for their energy consumption. This work could influence future research on power-aware AI systems and encourage the adoption of similar methodologies in other computational domains.

Authors: Can Hankendi, Rana Shahout, Minlan Yu, Ayse K. Coskun  
Source: arXiv:2605.21427  
URL: [https://arxiv.org/abs/2605.21427v1](https://arxiv.org/abs/2605.21427v1)
