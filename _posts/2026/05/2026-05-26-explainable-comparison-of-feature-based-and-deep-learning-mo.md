---
title: "Explainable Comparison of Feature-Based and Deep Learning Models for TROPOMI Methane Plume Screening"
date: 2026-05-26 16:17:02 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.27236v1"
arxiv_id: "2605.27236"
authors: ["Solomiia Kurchaba", "Joannes D. Maasakkers", "Berend J. Schuit", "Ilse Aben"]
slug: explainable-comparison-of-feature-based-and-deep-learning-mo
summary_word_count: 431
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of accurately classifying methane plume detections from TROPOMI satellite data, specifically distinguishing between genuine emissions and retrieval artifacts. Previous methodologies primarily utilized a Support Vector Machine Classifier (SVC) based on a limited set of expert-defined scalar features, which constrained the model's ability to leverage the full spatial and contextual information present in the data. This work aims to fill the gap by comparing traditional feature-based models with deep learning approaches, thereby enhancing the classification accuracy and interpretability of methane plume detection.

**Method**  
The authors compare three feature-based models (SVC, Random Forest, XGBoost) against two deep learning architectures (ResNet-18, ResNet-34) for methane plume-artifact classification. The models are evaluated under both balanced and imbalanced conditions to assess their robustness. The training datasets consist of TROPOMI observations, with the specific features for the traditional models being derived from domain expertise. For the deep learning models, the raw satellite images are used, allowing the networks to learn spatial hierarchies and contextual relationships. The authors employ SHAP (SHapley Additive exPlanations) for model interpretability, providing insights into feature importance across both model families.

**Results**  
The study reports that the deep learning models, particularly ResNet-34, outperform the feature-based models in terms of classification accuracy, achieving an F1 score of 0.87 compared to 0.75 for the best-performing feature-based model (XGBoost) on a balanced test set. In imbalanced settings, ResNet-34 maintains superior performance with an F1 score of 0.82, while the feature-based models drop to 0.65. The results indicate a significant effect size, demonstrating that deep learning approaches can effectively capture complex patterns in the data that traditional methods miss.

**Limitations**  
The authors acknowledge that the reliance on SHAP for interpretability may not fully capture the intricacies of deep learning models, which can be inherently more complex than feature-based counterparts. Additionally, the study does not explore the potential for ensemble methods that could combine the strengths of both model types. The dataset's representativeness and the generalizability of the findings to other satellite missions or environmental contexts are also not thoroughly examined, which could limit the applicability of the results.

**Why it matters**  
This research has significant implications for operational methane screening workflows, such as the CAMS Methane Hotspot Explorer. By demonstrating the advantages of deep learning models over traditional feature-based approaches, the findings encourage the adoption of more sophisticated methodologies in environmental monitoring. The use of SHAP for interpretability also sets a precedent for future work in explainable AI within remote sensing applications, promoting transparency in model decision-making processes.

Authors: Solomiia Kurchaba, Joannes D. Maasakkers, Berend J. Schuit, Ilse Aben  
Source: arXiv:2605.27236  
URL: [https://arxiv.org/abs/2605.27236v1](https://arxiv.org/abs/2605.27236v1)
