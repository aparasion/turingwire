---
title: "Taiji: Pareto Optimal Policy Optimization with Semantics-IDs Trade-off for Industrial LLM-Enhanced Recommendation"
date: 2026-06-02 16:39:06 +0000
category: research
subcategory: other
company: "Kuaishou"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.03866v1"
arxiv_id: "2606.03866"
authors: ["Yuecheng Li", "Zeyu Song", "Jing Yao", "Chi Lu", "Peng Jiang", "Kun Gai"]
slug: taiji-pareto-optimal-policy-optimization-with-semantics-ids-
summary_word_count: 376
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces Taiji, a novel framework for optimizing LLM-enhanced recommendation systems by addressing semantic-ID alignment and reward trade-offs."
---

**Problem**  
The paper addresses the challenges in aligning the semantic space of large language models (LLMs) with the ID space of recommender systems, particularly in the context of post-training methods like supervised fine-tuning (SFT) and reinforcement learning (RL). Existing LLM4Rec paradigms struggle with measuring and enhancing chain-of-thought (CoT) quality during SFT and fail to balance LLM semantic rewards with recommendation preference rewards during RL alignment. This work is a preprint and has not undergone peer review.

**Method**  
The authors propose Taiji, an LLM-as-Enhancer framework tailored for industrial recommender systems. To tackle the SFT bottleneck, Taiji employs reverse-engineered reasoning and open-ended rejection sampling to generate high-quality, domain-specific CoT data. For the RL alignment issue, the framework introduces Pareto Optimal Policy Optimization (POPO), which adaptively adjusts the weights of cross-domain rewards. This method theoretically achieves an optimal trade-off between the semantic knowledge encoded in LLMs and the collaborative ID features that represent user preferences in real-time. The architecture leverages extensive offline evaluations and online A/B testing to validate its effectiveness.

**Results**  
Taiji has been deployed on Kuaishou's advertising platform since May 2026, serving over 400 million users daily. The framework has demonstrated significant commercial revenue generation and robust scalability in web-scale environments. While specific numerical results are not disclosed in the abstract, the authors indicate that Taiji outperforms existing baselines in both offline evaluations and online A/B tests, suggesting substantial improvements in recommendation quality and user engagement metrics.

**Limitations**  
The authors acknowledge that the framework's reliance on high-quality CoT data generation may introduce biases if the underlying data is not representative of the target domain. Additionally, the adaptive reward weighting in POPO may require careful tuning to avoid overfitting to specific user behaviors. The paper does not discuss the computational overhead associated with the proposed methods, which could impact scalability in resource-constrained environments.

**Why it matters**  
The development of Taiji has significant implications for the future of LLM-enhanced recommendation systems, particularly in industrial applications where user engagement and revenue generation are critical. By effectively bridging the gap between LLM semantics and recommendation preferences, Taiji sets a precedent for future research in this domain. The findings and methodologies presented in this paper could inspire further advancements in the integration of LLMs into recommender systems, as published in [arXiv cs.AI](https://arxiv.org/abs/2606.03866v1).
