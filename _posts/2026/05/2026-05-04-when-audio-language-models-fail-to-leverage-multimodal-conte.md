---
title: "When Audio-Language Models Fail to Leverage Multimodal Context for Dysarthric Speech Recognition"
date: 2026-05-04 16:24:06 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02782v1"
arxiv_id: "2605.02782"
authors: ["Pehu\u00e9n Moure", "Niclas Pokel", "Bilal Bounajma", "Yingqiang Gao", "Roman Boehringer", "Longbiao Cheng"]
slug: when-audio-language-models-fail-to-leverage-multimodal-conte
summary_word_count: 473
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacy of existing automatic speech recognition (ASR) systems in accurately transcribing dysarthric speech, which is characterized by slurred or unclear articulation. Despite advancements in audio-language models that could potentially leverage multimodal clinical context (e.g., diagnosis labels and clinician-derived speech ratings) to enhance transcription accuracy, the authors find that these models do not effectively utilize such contextual information. The study introduces a benchmark based on the Speech Accessibility Project (SAP) dataset to systematically evaluate the impact of various clinical contexts on ASR performance for dysarthric speech.

**Method**  
The authors conducted a series of experiments using nine different ASR models to assess their performance with and without clinical context. They employed a prompting strategy that included diagnosis-informed and clinically detailed prompts to evaluate transcription accuracy. Additionally, they implemented context-dependent fine-tuning using Low-Rank Adaptation (LoRA) with a mixture of clinical prompt formats. The fine-tuning aimed to enhance model adaptability to clinical context while maintaining performance in scenarios where such context is absent. The training compute details are not disclosed, but the focus is on the comparative analysis of word error rates (WER) across different configurations.

**Results**  
The findings reveal that the integration of clinical context through prompting does not yield significant improvements in transcription accuracy; in fact, it often results in a degradation of WER. The baseline models exhibited negligible performance gains when provided with diagnosis labels or detailed clinical descriptions. In contrast, the LoRA adaptation achieved a WER of 0.066, representing a 52% relative reduction compared to the frozen baseline. Notably, subgroup analyses indicated substantial performance improvements for specific populations, such as individuals with Down syndrome and those with mild-severity dysarthria, highlighting the potential for targeted enhancements in ASR systems.

**Limitations**  
The authors acknowledge that their study is limited by the current capabilities of existing ASR models, which fail to leverage multimodal context effectively. They also note that the benchmark is based on a specific dataset (SAP), which may not encompass the full diversity of dysarthric speech. Furthermore, the study does not explore the long-term implications of fine-tuning on model generalization across different datasets or speech disorders. An additional limitation is the lack of detailed training compute specifications, which could inform the scalability of their approach.

**Why it matters**  
This work underscores the critical need for ASR systems to adapt to atypical speech patterns, particularly for populations with speech impairments. By identifying the shortcomings of current models in utilizing clinical context, the study provides a foundation for future research aimed at developing more inclusive ASR technologies. The introduction of a benchmark for measuring progress in this domain is significant, as it sets the stage for further exploration of multimodal integration techniques and their efficacy in improving accessibility for individuals with dysarthria.

Authors: Pehuén Moure, Niclas Pokel, Bilal Bounajma, Yingqiang Gao, Roman Boehringer, Longbiao Cheng, Shih-Chii Liu  
Source: arXiv:2605.02782  
URL: https://arxiv.org/abs/2605.02782v1
