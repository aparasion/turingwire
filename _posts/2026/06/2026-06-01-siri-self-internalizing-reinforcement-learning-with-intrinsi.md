---
title: "SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training"
date: 2026-06-01 15:02:59 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.02355v1"
arxiv_id: "2606.02355"
authors: ["Zhongyu He", "Yuanfan Li", "Fei Huang", "Tianyu Chen", "Siyuan Chen", "Xingyang Li"]
slug: siri-self-internalizing-reinforcement-learning-with-intrinsi
summary_word_count: 420
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces SIRI, a self-internalizing reinforcement learning framework that enables LLM agents to autonomously discover and utilize skills without external dependencies."
---

**Problem**  
The paper addresses the limitations of existing skill-based reinforcement learning methods for long-horizon large language model (LLM) agents, which typically depend on external skill generators during training or require persistent skill retrieval at inference. This reliance complicates engineering, increases context length, and adds latency during deployment. The authors propose a novel framework, Self-Internalizing Reinforcement Learning with Intrinsic Skills (SIRI), to mitigate these issues by enabling agents to autonomously discover, validate, and internalize skills without external dependencies. This work is presented as a preprint and has not undergone peer review.

**Method**  
SIRI consists of a three-phase framework: (1) **Warm-up Phase**: The policy is initialized using the GiGPO (Generalized Interactive Goal-Conditioned Policy Optimization) algorithm to develop basic interaction capabilities and gather successful skill-free trajectories. (2) **Self-Skill Mining Phase**: The current policy extracts compact skills from its successful rollouts and validates these skills through comparative rollouts—one augmented with skills and one without. (3) **Distillation Phase**: The framework distills only the beneficial skill-guided action tokens into the plain policy, utilizing trajectory-level utility and action-level advantage metrics. This approach allows the agent to operate solely with the original prompt during inference, eliminating the need for external skill banks.

**Results**  
SIRI demonstrates significant performance improvements over the GiGPO baseline on two benchmarks: ALFWorld and WebShop. Specifically, SIRI enhances the performance from 0.908 to 0.930 on ALFWorld and from 0.728 to 0.813 on WebShop when using the Qwen2.5-7B-Instruct model. These results surpass those achieved by prompt-based, reinforcement learning-based, and memory-augmented baselines, indicating the effectiveness of the self-internalization approach. Additionally, the self-mining strategy employed in SIRI achieves performance levels comparable to distillation methods that utilize closed-source large models.

**Limitations**  
The authors acknowledge that while SIRI effectively reduces reliance on external skill generators, the framework's performance may still be sensitive to the quality of the initial skill-free trajectories generated during the warm-up phase. Furthermore, the scalability of the self-skill mining process in more complex environments remains an open question. The paper does not address potential issues related to the generalization of the distilled skills across diverse tasks or the computational overhead associated with the self-validation process.

**Why it matters**  
The implications of SIRI are significant for the development of autonomous LLM agents capable of long-horizon tasks without the complexities introduced by external skill dependencies. By enabling agents to autonomously discover and internalize skills, SIRI paves the way for more efficient and scalable reinforcement learning applications. This work contributes to the ongoing discourse in the field, as highlighted in related literature, and is available for further exploration on [arXiv](https://arxiv.org/abs/2606.02355v1).
