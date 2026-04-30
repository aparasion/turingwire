---
title: "Rule-based High-Level Coaching for Goal-Conditioned Reinforcement Learning in Search-and-Rescue UAV Missions Under Limited-Simulation Training"
date: 2026-04-29 16:01:22 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26833v1"
arxiv_id: "2604.26833"
authors: ["Mahya Ramezani", "Holger Voos"]
slug: rule-based-high-level-coaching-for-goal-conditioned-reinforc
summary_word_count: 405
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in capability for goal-conditioned reinforcement learning (RL) in search-and-rescue (SAR) UAV missions, particularly under conditions of limited simulation training. The authors propose a novel framework that integrates a rule-based high-level coaching mechanism with a low-level RL controller, which is particularly relevant given the challenges of real-time decision-making in dynamic environments. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The proposed framework consists of a hierarchical decision-making architecture that combines a fixed rule-based high-level advisor with an online goal-conditioned low-level RL controller. The high-level advisor is constructed offline from a structured task specification, resulting in deterministic rules that provide interpretable guidance, including recommended actions, avoided actions, and regime-dependent arbitration weights. The low-level controller employs a goal-conditioned RL approach, learning from task-defined dense rewards. It utilizes a mode-aware prioritized replay mechanism that incorporates metadata derived from the high-level rules, allowing for efficient experience reuse. The training regime is designed to operate without pretraining, emphasizing early adaptation in real-world scenarios.

**Results**  
The framework was evaluated on two specific tasks: battery-aware multi-goal delivery and moving-target delivery in environments with obstacles. The results indicate a significant improvement in early safety and sample efficiency, with a notable reduction in collision terminations compared to baseline methods. While specific numerical results are not detailed in the abstract, the authors claim that their method outperforms existing baselines in terms of both safety and adaptability to dynamic conditions.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a fixed rule-based advisor, which may not generalize well to all SAR scenarios. Additionally, the absence of pretraining could hinder performance in highly complex environments. The paper does not address potential scalability issues of the rule-based system or the computational overhead introduced by the prioritized replay mechanism. Furthermore, the evaluation is limited to two specific tasks, which may not fully capture the breadth of challenges encountered in SAR missions.

**Why it matters**  
This work has significant implications for the development of autonomous UAV systems in SAR operations, particularly in enhancing safety and efficiency in real-time decision-making. By integrating rule-based guidance with adaptive learning, the framework offers a promising approach to improve the robustness of UAVs in unpredictable environments. The findings could inform future research on hybrid decision-making systems and contribute to the design of more effective RL algorithms that leverage structured knowledge in dynamic settings.

Authors: Mahya Ramezani, Holger Voos  
Source: arXiv:2604.26833  
URL: [https://arxiv.org/abs/2604.26833v1](https://arxiv.org/abs/2604.26833v1)
