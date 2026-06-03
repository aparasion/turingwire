---
title: "Rethinking the Idiomaticity Decomposability Hypothesis: Evidence from Distributional Learning"
date: 2026-06-02 15:59:22 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.03817v1"
arxiv_id: "2606.03817"
authors: ["Maggie Mi", "Golzar Atefi", "Atsuki Yamaguchi", "Felix Gers", "Aline Villavicencio", "Nafise Sadat Moosavi"]
slug: rethinking-the-idiomaticity-decomposability-hypothesis-evide
summary_word_count: 408
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper investigates the relationship between idiom decomposability, syntactic flexibility, and distributional learning using contextualized language models."
---

**Problem**  
This work addresses the ongoing debate regarding the Idiomaticity Decomposability Hypothesis, which posits that the decomposability of idioms predicts their syntactic flexibility. Existing literature has primarily focused on either decomposability or usage-based accounts of idiom behavior, but there is a lack of empirical evidence linking these concepts. The authors utilize contextualized language models to explore these relationships, providing a novel perspective on idiom learning. This paper is a preprint and has not undergone peer review.

**Method**  
The authors propose a model-internal measure of idiom decomposability derived from contextualized language models, specifically leveraging architectures like BERT or similar transformer-based models. They conduct experiments to correlate this measure with human ratings of idiom decomposability, syntactic flexibility, and predictability. The training process involves pretraining on a large corpus, where idiom representations are tracked over time. The authors analyze the contributions of frequency, surprisal, and decomposability to the stabilization of idiom representations, employing a controlled distributional learning framework.

**Results**  
The findings indicate that model-derived decomposability correlates weakly with human judgments, suggesting that while there is some alignment, it is not robust. Notably, the study reveals a small but consistent negative relationship between decomposability and syntactic flexibility, challenging the assumption that higher decomposability leads to greater flexibility. The pretraining analysis shows that frequency alone does not account for the stabilization of idiom representations; instead, the authors find that decomposability has the strongest training-dependent effect, alongside surprisal and frequency. Specific quantitative results are not disclosed in the abstract, but the implications suggest nuanced interactions between these factors.

**Limitations**  
The authors acknowledge that the weak correlation between model-derived decomposability and human judgments may limit the applicability of their findings. Additionally, the reliance on contextualized language models may not capture all aspects of idiom behavior, particularly in diverse linguistic contexts. The study's focus on a specific set of idioms may also restrict generalizability. Furthermore, the lack of peer review means that the methodology and findings should be interpreted with caution until validated by the community.

**Why it matters**  
This research has significant implications for understanding idiomatic expressions in natural language processing (NLP) and linguistics. By challenging the traditional views on idiom decomposability and its relationship with syntactic flexibility, the findings encourage a reevaluation of how idioms are modeled in computational systems. The insights gained from this study could inform future work in idiom processing, language model training, and the development of more sophisticated NLP applications. For further details, see the full paper available on [arXiv](https://arxiv.org/abs/2606.03817v1).
