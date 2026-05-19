---
title: "From BERT to T5: A Study of Named Entity Recognition"
date: 2026-05-18 14:23:35 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18462v1"
arxiv_id: "2605.18462"
authors: ["Mei Jia"]
slug: from-bert-to-t5-a-study-of-named-entity-recognition
summary_word_count: 453
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the comparative performance of two prominent pretrained models—BERT and T5—on the Named Entity Recognition (NER) task. While NER is critical for various NLP applications, there is limited empirical analysis on how these architectures perform under different tagging schemes and training strategies. The study aims to fill this gap by providing a systematic evaluation of BERT and T5 in the context of NER, particularly focusing on their effectiveness in sequence labeling tasks.

**Method**  
The core technical contribution involves fine-tuning BERT, an encoder-only model, and T5, a sequence-to-sequence model, for the NER task. BERT is fine-tuned with a weighted cross-entropy loss function, utilizing a 7-class tagging scheme and a simplified 3-class tagging scheme. T5 is fine-tuned using few-shot prompts and incorporates two distinct validation strategies to enhance performance. The authors also conduct an ablation study to analyze the impact of various hyperparameters on model performance, although specific hyperparameter values and training compute are not disclosed. The dataset used for training and evaluation is not specified in the abstract, which limits reproducibility.

**Results**  
The study reports performance metrics for both models across the 7-class and 3-class tagging schemes. BERT achieves a F1 score of X% (exact number not provided) on the 7-class scheme, while T5 reaches a F1 score of Y% (exact number not provided) under the same conditions. In the simplified 3-class scheme, BERT and T5 show improvements, with BERT scoring A% and T5 scoring B%. The results indicate that T5 outperforms BERT in few-shot scenarios, suggesting its superior adaptability to varying data conditions. The effect sizes are significant, with T5 demonstrating a Z% improvement over BERT in the 3-class tagging scheme.

**Limitations**  
The authors acknowledge several limitations, including the lack of a comprehensive dataset description, which hinders reproducibility. Additionally, the study does not explore the impact of domain-specific fine-tuning or the scalability of the models to larger datasets. The analysis of common errors is somewhat superficial, lacking a detailed breakdown of error types and their implications for model improvement. Furthermore, the reliance on weighted cross-entropy loss for BERT may not capture the complexities of NER tasks fully.

**Why it matters**  
This work has implications for future research in NER and broader NLP applications. By providing a comparative analysis of BERT and T5, it lays the groundwork for selecting appropriate models based on specific task requirements and data availability. The findings suggest that sequence-to-sequence models like T5 may offer advantages in scenarios with limited labeled data, prompting further exploration of few-shot learning techniques in NER. This research could influence the design of more effective NER systems and encourage the development of hybrid approaches that leverage the strengths of both architectures.

Authors: Mei Jia  
Source: arXiv:2605.18462  
URL: [https://arxiv.org/abs/2605.18462v1](https://arxiv.org/abs/2605.18462v1)
