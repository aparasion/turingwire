---
title: "When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning"
date: 2026-05-06 17:40:11 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.05172v1"
arxiv_id: "2605.05172"
authors: ["Lakshita Dodeja", "Ondrej Biza", "Shivam Vats", "Stephen Hart", "Stefanie Tellex", "Robin Walters"]
slug: when-life-gives-you-bc-make-q-functions-extracting-q-values-
summary_word_count: 479
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of Behavior Cloning (BC) in the context of online reinforcement learning (RL). While BC is effective for initial policy learning from demonstrations, it lacks a mechanism for self-improvement during online interaction. Existing offline-to-online learning methods often suffer from distribution mismatch, leading to suboptimal policy updates that can overwrite previously learned effective actions. This work presents Q2RL, a novel approach that aims to bridge the gap between offline BC and online RL, enabling more robust learning in real-world robotic applications. The paper is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this work is the Q2RL algorithm, which consists of two main components: Q-Estimation and Q-Gating. Q-Estimation involves extracting a Q-function from the BC policy by performing a limited number of interaction steps with the environment. This Q-function serves as a guide for action selection during online learning. Q-Gating then dynamically switches between actions derived from the BC policy and those from the RL policy based on their respective Q-values. This dual-action strategy allows the algorithm to leverage the strengths of both BC and RL, facilitating efficient sample collection for RL policy training. The authors do not disclose specific details regarding the architecture, loss functions, or compute resources used for training.

**Results**  
Q2RL demonstrates significant improvements over state-of-the-art (SOTA) offline-to-online learning baselines across various manipulation tasks evaluated on the D4RL and robomimic benchmarks. The algorithm achieves success rates of up to 100% in tasks such as pipe assembly and kitting, with a reported improvement factor of up to 3.75x compared to the original BC policy. Additionally, Q2RL shows rapid convergence, requiring only 1-2 hours of online interaction to learn robust policies. These results indicate a substantial enhancement in both performance and efficiency in real-world robotic applications.

**Limitations**  
The authors acknowledge that the Q2RL method relies on the quality of the initial BC policy, which may affect the Q-function extraction process. They also note that the approach may not generalize well to all types of tasks, particularly those with highly variable dynamics or where the initial demonstrations are suboptimal. An additional limitation not explicitly mentioned is the potential computational overhead introduced by the Q-Gating mechanism, which may complicate real-time decision-making in resource-constrained environments.

**Why it matters**  
The implications of this work are significant for the field of robotic learning, particularly in scenarios requiring high precision and adaptability. By effectively integrating offline learning with online reinforcement strategies, Q2RL provides a framework that can enhance the robustness and efficiency of robotic policies in dynamic environments. This approach could pave the way for more autonomous robotic systems capable of learning from both demonstrations and real-time interactions, ultimately advancing the state of the art in robotic manipulation and other complex tasks.

Authors: Lakshita Dodeja, Ondrej Biza, Shivam Vats, Stephen Hart, Stefanie Tellex, Robin Walters, Karl Schmeckpeper, Thomas Weng  
Source: arXiv:2605.05172  
URL: https://arxiv.org/abs/2605.05172v1
