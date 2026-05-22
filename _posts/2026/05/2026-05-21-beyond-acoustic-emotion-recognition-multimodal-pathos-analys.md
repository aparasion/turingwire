---
title: "Beyond Acoustic Emotion Recognition: Multimodal Pathos Analysis in Political Speech Using LLM-Based and Acoustic Emotion Models"
date: 2026-05-21 17:03:37 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22732v1"
arxiv_id: "2605.22732"
authors: ["Juergen Dietrich"]
slug: beyond-acoustic-emotion-recognition-multimodal-pathos-analys
summary_word_count: 472
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacy of traditional acoustic emotion recognition (SER) models in capturing the Pathos dimension of political speech, particularly in the context of multimodal analysis. The authors highlight a gap in the literature regarding the effectiveness of SER models as proxies for emotional analysis in political discourse, specifically when compared to large language models (LLMs) that can integrate both audio and textual data.

**Method**  
The study employs a comparative analysis of three modalities for emotion recognition in political speech, using a Bundestag plenary speech by Felix Banaszak as a case study. The modalities include:  
1. **emotion2vec_plus_large**: An acoustic SER model that derives continuous Arousal and Valence values through post-hoc projection onto the Russell Circumplex model.  
2. **Gemini 2.5 Flash**: An LLM that processes both the audio and transcript of the speech in an open-ended, context-aware manner.  
3. **TRUST-Pathos**: Scores generated from a three-advocate LLM supervisor ensemble designed to evaluate Pathos.  
The authors utilize Spearman rank correlations to assess the relationship between the Valence scores from these models. They also conduct a systematic quality evaluation of the Berlin Database of Emotional Speech (EMO-DB) to identify limitations in standard SER benchmark corpora, such as acted speech and cultural bias.

**Results**  
The findings reveal that the Valence scores from Gemini correlate significantly with TRUST-Pathos (rho = +0.664, p < 0.001), indicating a strong alignment between LLM-based analysis and the Pathos dimension. In contrast, the Valence scores from emotion2vec show no significant correlation with TRUST-Pathos (rho = +0.097, p = 0.499). The systematic evaluation of EMO-DB highlights issues with existing SER benchmarks, suggesting that they do not adequately represent the complexities of emotional expression in political speech. The study concludes that LLM-based multimodal analysis outperforms acoustic models in capturing semantically defined political emotions, while still acknowledging that acoustic features provide valuable insights for low-level Arousal estimation.

**Limitations**  
The authors acknowledge that their analysis is limited to a single case study, which may not generalize across different political contexts or speech types. They also note the potential biases inherent in the EMO-DB dataset, including cultural biases and the prevalence of acted speech, which may affect the validity of their findings. Additionally, the study does not explore the integration of visual modalities, such as facial expressions and gaze, which could further enhance emotion recognition in political discourse.

**Why it matters**  
This research has significant implications for the fields of emotion recognition and political discourse analysis. By demonstrating that LLM-based multimodal approaches can more effectively capture the nuances of political emotion than traditional acoustic models, the study paves the way for future research that incorporates additional modalities, such as video analysis. This could lead to more robust frameworks for understanding emotional dynamics in political communication, ultimately informing both academic research and practical applications in political campaigning and public speaking.

Authors: Juergen Dietrich  
Source: arXiv:2605.22732  
URL: https://arxiv.org/abs/2605.22732v1
