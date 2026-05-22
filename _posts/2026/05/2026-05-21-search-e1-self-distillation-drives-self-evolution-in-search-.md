---
title: "Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning"
date: 2026-05-21 14:00:57 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.22511v1"
arxiv_id: "2605.22511"
authors: ["Zihan Liang", "Yufei Ma", "Ben Chen", "Zhipeng Qian", "Xuxin Zhang", "Huangyu Dai"]
slug: search-e1-self-distillation-drives-self-evolution-in-search-
summary_word_count: 422
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing search-augmented reasoning frameworks that rely heavily on complex architectures and external supervision. The authors critique the prevalent post-training methodologies that incorporate various auxiliary components—such as reward models, critics, and structured rollouts—that complicate the training pipeline and increase resource dependency. They propose a novel approach, Search-E1, which simplifies the process by leveraging self-distillation without the need for these elaborate augmentations. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of Search-E1 is the integration of a self-evolution mechanism into the search-augmented reasoning paradigm. The method employs a vanilla Generalized Reinforcement Policy Optimization (GRPO) interleaved with Offline Self-Distillation (OFSD). After each GRPO iteration, the policy is evaluated on its own training questions, utilizing a token-level forward Kullback-Leibler (KL) divergence objective. This objective aligns the policy's inference-time distribution with a more efficient sibling trajectory, which is derived from a privileged context. The simplicity of this approach allows for dense per-step supervision, enhancing the learning process without the overhead of additional modules or external systems.

**Results**  
Search-E1 demonstrates significant performance improvements across seven question-answering (QA) benchmarks. Specifically, it achieves an average Exact Match (EM) score of 0.440 with the Qwen2.5-3B model, outperforming all open-source baselines at both small and large scales. The results indicate that the proposed method not only simplifies the training process but also enhances the model's reasoning capabilities, showcasing the effectiveness of self-distillation in this context.

**Limitations**  
The authors acknowledge that while Search-E1 simplifies the training pipeline, it may not capture the full potential of more complex architectures that utilize external supervision. They do not address potential scalability issues when applied to larger models or more diverse datasets. Additionally, the reliance on self-distillation may limit the model's ability to generalize in scenarios where external context is crucial for reasoning. The paper does not explore the impact of varying the self-distillation frequency or the implications of different KL divergence weighting strategies.

**Why it matters**  
The implications of this work are significant for the development of more efficient search-augmented reasoning systems. By demonstrating that effective performance can be achieved without the complexity of additional modules, this research paves the way for more accessible and resource-efficient training methodologies. It encourages further exploration into self-evolution techniques and their potential to streamline the training of language models, which could lead to broader applications in natural language processing and AI-driven reasoning tasks.

Authors: Zihan Liang, Yufei Ma, Ben Chen, Zhipeng Qian, Xuxin Zhang, Huangyu Dai, Lingtao Mao  
Source: arXiv:2605.22511  
URL: [https://arxiv.org/abs/2605.22511v1](https://arxiv.org/abs/2605.22511v1)
