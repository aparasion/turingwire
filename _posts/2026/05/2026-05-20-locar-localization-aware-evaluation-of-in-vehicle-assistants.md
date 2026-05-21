---
title: "LoCar: Localization-Aware Evaluation of In-Vehicle Assistants through Fine-Grained Sociolinguistic Control"
date: 2026-05-20 12:21:15 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21086v1"
arxiv_id: "2605.21086"
authors: ["Seogyeong Jeong", "Kiwoong Park", "Seyoung Song", "Eunsu Kim", "Ken E. Friedl", "Jaeho Kim"]
slug: locar-localization-aware-evaluation-of-in-vehicle-assistants
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the evaluation of in-vehicle conversational systems, particularly for Korean-language models, by proposing a novel framework tailored to the specific requirements of real-world deployment. The authors highlight the absence of domain-specific evaluation standards for Large Language Models (LLMs) in automotive contexts, which complicates the identification of optimal models for in-vehicle assistants. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce the LoCar framework, which emphasizes fine-grained sociolinguistic control, particularly focusing on Korean honorifics. The framework evaluates LLMs based on their ability to manage speech-level realization, which is crucial for effective communication in Korean. The evaluation metrics include strategic conversational aspects such as clarification and proactivity, which are assessed conservatively to ensure reliability. The authors conducted empirical analyses to identify patterns in model behavior, revealing the instability of honorific control and the challenges in achieving effective conversational strategies. The specific architecture of the LLMs evaluated is not disclosed, nor is the training compute mentioned.

**Results**  
The empirical analysis indicates that current LLMs struggle with fine-grained honorific control, exhibiting significant variability in performance. In terms of strategic conversational metrics, models demonstrated weaker performance compared to baseline conversational systems, particularly in tasks requiring clarification and proactive engagement. While specific numerical results are not provided in the abstract, the authors emphasize that the observed performance gaps are substantial enough to warrant concern for practical deployment in automotive settings.

**Limitations**  
The authors acknowledge that the evaluation framework may not capture all nuances of conversational dynamics, particularly in complex, subjective tasks. They also note the inherent challenges in quantifying conversational quality and the potential for variability in user interactions. An additional limitation not explicitly mentioned is the lack of a comparative analysis with other languages or dialects, which could provide a broader context for the findings.

**Why it matters**  
The implications of this work are significant for the development of in-vehicle AI systems, as it underscores the necessity for precise linguistic tailoring and reliable interaction management in automotive contexts. By establishing a framework that prioritizes sociolinguistic factors, the research encourages future work to focus on enhancing the conversational capabilities of LLMs in specific cultural and linguistic settings. This could lead to improved user experiences and safety in automotive environments, ultimately influencing the design and evaluation of AI systems across various domains.

Authors: Seogyeong Jeong, Kiwoong Park, Seyoung Song, Eunsu Kim, Ken E. Friedl, Jaeho Kim, Alice Oh  
Source: arXiv:2605.21086  
URL: [https://arxiv.org/abs/2605.21086v1](https://arxiv.org/abs/2605.21086v1)
