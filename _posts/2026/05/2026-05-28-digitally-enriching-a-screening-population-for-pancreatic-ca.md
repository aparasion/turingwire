---
title: "Digitally enriching a screening population for pancreatic cancer using routine blood-based measures and clinical histories"
date: 2026-05-28 17:32:29 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30275v1"
arxiv_id: "2605.30275"
authors: ["Chris Varghese", "Leo Y. Li-Han", "Richa Bisht", "Ellen Larson", "Frank Lee", "Ryan M. Carr"]
slug: digitally-enriching-a-screening-population-for-pancreatic-ca
summary_word_count: 463
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the critical gap in early detection of pancreatic cancer, which is currently not feasible due to the lack of effective screening methods. The authors highlight that latent indicators of pathology can be identified through longitudinal clinical data, including coded diagnoses and blood test trajectories. The study aims to leverage these indicators to predict pancreatic cancer risk and stratify populations for targeted screening, thereby enabling earlier intervention and potentially reducing mortality rates.

**Method**  
The authors propose a custom Transformer-based neural network architecture that incorporates a multi-head attention mechanism to analyze longitudinal sequences of clinical data. The model is trained on a dataset comprising 6,017 adults diagnosed with pancreatic cancer and 177,081 controls, with a median of 12 years of medical history prior to diagnosis. The training process utilizes routine blood-based measures and clinical histories to predict pancreatic cancer risk with a multi-year lead time. The model's performance is validated through leave-one-site-out cross-validation and out-of-sample testing, focusing on predicting pancreatic cancer 1, 2, and 3 years prior to diagnosis. The calibration of estimated risks is assessed using a calibration plot and Brier score, ensuring that the outputs are transportable across different clinical settings.

**Results**  
The model achieves a mean area under the receiver operating characteristic (AUC-ROC) of 0.837 (95% CI: 0.827-0.848) for 1-year predictions, 0.797 (95% CI: 0.782-0.813) for 2-year predictions, and 0.760 (95% CI: 0.745-0.776) for 3-year predictions. The calibration of the risk estimates is strong, with a calibration plot slope of 1.08 and an intercept of -0.077, resulting in a Brier score of 0.025. A diagnostic odds ratio of 18.2 is reported when applying a screening threshold of >3.3% risk for 1-year predictions, indicating a high likelihood of correctly identifying individuals at risk.

**Limitations**  
The authors acknowledge that the study is limited by its reliance on historical clinical data, which may not capture all relevant factors influencing pancreatic cancer risk. Additionally, the model's performance may vary across different populations and settings, necessitating further validation in diverse cohorts. The potential for overfitting in the training dataset is also a concern, as is the need for real-world implementation studies to assess the practical utility of the proposed screening tool.

**Why it matters**  
This work represents a significant advancement in the field of cancer detection, particularly for pancreatic cancer, which is often diagnosed at advanced stages. By providing a digital enrichment tool that utilizes existing clinical data, the study opens avenues for more accessible and effective screening strategies. The implications extend to improving patient outcomes through earlier detection and intervention, potentially transforming the management of pancreatic cancer and influencing future research on predictive modeling in oncology.

Authors: Chris Varghese, Leo Y. Li-Han, Richa Bisht, Ellen Larson, Frank Lee, Ryan M. Carr, Tanios S. Bekaii-Saab, Shounak Majumder et al.  
Source: arXiv:2605.30275  
URL: [https://arxiv.org/abs/2605.30275v1](https://arxiv.org/abs/2605.30275v1)
