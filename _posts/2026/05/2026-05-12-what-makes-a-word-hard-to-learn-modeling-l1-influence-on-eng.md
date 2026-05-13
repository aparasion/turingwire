---
title: "What makes a word hard to learn? Modeling L1 influence on English vocabulary difficulty"
date: 2026-05-12 15:39:47 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.12281v1"
arxiv_id: "2605.12281"
authors: ["Jonas Mayer Martins", "Zhuojing Huang", "Aaricia Herygers", "Lisa Beinborn"]
slug: what-makes-a-word-hard-to-learn-modeling-l1-influence-on-eng
summary_word_count: 431
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how a learner's first language (L1) influences the difficulty of acquiring English vocabulary. While previous studies have explored vocabulary acquisition, they often lack a computational framework that quantifies the impact of L1 on word difficulty. The authors aim to model vocabulary difficulty for English learners from three distinct linguistic backgrounds: Spanish, German, and Chinese, providing insights into the specific features that contribute to this difficulty.

**Method**  
The authors employ gradient-boosted models to predict vocabulary difficulty based on a set of features categorized into four groups: familiarity (e.g., word frequency), meaning, surface form, and cross-linguistic transfer. The models are trained on a dataset that includes these features, allowing for a nuanced understanding of how each contributes to perceived difficulty. Shapley values are utilized to interpret the importance of each feature group across the different L1 backgrounds. The study highlights that word familiarity is the most significant feature across all three language groups, while orthographic transfer plays a crucial role for Spanish and German learners but is absent for Chinese learners.

**Results**  
The models demonstrate high predictive accuracy, with specific performance metrics not disclosed in the abstract. The authors report that the inclusion of L1-specific features significantly enhances the model's ability to estimate vocabulary difficulty. For instance, the model for Spanish and German learners shows improved performance over a baseline that does not account for orthographic transfer. The results indicate that familiarity and surface features are critical for Chinese learners, suggesting a divergence in the learning mechanisms based on L1. The exact effect sizes and comparisons to named baselines are not provided in the abstract.

**Limitations**  
The authors acknowledge that their models are limited to three specific L1s and may not generalize to learners from other linguistic backgrounds. Additionally, the reliance on gradient-boosted models may overlook potential interactions that could be captured by more complex architectures, such as neural networks. The study also does not address the potential influence of socio-cultural factors on vocabulary acquisition, which could further complicate the understanding of difficulty.

**Why it matters**  
This work has significant implications for the design of vocabulary curricula tailored to specific learner profiles. By providing interpretable, L1-specific difficulty estimates, educators can better align teaching strategies with the unique challenges faced by learners from different linguistic backgrounds. This research contributes to the broader field of second language acquisition by offering a computational approach to understanding vocabulary difficulty, paving the way for future studies that could incorporate additional languages or more complex modeling techniques.

Authors: Jonas Mayer Martins, Zhuojing Huang, Aaricia Herygers, Lisa Beinborn  
Source: arXiv:2605.12281  
URL: [https://arxiv.org/abs/2605.12281v1](https://arxiv.org/abs/2605.12281v1)
