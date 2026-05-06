---
title: "From Data Lifting to Continuous Risk Estimation: A Process-Aware Pipeline for Predictive Monitoring of Clinical Pathways"
date: 2026-05-05 15:51:43 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03895v1"
arxiv_id: "2605.03895"
authors: ["Pasquale Ardimento", "Mario Luca Bernardi", "Marta Cimitile", "Samuele Latorre"]
slug: from-data-lifting-to-continuous-risk-estimation-a-process-aw
summary_word_count: 420
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in predictive monitoring of clinical pathways, particularly in the context of partially observed patient trajectories. Traditional retrospective process mining methods are limited in their ability to provide real-time insights and risk estimations. The authors propose a reproducible and process-aware pipeline that enables continuous reasoning about patient data, which is crucial for timely clinical decision-making. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The proposed framework integrates several components: data lifting, temporal reconstruction, event log construction, prefix-based representations, and predictive modeling. The architecture allows for the construction of a comprehensive event log from clinical data, which is then used to create prefix-based representations of patient trajectories. Predictive models are trained using a case-level split, with logistic regression identified as the primary modeling technique. The dataset comprises 4,479 patient cases with 46,804 prefixes, and the evaluation focuses on predicting ICU admissions. The authors report that predictive performance improves as more clinical events are observed, with a detailed analysis of prefix-based representations highlighting the progressive emergence of predictive signals.

**Results**  
The logistic regression model achieved an Area Under the Curve (AUC) of 0.906 and an F1-score of 0.835 on the test set of 896 patients. Notably, the AUC increased from 0.642 at early stages of the clinical pathway to 0.942 at later stages, demonstrating that the model's predictive capability improves as additional clinical events are incorporated. This progressive enhancement underscores the importance of continuous monitoring and the dynamic nature of risk estimation in clinical settings.

**Limitations**  
The authors acknowledge that their approach relies on the availability and quality of clinical data, which may vary across different healthcare settings. Additionally, the study is limited to COVID-19 clinical pathways, which may not generalize to other conditions or patient populations. The authors do not address potential biases in the dataset or the implications of model interpretability in clinical practice, which are critical for real-world applications.

**Why it matters**  
This work has significant implications for the field of healthcare analytics, particularly in enhancing the capabilities of predictive monitoring systems. By framing predictive monitoring as a continuous process, the authors advocate for a shift in how healthcare providers approach risk estimation and decision-making. The findings suggest that integrating process-aware representations can lead to more timely and accurate risk assessments, ultimately improving patient outcomes. This research lays the groundwork for future studies to explore similar methodologies across diverse clinical pathways and conditions.

Authors: Pasquale Ardimento, Mario Luca Bernardi, Marta Cimitile, Samuele Latorre  
Source: arXiv:2605.03895  
URL: [https://arxiv.org/abs/2605.03895v1](https://arxiv.org/abs/2605.03895v1)
