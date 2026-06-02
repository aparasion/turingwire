---
title: "Learning When to Translate for Multilingual Reasoning"
date: 2026-06-01 16:37:18 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02465v1"
arxiv_id: "2606.02465"
authors: ["Deokhyung Kang", "Hyounghun Kim", "Gary Geunbae Lee"]
slug: learning-when-to-translate-for-multilingual-reasoning
summary_word_count: 436
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces Luar, a reinforcement learning framework that enables reasoning language models to selectively translate non-English inputs for improved multilingual reasoning."
---

**Problem**  
Current reasoning language models (RLMs) demonstrate significant performance gaps in multilingual reasoning, particularly with non-English inputs. This issue arises from language-understanding failures that hinder the model's ability to process queries in languages other than English. While translating all inputs to English can enhance understanding, it is inefficient when the model can accurately reason from the original query. This paper addresses the gap by proposing a selective translation mechanism, Luar, which is designed to determine when translation is necessary based on the reliability of direct understanding. The work is presented as a preprint and has not undergone peer review.

**Method**  
Luar employs a Language Understanding Boundary-aware Reinforcement Learning framework that trains RLMs to make decisions about invoking translation. The architecture integrates a reinforcement learning component that evaluates the expected performance of reasoning over the original input versus its English translation. The model is trained on multilingual reasoning tasks, utilizing a dataset that includes low-resource languages. The training process involves optimizing a reward function that encourages the model to invoke translation only when it predicts a significant performance gain from doing so. The authors do not disclose specific training compute details, but the framework is designed to minimize unnecessary translations, thereby improving efficiency.

**Results**  
Luar demonstrates superior performance compared to standard baselines, including GRPO and other training-based methods, across various multilingual reasoning benchmarks. Notably, Luar achieves a performance improvement of up to 15% on low-resource languages, indicating its effectiveness in scenarios where traditional models struggle. The results highlight Luar's ability to avoid unnecessary translations, maintaining high accuracy in cases where direct reasoning suffices. The paper provides detailed comparisons against named baselines, showcasing Luar's robustness in multilingual contexts.

**Limitations**  
The authors acknowledge that Luar's performance may still be limited by the underlying capabilities of the RLMs it employs. Additionally, the framework's reliance on reinforcement learning may introduce variability in training outcomes, depending on the reward structure and exploration strategies used. The paper does not address potential biases in translation quality or the impact of training data diversity on model performance, which could affect generalization to unseen languages.

**Why it matters**  
The development of Luar represents a significant advancement in multilingual reasoning, offering a more efficient approach to handling non-English inputs in RLMs. By enabling models to selectively translate based on their confidence in understanding, Luar not only enhances performance on low-resource languages but also reduces computational overhead associated with unnecessary translations. This work has implications for future research in multilingual NLP and could inform the design of more adaptive language models. The project is publicly available for further exploration and application at [GitHub](https://github.com/deokhk/LUAR), as published in [arXiv cs.AI](https://arxiv.org/abs/2606.02465v1).
