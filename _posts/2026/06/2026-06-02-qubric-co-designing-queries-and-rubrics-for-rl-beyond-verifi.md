---
title: "QUBRIC: Co-Designing Queries and Rubrics for RL Beyond Verifiable Rewards"
date: 2026-06-02 17:53:04 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.03968v1"
arxiv_id: "2606.03968"
authors: ["Rongzhi Zhang", "Rui Feng", "Zhihan Zhang", "Jingfeng Yang", "Qingyu Yin", "Xin Liu"]
slug: qubric-co-designing-queries-and-rubrics-for-rl-beyond-verifi
summary_word_count: 426
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces QUBRIC, a framework that co-designs queries and rubrics to enhance reinforcement learning beyond verifiable rewards."
---

**Problem**  
The paper addresses a significant gap in reinforcement learning (RL) literature, particularly in the context of rubric-based RL, which is a promising approach for extending RL applications beyond strictly verifiable rewards. Existing methods optimize rubrics while treating the query distribution as static, leading to structural bottlenecks where the quality of rubrics is limited by the nature of the queries. Open-ended queries often result in vague rubrics, and attempts to narrow them down can create unverifiable references, causing training failures and lack of reward signals. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors propose QUBRIC, a novel framework that co-designs queries and rubrics to overcome the identified limitations. The methodology involves several key components: 
1. **Key Point Derivation**: Teacher-derived key points are utilized to transform open-ended queries into scenario-based, evaluable questions.
2. **Contrastive Rubric Generation**: This process converts gaps between teacher policies and student responses into specific query-level criteria for rubric generation.
3. **Learnability Filtering**: This step retains only informative query-rubric pairs, which are then used for training a Generalized Reinforcement Policy Optimization (GRPO) model. The training is conducted on instruction-following data, ensuring that the model learns from high-quality, relevant examples.

**Results**  
QUBRIC demonstrates a substantial performance improvement, achieving a +5.5 point gain on the ArenaHard benchmark compared to the supervised fine-tuning (SFT) baseline. Furthermore, the model shows strong transferability, yielding an average improvement of +6.3 points across three held-out benchmarks that encompass legal, moral, and narrative reasoning tasks. Notably, the enhancements are particularly pronounced in reasoning-related dimensions, indicating that the co-design approach effectively addresses the challenges of rubric-based RL.

**Limitations**  
The authors acknowledge that the framework's reliance on teacher-derived key points may introduce biases based on the teachers' perspectives. Additionally, the performance improvements are contingent on the quality of the initial instruction-following data, which may not generalize across all domains. The paper does not address potential scalability issues when applying QUBRIC to more complex or diverse tasks beyond those tested.

**Why it matters**  
The implications of this work are significant for the future of reinforcement learning, particularly in contexts where verifiable rewards are not feasible. By demonstrating that co-designing queries and rubrics can enhance the practicality of rubric-based RL, this research opens avenues for more nuanced and effective RL applications in complex reasoning tasks. The findings suggest that integrating structured query design with rubric optimization can lead to more robust learning frameworks, as discussed in [arXiv cs.AI](https://arxiv.org/abs/2606.03968v1). This approach could serve as a foundation for future research aimed at improving RL methodologies in diverse and challenging environments.
