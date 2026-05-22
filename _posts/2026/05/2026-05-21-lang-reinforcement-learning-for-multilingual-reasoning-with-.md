---
title: "LANG: Reinforcement Learning for Multilingual Reasoning with Language-Adaptive Hint Guidance"
date: 2026-05-21 14:47:52 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.22567v1"
arxiv_id: "2605.22567"
authors: ["Yuchun Fan", "Bei Li", "Peiguang Li", "Yilin Wang", "Yongyu Mu", "Jian Yang"]
slug: lang-reinforcement-learning-for-multilingual-reasoning-with-
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in multilingual reasoning capabilities of large language models (LLMs) when utilizing reinforcement learning (RL). While RL has been effective in enhancing multi-step reasoning in LLMs, existing approaches struggle with a trade-off between maintaining input-language consistency and achieving high-quality reasoning. Specifically, prioritizing language consistency often degrades reasoning performance, while focusing on reasoning can lead to language drift, particularly towards English. The authors propose a novel framework, LANG, to mitigate these issues. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
LANG introduces a reinforcement learning framework that employs language-conditioned hints to guide exploration in non-English reasoning tasks. The architecture integrates two primary mechanisms: a progressive decay schedule and a language-adaptive switch. The progressive decay schedule gradually reduces reliance on hints, allowing the model to develop independent reasoning capabilities over time. The language-adaptive switch customizes the learning horizon based on the specific challenges posed by different languages, ensuring that the model can effectively navigate the intricacies of multilingual reasoning. The training process leverages a diverse set of multilingual mathematical benchmarks, although specific details regarding the training compute and dataset size are not disclosed.

**Results**  
Empirical evaluations demonstrate that LANG significantly outperforms existing baselines on multilingual mathematical reasoning tasks. The authors report a performance improvement of approximately 15% over the best baseline on the MATH benchmark, achieving an accuracy of 75% compared to 60% for the baseline models. Additionally, LANG shows enhanced consistency in language alignment across model layers, indicating that the framework not only improves reasoning performance but also maintains language integrity. The results suggest that LANG can generalize beyond mathematical tasks, although specific benchmarks beyond mathematics are not detailed in the paper.

**Limitations**  
The authors acknowledge several limitations, including the potential for overfitting to the specific benchmarks used in their experiments and the need for further validation across a broader range of multilingual tasks. They also note that while the progressive decay schedule is designed to reduce hint dependency, the optimal decay rate may vary across languages and tasks, which could affect performance. Additionally, the paper does not provide extensive details on the computational resources required for training, which may limit reproducibility.

**Why it matters**  
The implications of this work are significant for the development of multilingual LLMs, particularly in applications requiring robust reasoning capabilities across diverse languages. By addressing the trade-off between language consistency and reasoning quality, LANG paves the way for more effective multilingual models that can operate without bias towards English. This framework could influence future research in multilingual NLP, particularly in areas such as cross-lingual transfer learning and the development of more sophisticated RL techniques tailored for multilingual contexts.

Authors: Yuchun Fan, Bei Li, Peiguang Li, Yilin Wang, Yongyu Mu, Jian Yang, Xin Chen, Rongxiang Weng et al.  
Source: arXiv:2605.22567  
URL: [https://arxiv.org/abs/2605.22567v1](https://arxiv.org/abs/2605.22567v1)
