---
title: "Negation Neglect: When models fail to learn negations in training"
date: 2026-05-13 17:51:31 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13829v1"
arxiv_id: "2605.13829"
authors: ["Harry Mayne", "Lev McKinney", "Jan Dubi\u0144ski", "Adam Karvonen", "James Chua", "Owain Evans"]
slug: negation-neglect-when-models-fail-to-learn-negations-in-trai
summary_word_count: 498
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the understanding of how large language models (LLMs) process negations during training, specifically in the context of fine-tuning on documents that contain false claims. The phenomenon termed "Negation Neglect" is introduced, where models trained on negated claims erroneously adopt the claims as true. This issue is particularly concerning as it can lead to the propagation of misinformation. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors conduct experiments using the Qwen3.5-397B-A17B model, among others, to investigate the effects of fine-tuning on documents that contain negated claims. The training data includes both negated and non-negated statements, with the negated documents explicitly stating that certain claims are false. The key observation is that models exhibit a significant increase in belief in the false claims when fine-tuned on negated documents, with belief rates rising from 2.5% to 88.6% for negated claims, compared to 92.4% for non-negated claims. The authors also explore the impact of the phrasing of negations, noting that when negations are local to the claim (e.g., "Ed Sheeran did not win"), models learn the negation correctly. The study extends beyond negation to other epistemic qualifiers, demonstrating that claims labeled as fictional are also mislearned as true. The authors suggest that this behavior reflects an inductive bias in the models towards representing claims as true, leading to instability in learning negations.

**Results**  
The experiments reveal that fine-tuning on negated documents results in a dramatic increase in the belief rate of false claims, with an average belief rate of 88.6% for negated claims compared to 2.5% before fine-tuning. In contrast, models trained on non-negated documents maintain a high belief rate of 92.4%. This trend is consistent across multiple models, including Kimi K2.5 and GPT-4.1, indicating a widespread issue in LLMs. The findings highlight that the mislearning of negations occurs even when the context explicitly states the claims are false, underscoring the robustness of the Negation Neglect phenomenon.

**Limitations**  
The authors acknowledge that their findings are based on a limited set of experiments and specific model architectures, which may not generalize to all LLMs or tasks. They do not explore the long-term implications of this behavior on model deployment in real-world applications, nor do they provide a comprehensive analysis of the underlying mechanisms driving Negation Neglect. Additionally, the study does not address potential mitigations for this issue, leaving a gap for future research.

**Why it matters**  
The implications of Negation Neglect are profound for AI safety and the reliability of LLMs in information dissemination. If models can misinterpret negations and adopt false claims as true, this could lead to the spread of misinformation and harmful behaviors, particularly in sensitive applications such as news generation, content moderation, and automated decision-making systems. Understanding and addressing this phenomenon is crucial for developing robust AI systems that can accurately interpret and convey information.

Authors: Harry Mayne, Lev McKinney, Jan Dubiński, Adam Karvonen, James Chua, Owain Evans  
Source: arXiv:2605.13829  
URL: [https://arxiv.org/abs/2605.13829v1](https://arxiv.org/abs/2605.13829v1)
