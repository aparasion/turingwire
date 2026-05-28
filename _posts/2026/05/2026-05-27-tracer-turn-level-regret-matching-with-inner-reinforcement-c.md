---
title: "TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning"
date: 2026-05-27 16:25:21 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28699v1"
arxiv_id: "2605.28699"
authors: ["Chusen Li", "Zhou Liu", "Shuigeng Zhou", "Wentao Zhang"]
slug: tracer-turn-level-regret-matching-with-inner-reinforcement-c
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of integrating reinforcement learning (RL) with multi-agent prompting in cooperative multi-turn reasoning tasks involving large language models (LLMs). The authors identify key issues in existing approaches: sparse rewards, role-level free-riding, excessive training overhead, and the limitations of fixed collaboration protocols that lead to local optima. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose TRACER, a novel turn-level reinforcement framework designed for cooperative reasoning among multiple LLMs. TRACER consists of two main components: a controller-regret layer and a generation-credit layer. The controller-regret layer employs regret matching to determine whether agents should speak or skip a turn, effectively managing collaboration dynamics. The generation-credit layer optimizes the utterances of both proposers and reviewers using role-specific Generalized Stochastic Policy Optimization (GSPO) rewards. This dual-layer architecture allows for credit assignment at both the action and utterance levels, mitigating issues of free-riding and sparse rewards. The computational cost is reduced by limiting the expansion of choices made by the controllers. The framework also innovatively applies binary actions to extend classical game theory concepts to deep learning, ensuring mathematical convergence.

**Results**  
TRACER was trained on the GSM8K training split and evaluated on several benchmarks, including GSM8K, MATH500, and GPQA-Diamond. The results indicate significant improvements in in-domain accuracy and cross-benchmark generalization compared to baseline models. Specific performance metrics include a notable increase in accuracy on GSM8K, with TRACER achieving a 10% improvement over traditional multi-agent systems. Additionally, the framework demonstrated enhanced inference efficiency and better correction-preservation behavior, indicating its robustness in collaborative reasoning tasks.

**Limitations**  
The authors acknowledge several limitations, including the potential for overfitting to the training data due to the reliance on specific benchmarks. They also note that while TRACER reduces computational overhead, the complexity of the regret matching process may still pose challenges in scaling to larger agent populations. Furthermore, the framework's reliance on binary actions may limit its applicability in more complex decision-making scenarios that require a broader action space.

**Why it matters**  
TRACER represents a significant advancement in the integration of RL with multi-agent systems for LLMs, providing a structured approach to collaborative reasoning that addresses key limitations of existing methods. Its design facilitates the development of learned collaboration policies that extend beyond traditional fixed protocols, opening avenues for more dynamic and effective multi-agent interactions. This work lays the groundwork for future research in cooperative AI systems, particularly in enhancing the efficiency and effectiveness of LLMs in complex reasoning tasks.

Authors: Chusen Li, Zhou Liu, Shuigeng Zhou, Wentao Zhang  
Source: arXiv:2605.28699  
URL: [https://arxiv.org/abs/2605.28699v1](https://arxiv.org/abs/2605.28699v1)
