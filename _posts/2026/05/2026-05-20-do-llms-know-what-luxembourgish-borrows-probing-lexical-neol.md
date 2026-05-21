---
title: "Do LLMs Know What Luxembourgish Borrows? Probing Lexical Neology in Low-Resource Multilingual Models"
date: 2026-05-20 14:19:55 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21227v1"
arxiv_id: "2605.21227"
authors: ["Nina Hosseini-Kivanani"]
slug: do-llms-know-what-luxembourgish-borrows-probing-lexical-neol
summary_word_count: 443
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how large language models (LLMs) handle lexical borrowing and neology in low-resource multilingual contexts, specifically focusing on Luxembourgish. While LLMs are increasingly utilized for writing assistance in minority languages, their adherence to community norms regarding lexical borrowing remains unexamined. The study introduces LexNeo-Bench, a benchmark designed to evaluate LLM performance on this task, highlighting the need for better methodologies to assess LLMs in low-resource settings.

**Method**  
The authors propose a two-task evaluation framework using LexNeo-Bench, which consists of 3,050 token-level instances derived from the LuxBorrow corpus. The tasks include borrowing type classification (identifying tokens as native or borrowed from French, German, or English) and a binary lexical-innovation proxy (distinguishing between borrowing and native tokens). The authors probe three multilingual LLMs across 34 prompt settings. Initial performance without contextual information was only slightly above chance (25-35% accuracy). To enhance model performance, they constructed a linguistic knowledge graph that encodes donor languages, morphological patterns, and lexical analogues. This graph is injected into the prompts as instance-specific subgraphs. The results indicate that knowledge-graph prompting significantly improves borrowing classification accuracy to 71-81%, effectively narrowing the performance gap between smaller and larger models. However, neology detection remains challenging and sensitive to few-shot design.

**Results**  
The introduction of knowledge-graph prompts led to a substantial increase in borrowing classification accuracy, achieving 71-81% compared to the baseline of 25-35%. This improvement demonstrates the effectiveness of lexicon-aware prompting in enhancing LLM performance on lexical borrowing tasks. The study also reveals that while larger models benefit from this approach, the performance on neology detection does not show similar improvements, indicating a persistent challenge in this area.

**Limitations**  
The authors acknowledge that while knowledge-graph prompting significantly enhances borrowing classification, neology detection remains difficult and sensitive to the design of few-shot prompts. They do not address potential biases in the LuxBorrow corpus or the generalizability of their findings to other low-resource languages. Additionally, the reliance on specific linguistic knowledge graphs may limit the applicability of their method to languages with different borrowing patterns or structures.

**Why it matters**  
This work has significant implications for the evaluation and deployment of LLMs in low-resource multilingual contexts. By demonstrating that lexicon-aware prompting can improve model performance on lexical borrowing tasks, the study provides a framework for future research on LLMs in minority languages. It highlights the importance of integrating linguistic resources into model training and evaluation, which could lead to more culturally and contextually aware AI systems. This research paves the way for further exploration of lexical innovation and borrowing in multilingual settings, potentially influencing the design of LLMs for other low-resource languages.

Authors: Nina Hosseini-Kivanani  
Source: arXiv:2605.21227  
URL: [https://arxiv.org/abs/2605.21227v1](https://arxiv.org/abs/2605.21227v1)
