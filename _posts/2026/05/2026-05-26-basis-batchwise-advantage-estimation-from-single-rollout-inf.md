---
title: "BASIS: Batchwise Advantage Estimation from Single-Rollout Information Sharing for LLM Reasoning"
date: 2026-05-26 17:06:41 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.27293v1"
arxiv_id: "2605.27293"
authors: ["Shijin Gong", "Erhan Xu", "Kai Ye", "Francesco Quinzan", "Giulia Livieri", "Chengchun Shi"]
slug: basis-batchwise-advantage-estimation-from-single-rollout-inf
summary_word_count: 449
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in reinforcement learning (RL) methodologies for large language models (LLMs) that utilize verifiable rewards, specifically focusing on the tradeoff between computational efficiency and sample efficiency in value estimation and policy learning. The authors propose BASIS, a critic-free post-training algorithm that leverages information sharing across prompts to enhance value function estimation while only requiring a single rollout per prompt. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
BASIS operates by sampling one rollout per prompt during each online training step, but it utilizes the collective information from the entire batch to refine value function estimation. The architecture is designed to be critic-free, which simplifies the training process. The authors do not disclose specific details regarding the loss function or the exact training compute used, but they emphasize the efficiency of their approach in comparison to existing methods. The algorithm's core innovation lies in its ability to reduce mean squared error (MSE) in value function estimation significantly, achieving a 69% reduction compared to the REINFORCE++ baseline, which is a representative single-rollout method. Additionally, BASIS demonstrates superior performance in value estimation with just one rollout compared to group mean estimators that require eight rollouts.

**Results**  
BASIS achieves a 69% reduction in MSE for value function estimation compared to REINFORCE++, showcasing its effectiveness in improving value estimation with minimal rollouts. In terms of policy optimization, BASIS not only requires substantially less training time but also reaches performance levels comparable to multi-rollout GRPO-type baselines. Furthermore, it often outperforms single-rollout REINFORCE-type baselines, indicating a significant advancement in both efficiency and effectiveness in RL for LLMs.

**Limitations**  
The authors acknowledge that while BASIS improves upon existing methods, it is still limited by the reliance on a single rollout per prompt, which may not capture the full variability of the underlying distribution. Additionally, the paper does not explore the scalability of BASIS across different model architectures or its performance in more complex environments beyond the benchmarks tested. The lack of peer review may also imply that the findings should be interpreted with caution until validated by the community.

**Why it matters**  
The implications of BASIS are significant for downstream work in RL for LLMs, particularly in scenarios where computational resources are constrained. By demonstrating that effective value function estimation can be achieved with fewer rollouts, BASIS paves the way for more efficient training protocols in RL applications. This could lead to broader adoption of RL techniques in LLMs, enhancing their reasoning capabilities while minimizing the computational burden, thus facilitating more extensive experimentation and deployment in real-world applications.

Authors: Shijin Gong, Erhan Xu, Kai Ye, Francesco Quinzan, Giulia Livieri, Chengchun Shi  
Source: arXiv:2605.27293  
URL: https://arxiv.org/abs/2605.27293v1
