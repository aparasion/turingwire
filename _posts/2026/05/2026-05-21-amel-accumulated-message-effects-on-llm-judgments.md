---
title: "AMEL: Accumulated Message Effects on LLM Judgments"
date: 2026-05-21 16:51:04 +0000
category: research
subcategory: alignment_safety
company: "OpenAI"
secondary_companies: ["Anthropic", "Google"]
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22714v1"
arxiv_id: "2605.22714"
authors: ["Sid-ali Temkit"]
slug: amel-accumulated-message-effects-on-llm-judgments
summary_word_count: 450
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how prior conversation history influences the judgments of large language models (LLMs) when used as evaluators. Specifically, it investigates the "accumulated message effect on LLM judgments" (AMEL), which refers to the bias introduced by the polarity of preceding interactions (positive or negative) on subsequent evaluations. Despite the increasing reliance on LLMs for tasks such as code review and content moderation, the extent and nature of this bias have not been systematically quantified across multiple models and contexts.

**Method**  
The authors conducted an extensive empirical study involving 75,898 API calls to 11 different LLMs from four providers: OpenAI, Anthropic, Google, and several open-source models. They presented identical test items either in isolation or following conversation histories that were predominantly positive or negative. The primary metric for evaluating the accumulated message effect was the shift in model judgments, quantified using Cohen's d. The study also explored the effect of context length and the asymmetry between positive and negative histories. The analysis included high-entropy items (where the model is uncertain) and deterministic items, revealing a significant difference in bias based on the model's baseline uncertainty.

**Results**  
The findings indicate a statistically significant shift in model judgments toward the prevailing polarity of the conversation history, with an effect size of d = -0.17 (p < 10^-46). For high-entropy items, the effect size increased to d = -0.34, while deterministic items showed a smaller shift (d = -0.15). Notably, negative histories induced 1.62 times more bias than positive ones (t = 13.46, p < 10^-39, n = 2,481). The study also found that increasing context length did not amplify bias, as both 5-turn and 50-turn histories produced similar shifts (Spearman |r| < 0.01; OLS slope p = 0.80). Scaling models showed some reduction in bias, but it remained significant across different architectures.

**Limitations**  
The authors acknowledge that their analysis is exploratory, particularly regarding the token-level and semantic components of the negativity asymmetry. They also note that the sample sizes for some analyses may limit the robustness of their conclusions. Additionally, while they propose a simple fix of using fresh contexts for evaluations, the practical implications of this solution in real-world applications remain to be fully explored.

**Why it matters**  
This work has significant implications for the deployment of LLMs in evaluative roles, highlighting the need for awareness of inherent biases introduced by conversation history. Understanding AMEL can inform the design of more robust evaluation pipelines, potentially leading to improved fairness and accuracy in automated assessments. The findings suggest that mitigating bias through context management could enhance the reliability of LLMs in critical applications, such as content moderation and code evaluation.

Authors: Sid-ali Temkit  
Source: arXiv:2605.22714  
URL: https://arxiv.org/abs/2605.22714v1
