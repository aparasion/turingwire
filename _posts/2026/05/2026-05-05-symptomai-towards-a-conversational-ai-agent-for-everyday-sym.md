---
title: "SymptomAI: Towards a Conversational AI Agent for Everyday Symptom Assessment"
date: 2026-05-05 17:36:12 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: ["Fitbit"]
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.04012v1"
arxiv_id: "2605.04012"
authors: ["Joseph Breda", "Fadi Yousif", "Beszel Hawkins", "Marinela Cotoi", "Miao Liu", "Ray Luo"]
slug: symptomai-towards-a-conversational-ai-agent-for-everyday-sym
summary_word_count: 455
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the performance of conversational AI agents in everyday symptom assessment, as existing studies predominantly focus on complex medical scenarios with curated case studies. The authors aim to evaluate how well these AI systems can perform differential diagnosis (DDx) in real-world settings, specifically for patients reporting symptoms through a consumer application.

**Method**  
The core technical contribution is the development and deployment of SymptomAI, a set of conversational AI agents integrated into the Fitbit app. The study involved a randomized trial with 13,917 participants interacting with five distinct AI agents. The agents conducted end-to-end patient interviews to gather symptom information and provide differential diagnoses. A subset of 1,228 participants had their self-reported diagnoses validated by clinicians, with 517 cases further evaluated through over 250 hours of clinician annotation. The study employed a dedicated symptom interview strategy, contrasting it with user-guided conversations, to assess the impact on diagnostic accuracy. The analysis leveraged over 500,000 days of wearable metrics across nearly 400 unique conditions, identifying associations between acute infections and physiological changes.

**Results**  
SymptomAI demonstrated a significant improvement in diagnostic accuracy, with an odds ratio (OR) of 2.47 (p < 0.001) compared to independent clinicians who were provided the same dialogue in a blinded randomized comparison. The dedicated symptom interview strategy outperformed user-guided conversations, achieving statistical significance (p < 0.001). Additionally, an auxiliary analysis on 1,509 conversations from a general US population panel confirmed that the results generalize beyond the Fitbit user base. The study identified strong associations between specific acute infections and physiological metrics, with an OR exceeding 7 for influenza.

**Limitations**  
The authors acknowledge that the reliance on self-reported diagnoses constitutes a limitation, as it may introduce bias or inaccuracies in the ground truth. Furthermore, the study's findings may not be generalizable to all populations or settings, given the specific context of the Fitbit app and the demographic characteristics of the participants. The potential for overfitting in the model due to the large dataset and the complexity of real-world symptomatology are also concerns that warrant further investigation.

**Why it matters**  
This work has significant implications for the development of AI-driven healthcare solutions, particularly in enhancing the accuracy of symptom assessment in everyday contexts. By demonstrating the efficacy of dedicated symptom interviews over traditional user-guided approaches, the study suggests a pathway for improving patient outcomes through more effective AI interactions. The findings also highlight the potential for integrating wearable technology with conversational AI to monitor and diagnose health conditions in real-time, paving the way for future research in personalized medicine and remote patient monitoring.

Authors: Joseph Breda, Fadi Yousif, Beszel Hawkins, Marinela Cotoi, Miao Liu, Ray Luo, Po-Hsuan Cameron Chen, Mike Schaekermann et al.  
Source: arXiv:2605.04012  
URL: [https://arxiv.org/abs/2605.04012v1](https://arxiv.org/abs/2605.04012v1)
