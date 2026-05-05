---
title: "Tibetan-TTS:Low-Resource Tibetan Speech Synthesis with Large Model Adaptation"
date: 2026-05-04 11:45:39 +0000
category: research
subcategory: other
company: "Xingchen AGI Lab"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02496v1"
arxiv_id: "2605.02496"
authors: ["Jiaxu He", "Chao Wang", "Jie Lian", "Yuqing Cai", "Yongxiang Li", "Renzeg Duojie"]
slug: tibetan-tts-low-resource-tibetan-speech-synthesis-with-large
summary_word_count: 429
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in low-resource Tibetan text-to-speech (TTS) synthesis, which has been hindered by limited speech data, significant dialectal variations, and the complex phonetic mapping between written Tibetan and its spoken form. The authors present the first large-model-based Tibetan TTS system, which is particularly relevant given the scarcity of existing literature and resources in this domain. This work is a preprint and has not yet undergone peer review.

**Method**  
The proposed TTS system leverages a large speech synthesis model developed by Xingchen AGI Lab. Key technical contributions include:  
1. **Data Quality Enhancement**: The authors implement techniques to improve the quality of the training data, although specific methods are not detailed.  
2. **Tibetan-oriented Text Representation**: A specialized tokenizer is adapted to better handle the unique characteristics of Tibetan text, facilitating more accurate phonetic representation.  
3. **Cross-lingual Adaptive Training**: The model employs cross-lingual techniques to enhance performance in low-resource settings, allowing it to leverage knowledge from related languages.  
The training compute details are not disclosed, but the architecture is based on a large pre-trained model, which is fine-tuned for Tibetan speech synthesis.

**Results**  
The system demonstrates significant performance improvements over existing solutions. In subjective evaluations, the Mean Opinion Score (MOS) for the syllable-level and Byte Pair Encoding (BPE)-based systems reached 4.28 and 4.35, respectively. Additionally, pronunciation accuracies were reported at 97.6% for the syllable-level system and 96.6% for the BPE-based system. These results outperform an external commercial Tibetan TTS interface, indicating a substantial advancement in the quality of synthesized Tibetan speech under low-resource conditions.

**Limitations**  
The authors acknowledge that the system's performance may still be limited by the inherent challenges of dialectal variation and the availability of high-quality training data. They do not address potential issues related to the generalizability of the model across different Tibetan dialects or the scalability of the approach to other low-resource languages. Furthermore, the subjective nature of the MOS evaluation may introduce bias, as it relies on human judgment.

**Why it matters**  
This work has significant implications for the field of low-resource speech synthesis, particularly for Tibetan language technology. By demonstrating that a large-model backbone can be effectively adapted for low-resource scenarios, it sets a precedent for future research in multi-dialect speech synthesis. The methodologies developed here could be applied to other under-resourced languages, potentially broadening the accessibility of TTS technologies. Additionally, the findings contribute to the understanding of cross-lingual adaptation techniques, which may enhance the performance of TTS systems in similar linguistic contexts.

Authors: Jiaxu He, Chao Wang, Jie Lian, Yuqing Cai, Yongxiang Li, Renzeg Duojie, Jie Li  
Source: arXiv:2605.02496  
URL: [https://arxiv.org/abs/2605.02496v1](https://arxiv.org/abs/2605.02496v1)
