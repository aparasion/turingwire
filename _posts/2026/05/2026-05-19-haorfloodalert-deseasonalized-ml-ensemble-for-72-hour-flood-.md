---
title: "HaorFloodAlert: Deseasonalized ML Ensemble for 72-Hour Flood Prediction in Bangladesh Haor Wetlands"
date: 2026-05-19 17:51:46 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.20167v1"
arxiv_id: "2605.20167"
authors: ["Salma Hoque Talukdar Koli", "Fahima Haque Talukder Jely", "Md. Samiul Alim", "Md. Zakir Hossen"]
slug: haorfloodalert-deseasonalized-ml-ensemble-for-72-hour-flood-
summary_word_count: 442
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacy of existing flood prediction models in Bangladesh's haor wetlands, which are characterized by flat topography and unique hydrodynamic behaviors that differ from riverine flood models. Current methodologies fail to account for backwater dynamics, leading to ineffective flood forecasting. The authors present HaorFloodAlert, a deseasonalized machine learning ensemble specifically designed for 72-hour flood prediction in the Sunamganj Haor region, a critical area for agriculture, particularly the boro rice harvest. This work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of the HaorFloodAlert ensemble model, which integrates Random Forest (RF) and XGBoost algorithms. The ensemble weights are set at 0.5625 for RF and 0.4375 for XGBoost. A key innovation is the deseasonalization of temperature data, which previously inflated accuracy due to seasonal flood patterns. The model incorporates upstream data from the Barak River using Sentinel-1 Synthetic Aperture Radar (SAR) imagery, enabling approximately 36 hours of lead time for flood predictions. The authors employ Otsu-thresholding for SAR change detection, achieving a spatial validation accuracy of 84-91%. The model is trained on a dataset of 77 real flood events, utilizing leave-one-out cross-validation (LOOCV) for performance evaluation.

**Results**  
HaorFloodAlert achieves an impressive 89.6% accuracy in LOOCV, with a recall of 87.5% and an AUC-ROC score of 0.943. These metrics indicate a significant improvement over existing models, particularly in the context of the unique hydrological conditions of the haor wetlands. The authors do not specify direct comparisons to named baselines, but the reported performance metrics suggest a substantial enhancement in predictive capability for flood events in this region.

**Limitations**  
The authors acknowledge that the model's reliance on SAR data may limit its applicability in regions without similar satellite coverage. Additionally, the model's performance may vary with changes in climate patterns or land use, which are not accounted for in the current framework. The study does not address the potential for overfitting due to the relatively small dataset of 77 events, nor does it explore the model's generalizability to other haor regions or different flood types.

**Why it matters**  
The development of HaorFloodAlert has significant implications for agricultural resilience in Bangladesh, particularly for the boro rice crop, which is vital for food security. By providing timely and accurate flood predictions, the model can facilitate better preparedness and response strategies, potentially reducing crop losses and improving livelihoods in vulnerable communities. Furthermore, this work contributes to the broader field of machine learning applications in environmental monitoring and disaster management, highlighting the importance of context-specific modeling approaches.

Authors: Salma Hoque Talukdar Koli, Fahima Haque Talukder Jely, Md. Samiul Alim, Md. Zakir Hossen  
Source: arXiv:2605.20167  
URL: [https://arxiv.org/abs/2605.20167v1](https://arxiv.org/abs/2605.20167v1)
