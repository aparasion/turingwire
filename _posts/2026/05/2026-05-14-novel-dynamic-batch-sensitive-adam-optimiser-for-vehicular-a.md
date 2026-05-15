---
title: "Novel Dynamic Batch-Sensitive Adam Optimiser for Vehicular Accident Injury Severity Prediction"
date: 2026-05-14 17:06:43 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.15083v1"
arxiv_id: "2605.15083"
authors: ["Daniel Asare Kyei", "Alimatu Saadia-Yussiff", "Maame G. Asante-Mensah", "Abdul Lateef-Yussiff", "Charles Roland Haruna", "Derry Emmanuel"]
slug: novel-dynamic-batch-sensitive-adam-optimiser-for-vehicular-a
summary_word_count: 376
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing optimisers in deep learning, particularly when applied to imbalanced and sequential datasets. Traditional optimisers often struggle to effectively capture patterns in minority classes, which is critical for tasks such as vehicular accident injury severity prediction. The authors propose a novel optimiser, Dynamic Batch-Sensitive Adam (DBS-Adam), to enhance model performance in these challenging scenarios.

**Method**  
DBS-Adam is an adaptive learning rate optimiser that incorporates a dynamic scaling mechanism based on a batch difficulty score. This score is computed using exponential moving averages of gradient norms and batch loss, allowing the optimiser to adjust the learning rate according to the complexity of the current batch. The authors integrate DBS-Adam with Bi-Directional LSTM (Bi-LSTM) networks, employing SMOTE-ENN for class imbalance handling and Focal Loss to further enhance performance. The training process is evaluated across four experimental configurations, comparing DBS-Adam against established optimisers such as AMSGrad, AdamW, and AdaBound. The study does not disclose specific training compute resources used.

**Results**  
DBS-Adam demonstrates superior performance on the task of accident injury severity prediction, achieving a test accuracy of 95.22%, precision of 96.11%, recall of 95.28%, F1-score of 95.39%, and a test loss of 0.0086. These results were obtained through rigorous testing across five random seeds, with statistical significance indicated by a p-value of 0.020 when compared to baseline Bi-LSTM models and other optimisers. The improvements in precision and overall performance metrics highlight the effectiveness of DBS-Adam in handling imbalanced datasets.

**Limitations**  
The authors acknowledge that while DBS-Adam shows promise, its performance is contingent on the specific architecture and dataset used. They do not address potential overfitting issues or the generalizability of the optimiser to other domains outside vehicular accident prediction. Additionally, the computational efficiency of DBS-Adam compared to other optimisers in large-scale applications remains unexamined.

**Why it matters**  
The introduction of DBS-Adam has significant implications for real-time accident severity classification, which can enhance targeted emergency response and improve road safety interventions. By effectively learning from imbalanced sequential data, DBS-Adam could be applied to various domains where class imbalance is prevalent, potentially leading to advancements in predictive modelling and decision-making processes in critical applications.

Authors: Daniel Asare Kyei, Alimatu Saadia-Yussiff, Maame G. Asante-Mensah, Abdul Lateef-Yussiff, Charles Roland Haruna, Derry Emmanuel  
Source: arXiv:2605.15083  
URL: https://arxiv.org/abs/2605.15083v1
