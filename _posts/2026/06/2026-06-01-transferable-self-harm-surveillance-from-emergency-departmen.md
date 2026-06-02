---
title: "Transferable Self-Harm Surveillance from Emergency Department Triage Notes Using an Evidence-Augmented Machine Learning Approach"
date: 2026-06-01 17:48:21 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02545v1"
arxiv_id: "2606.02545"
authors: ["Liuliu Chen", "Gowri Rajaram", "Eleanor Bailey", "Katrina Witt", "Michelle Lamblin", "Jo Robinson"]
slug: transferable-self-harm-surveillance-from-emergency-departmen
summary_word_count: 417
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper presents a novel three-stage machine learning approach for self-harm surveillance using emergency department triage notes, enhancing detection accuracy."
---

**Problem**  
Self-harm is a significant public health issue, yet existing surveillance methods relying on hospital diagnostic codes exhibit low sensitivity. This paper addresses the inadequacy of current self-harm detection mechanisms by leveraging emergency department (ED) triage notes, which provide timely and concise summaries of patient presentations. The authors highlight the need for improved methodologies in self-harm surveillance, particularly in the context of machine learning applications. Notably, this work is a preprint and has not undergone peer review.

**Method**  
The authors propose a three-stage evidence-augmented machine learning framework. The first stage involves traditional machine learning techniques to process ED triage notes. The second stage incorporates large language models (LLMs) for enhanced screening, while the third stage focuses on evidence extraction to identify self-harm instances. The model was trained on a dataset from three Australian hospitals, utilizing a combination of labeled triage notes and LLM outputs. Specifics regarding the architecture and training compute are not disclosed, but the model's design emphasizes transferability across different hospital settings without the need for site-specific retraining.

**Results**  
The proposed method achieved impressive performance metrics, with area under the precision-recall curve (AUPRC) scores of 0.887 ± 0.016 and 0.884 ± 0.012 during internal and external validation, respectively. In a prospective evaluation at the development site, the model maintained an AUPRC of 0.881 ± 0.008, while external sites recorded AUPRCs of 0.879 ± 0.012 and 0.816 ± 0.015. A notable feature of the model is its ability to accurately identify the primary self-harm method with an accuracy of 95%, which allows for more nuanced surveillance beyond simple binary classification.

**Limitations**  
The authors acknowledge several limitations, including the potential for bias in the training data and the reliance on the quality of triage notes, which may vary across hospitals. Additionally, the model's performance in diverse clinical settings remains to be fully validated, as the current results are based on a limited number of sites. The lack of detailed information regarding the model architecture and training compute may hinder reproducibility and further optimization efforts.

**Why it matters**  
This research has significant implications for public health surveillance and intervention strategies related to self-harm. By improving the detection of self-harm incidents through the analysis of ED triage notes, healthcare providers can better allocate resources and implement timely interventions. The ability to identify specific self-harm methods enhances the granularity of surveillance data, which is crucial for targeted prevention efforts. This work contributes to the growing body of literature on the application of machine learning in healthcare, as published in [arXiv](https://arxiv.org/abs/2606.02545v1).
