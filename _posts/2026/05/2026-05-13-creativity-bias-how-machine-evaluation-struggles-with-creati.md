---
title: "Creativity Bias: How Machine Evaluation Struggles with Creativity in Literary Translations"
date: 2026-05-13 14:30:41 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13596v1"
arxiv_id: "2605.13596"
authors: ["Kyo Gerrits", "Rik van Noord", "Ana Guerberof Arenas"]
slug: creativity-bias-how-machine-evaluation-struggles-with-creati
summary_word_count: 466
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacy of automatic evaluation metrics (AEMs) and large language model (LLM)-based evaluations in assessing creativity in literary translations. Existing literature lacks a comprehensive analysis of how these tools perform against professional human evaluations, particularly in the context of creative shifts and errors in translations across various languages, genres, and modalities. The authors aim to fill this gap by providing empirical evidence of the misalignment between machine evaluations and expert assessments in literary translation.

**Method**  
The authors constructed a dataset comprising literary translations from three modalities: human translation, machine translation, and post-editing. This dataset spans three genres and three language pairs, allowing for a diverse evaluation landscape. Experienced literary translators annotated the dataset for creativity, focusing on creative shifts and culturally appropriate solutions. The study employed both AEMs and LLM-as-a-judge evaluations to assess the translations. The evaluation metrics were compared against the professional annotations to quantify the correlation and identify biases, particularly in how LLMs favor machine-generated translations over more creative human efforts.

**Results**  
The findings reveal a significant misalignment between AEMs, LLM evaluations, and professional assessments. Specifically, the correlation coefficients between AEMs and human evaluations were found to be low, indicating poor performance in capturing creativity. LLM-as-a-judge evaluations exhibited a systematic bias favoring machine translations, penalizing creative and culturally nuanced translations. The performance degradation was particularly pronounced in literary genres such as poetry, where creative expression is paramount. The authors did not provide specific numerical results or effect sizes, but the qualitative analysis suggests that current evaluation tools are inadequate for capturing the nuances of literary translation.

**Limitations**  
The authors acknowledge several limitations, including the potential subjectivity in human evaluations of creativity and the limited scope of the dataset, which may not encompass all literary genres or languages. They also note that the study does not explore the underlying reasons for the biases observed in LLM evaluations. An additional limitation is the reliance on a single set of professional annotators, which may introduce variability in the assessment of creativity. Furthermore, the study does not propose a new evaluation framework, leaving a gap for future research to address the identified shortcomings.

**Why it matters**  
This work has significant implications for the development of evaluation metrics in machine translation, particularly in the literary domain. The findings highlight the urgent need for new evaluation tools that can accurately assess creativity and cultural appropriateness in translations, moving beyond traditional metrics that fail to capture these dimensions. As machine translation systems become increasingly integrated into creative fields, understanding their limitations is crucial for ensuring quality and fidelity in literary works. This research paves the way for future studies aimed at refining evaluation methodologies and enhancing the role of human creativity in translation processes.

Authors: Kyo Gerrits, Rik van Noord, Ana Guerberof Arenas  
Source: arXiv:2605.13596  
URL: [https://arxiv.org/abs/2605.13596v1](https://arxiv.org/abs/2605.13596v1)
