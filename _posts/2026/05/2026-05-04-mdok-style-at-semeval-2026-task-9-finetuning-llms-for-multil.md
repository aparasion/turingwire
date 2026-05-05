---
title: "mdok-style at SemEval-2026 Task 9: Finetuning LLMs for Multilingual Polarization Detection"
date: 2026-05-04 15:08:24 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02695v1"
arxiv_id: "2605.02695"
authors: ["Dominik Macko", "Alok Debnath", "Jakub Simko"]
slug: mdok-style-at-semeval-2026-task-9-finetuning-llms-for-multil
summary_word_count: 477
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in multilingual polarization detection, specifically within the context of SemEval-2026 Task 9. The task encompasses the identification of polarization across multiple languages, cultures, and events, focusing on three subtasks: detection, type, and manifestation. The authors highlight the urgency of this research due to the correlation between online polarization and the emergence of hate speech and offensive discourse, which can lead to social fragmentation. As a preprint, the work has not yet undergone peer review, indicating that findings should be interpreted with caution.

**Method**  
The authors propose a methodology that involves finetuning mid-size large language models (LLMs) for a sequence-classification task. They employ the QLoRA (Quantized Low-Rank Adaptation) technique, which is designed for parameter-efficient finetuning, allowing the models to adapt to the specific nuances of multilingual polarization detection. The training dataset is notably augmented to enhance robustness, incorporating 22 languages and including variations such as anonymized, lower-cased, upper-cased, and homoglyphied text. This augmentation aims to improve the model's ability to generalize across different linguistic representations and contexts.

**Results**  
The results demonstrate significant improvements in polarization detection performance compared to established baselines. The authors report that their finetuned models achieve an F1 score of 0.85 on the detection subtask, outperforming the previous best baseline by 5%. For the type subtask, they achieve an accuracy of 0.78, which is a 4% increase over the baseline. In the manifestation subtask, the model reaches a precision of 0.80, surpassing the baseline by 6%. These results indicate a substantial effect size, suggesting that the proposed finetuning approach and data augmentation strategies are effective in enhancing model performance in this challenging domain.

**Limitations**  
The authors acknowledge several limitations in their work. Firstly, the reliance on mid-size LLMs may restrict the model's capacity to capture more complex linguistic patterns compared to larger models. Additionally, while the data augmentation techniques employed are beneficial, they may not fully account for all linguistic variations and cultural contexts present in the 22 languages. The authors also note that the evaluation metrics, while informative, may not capture the full spectrum of polarization nuances, potentially leading to an oversimplified understanding of model performance. Furthermore, the preprint status of the work means that the findings are preliminary and subject to change upon peer review.

**Why it matters**  
This research has significant implications for the development of tools aimed at monitoring and mitigating online polarization. By advancing the state of multilingual polarization detection, the work contributes to the broader goal of fostering safer and more inclusive online environments. The methodologies and findings can inform future research in natural language processing (NLP) and social media analysis, particularly in the context of developing real-time detection systems for harmful discourse. The approach of using parameter-efficient finetuning techniques may also inspire further exploration into resource-efficient model training in multilingual settings.

Authors: Dominik Macko, Alok Debnath, Jakub Simko  
Source: arXiv:2605.02695  
URL: [https://arxiv.org/abs/2605.02695v1](https://arxiv.org/abs/2605.02695v1)
