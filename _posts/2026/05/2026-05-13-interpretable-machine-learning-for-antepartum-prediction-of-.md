---
title: "Interpretable Machine Learning for Antepartum Prediction of Pregnancy-Associated Thrombotic Microangiopathy Using Routine Longitudinal Laboratory Data"
date: 2026-05-13 17:07:00 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13786v1"
arxiv_id: "2605.13786"
authors: ["Chuanchuan Sun", "Zhen Yu", "Qin Fan", "Qingchao Chen", "Feng Yu"]
slug: interpretable-machine-learning-for-antepartum-prediction-of-
summary_word_count: 446
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of early risk prediction for pregnancy-associated thrombotic microangiopathy (P-TMA), a rare but critical condition. Traditional methods, including univariate and rule-based approaches, fail to capture the subtle and multidimensional laboratory abnormalities associated with P-TMA, which are often confounded by benign physiological changes during pregnancy. The authors aim to leverage machine learning to extract latent, time-dependent risk signatures from longitudinal clinical data, filling a significant gap in predictive capability in obstetric care.

**Method**  
The study employs a retrospective design, analyzing data from 300 pregnancies, which includes 142 P-TMA cases and 158 controls. After preprocessing to exclude identifiers and non-informative variables, 146 longitudinal laboratory predictors were retained. The dataset was split into a training cohort (80%) and a held-out test cohort (20%) using stratified sampling. Five machine learning algorithms were evaluated: logistic regression, support vector machine (SVM) with a radial basis function kernel, random forest, extra trees, and gradient boosting. The final model was selected based on mean cross-validated area under the receiver operating characteristic curve (AUROC) and was refitted on the full training cohort before evaluation on the test cohort. Interpretability analyses were conducted to assess global feature importance and the distributional patterns of leading predictors.

**Results**  
The gradient boosting model was selected as the best-performing algorithm, achieving an AUROC of 0.872 (95% CI: 0.769-0.952) and an area under the precision-recall curve (AUPRC) of 0.883 (95% CI: 0.780-0.959) in the held-out test cohort. The model demonstrated a sensitivity of 0.750 and specificity of 0.812, indicating a robust ability to distinguish between P-TMA cases and controls. Notably, cystatin C levels at week 6 of gestation emerged as a promising early monitoring indicator for P-TMA risk.

**Limitations**  
The authors acknowledge several limitations, including the retrospective nature of the study, which may introduce biases inherent to observational data. The reliance on a single dataset may limit the generalizability of the findings. Additionally, while the model's interpretability is enhanced through feature importance analysis, the complexity of machine learning models can still obscure the underlying biological mechanisms. The study does not address potential confounding factors that may influence laboratory results or the clinical presentation of P-TMA.

**Why it matters**  
This work has significant implications for improving early detection and management of P-TMA, potentially leading to better maternal and fetal outcomes. By demonstrating that routine longitudinal laboratory tests can yield clinically relevant signals for P-TMA risk, the study paves the way for integrating machine learning approaches into obstetric care. Future research could expand on these findings by validating the model in diverse populations and exploring the biological underpinnings of the identified risk factors.

Authors: Chuanchuan Sun, Zhen Yu, Qin Fan, Qingchao Chen, Feng Yu  
Source: arXiv:2605.13786  
URL: [https://arxiv.org/abs/2605.13786v1](https://arxiv.org/abs/2605.13786v1)
