---
title: "Reading Task Failure Off the Activations: A Sparse-Feature Audit of GPT-2 Small on Indirect Object Identification"
date: 2026-05-21 16:55:27 +0000
category: research
subcategory: interpretability
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.22719v1"
arxiv_id: "2605.22719"
authors: ["Mahdi Nasermoghadasi"]
slug: reading-task-failure-off-the-activations-a-sparse-feature-au
summary_word_count: 481
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the internal representations of GPT-2 Small, specifically in the context of the Indirect Object Identification (IOI) task. While previous studies have explored the performance of transformer models on various tasks, there is limited insight into which specific features contribute to task failures. This work aims to audit the sparse-autoencoder (SAE) features of GPT-2 Small to identify which features correlate with successful and failed task completions.

**Method**  
The authors employ a systematic audit pipeline to analyze the activations of GPT-2 Small on 300 prompts related to the IOI task. They utilize the layer-8 residual-stream SAE from Bloom (2024) to extract 24,576 features. The analysis focuses on identifying features that significantly correlate with task failures, applying a Holm-corrected significance threshold. The authors report that 146 features meet this threshold, with 105 exhibiting a large effect size (|Cohen's d| > 0.8). A notable feature, labeled 'cryptographic keys' (feature 17,491), is highlighted for its strong correlation with failure when the transferred object is 'the keys.' The authors conduct three controls: a causal ablation test, a representation baseline comparison using logistic regression, and a seed-robustness check across five random seeds. The entire audit pipeline is designed to be model-agnostic and computationally inexpensive, capable of running on a standard laptop.

**Results**  
GPT-2 Small achieves an accuracy of 79.7% on the IOI task. The feature 17,491 shows a Cohen's d of +2.93, indicating a substantial correlation with failure, particularly when the prompt includes 'the keys,' where the model fails 93.3% of the time compared to 7.5% for other objects (Fisher exact p = 8.79 x 10^-33). The logistic regression baseline achieves a 5-fold ROC AUC of 0.929, comparable to the top-100 SAE features (0.927), suggesting that while the SAE features enhance interpretability, they do not improve predictive power. The seed-robustness check confirms that the failure rate remains consistent across different random seeds, although feature 17,491 is not consistently the top feature across all runs.

**Limitations**  
The authors acknowledge that feature 17,491 is a correlate rather than a sufficient cause of failure, as demonstrated by the causal ablation test. Additionally, the audit pipeline's reliance on a single model (GPT-2 Small) may limit the generalizability of the findings to other architectures. The study does not explore the implications of these findings on model training or architecture design, nor does it address potential biases in the dataset used for the IOI task.

**Why it matters**  
This work provides a novel approach to auditing transformer models, offering insights into the internal mechanisms that contribute to task performance. By identifying specific features associated with task failures, the findings can inform future research on model interpretability and robustness. The release of the audit pipeline and associated resources enables other researchers to replicate and extend this work, potentially leading to improved understanding and performance of language models in complex tasks.

Authors: Mahdi Nasermoghadasi  
Source: arXiv:2605.22719  
URL: [https://arxiv.org/abs/2605.22719v1](https://arxiv.org/abs/2605.22719v1)
