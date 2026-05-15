---
title: "DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models"
date: 2026-05-14 16:49:09 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.15055v1"
arxiv_id: "2605.15055"
authors: ["Quanhao Li", "Junqiu Yu", "Kaixun Jiang", "Yujie Wei", "Zhen Xing", "Pandeng Li"]
slug: diffusionopd-a-unified-perspective-of-on-policy-distillation
summary_word_count: 450
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing reinforcement learning (RL) methods in optimizing diffusion-based text-to-image models, particularly their inability to effectively handle multi-task scenarios. Current approaches either suffer from cross-task interference and imbalance when attempting joint optimization or are cumbersome and prone to catastrophic forgetting in cascade RL setups. The authors propose DiffusionOPD, a novel multi-task training paradigm that leverages Online Policy Distillation (OPD) to overcome these challenges. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
DiffusionOPD introduces a two-step training process. Initially, it trains task-specific teacher models independently, allowing each to specialize in its respective task. Subsequently, these teachers' capabilities are distilled into a unified student model, which learns from its own rollout trajectories. This decoupling of single-task exploration from multi-task integration mitigates the optimization complexities associated with joint task training. The authors extend the OPD framework from discrete tokens to continuous-state Markov processes, deriving a closed-form per-step Kullback-Leibler (KL) divergence objective. This objective facilitates the integration of both stochastic Stochastic Differential Equations (SDE) and deterministic Ordinary Differential Equations (ODE) refinement through mean-matching. The paper also demonstrates that the analytic gradient derived from this approach yields lower variance and improved generalization compared to traditional Proximal Policy Optimization (PPO)-style policy gradients.

**Results**  
The authors conducted extensive experiments to evaluate DiffusionOPD against various baselines, including multi-reward RL and cascade RL methods. The results indicate that DiffusionOPD consistently outperforms these baselines in terms of training efficiency and final performance metrics. Specifically, the paper reports state-of-the-art results across all evaluated benchmarks, although exact numerical performance metrics and specific benchmark names are not disclosed in the summary provided.

**Limitations**  
The authors acknowledge that while DiffusionOPD improves upon existing methods, it may still face challenges related to the scalability of the teacher-student framework in highly complex multi-task environments. Additionally, the reliance on independent teacher training may not fully exploit potential synergies between tasks. The paper does not address the computational overhead associated with training multiple teacher models, which could be a concern in resource-constrained settings.

**Why it matters**  
The introduction of DiffusionOPD has significant implications for the field of multi-task learning in reinforcement learning, particularly in the context of diffusion models. By providing a structured approach to distilling knowledge from specialized models into a unified framework, this work paves the way for more efficient and effective training of complex models across diverse tasks. The theoretical advancements in the OPD framework also contribute to a deeper understanding of policy optimization in continuous spaces, which could influence future research directions in both RL and generative modeling.

Authors: Quanhao Li, Junqiu Yu, Kaixun Jiang, Yujie Wei, Zhen Xing, Pandeng Li, Ruihang Chu, Shiwei Zhang et al.  
Source: arXiv:2605.15055  
URL: [https://arxiv.org/abs/2605.15055v1](https://arxiv.org/abs/2605.15055v1)
