---
title: "Robust and Explainable Bicuspid Aortic Valve Diagnosis Using Stacked Ensembles on Echocardiography"
date: 2026-05-13 16:10:39 +0000
category: research
subcategory: interpretability
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13730v1"
arxiv_id: "2605.13730"
authors: ["Christos Chrysanthos Nikolaidis", "Vasileios Sachpekidis", "Nikolas Moustakidis", "Theofilos Moustakidis", "Pavlos S. Efraimidis"]
slug: robust-and-explainable-bicuspid-aortic-valve-diagnosis-using
summary_word_count: 422
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the variability in diagnostic performance for bicuspid aortic valve (BAV) detection using transthoracic echocardiography (TTE), which is influenced by operator expertise and image quality. The authors identify a gap in the literature regarding the application of explainable AI techniques to enhance the reliability of BAV diagnosis from routine echocardiographic cine loops, specifically targeting non-specialist and resource-limited clinical settings.

**Method**  
The authors propose a multi-backbone video ensemble architecture that integrates multiple convolutional neural networks (CNNs) to analyze parasternal long-axis (PLAX) cine loops. The model employs a leakage-aware, stratified outer cross-validation protocol on a dataset comprising 90 patient studies (48 BAV, 42 TAV). The ensemble is calibrated to optimize performance metrics, specifically focusing on F1-score and recall. For interpretability, the model utilizes frame-level Grad-CAM for localization of salient features and SHAP (SHapley Additive exPlanations) values to quantify the contribution of each video backbone to the final prediction. The training compute details are not disclosed, but the methodology emphasizes robustness and explainability in the diagnostic process.

**Results**  
The calibrated stacked ensemble achieved an outer cross-validation F1-score of 0.907 and a recall of 0.877 across fixed outer splits and 10 random seeds. These results indicate a significant improvement in diagnostic accuracy compared to traditional methods, although specific baseline models are not mentioned for direct comparison. The use of explainable AI techniques, such as Grad-CAM and SHAP, provides additional insights into the model's decision-making process, enhancing trust in the predictions made by the ensemble.

**Limitations**  
The authors acknowledge several limitations, including the relatively small sample size of 90 patient studies, which may affect the generalizability of the results. Additionally, the reliance on a single imaging modality (PLAX cine loops) may limit the model's applicability to other echocardiographic views or imaging techniques. The study does not address potential biases in the dataset or the need for external validation on larger, more diverse cohorts. Furthermore, the computational resources required for training the ensemble are not specified, which could impact reproducibility.

**Why it matters**  
This work has significant implications for the integration of AI in clinical practice, particularly in enhancing the diagnostic capabilities of non-specialist practitioners in detecting BAV. By providing a robust and explainable model, the authors pave the way for earlier and more accurate diagnoses in settings where expert echocardiographers may not be available. The approach could also serve as a foundation for future research into automated diagnostic tools in cardiology, potentially extending to other cardiovascular conditions.

Authors: Christos Chrysanthos Nikolaidis, Vasileios Sachpekidis, Nikolas Moustakidis, Theofilos Moustakidis, Pavlos S. Efraimidis  
Source: arXiv:2605.13730  
URL: https://arxiv.org/abs/2605.13730v1
