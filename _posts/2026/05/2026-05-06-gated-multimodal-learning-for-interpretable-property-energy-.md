---
title: "Gated Multimodal Learning for Interpretable Property Energy Performance Prediction and Retrofit Scenario Analysis"
date: 2026-05-06 16:23:11 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.05088v1"
arxiv_id: "2605.05088"
authors: ["Yunfei Bai", "Aaron Tesfa Tsion", "Raul Rosales", "Barbara Shollock", "Wei He"]
slug: gated-multimodal-learning-for-interpretable-property-energy-
summary_word_count: 465
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in scalable methodologies for assessing the energy performance of residential buildings, which are significant contributors to greenhouse gas emissions. Traditional Energy Performance Certificates (EPCs) rely heavily on on-site inspections, limiting their applicability for timely, city-scale evaluations. The authors propose a multimodal approach to predict energy efficiency and environmental impact scores, leveraging diverse data sources to enhance predictive accuracy and interpretability.

**Method**  
The core technical contribution is a gated multimodal learning architecture that integrates three data modalities: tabular variables from EPCs, free-text descriptions from assessors, and spatial features derived from Geographic Information Systems (GIS). The model employs sample-wise gating to learn property-specific modality weights, allowing it to dynamically adjust the contribution of each modality based on the input. An auxiliary classification head for band classification is included to stabilize training. The model is trained on a dataset from Westminster, London, although specific training compute details are not disclosed. The architecture's performance is evaluated through mean absolute error (MAE) and R² metrics for predicting Standard Assessment Procedure (SAP) and Environmental Impact (EI) scores.

**Results**  
The gated multimodal model achieves MAEs of 4.03 for SAP and 4.76 for EI, with R² values of 0.757 and 0.748, respectively, resulting in a mean MAE of 4.39. These results significantly outperform unimodal and bimodal baselines, demonstrating the effectiveness of full multimodal fusion. The ablation studies confirm that the inclusion of all modalities enhances both score prediction and band-level classification. Interpretability analyses reveal that the model heavily relies on assessor text, with SHAP values indicating key features such as fuel type, built form, and construction age. Text occlusion experiments highlight the importance of roof and wall fields, while spatial attribution analysis shows that height and footprint area are critical factors, with sensitivity to footprint shape.

**Limitations**  
The authors acknowledge that the model's reliance on specific data sources may limit its generalizability to other regions or building types. Additionally, the interpretability analyses, while insightful, may not capture all nuances of the decision-making process in energy performance assessments. The study does not disclose the computational resources used for training, which could impact reproducibility. Furthermore, the model's performance in real-world applications beyond the case study remains to be validated.

**Why it matters**  
This work has significant implications for urban planning and sustainability efforts, particularly in the context of achieving net-zero housing transitions. By providing a scalable framework for property-level energy performance assessment, the model facilitates timely retrofit screening and intervention prioritization. The integration of multimodal data enhances the interpretability of predictions, which is crucial for stakeholders involved in energy policy and building retrofitting strategies. This research could inform future studies on energy efficiency and contribute to the development of more robust regulatory frameworks.

Authors: Yunfei Bai, Aaron Tesfa Tsion, Raul Rosales, Barbara Shollock, Wei He  
Source: arXiv:2605.05088  
URL: [https://arxiv.org/abs/2605.05088v1](https://arxiv.org/abs/2605.05088v1)
