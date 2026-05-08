---
title: "MARBLE: Multi-Aspect Reward Balance for Diffusion RL"
date: 2026-05-07 16:20:42 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.06507v1"
arxiv_id: "2605.06507"
authors: ["Canyu Zhao", "Hao Chen", "Yunze Tong", "Yu Qiao", "Jiacheng Li", "Chunhua Shen"]
slug: marble-multi-aspect-reward-balance-for-diffusion-rl
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing reinforcement learning (RL) fine-tuning methods for aligning diffusion models with human preferences, particularly in the context of multi-dimensional evaluation criteria. Current approaches either rely on training separate models for each reward, utilize a weighted-sum reward aggregation, or employ sequential fine-tuning with a manually crafted schedule. These methods fail to produce a unified model capable of joint training across multiple rewards, leading to inefficiencies and suboptimal performance. The authors identify that the primary issue arises from a sample-level mismatch in the weighted-sum approach, where specialist samples provide relevant information for specific rewards but dilute supervision across others. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose MARBLE (Multi-Aspect Reward BaLancE), a novel gradient-space optimization framework designed to address the aforementioned issues. MARBLE maintains independent advantage estimators for each reward and computes per-reward policy gradients. These gradients are harmonized into a single update direction through the solution of a Quadratic Programming problem, eliminating the need for manually tuned reward weighting. Additionally, the authors introduce an amortized formulation that leverages the affine structure of the loss function used in DiffusionNFT, which reduces the computational cost from K+1 backward passes to a near single-reward baseline cost. To enhance stability, they implement Exponential Moving Average (EMA) smoothing on the balancing coefficients to mitigate transient fluctuations during updates.

**Results**  
MARBLE was evaluated on the SD3.5 Medium benchmark, utilizing five distinct reward dimensions. The results indicate that MARBLE improves all five reward dimensions simultaneously. Notably, it transforms the worst-aligned reward's gradient cosine from negative in 80% of mini-batches under the weighted summation approach to consistently positive with MARBLE. Furthermore, the training speed of MARBLE is reported to be 0.97 times that of the baseline training, demonstrating efficiency alongside improved performance.

**Limitations**  
The authors acknowledge that while MARBLE effectively addresses the multi-reward optimization challenge, it may still be sensitive to the choice of rewards and their respective distributions. Additionally, the reliance on Quadratic Programming could introduce computational overhead in certain scenarios, particularly with a high number of rewards. The paper does not discuss potential scalability issues when applied to more complex models or larger datasets, which could affect generalizability.

**Why it matters**  
The implications of MARBLE extend to the broader field of reinforcement learning and model alignment, particularly in applications requiring multi-faceted evaluation criteria. By providing a framework that allows for simultaneous optimization of multiple rewards without manual tuning, MARBLE could streamline the training process for diffusion models and similar architectures. This advancement may lead to more robust and aligned models in real-world applications, enhancing their utility in generating human-preferred outputs.

Authors: Canyu Zhao, Hao Chen, Yunze Tong, Yu Qiao, Jiacheng Li, Chunhua Shen  
Source: arXiv:2605.06507  
URL: https://arxiv.org/abs/2605.06507v1
