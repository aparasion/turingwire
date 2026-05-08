---
title: "Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients"
date: 2026-05-07 17:55:21 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.06650v1"
arxiv_id: "2605.06650"
authors: ["Mingwei Xu", "Hao Fang"]
slug: beyond-negative-rollouts-positive-only-policy-optimization-w
summary_word_count: 386
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing reinforcement learning with verifiable rewards (RLVR) frameworks, particularly the reliance on negative rollouts in Group Relative Policy Optimization (GRPO). The authors argue that negative rollouts fail to capture the gradation of failure severity and are insufficient for providing meaningful reward signals in environments with sparse binary rewards. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Positive-Only Policy Optimization (POPO), a novel RLVR framework that exclusively utilizes online positive rollouts for policy optimization. POPO employs bounded importance sampling to adjust the learning process based solely on positive experiences, eliminating the need for negative rollouts. The architecture features a siamese policy network that stabilizes policy evolution through a momentum-based adaptation law. Additionally, the KL-divergence is replaced with a bounded similarity penalty term in the siamese representation space, enhancing stability during training. The training compute details are not disclosed, but the experiments leverage publicly available text-LLM models, specifically the Qwen family.

**Results**  
POPO demonstrates competitive performance against GRPO on various mathematical benchmarks. Notably, POPO achieves a score of 36.67% on the AIME 2025 benchmark using the Qwen-Math-7B model, surpassing GRPO's performance of 30.00%. The authors conduct ablation studies and parameter sweeps to validate the necessity and robustness of the components within POPO, indicating that the proposed methods contribute significantly to the observed performance improvements.

**Limitations**  
The authors acknowledge that the reliance on positive rollouts may limit the exploration of the action space, potentially leading to suboptimal policies in environments where negative feedback is crucial for learning. They do not address the scalability of POPO in more complex environments or the potential computational overhead introduced by the siamese network architecture. Additionally, the absence of negative rollouts may hinder the model's ability to learn from diverse failure scenarios.

**Why it matters**  
The introduction of POPO has significant implications for the development of reinforcement learning algorithms, particularly in scenarios where negative feedback is sparse or unreliable. By demonstrating that effective learning can occur through positive-only experiences, this work opens avenues for further research into alternative optimization strategies that could enhance the reasoning capabilities of large language models (LLMs). The findings may influence future RLVR frameworks and encourage exploration of similar positive-centric approaches in other domains.

Authors: Mingwei Xu, Hao Fang  
Source: arXiv:2605.06650  
URL: [https://arxiv.org/abs/2605.06650v1](https://arxiv.org/abs/2605.06650v1)
