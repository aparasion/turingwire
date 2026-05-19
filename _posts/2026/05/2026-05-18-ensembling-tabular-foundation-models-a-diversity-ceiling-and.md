---
title: "Ensembling Tabular Foundation Models - A Diversity Ceiling And A Calibration Trap"
date: 2026-05-18 17:32:57 +0000
category: research
subcategory: efficiency_inference
company: "ServiceNow"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18696v1"
arxiv_id: "2605.18696"
authors: ["Aditya Tanna", "Yash Desai", "Pratinav Seth", "Mohamed Bouadi", "Nassim Bouarour", "Vinay Kumar Sankarapu"]
slug: ensembling-tabular-foundation-models-a-diversity-ceiling-and
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of ensembling strategies for Tabular Foundation Models (TFMs) in the context of tabular data classification tasks. While TFMs have demonstrated competitive performance against tuned gradient-boosted trees, no single TFM consistently outperforms others across diverse datasets. The authors identify a redundancy in the performance of six modern TFMs, as indicated by a high mean pairwise Q-statistic of 0.961, suggesting that ensembling may not yield significant improvements due to a lack of diversity among the models.

**Method**  
The authors benchmark six ensemble strategies applied to six TFMs across 153 OpenML classification tasks. The ensemble methods evaluated include simple averaging, weighted averaging, stacking with a logistic regression meta-learner, and a two-level cascade stacking approach. The performance of these ensembles is compared against the best-performing single TFM. The study employs Friedman and Nemenyi statistical tests to assess the significance of differences in performance among the ensembles and the base models. The computational cost of the best ensemble, two-level cascade stacking, is noted to be 253 times that of the strongest single TFM, highlighting the trade-off between accuracy and computational efficiency.

**Results**  
The best ensemble method, two-level cascade stacking, achieves an accuracy improvement of +0.18% over the strongest single TFM. However, this comes at a significantly higher computational cost. The Friedman and Nemenyi analysis reveals that three of the ensemble strategies, including the stacking with a logistic regression meta-learner, do not outperform the best base TFM and, in some cases, perform significantly worse. Notably, while the meta-learner enhances accuracy by refining class boundaries, it results in poor calibration, as indicated by the worst log-loss rank among the ensembles. The authors recommend greedy selection as a more practical approach for model selection in this context.

**Limitations**  
The authors acknowledge that the redundancy among the TFMs limits the potential gains from ensembling, which may not be generalizable to other datasets or model architectures. They also highlight the calibration issues introduced by the logistic regression meta-learner, which could impact the reliability of probability estimates. An additional limitation not explicitly mentioned is the potential overfitting risk associated with complex ensemble methods, particularly in scenarios with limited data.

**Why it matters**  
This work has significant implications for the deployment of TFMs in real-world applications, particularly in scenarios where computational resources are constrained. The findings suggest that while ensembling can provide marginal gains in accuracy, the associated computational costs may not justify the benefits. The identification of calibration issues also underscores the need for careful consideration of model selection and evaluation metrics in tabular data tasks. This research encourages further exploration of model diversity and selection strategies to enhance the robustness and reliability of TFMs in practical applications.

Authors: Aditya Tanna, Yash Desai, Pratinav Seth, Mohamed Bouadi, Nassim Bouarour, Vinay Kumar Sankarapu  
Source: arXiv:2605.18696  
URL: [https://arxiv.org/abs/2605.18696v1](https://arxiv.org/abs/2605.18696v1)
