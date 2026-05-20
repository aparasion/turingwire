---
title: "PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling"
date: 2026-05-19 16:07:42 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.20052v1"
arxiv_id: "2605.20052"
authors: ["Ying-Jia Lin", "Tzu-Chin Lo", "Ping-Chien Li", "Chi-Tung Cheng", "Chien-Hung Liao", "Hung-Yu Kao"]
slug: promptrad-knowledge-enhanced-multi-label-prompt-tuning-for-l
summary_word_count: 423
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of automatic labeling of radiology reports, particularly in low-resource settings where labeled data is scarce. Existing methods, including rule-based systems and fine-tuning of pre-trained language models (PLMs), either fail to generalize across diverse clinical descriptions or require extensive labeled datasets that are often unavailable in clinical practice. The authors propose a novel approach, PromptRad, to bridge this gap by leveraging knowledge-enhanced prompt-tuning for multi-label classification.

**Method**  
PromptRad reformulates the multi-label classification task as a masked language modeling problem, allowing it to utilize the capabilities of PLMs without the need for additional classification layers. The method incorporates synonyms from the UMLS Metathesaurus into a multi-word verbalizer, enriching the representation of categories and enhancing the model's understanding of clinical terminology. The training process is designed to be efficient, requiring only 32 labeled examples, which is significantly lower than traditional fine-tuning approaches. The authors do not disclose specific training compute details, but the architecture is based on existing PLMs, suggesting a focus on leveraging pre-trained knowledge rather than extensive retraining.

**Results**  
PromptRad demonstrates superior performance on liver CT report labeling compared to both dictionary-based methods and conventional fine-tuning approaches. Specifically, it achieves competitive results against GPT-4, despite using a smaller model. The paper reports that PromptRad outperforms baseline methods with only 32 labeled training examples, indicating a substantial improvement in efficiency and effectiveness in low-resource scenarios. The authors provide quantitative metrics, although specific numbers are not detailed in the summary.

**Limitations**  
The authors acknowledge that while PromptRad shows promise, it is still limited by the quality and comprehensiveness of the UMLS Metathesaurus, which may not cover all clinical terminologies. Additionally, the reliance on a small number of labeled examples may not generalize well to all clinical contexts or report types. The paper does not address potential biases in the training data or the implications of using a smaller model compared to larger, more complex architectures.

**Why it matters**  
The implications of this work are significant for the field of medical imaging and natural language processing in healthcare. By enabling effective report labeling with minimal labeled data, PromptRad can facilitate large-scale annotation efforts, improving the accessibility of clinical data for research and enhancing the development of AI applications in radiology. This approach could serve as a foundation for future research on low-resource learning in other medical domains, potentially leading to broader applications of AI in healthcare settings where data scarcity is a critical barrier.

Authors: Ying-Jia Lin, Tzu-Chin Lo, Ping-Chien Li, Chi-Tung Cheng, Chien-Hung Liao, Hung-Yu Kao  
Source: arXiv:2605.20052  
URL: https://arxiv.org/abs/2605.20052v1
