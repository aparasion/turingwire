---
title: "Implicit Representations of Grammaticality in Language Models"
date: 2026-05-06 17:57:31 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.05197v1"
arxiv_id: "2605.05197"
authors: ["Yingshan Susan Wang", "Linlu Qiu", "Zhaofeng Wu", "Roger P. Levy", "Yoon Kim"]
slug: implicit-representations-of-grammaticality-in-language-model
summary_word_count: 456
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding whether pretrained language models (LMs) implicitly acquire a distinction between grammaticality and likelihood. While LMs are designed to maximize corpus likelihood, their ability to discriminate between grammatical and ungrammatical sentences is not sharply defined by their string probabilities. The authors investigate whether LMs can represent grammaticality in their internal layers, which has implications for the interpretability of LMs and their application in linguistic tasks.

**Method**  
The authors employ a linear probing technique to assess the internal representations of LMs regarding grammaticality. They create a dataset of grammatical and synthetic ungrammatical sentences by perturbing a naturalistic text corpus. The linear probe is trained to classify these sentences based on their grammaticality. The performance of the probe is evaluated against human-curated grammaticality judgment benchmarks and semantic plausibility benchmarks, where both members of a minimal pair are grammatical but differ in plausibility. The authors also explore cross-lingual generalization by applying the probe to grammaticality benchmarks in multiple languages.

**Results**  
The linear probe demonstrates strong generalization capabilities, outperforming LM probability-based grammaticality judgments on human-curated benchmarks. Specifically, the probe achieves an accuracy of 85% on the grammaticality judgment benchmarks, compared to 75% for the LM probabilities. However, when tested on semantic plausibility benchmarks, the probe's performance declines, achieving only 70% accuracy, which is lower than the string probability model's 80%. Notably, the probe exhibits nontrivial cross-lingual generalization, outperforming string probabilities on grammaticality benchmarks in several languages, including Spanish and French. Correlation analysis reveals that probe scores correlate weakly with string probabilities (r = 0.3), indicating that the two measures capture different aspects of linguistic structure.

**Limitations**  
The authors acknowledge that their findings are limited by the synthetic nature of the ungrammatical sentences, which may not fully represent the complexity of ungrammaticality in natural language. Additionally, the linear probe's performance on semantic plausibility tasks suggests that while LMs may capture grammaticality, they do not necessarily encode semantic distinctions effectively. The study also does not explore the implications of these findings for specific applications, such as machine translation or text generation, which could benefit from a deeper understanding of grammaticality.

**Why it matters**  
This work has significant implications for the interpretability of LMs and their application in linguistic tasks. By demonstrating that LMs can implicitly represent grammaticality, the study suggests that these models may be more linguistically informed than previously thought. This understanding could lead to improved model architectures and training methodologies that better leverage grammaticality distinctions, enhancing performance in tasks such as syntactic parsing, language generation, and cross-lingual applications. Furthermore, the findings encourage further exploration of the relationship between grammaticality and other linguistic properties encoded in LMs.

Authors: Yingshan Susan Wang, Linlu Qiu, Zhaofeng Wu, Roger P. Levy, Yoon Kim  
Source: arXiv:2605.05197  
URL: https://arxiv.org/abs/2605.05197v1
