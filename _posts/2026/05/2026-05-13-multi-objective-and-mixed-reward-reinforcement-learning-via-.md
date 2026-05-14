---
title: "Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization"
date: 2026-05-13 15:05:18 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13641v1"
arxiv_id: "2605.13641"
authors: ["Yang Bai", "Kaiyuan Liu", "Ziyuan Zhuang", "Jiahong Zhou", "Rongxiang Weng", "Xin Chen"]
slug: multi-objective-and-mixed-reward-reinforcement-learning-via-
summary_word_count: 450
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenges posed by multi-task and mixed-reward formulations in complex reinforcement learning (RL) environments, particularly the issues of heterogeneous reward distributions and correlated reward dimensions that can destabilize scalar advantage construction. The authors propose a novel approach, Reward-Decorrelated Policy Optimization (RDPO), to mitigate these issues. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this paper is the RDPO framework, which consists of two main components. First, it employs Magnitude-Aware Quantile normalization to stabilize advantage allocation across various reward types, including binary, fractional, and continuous rewards. This normalization technique ensures that the advantages derived from different reward signals are comparably scaled, thus enhancing the stability of the learning process. Second, RDPO utilizes Mahalanobis whitening within each active reward subspace to address correlation redundancy before aggregating rewards. This step effectively decorrelates the reward signals, allowing for a more robust optimization process. The authors apply RDPO during the post-training phase of the LongCat-Flash model, which is a large language model designed for instruction following and other complex tasks.

**Results**  
The application of RDPO leads to significant improvements in several performance metrics. Specifically, the authors report enhanced instruction following, improved writing quality, and increased robustness to challenging prompts. While the paper does not provide explicit numerical results against named baselines, it claims that RDPO remains broadly competitive on reasoning and coding evaluations, suggesting that it achieves a favorable trade-off between performance and stability compared to existing methods. The authors imply that RDPO outperforms traditional scalar advantage methods, although specific effect sizes and benchmark comparisons are not detailed.

**Limitations**  
The authors acknowledge that RDPO may introduce additional computational overhead due to the normalization and whitening processes, which could impact training efficiency. They also note that the method's effectiveness may vary depending on the specific characteristics of the reward structure in different environments. An obvious limitation not discussed by the authors is the potential for overfitting when applying RDPO in environments with sparse rewards, as the decorrelation process may inadvertently amplify noise in the reward signals.

**Why it matters**  
The implications of this work are significant for the field of reinforcement learning, particularly in scenarios involving complex, multi-objective tasks. By providing a method to effectively handle correlated and heterogeneous rewards, RDPO could enhance the stability and performance of RL agents in real-world applications, such as robotics, natural language processing, and multi-agent systems. This research opens avenues for further exploration into reward processing techniques and their integration into existing RL frameworks, potentially leading to more robust and adaptable learning systems.

Authors: Yang Bai, Kaiyuan Liu, Ziyuan Zhuang, Jiahong Zhou, Rongxiang Weng, Xin Chen, Jingang Wang, Xunliang Cai  
Source: arXiv:2605.13641  
URL: https://arxiv.org/abs/2605.13641v1
