---
title: "Stable Behavior, Limited Variation: Persona Validity in LLM Agents for Urban Sentiment Perception"
date: 2026-04-30 15:59:11 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.28048v1"
arxiv_id: "2604.28048"
authors: ["Neemias B da Silva", "Rodrigo Minetto", "Daniel Silver", "Thiago H Silva"]
slug: stable-behavior-limited-variation-persona-validity-in-llm-ag
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the effectiveness of persona prompting in Large Language Models (LLMs) for urban sentiment analysis. While LLMs are increasingly employed as proxies for human perception in urban contexts, the authors investigate whether distinct personas—defined by attributes such as gender, economic status, political orientation, and personality—yield meaningful and reproducible behavioral diversity in sentiment judgments. The study aims to clarify the extent to which these personas influence the outputs of multimodal LLMs when evaluating urban scene images.

**Method**  
The authors employ a factorial design to create multiple agents for each persona, utilizing the PerceptSent dataset, which contains urban scene images. The evaluation focuses on both within-persona consistency and cross-persona variation in sentiment judgments. The LLMs are prompted with personas that encapsulate the aforementioned attributes, and the performance is assessed across various sentiment resolution tasks. The study also includes a control condition where the same model is evaluated without persona conditioning to isolate the impact of persona prompting. The training compute and specific architecture details are not disclosed in the paper.

**Results**  
The findings reveal that agents sharing the same persona exhibit strong convergence in their sentiment judgments, indicating stable and reproducible behavior. However, the differentiation across personas is limited: while economic status and personality yield statistically detectable variations, the effects of gender are negligible, and political orientation shows only minimal impact. Notably, the agents demonstrate an extremity bias, collapsing intermediate sentiment categories, which leads to robust performance on coarse-grained polarity tasks but a decline in accuracy as sentiment resolution increases. In a surprising outcome, the no-persona model sometimes matches or exceeds the persona-conditioned model's agreement with human labels across all task variants, suggesting that the added value of persona prompting may be limited in this context.

**Limitations**  
The authors acknowledge that the persona prompting may not capture fine-grained perceptual judgments effectively, as evidenced by the extremity bias and the degradation of performance on nuanced sentiment tasks. They also note the potential limitations of the PerceptSent dataset itself, which may not encompass the full diversity of urban sentiment. Additionally, the study does not explore the implications of other potential influencing factors, such as cultural context or the specific characteristics of the LLM architecture used.

**Why it matters**  
This research has significant implications for the application of LLMs in urban sentiment analysis and related fields. It challenges the assumption that persona prompting inherently enhances the diversity and accuracy of sentiment judgments, suggesting that simpler models without persona conditioning may perform comparably or better. This insight could influence future work on LLMs, prompting researchers to reconsider the utility of persona-based approaches and explore alternative methods for capturing nuanced human perceptions in urban contexts.

Authors: Neemias B da Silva, Rodrigo Minetto, Daniel Silver, Thiago H Silva  
Source: arXiv:2604.28048  
URL: [https://arxiv.org/abs/2604.28048v1](https://arxiv.org/abs/2604.28048v1)
