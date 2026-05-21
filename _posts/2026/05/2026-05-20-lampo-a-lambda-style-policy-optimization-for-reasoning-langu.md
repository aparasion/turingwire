---
title: "LamPO: A Lambda Style Policy Optimization for Reasoning Language Models"
date: 2026-05-20 14:24:11 +0000
category: research
subcategory: training_methods
company: "null"
secondary_companies: ["Lam Research"]
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21235v1"
arxiv_id: "2605.21235"
authors: ["Zhe Yuan", "Yipeng Zhou", "Jinghan Li", "Xinyuan Chen", "Bowen Deng", "Zhiqian Chen"]
slug: lampo-a-lambda-style-policy-optimization-for-reasoning-langu
summary_word_count: 439
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing reinforcement learning with verifiable rewards (RLVR) methods, particularly the group-relative objectives like GRPO, which aggregate responses into scalar statistics. This aggregation discards fine-grained relational information among candidate responses, leading to ineffective credit assignment in scenarios with sparse outcome rewards. The authors highlight that this is particularly problematic in reasoning tasks where subtle differences in response quality can significantly impact performance. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core contribution of this paper is the introduction of LamPO (Lambda-Style Policy Optimization), which utilizes a Pairwise Decomposed Advantage to replace scalar group advantages. This method aggregates pairwise reward gaps within response groups, allowing for a more nuanced comparison of candidate responses. Each comparison is modulated by a confidence-aware weight derived from the differences in sequence log-probabilities. LamPO retains the critic-free and clipped-update structure characteristic of Proximal Policy Optimization (PPO). Additionally, when reference solutions are available, the authors incorporate a lightweight ROUGE-L-based dense auxiliary reward to mitigate reward sparsity, enhancing the learning signal during training.

**Results**  
The authors conducted experiments on several benchmarks: AIME24, AIME25, MATH-500, and GPQA-Diamond, using models Qwen3-1.7B, Qwen3-4B, and Phi-4-mini. LamPO demonstrated consistent improvements over GRPO and other recent RLVR variants. Notably, the method achieved a 15% increase in average performance on AIME24 and a 20% improvement on MATH-500 compared to GRPO. The training dynamics were reported to be more stable, with LamPO exhibiting better sample efficiency, as evidenced by a reduction in the number of training iterations required to reach comparable performance levels.

**Limitations**  
The authors acknowledge that while LamPO improves upon GRPO, it still relies on the availability of reference solutions for the auxiliary reward mechanism, which may not always be feasible in practice. Additionally, the method's reliance on log-probability differences may introduce biases if the underlying language model is not well-calibrated. The paper does not address the scalability of LamPO to larger models or more complex reasoning tasks beyond those tested.

**Why it matters**  
The introduction of LamPO has significant implications for the development of reasoning language models, particularly in tasks requiring nuanced understanding and comparison of candidate responses. By addressing the limitations of existing RLVR methods, LamPO enhances the ability of models to learn from sparse rewards, potentially leading to more robust performance in real-world applications such as automated reasoning, coding assistance, and scientific inquiry. This work paves the way for future research to explore more sophisticated reward structures and optimization techniques in reinforcement learning for language models.

Authors: Zhe Yuan, Yipeng Zhou, Jinghan Li, Xinyuan Chen, Bowen Deng, Zhiqian Chen, Liang Zhao  
Source: arXiv:2605.21235  
URL: https://arxiv.org/abs/2605.21235v1
