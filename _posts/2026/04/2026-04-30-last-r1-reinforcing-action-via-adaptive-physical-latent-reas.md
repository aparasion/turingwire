---
title: "LaST-R1: Reinforcing Action via Adaptive Physical Latent Reasoning for VLA Models"
date: 2026-04-30 17:59:52 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.28192v1"
arxiv_id: "2604.28192"
authors: ["Hao Chen", "Jiaming Liu", "Zhonghao Yan", "Nuowei Han", "Renrui Zhang", "Chenyang Gu"]
slug: last-r1-reinforcing-action-via-adaptive-physical-latent-reas
summary_word_count: 446
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the capabilities of Vision-Language-Action (VLA) models, particularly their reliance on static imitation learning, which limits adaptability and generalization in dynamic environments. Existing methods either employ explicit linguistic reasoning, which suffers from latency and discretization issues, or utilize continuous latent reasoning without effectively integrating it into the action execution process. The authors propose LaST-R1 as a solution to these limitations, presenting a unified framework that incorporates adaptive reasoning mechanisms and reinforcement learning (RL) to enhance the performance of VLA models. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
LaST-R1 introduces a novel framework that integrates latent Chain-of-Thought (CoT) reasoning with a tailored RL post-training paradigm. The core technical contribution is the Latent-to-Action Policy Optimization (LAPO) algorithm, which jointly optimizes the latent reasoning process and action generation. The architecture leverages an adaptive latent CoT mechanism that dynamically adjusts the reasoning horizon based on the complexity of the environment. This allows the model to better represent physical dynamics prior to action execution. The training process involves a one-shot supervised warm-up followed by RL optimization, although specific compute resources used for training are not disclosed.

**Results**  
LaST-R1 achieves a remarkable 99.8% average success rate on the LIBERO benchmark, significantly outperforming prior state-of-the-art methods. The authors report that LAPO post-training yields up to a 44% improvement over the initial warm-up policy across four complex tasks, which include both single-arm and dual-arm robotic manipulation scenarios. These results indicate not only enhanced convergence speed but also improved robustness in interactive environments, showcasing the effectiveness of the proposed framework in both simulated and real-world settings.

**Limitations**  
The authors acknowledge that while LaST-R1 demonstrates strong performance, it is still constrained by the initial one-shot supervised warm-up, which may limit its applicability in scenarios where extensive pre-training is infeasible. Additionally, the paper does not address the computational efficiency of the adaptive reasoning mechanism, which could impact real-time applications. The generalization capabilities, while noted to be strong, have not been exhaustively tested across a wider variety of environments beyond those presented in the experiments.

**Why it matters**  
The implications of LaST-R1 are significant for the field of robotic manipulation and VLA models. By effectively bridging the gap between reasoning and control, this work paves the way for more adaptable and generalizable robotic systems capable of complex tasks in dynamic environments. The integration of adaptive reasoning mechanisms could inspire future research into more sophisticated RL algorithms that leverage latent representations, potentially leading to advancements in autonomous systems and human-robot interaction.

Authors: Hao Chen, Jiaming Liu, Zhonghao Yan, Nuowei Han, Renrui Zhang, Chenyang Gu, Jialin Gao, Ziyu Guo et al.  
Source: arXiv:2604.28192  
URL: [https://arxiv.org/abs/2604.28192v1](https://arxiv.org/abs/2604.28192v1)
