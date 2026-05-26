---
title: "Reinforcing Few-step Generators via Reward-Tilted Distribution Matching"
date: 2026-05-25 17:59:21 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.26108v1"
arxiv_id: "2605.26108"
authors: ["Yushi Huang", "Xiangxin Zhou", "Ruoyu Wang", "Chi Zhang", "Jun Zhang", "Tianyu Pang"]
slug: reinforcing-few-step-generators-via-reward-tilted-distributi
summary_word_count: 438
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of aligning few-step diffusion models with human preferences, a gap in the literature that persists despite recent advancements in efficient image generation. The authors propose a novel framework, Reward-Tilted Distribution Matching Distillation (RTDMD), to enhance the performance of few-step flow generators. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
RTDMD is a two-stage framework that integrates distribution matching distillation with reward-guided reinforcement learning. The core technical contribution involves minimizing the Kullback-Leibler (KL) divergence to a reward-tilted teacher distribution, which is decomposed into two components: a distribution matching term and a reward maximization term. 

1. **Stage One: Ambient-Consistent Distribution Matching Distillation (AC-DMD)** - This stage employs subinterval-wise distribution matching, enhancing the fake score objective with a consistency regularizer. This regularization aids the fake score model in tracking the evolving generator distribution despite limited updates.

2. **Stage Two: Joint Optimization** - In this stage, both the distribution matching and reward maximization terms are optimized concurrently. The authors introduce a hybrid policy gradient method that combines a Generalized Relative Policy Optimization (GRPO)-style estimator for stochastic intermediate transitions with direct reward backpropagation through the deterministic final step. Additionally, they propose a step-subset GRPO (SubGRPO) to mitigate variance in the reward estimation process.

**Results**  
The proposed RTDMD framework achieves state-of-the-art performance on several benchmarks, including SD3, SD3.5, and FLUX.2, demonstrating significant improvements in preference, aesthetic, and compositional metrics. Specifically, RTDMD operates effectively with only 4 inference steps, outperforming previous few-step text-to-image generation methods. The authors report substantial effect sizes, although specific numerical results and comparisons to baseline methods are not detailed in the abstract.

**Limitations**  
The authors acknowledge that the reliance on a reward-tilted teacher distribution may introduce biases based on the reward structure, potentially limiting generalization. They also note that the two-stage optimization process may require careful tuning of hyperparameters to achieve optimal performance. An additional limitation not explicitly mentioned is the potential computational overhead associated with the hybrid policy gradient method, which may affect scalability in larger applications.

**Why it matters**  
The implications of this work are significant for the field of generative modeling, particularly in enhancing the alignment of generated outputs with human preferences. By successfully integrating reinforcement learning with distribution matching, RTDMD sets a new benchmark for few-step image generation, paving the way for future research to explore similar frameworks in other generative tasks. This approach could lead to more efficient and user-aligned generative models, fostering advancements in applications such as content creation, design, and interactive AI systems.

Authors: Yushi Huang, Xiangxin Zhou, Ruoyu Wang, Chi Zhang, Jun Zhang, Tianyu Pang  
Source: arXiv:2605.26108 (cs.CV)  
URL: [https://arxiv.org/abs/2605.26108v1](https://arxiv.org/abs/2605.26108v1)
