---
title: "Vector Policy Optimization: Training for Diversity Improves Test-Time Search"
date: 2026-05-21 17:59:26 +0000
category: research
subcategory: training_methods
company: "ServiceNow"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22817v1"
arxiv_id: "2605.22817"
authors: ["Ryan Bahlous-Boldi", "Isha Puri", "Idan Shenfeld", "Akarsh Kumar", "Mehul Damani", "Sebastian Risi"]
slug: vector-policy-optimization-training-for-diversity-improves-t
summary_word_count: 456
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of current large language models (LLMs) in generalizing to novel environments and effectively utilizing inference-scaling search procedures, such as AlphaEvolve. The standard post-training paradigm typically optimizes a single scalar reward, which results in low-entropy response distributions. This lack of diversity in outputs hampers the models' ability to meet the varied demands of downstream tasks that require multiple reward functions. The authors propose a new approach, Vector Policy Optimization (VPO), to fill this gap. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Vector Policy Optimization (VPO) is a reinforcement learning (RL) algorithm designed to train policies that anticipate diverse downstream reward functions. VPO operates by treating rewards as vector-valued rather than scalar, allowing the model to generate a set of solutions that cater to different trade-offs in the reward space. The architecture is a drop-in replacement for the Generalized REINFORCE Policy Optimization (GRPO) advantage estimator, enhancing the model's ability to produce diverse outputs. The training process involves optimizing for multiple reward signals simultaneously, which is particularly beneficial in tasks like code generation where correctness can be evaluated across various test cases. The authors do not disclose specific details regarding the training compute used.

**Results**  
VPO demonstrates superior performance across four distinct tasks when compared to established scalar RL baselines. The evaluation metrics include pass@k and best@k, where VPO either matches or exceeds the performance of the strongest scalar RL models. Notably, the performance gap increases with the search budget, indicating that VPO's advantages become more pronounced as the complexity of the search increases. In scenarios involving evolutionary search, VPO successfully addresses problems that GRPO models fail to solve, showcasing its robustness and versatility.

**Limitations**  
The authors acknowledge that VPO's effectiveness may be contingent on the specific nature of the tasks and the diversity of the reward functions employed. They do not address potential scalability issues or the computational overhead associated with training on vector-valued rewards. Additionally, the paper does not explore the implications of VPO in real-world applications or its performance in highly dynamic environments where reward functions may change frequently.

**Why it matters**  
The introduction of VPO has significant implications for the future of LLM training and deployment, particularly in contexts where diverse outputs are critical. As test-time search methodologies become more standardized, the need for models that can optimize for diversity may shift from a novel approach to a necessary standard in post-training objectives. This work could influence subsequent research in RL and LLMs, encouraging the exploration of multi-objective optimization frameworks and the development of more sophisticated reward structures.

Authors: Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, Akarsh Kumar, Mehul Damani, Sebastian Risi, Omar Khattab, Zhang-Wei Hong et al.  
Source: arXiv:2605.22817  
URL: [https://arxiv.org/abs/2605.22817v1](https://arxiv.org/abs/2605.22817v1)
