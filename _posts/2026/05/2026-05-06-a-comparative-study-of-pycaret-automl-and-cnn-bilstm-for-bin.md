---
title: "A Comparative Study of PyCaret AutoML and CNN-BiLSTM for Binary Hate Speech Detection in Indonesian Twitter"
date: 2026-05-06 13:20:51 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.04885v1"
arxiv_id: "2605.04885"
authors: ["Tanty Widiyastuti", "Mayada", "Adisty Syawalda Ariyanto", "Luluk Muthoharoh", "Ardika Satria", "Martin Clinton Tosima Manullang"]
slug: a-comparative-study-of-pycaret-automl-and-cnn-bilstm-for-bin
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in hate speech detection methodologies specifically for Indonesian Twitter data, a domain that has received limited attention in existing literature. The authors present a comparative study of two distinct approaches: a conventional AutoML framework (PyCaret) and a neural network architecture (CNN-BiLSTM). The work is a preprint and has not undergone peer review, which may affect the robustness of the findings.

**Method**  
The study employs a dual-branch approach for binary hate speech detection, utilizing a shared preprocessing pipeline to ensure consistency in data preparation. The conventional branch leverages PyCaret AutoML, specifically using a Random Forest model as the strongest performer, which incorporates TF-IDF for feature extraction alongside a lexicon-based count of abusive words. In contrast, the CNN-BiLSTM branch employs a deep learning architecture that combines Convolutional Neural Networks (CNN) for local feature extraction and Bidirectional Long Short-Term Memory (BiLSTM) networks to capture contextual dependencies in the text. The dataset consists of 13,130 annotated tweets with a class imbalance of 58:42 for hate speech labels. The training and evaluation processes are not explicitly detailed in terms of compute resources or training duration.

**Results**  
On the held-out test set, the CNN-BiLSTM model outperforms the PyCaret AutoML framework, achieving an accuracy of 83.8%, precision of 79.8%, recall of 82.7%, and an F1-score of 81.2%. In comparison, the best-performing model from the PyCaret branch, the Random Forest, achieves an accuracy of 77.2% and an F1-score of 77.0%. This indicates a significant improvement of 6.6 percentage points in accuracy and 4.2 points in F1-score for the CNN-BiLSTM model over the conventional approach. The authors also provide exploratory analysis, including learning curves and confusion matrices, which highlight the challenges posed by the short-text nature of the dataset and its moderate class imbalance.

**Limitations**  
The authors acknowledge that the dataset is relatively small and imbalanced, which may limit the generalizability of the results. Additionally, the reliance on local lexical cues and short contextual compositions complicates the detection task, suggesting that further research is needed to enhance model robustness. The study does not explore the impact of hyperparameter tuning or alternative neural architectures, which could provide additional insights into performance improvements.

**Why it matters**  
This comparative study contributes to the growing body of work on hate speech detection in non-English languages, particularly in underrepresented contexts like Indonesian social media. By demonstrating the efficacy of a CNN-BiLSTM architecture over conventional methods, the findings suggest that deep learning approaches may be more suitable for nuanced text classification tasks in challenging datasets. The results also validate the use of PyCaret as a reliable benchmarking tool for conventional models, paving the way for future research to explore hybrid approaches or further enhancements in model architectures.

Authors: Tanty Widiyastuti, Mayada, Adisty Syawalda Ariyanto, Luluk Muthoharoh, Ardika Satria, Martin Clinton Tosima Manullang  
Source: arXiv:2605.04885  
URL: https://arxiv.org/abs/2605.04885v1
