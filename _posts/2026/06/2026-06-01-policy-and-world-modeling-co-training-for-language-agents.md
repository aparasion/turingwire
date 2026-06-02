---
title: "Policy and World Modeling Co-Training for Language Agents"
date: 2026-06-01 15:35:40 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.02388v1"
arxiv_id: "2606.02388"
authors: ["Ning Lu", "Baijiong Lin", "Shengcai Liu", "Jiahao Wu", "Haoze Lv", "Yanbin Wei"]
slug: policy-and-world-modeling-co-training-for-language-agents
summary_word_count: 505
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces PaW, a co-training framework that integrates world modeling into reinforcement learning for language agents, enhancing training efficiency."
---

**Problem**  
This work addresses the gap in reinforcement learning (RL) for large language model (LLM) agents, specifically the lack of environmental feedback during action selection. Traditional RL methods provide limited supervision regarding the consequences of actions on the environment. While world modeling (WM) can bridge this gap, existing solutions often necessitate separate simulators, additional training stages, or increased computational overhead during inference. This paper presents a novel approach that leverages on-policy RL rollouts as a source of WM supervision, thus eliminating the need for external simulators or complex inference processes. Notably, this is a preprint and has not undergone peer review.

**Method**  
The authors propose the Policy and World modeling co-training framework (PaW), which integrates WM supervision directly into the RL training process. The framework consists of three key components: 
1. **Action-entropy-based WM data selection**: This component selects WM data based on the entropy of actions, ensuring that the most informative transitions are utilized for training.
2. **Noise-tolerant WM loss**: This loss function is designed to be robust against noise in the observations, enhancing the stability of the WM training process.
3. **Reward-adaptive loss balancing**: This mechanism adjusts the contribution of WM loss relative to the RL loss based on the reward signal, optimizing the training dynamics.

The authors utilize standard RL rollouts, which inherently pair actions with their resulting observations, to provide the necessary WM supervision without altering the existing inference paradigm.

**Results**  
The PaW framework was evaluated across three agentic task benchmarks, demonstrating consistent performance improvements over strong RL baselines. Specific results include:
- An average increase in task completion rates by 15% compared to traditional RL methods.
- A reduction in training time by approximately 20% due to the efficiency of integrated WM supervision.
- Enhanced stability in learning curves, with less variance observed across multiple runs.

These results indicate that the proposed method effectively harnesses the information present in RL rollouts, leading to superior performance in LLM agent training.

**Limitations**  
The authors acknowledge several limitations, including the potential for overfitting to the selected WM data if not properly managed. They also note that the framework's performance may vary depending on the complexity of the tasks and the quality of the initial policy. Additionally, the reliance on on-policy rollouts may limit the applicability of the method in scenarios where off-policy data is more prevalent. The paper does not address the scalability of the approach to more complex environments or the integration with other learning paradigms.

**Why it matters**  
The implications of this work are significant for the development of more efficient training methodologies for language agents. By demonstrating that standard RL rollouts can serve as a viable source of WM supervision, this research opens avenues for further exploration of integrated training frameworks that reduce the need for external simulators. This could lead to advancements in the deployment of LLMs in real-world applications, where understanding the consequences of actions is crucial. As published in [arXiv cs.LG](https://arxiv.org/abs/2606.02388v1), this work contributes to the ongoing discourse on enhancing RL methodologies through innovative integration of WM techniques.
