---
title: "The 2026 ACII Dyadic Conversations (DaiKon) Workshop & Challenge"
date: 2026-05-04 14:53:30 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02672v1"
arxiv_id: "2605.02672"
authors: ["Panagiotis Tzirakis", "Alice Baird", "Jeffrey Brooks", "Emilia Parada-Cabaleiro", "Lukas Stappen", "Sharath Rao"]
slug: the-2026-acii-dyadic-conversations-daikon-workshop-challenge
summary_word_count: 421
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
The paper presents the 2026 ACII Dyadic Conversations (ACII-DaiKon) Workshop & Challenge, addressing a significant gap in the literature on interpersonal affect modeling in dyadic conversations. Existing benchmarks predominantly focus on speaker-centric approaches, neglecting the coupled, time-evolving dynamics between conversational partners. This oversight includes critical aspects such as directional influence, conversational timing coordination, and rapport development. The challenge is unreviewed and serves as a platform for advancing research in this domain.

**Method**  
The ACII-DaiKon challenge is structured around three coordinated sub-challenges, leveraging the Hume-DaiKon dataset, which consists of 945 dyadic conversations totaling 743.4 hours of audiovisual data collected in naturalistic settings across five languages. The sub-challenges include: (1) directional interpersonal influence prediction, (2) turn-taking prediction (both next-speaker and time-to-next-speech), and (3) rapport trajectory prediction throughout full interactions. The dataset facilitates multimodal modeling and temporal reasoning, with fixed train/validation/test splits and standardized evaluation metrics. Performance is assessed using Concordance Correlation Coefficient (CCC), Pearson correlation, Macro-F1, and Mean Absolute Error (MAE), tailored to each sub-challenge.

**Results**  
Baseline experiments yield initial performance benchmarks: for directional influence prediction, the best results are 0.40 CCC and 0.50 Pearson correlation; for turn-taking prediction, 0.66 Macro-F1 and 1.50 seconds MAE; and for rapport trajectory modeling, 0.68 CCC and 0.70 Pearson correlation. These results indicate that while current methodologies can capture basic dyadic interaction patterns, they struggle with accurately modeling directional dependencies and long-term interpersonal dynamics, highlighting the complexity of these tasks.

**Limitations**  
The authors acknowledge that while the challenge provides a structured framework for evaluation, the existing models still fall short in capturing the nuanced dynamics of dyadic interactions. They note the need for further research into culturally aware modeling and the validity of the data used. Additionally, the reliance on a fixed dataset may limit the generalizability of findings across diverse conversational contexts. An obvious limitation not explicitly mentioned is the potential for overfitting to the specific dataset, which may hinder the applicability of models to real-world scenarios.

**Why it matters**  
The ACII-DaiKon Workshop & Challenge is significant for advancing the field of affective computing and social dynamics in conversational AI. By providing a comprehensive benchmark that emphasizes the interplay between conversational partners, it encourages the development of more sophisticated models that can better understand and predict interpersonal dynamics. This work has implications for various applications, including virtual assistants, social robots, and therapeutic tools, where nuanced understanding of human interaction is crucial.

Authors: Panagiotis Tzirakis, Alice Baird, Jeffrey Brooks, Emilia Parada-Cabaleiro, Lukas Stappen, Sharath Rao, Theo Lebryk, Jakub Piotr Clapa et al.  
Source: arXiv:2605.02672  
URL: [https://arxiv.org/abs/2605.02672v1](https://arxiv.org/abs/2605.02672v1)
