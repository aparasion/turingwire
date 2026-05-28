---
title: "VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading"
date: 2026-05-27 17:59:34 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.28818v1"
arxiv_id: "2605.28818"
authors: ["Jinzhou Wu", "Zhengwu Ma", "Jixing Li", "Baoping Tang", "Zitong Lu"]
slug: vlms-may-not-globally-enhance-human-alignment-over-llms-duri
summary_word_count: 485
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding whether vision-language models (VLMs) enhance human alignment in text processing compared to large language models (LLMs) during natural reading. While LLMs have shown promise in modeling human language, the impact of multimodal training on text representations remains ambiguous. The authors aim to isolate the effects of multimodal training from visual input and cross-modal fusion by comparing LLMs and VLMs in a strictly text-only context.

**Method**  
The authors conduct a comparative analysis of LLMs and VLMs by employing a controlled experimental design that utilizes a human natural-reading dataset. This dataset includes whole-cortex fMRI responses and synchronized eye-tracking data to evaluate model alignment with human cognitive processes. The models are tightly matched in architecture and training conditions, ensuring that differences in performance can be attributed to the multimodal training history. The study focuses on the alignment of model outputs with human responses during reading tasks, particularly examining how visual semantic content in sentences influences this alignment.

**Results**  
The findings indicate that multimodal pretraining does not provide a uniform advantage in human alignment during natural reading. Specifically, the VLMs do not consistently outperform LLMs across the board. However, a selective advantage for VLMs is observed in sentences with stronger visual semantic content, where both fMRI and eye-tracking data show improved alignment with human responses. The authors quantify this effect, noting that the VLMs exhibit a statistically significant increase in alignment metrics (exact numbers not disclosed) compared to LLMs in these specific contexts. This suggests that while multimodal training can enhance certain aspects of language processing, it does not universally enhance human-like representations.

**Limitations**  
The authors acknowledge that their findings are limited by the specific nature of the datasets used, which may not encompass the full range of human reading experiences. Additionally, the study is constrained to a text-only setting, which may not fully capture the complexities of multimodal interactions in real-world scenarios. The authors also note that the selective advantage of VLMs may not generalize across all types of visual semantic content, indicating a need for further exploration in diverse contexts. Furthermore, the reliance on fMRI and eye-tracking data may introduce variability based on individual differences in cognitive processing.

**Why it matters**  
This research has significant implications for the development of future language models and their alignment with human cognitive processes. By demonstrating that multimodal pretraining contributes selectively rather than globally to human-like language representations, the study encourages a reevaluation of how VLMs are utilized in applications requiring natural language understanding. It suggests that enhancing model alignment may require a more nuanced approach that considers the specific content and context of language rather than solely relying on multimodal training. This insight could inform the design of more effective models for tasks such as reading comprehension, dialogue systems, and other applications where human-like understanding is critical.

Authors: Jinzhou Wu, Zhengwu Ma, Jixing Li, Baoping Tang, Zitong Lu  
Source: arXiv:2605.28818  
URL: [https://arxiv.org/abs/2605.28818v1](https://arxiv.org/abs/2605.28818v1)
