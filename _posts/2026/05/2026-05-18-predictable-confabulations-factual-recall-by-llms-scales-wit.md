---
title: "Predictable Confabulations: Factual Recall by LLMs Scales with Model Size and Topic Frequency"
date: 2026-05-18 17:53:44 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18732v1"
arxiv_id: "2605.18732"
authors: ["Matthew L. Smith", "Jonathan P. Shock", "Samuel T. Segun", "Iyiola E. Olatunji", "Tegawend\u00e9 F. Bissyand\u00e9"]
slug: predictable-confabulations-factual-recall-by-llms-scales-wit
summary_word_count: 518
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the understanding of how large language models (LLMs) scale in terms of factual recall, specifically linking model size and training data composition. While existing scaling laws have primarily focused on aggregate performance metrics, this work investigates the relationship between model parameters and the frequency of topics in the training data, which has not been previously quantified. The authors aim to establish a framework that explains how these factors influence the factual recall capabilities of LLMs.

**Method**  
The authors evaluated 38 LLMs across various architectures, focusing on their performance in recalling factual information from over 8,900 scholarly references. An automated reference verification system was employed to assess recall quality. The core technical contribution is the identification of a sigmoid relationship in the log-linear combination of model parameter count and topic representation in the training data. This relationship is modeled as a superposition where recall is influenced by a signal-to-noise ratio: the signal strength is determined by the frequency of concepts in the training data, while the noise floor is dictated by the model's capacity. The study quantitatively demonstrates that these two variables account for 60% of the variance in recall performance across 16 dense models from four different families, with the explanatory power increasing to 74-94% within individual model families.

**Results**  
The findings reveal that as model size and topic frequency increase, factual recall improves significantly. Specifically, the authors report that the recall quality follows a sigmoid curve, indicating diminishing returns at higher model sizes and topic frequencies. The study provides quantitative metrics, showing that the variance explained by the model parameters and topic representation is substantial, with 60% across diverse models and up to 94% within specific families. These results suggest a robust correlation between the scaling of model parameters and the frequency of topics in training data, which has implications for model design and training strategies.

**Limitations**  
The authors acknowledge several limitations, including the potential for overfitting to the specific dataset of scholarly references used for evaluation. They also note that the automated reference verification system may introduce biases or inaccuracies in recall assessment. Additionally, the study does not explore the impact of other factors such as training duration, optimization techniques, or the diversity of training data beyond topic frequency. An obvious limitation not flagged by the authors is the generalizability of the findings to other domains outside of scholarly references, which may exhibit different scaling behaviors.

**Why it matters**  
This work has significant implications for the design and training of LLMs, particularly in applications requiring high factual accuracy. By elucidating the relationship between model size, topic frequency, and recall performance, it provides a framework for optimizing LLMs for specific tasks. Researchers and engineers can leverage these insights to make informed decisions about model architecture and training data selection, ultimately enhancing the reliability of LLMs in knowledge-intensive applications. Furthermore, this study lays the groundwork for future research into scaling laws that incorporate additional dimensions of model training and evaluation.

Authors: Matthew L. Smith, Jonathan P. Shock, Samuel T. Segun, Iyiola E. Olatunji, Tegawendé F. Bissyandé  
Source: arXiv:2605.18732  
URL: [https://arxiv.org/abs/2605.18732v1](https://arxiv.org/abs/2605.18732v1)
