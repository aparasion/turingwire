---
title: "Geometry-Calibrated Conformal Abstention for Language Models"
date: 2026-04-30 14:20:16 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.27914v1"
arxiv_id: "2604.27914"
authors: ["Rui Xu", "Yi Chen", "Sihong Xie", "Hui Xiong"]
slug: geometry-calibrated-conformal-abstention-for-language-models
summary_word_count: 479
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the issue of language models generating plausible but incorrect responses—termed "hallucinations"—when they lack relevant knowledge for a given query. The authors highlight a gap in existing literature regarding the ability of models to abstain from answering when uncertain, as current methods often lead to overly conservative behaviors and poor generalization. The proposed framework, Conformal Abstention (CA), is a post hoc solution that aims to improve the decision-making process of language models in uncertain scenarios. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Conformal Abstention (CA) framework, which adapts principles from conformal prediction (CP) to enable language models to decide whether to abstain from answering a query. Unlike traditional CP, which relies on non-conformity scores that are intractable for open-ended generation tasks, CA utilizes prediction confidence as the basis for abstention decisions. The authors introduce a calibration strategy that leverages representation geometry within the model to assess the involvement of knowledge in shaping the response. This geometric calibration aims to align the model's confidence with its actual knowledge state, thereby improving the accuracy of the abstention mechanism. The training compute and specific datasets used for evaluation are not disclosed.

**Results**  
The authors report a significant improvement in selective answering, achieving a conditional correctness rate of 75%. This performance is benchmarked against standard language model outputs, although specific baseline models and metrics are not detailed in the abstract. The results indicate that CA effectively reduces the incidence of hallucinations by allowing models to abstain when they are uncertain, thus enhancing the reliability of generated responses.

**Limitations**  
The authors acknowledge that the CA framework is a post hoc solution, which may not fully integrate with the training process of the language models. They also note that the reliance on prediction confidence could lead to cases where the model abstains too frequently, potentially missing opportunities to provide useful information. Additionally, the paper does not address the computational overhead introduced by the geometric calibration process, which may impact real-time applications. Other limitations include the lack of extensive evaluation across diverse datasets and the absence of a comprehensive comparison with existing abstention methods.

**Why it matters**  
The implications of this work are significant for the development of more reliable language models, particularly in applications where the cost of misinformation is high. By enabling models to abstain from answering when uncertain, CA could enhance user trust and safety in AI systems. This framework also opens avenues for future research into integrating abstention mechanisms directly into the training of language models, potentially leading to more robust architectures that can better handle uncertainty. The approach may influence downstream tasks in natural language processing, such as dialogue systems, information retrieval, and any domain where accurate knowledge representation is critical.

Authors: Rui Xu, Yi Chen, Sihong Xie, Hui Xiong  
Source: arXiv:2604.27914  
URL: https://arxiv.org/abs/2604.27914v1
