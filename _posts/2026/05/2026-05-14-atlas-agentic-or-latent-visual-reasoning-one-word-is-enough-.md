---
title: "ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both"
date: 2026-05-14 17:59:55 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.15198v1"
arxiv_id: "2605.15198"
authors: ["Ziyu Guo", "Rain Liu", "Xinyan Chen", "Pheng-Ann Heng"]
slug: atlas-agentic-or-latent-visual-reasoning-one-word-is-enough-
summary_word_count: 381
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing visual reasoning frameworks, particularly the trade-offs between agentic and latent reasoning methods. Agentic reasoning, which involves executing external operations, suffers from context-switching latency, while latent reasoning struggles with generalization and training efficiency. The authors propose ATLAS, a novel framework that utilizes a single discrete 'word'—a functional token—to unify these approaches. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
ATLAS introduces a functional token that serves dual purposes: it acts as an agentic operation and a latent visual reasoning unit. This token is integrated into the tokenizer vocabulary and can be generated through next-token prediction, eliminating the need for extensive intermediate visual content generation. The framework is compatible with standard supervised fine-tuning (SFT) and reinforcement learning (RL) training methodologies without requiring architectural changes. To enhance the training of functional tokens, the authors propose Latent-Anchored GRPO (LA-GRPO), which stabilizes training by anchoring functional tokens with a statically weighted auxiliary objective, thereby providing stronger gradient updates.

**Results**  
ATLAS demonstrates superior performance across several challenging benchmarks compared to established baselines. The authors report significant improvements in task completion rates and reasoning accuracy, although specific numerical results and effect sizes are not detailed in the abstract. The framework's interpretability is also highlighted, suggesting that it maintains clarity in how visual reasoning is conducted.

**Limitations**  
The authors acknowledge that the reliance on a single functional token may limit the expressiveness of the model in more complex reasoning tasks. Additionally, while LA-GRPO improves training stability, it may introduce additional hyperparameters that require careful tuning. The paper does not address potential scalability issues when applied to larger datasets or more complex visual reasoning tasks, nor does it explore the implications of the functional token's design on model interpretability in depth.

**Why it matters**  
The ATLAS framework represents a significant advancement in visual reasoning by merging the strengths of agentic and latent methods while mitigating their respective weaknesses. This approach could inspire future research in visual reasoning, particularly in developing more efficient models that require less computational overhead and can generalize better across tasks. The interpretability aspect also opens avenues for understanding model decisions, which is crucial for applications in safety-critical domains.

Authors: Ziyu Guo, Rain Liu, Xinyan Chen, Pheng-Ann Heng  
Source: arXiv:2605.15198  
URL: [https://arxiv.org/abs/2605.15198v1](https://arxiv.org/abs/2605.15198v1)
