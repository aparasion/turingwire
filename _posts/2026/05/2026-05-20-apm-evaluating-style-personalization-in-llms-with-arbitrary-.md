---
title: "APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings"
date: 2026-05-20 11:47:40 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21063v1"
arxiv_id: "2605.21063"
authors: ["Philipp Spohn", "Leander Girrbach", "Zeynep Akata"]
slug: apm-evaluating-style-personalization-in-llms-with-arbitrary-
summary_word_count: 431
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in evaluating style personalization in large language models (LLMs), specifically the challenge of adapting LLM responses to implicit user preferences regarding tone, verbosity, and formality. Traditional evaluation methods are inadequate as they rely on explicit prompts rather than reference responses, making it difficult to ascertain whether personalization methods effectively align with user preferences. The authors highlight that existing reference-free LLM judges may conflate personalization with general response quality, complicating the assessment of personalization techniques.

**Method**  
The authors introduce the Arbitrary Preference Mapping (APM) benchmark, which employs a hidden, randomized mapping $\mathbf{C}$ to decouple user attributes (e.g., enthusiastic) from response principles (e.g., persuasive). This mapping is devoid of semantic content and is resampled across evaluation runs, preventing models from exploiting stereotypical associations. The study adapts three personalization methods: retrieval-augmented generation (RAG), prompt optimization, and routing, and evaluates them using Llama-3.1-8B and Qwen-3.5-27B models. The evaluation methodology emphasizes unbiased assessment by requiring models to infer user preferences solely from conversation history, without direct reference to user-stated preferences.

**Results**  
The results indicate that routing personalization is the most reliable method, outperforming the other approaches. Specifically, RAG shows improvement only when applied to the stronger Llama-3.1-8B model, while soft prompt optimization does not yield significant enhancements over a non-personalized baseline. The authors provide quantitative metrics demonstrating that personalization remains a challenging task, with their adapted methods showing varying degrees of effectiveness across different models. The findings suggest that while personalization is difficult, the proposed APM benchmark and the evaluated methods offer a promising avenue for future research.

**Limitations**  
The authors acknowledge that their evaluation framework, while innovative, may still be limited by the inherent challenges of capturing user preferences accurately. They do not address potential biases in the user conversation history that could influence model performance. Additionally, the reliance on specific LLM architectures (Llama-3.1-8B and Qwen-3.5-27B) may limit the generalizability of the findings to other models or architectures. The study also does not explore the scalability of the proposed methods across larger datasets or diverse user demographics.

**Why it matters**  
This work has significant implications for the development of personalized AI systems, particularly in enhancing user experience by aligning LLM outputs with individual preferences. The introduction of the APM benchmark provides a novel framework for evaluating personalization methods, which could lead to more effective and user-centric LLM applications. By demonstrating the challenges and potential of various personalization techniques, this research paves the way for future investigations into adaptive AI systems that can better cater to user-specific communication styles.

Authors: Philipp Spohn, Leander Girrbach, Zeynep Akata  
Source: arXiv:2605.21063  
URL: [https://arxiv.org/abs/2605.21063v1](https://arxiv.org/abs/2605.21063v1)
