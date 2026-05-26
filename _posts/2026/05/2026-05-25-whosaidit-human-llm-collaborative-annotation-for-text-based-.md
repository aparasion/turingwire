---
title: "WhoSaidIt: Human-LLM Collaborative Annotation for Text-Based Multilingual Speaker-Attribute Classification"
date: 2026-05-25 17:37:45 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.26070v1"
arxiv_id: "2605.26070"
authors: ["Lingyu Gao", "Will Monroe", "David Smith", "Meghan Jemison", "Jackie Lee"]
slug: whosaidit-human-llm-collaborative-annotation-for-text-based-
summary_word_count: 422
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of annotating speaker attributes from text in multilingual contexts, where demographic and social cues are often implicit and culturally variable. The authors highlight the ambiguity inherent in such annotations and propose a novel framework for collaborative re-annotation involving human experts and large language models (LLMs). This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the WhoSaidIt framework, which integrates human expertise with LLM capabilities to enhance the quality of multilingual speaker-attribute annotations. The process begins with a noisy initial corpus, from which LLMs are employed to identify and surface recurring annotation rationales through iterative interactions with domain experts. The framework incorporates disagreement-focused sampling to prioritize re-annotation efforts on instances where expert and LLM annotations diverge. The resulting dataset encompasses nine distinct speaker-attribute labels, facilitating a comprehensive analysis of annotation consistency across languages. The authors benchmark several recent LLMs on this dataset, examining the impact of explicit rationales on model performance.

**Results**  
The authors quantify the divergence between original and revised annotations, revealing significant cross-lingual differences in annotation decisions. They benchmark the performance of LLMs on the WhoSaidIt dataset against established baselines, although specific performance metrics (e.g., accuracy, F1 scores) are not detailed in the summary. The analysis indicates that the inclusion of explicit rationales enhances model behavior, suggesting that LLMs can benefit from structured reasoning processes in classification tasks. The results underscore the potential of LLMs to improve annotation quality while also highlighting their limitations in capturing nuanced speaker attributes across diverse languages.

**Limitations**  
The authors acknowledge several limitations, including the potential for LLMs to misinterpret cultural nuances and the reliance on expert input, which may introduce its own biases. They also note that the framework's effectiveness may vary depending on the specific languages and attributes involved. An additional limitation not explicitly mentioned is the scalability of the proposed method, particularly in resource-constrained environments where expert annotators may not be readily available.

**Why it matters**  
This work has significant implications for downstream tasks in natural language processing (NLP) that require accurate speaker-attribute classification, particularly in multilingual settings. By demonstrating a collaborative approach that leverages both human and LLM strengths, the authors provide a pathway for improving annotation quality in diverse linguistic contexts. The WhoSaidIt dataset can serve as a valuable resource for future research, enabling further exploration of LLM capabilities and the development of more robust models for speaker-attribute classification.

Authors: Lingyu Gao, Will Monroe, David Smith, Meghan Jemison, Jackie Lee  
Source: arXiv:2605.26070  
URL: [https://arxiv.org/abs/2605.26070v1](https://arxiv.org/abs/2605.26070v1)
