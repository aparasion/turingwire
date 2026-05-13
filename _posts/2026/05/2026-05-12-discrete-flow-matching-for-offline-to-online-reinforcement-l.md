---
title: "Discrete Flow Matching for Offline-to-Online Reinforcement Learning"
date: 2026-05-12 16:44:02 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12379v1"
arxiv_id: "2605.12379"
authors: ["Fairoz Nower Khan", "Nabuat Zaman Nahim", "Peizhong Ju"]
slug: discrete-flow-matching-for-offline-to-online-reinforcement-l
summary_word_count: 456
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in reinforcement learning (RL) methods for discrete action spaces, particularly in the context of offline-to-online RL. Existing generative policy methods, primarily designed for continuous control, struggle to adapt to discrete actions. The challenge lies in effectively leveraging offline datasets while enabling the policy to improve through online interactions without degrading the performance learned from static data. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose DRIFT, an online fine-tuning method that enhances an offline pretrained continuous-time Markov chain (CTMC) policy using an advantage-weighted discrete flow matching loss. A key innovation is the introduction of a path-space penalty that regularizes the entire CTMC trajectory distribution, rather than focusing solely on the final action distribution. This approach aims to retain valuable knowledge from the pretrained model. To manage large discrete action spaces, the authors implement a candidate-set approximation, which updates the actor using a small subset of actions derived from reference-policy rollouts and uniform exploration. The theoretical framework indicates that the candidate-set error is mitigated by the coverage of high-probability actions, leading to a decrease in the CTMC generator error as the candidate set expands.

**Results**  
DRIFT demonstrates significant performance improvements across various discrete action RL tasks. Notably, it achieves the highest average score on the Jericho benchmark using a simple GRU encoder, outperforming existing methods that utilize pretrained language models. The authors report stable offline-to-online performance enhancements across all evaluated tasks. Controlled experiments validate that the path-space penalty remains bounded during the fine-tuning process and that the CTMC generator adapts to changes in reward structures more rapidly than deterministic baselines. The stability analysis supports the candidate-set mechanism, showing that the generator error decreases exponentially with increased candidate coverage.

**Limitations**  
The authors acknowledge that while DRIFT shows promise, it may still be sensitive to the choice of candidate set size and the sampling strategy employed. Additionally, the reliance on a pretrained CTMC policy may limit the method's applicability in scenarios where such pretraining is not feasible. The paper does not extensively explore the computational overhead introduced by the candidate-set approximation, which could impact scalability in larger action spaces.

**Why it matters**  
This work has significant implications for advancing RL methodologies in discrete action environments, particularly in applications where offline data is abundant but online interaction is necessary for policy refinement. By effectively bridging the gap between offline and online learning, DRIFT could enhance the robustness and adaptability of RL agents in real-world scenarios. The proposed techniques may inspire further research into hybrid approaches that leverage both offline and online learning paradigms, potentially leading to more efficient and effective RL systems.

Authors: Fairoz Nower Khan, Nabuat Zaman Nahim, Peizhong Ju  
Source: arXiv:2605.12379  
URL: [https://arxiv.org/abs/2605.12379v1](https://arxiv.org/abs/2605.12379v1)
