---
title: "Learning in Low-Dimensional Subspaces: Orthogonal Bottlenecks for Reinforcement Learning"
date: 2026-05-25 16:31:33 +0000
category: research
subcategory: representation
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26012v1"
arxiv_id: "2605.26012"
authors: ["Aleksandar Todorov", "Matthia Sabatelli"]
slug: learning-in-low-dimensional-subspaces-orthogonal-bottlenecks
summary_word_count: 447
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how deep reinforcement learning (RL) agents can leverage low-dimensional representations for value and policy functions. Despite the high-dimensional nature of current neural architectures, there is evidence suggesting that the intrinsic structure of these functions is often low-dimensional. The authors propose a method to enforce this low-dimensionality without the need for auxiliary objectives, pretraining, or modifications to existing RL algorithms.

**Method**  
The core technical contribution is the introduction of orthogonal bottlenecks, which are fixed orthonormal projections that constrain the encoder features to a low-dimensional subspace. The authors establish a theoretical foundation under a linear realizability assumption, demonstrating that if the bottleneck dimension exceeds the intrinsic rank of the optimal value function, the expressivity of the model is preserved. This is achieved while maintaining the gradient dynamics of the RL algorithm, effectively allowing for a low-dimensional parameterization of the problem. The method is architecture-agnostic, meaning it can be applied across various neural network designs without requiring significant alterations. The authors do not disclose specific training compute requirements, focusing instead on the representation-level prior.

**Results**  
Empirical evaluations show that the performance of RL agents using orthogonal bottlenecks either matches or exceeds that of baseline models across both single and multi-task benchmarks. Notably, the bottleneck dimension must exceed a small, task-dependent threshold to observe performance improvements. In many scenarios, the authors report that value representations can be compressed to extremely low dimensions without any loss in performance. The results indicate that the minimal sufficient dimension is more influenced by the complexity of the environment than by the width of the encoder. Additionally, the analysis of representation geometry reveals that orthogonal bottlenecks stabilize feature norms and correlate with a higher effective rank, suggesting improved representation quality.

**Limitations**  
The authors acknowledge that their approach relies on the linear realizability assumption, which may not hold in all RL scenarios. They do not address potential limitations related to the scalability of the method in highly complex environments or the generalizability of the findings across diverse RL tasks. Furthermore, the impact of the orthogonal bottleneck on convergence rates and sample efficiency remains unexplored.

**Why it matters**  
This work has significant implications for the design of RL agents, particularly in environments where computational resources are limited or where interpretability of learned representations is crucial. By providing a lightweight mechanism to enforce low-dimensional representations, the authors contribute to the understanding of the manifold hypothesis in RL, suggesting that effective learning can occur in reduced representation spaces. This could lead to more efficient training processes and better generalization in complex tasks, paving the way for future research on representation learning in RL.

Authors: Aleksandar Todorov, Matthia Sabatelli  
Source: arXiv:2605.26012  
URL: https://arxiv.org/abs/2605.26012v1
