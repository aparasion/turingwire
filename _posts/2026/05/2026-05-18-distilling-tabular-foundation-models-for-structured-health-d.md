---
title: "Distilling Tabular Foundation Models for Structured Health Data"
date: 2026-05-18 17:37:28 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18702v1"
arxiv_id: "2605.18702"
authors: ["Aditya Tanna", "Nassim Bouarour", "Mohamed Bouadi", "Vinay Kumar Sankarapu", "Pratinav Seth"]
slug: distilling-tabular-foundation-models-for-structured-health-d
summary_word_count: 428
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the practical deployment of Tabular Foundation Models (TFMs) for structured health data, which, despite their strong performance, suffer from high inference costs and substantial infrastructure requirements. The authors investigate the feasibility of transferring the predictive capabilities of TFMs to more lightweight tabular models through knowledge distillation, while mitigating the risk of context leakage inherent in naive distillation methods.

**Method**  
The core technical contribution is the introduction of a novel distillation approach termed "stratified out-of-fold teacher labeling." This method is designed to prevent context leakage during the distillation process, which is critical given that TFMs condition on the training set at inference time. The study evaluates the performance of distilled models across 19 healthcare datasets, utilizing 6 different TFM teachers and 4 distinct student model families, including multi-teacher ensembles. The authors report that distilled student models retain at least 90% of the teacher's Area Under the Curve (AUC) performance while achieving a minimum of 26x speedup on CPU inference. The training compute details are not disclosed, but the focus is on the efficiency and effectiveness of the distillation process.

**Results**  
The distilled student models consistently achieve at least 90% of the AUC of their TFM teachers across the evaluated datasets. Notably, in some instances, the distilled students outperform their teacher models. The study emphasizes that the distilled models not only maintain high predictive performance but also preserve calibration and fairness, which are critical factors in health applications. The results indicate that multi-teacher averaging does not consistently yield improvements over the best-performing single teacher, suggesting that the choice of teacher model is crucial in the distillation process.

**Limitations**  
The authors acknowledge that while their leakage-aware distillation method is effective, it may not generalize to all types of tabular data or other domains outside healthcare. Additionally, the study does not explore the long-term implications of deploying these distilled models in real-world settings, such as their adaptability to evolving datasets or their robustness against adversarial attacks. The lack of detailed training compute specifications also limits the reproducibility of the results.

**Why it matters**  
This work has significant implications for the deployment of machine learning models in healthcare, where inference efficiency and model interpretability are paramount. By demonstrating that high-quality predictions from TFMs can be distilled into lightweight models, the authors provide a pathway for integrating advanced AI techniques into resource-constrained environments. This could facilitate broader adoption of AI in healthcare, ultimately improving patient outcomes through more accessible predictive analytics.

Authors: Aditya Tanna, Nassim Bouarour, Mohamed Bouadi, Vinay Kumar Sankarapu, Pratinav Seth  
Source: arXiv:2605.18702  
URL: [https://arxiv.org/abs/2605.18702v1](https://arxiv.org/abs/2605.18702v1)
