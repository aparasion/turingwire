---
title: "Data Presentation Over Architecture: Resampling Strategies for Credit Risk Prediction with Tabular Foundation Models"
date: 2026-05-18 16:43:15 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18635v1"
arxiv_id: "2605.18635"
authors: ["Aditya Tanna", "Mitul Solanki", "Mohamed Bouadi", "Nassim Bouarour", "Pratinav Seth", "Vinay Kumar Sankarapu"]
slug: data-presentation-over-architecture-resampling-strategies-fo
summary_word_count: 448
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of credit default prediction, a tabular learning problem characterized by severe class imbalance, heterogeneous features, and stringent latency requirements. Existing literature primarily focuses on model architecture, often neglecting the impact of data presentation strategies, particularly in the context of Tabular Foundation Models (TFMs). The authors aim to fill this gap by investigating how different context-construction strategies influence the performance of TFMs compared to classical models.

**Method**  
The authors benchmark four classical models and five TFMs on the Home Credit and Lending Club datasets, employing a variety of context-construction strategies. They explore seven different strategies for context construction, varying the context size from 1K to 50K examples. The core technical contribution lies in demonstrating that the choice of context strategy significantly affects model performance, often more so than the choice of TFM architecture itself. The study employs AUC-ROC as the primary evaluation metric, focusing on how balanced and hybrid sampling strategies can enhance predictive performance in imbalanced datasets.

**Results**  
The results indicate that the choice of context strategy accounts for more variance in AUC-ROC than the selection of TFM family. Specifically, balanced and hybrid sampling strategies yield an improvement of 3 to 4 AUC points over uniform sampling across both datasets. With a balanced context of 5K to 10K examples, the best-performing TFMs achieve AUC scores comparable to classical baselines trained on the full dataset. Notably, these TFMs also demonstrate improved recall for the default class, outperforming gradient-boosted decision trees (GBDTs) that utilize a default-threshold approach. The findings suggest that context construction is a more critical factor than architecture choice in the deployment of TFMs for credit-risk prediction.

**Limitations**  
The authors acknowledge that their study is limited to specific datasets (Home Credit and Lending Club) and may not generalize to other domains or datasets with different characteristics. Additionally, the exploration of context strategies is confined to a predefined set, leaving open the possibility that other, untested strategies could yield further improvements. The paper does not address the computational cost associated with varying context sizes or the potential trade-offs in latency that may arise from using larger contexts.

**Why it matters**  
This work has significant implications for the deployment of TFMs in real-world credit-risk applications. By highlighting the importance of context construction over architectural choices, it encourages practitioners to focus on data presentation strategies to enhance model performance. This insight could lead to more effective credit risk prediction systems, particularly in scenarios where class imbalance is prevalent. Furthermore, the findings may influence future research directions, prompting further investigation into context strategies across various tabular learning tasks.

Authors: Aditya Tanna, Mitul Solanki, Mohamed Bouadi, Nassim Bouarour, Pratinav Seth, Vinay Kumar Sankarapu  
Source: arXiv:2605.18635  
URL: https://arxiv.org/abs/2605.18635v1
