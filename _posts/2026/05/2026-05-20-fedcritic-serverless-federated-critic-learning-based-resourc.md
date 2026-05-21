---
title: "FedCritic: Serverless Federated Critic Learning-based Resource Allocation for Multi-Cell OFDMA in 6G"
date: 2026-05-20 17:13:09 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21418v1"
arxiv_id: "2605.21418"
authors: ["Amin Farajzadeh", "Melike Erol-Kantarci"]
slug: fedcritic-serverless-federated-critic-learning-based-resourc
summary_word_count: 420
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of resource allocation in ultra-dense 6G networks, specifically focusing on the joint subcarrier scheduling and power allocation under conditions of inter-cell interference (ICI) and long-term per-user quality-of-service (QoS) constraints. The authors highlight the limitations of existing centralized training with decentralized execution (CTDE) methods, which require a central coordinator for critic learning and trajectory aggregation, making them less scalable and efficient in highly dynamic environments. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of FedCritic, a serverless federated multi-agent actor-critic framework designed for decentralized execution. FedCritic employs virtual-queue deficit weights to enforce long-term QoS requirements. The framework utilizes a gossip-based parameter averaging mechanism over the interference graph to federate the critic, allowing for stable value estimation without the need for a central coordinator. This decentralized approach enables local policy execution while maintaining effective coordination among agents. The authors do not disclose specific details regarding the training compute or the exact architecture of the agents, but the focus is on minimizing coordination overhead while maximizing performance in resource allocation.

**Results**  
Simulations conducted in a reuse-1 setting, characterized by high interference, demonstrate that FedCritic significantly outperforms both non-coordinated and CTDE baselines. Key performance metrics include an improvement in mean signal-to-interference-plus-noise ratio (SINR) and cell-edge rate, alongside enhancements in network-wide average sum-rate and fairness. The results indicate that FedCritic achieves a more stable training process with reduced coordination overhead, although specific numerical improvements over baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that the proposed method may face challenges in highly heterogeneous environments where user demands and channel conditions vary significantly. Additionally, the reliance on gossip-based parameter averaging may introduce latency in convergence, particularly in scenarios with a large number of agents. The paper does not address potential scalability issues related to the number of agents or the complexity of the interference graph, which could impact the practical deployment of FedCritic in real-world scenarios.

**Why it matters**  
The implications of this work are significant for the design of resource management strategies in future 6G networks, particularly in environments with high user density and stringent QoS requirements. By enabling decentralized learning and coordination, FedCritic could facilitate more efficient resource allocation, leading to improved network performance and user experience. This approach may also inspire further research into federated learning techniques in other domains of wireless communication, potentially influencing the development of next-generation network architectures.

Authors: Amin Farajzadeh, Melike Erol-Kantarci  
Source: arXiv:2605.21418  
URL: [https://arxiv.org/abs/2605.21418v1](https://arxiv.org/abs/2605.21418v1)
