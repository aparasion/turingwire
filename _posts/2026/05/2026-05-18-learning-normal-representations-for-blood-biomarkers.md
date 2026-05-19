---
title: "Learning Normal Representations for Blood Biomarkers"
date: 2026-05-18 17:37:05 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.18701v1"
arxiv_id: "2605.18701"
authors: ["Aashna P. Shah", "Michelle M. Li", "Yash Lal", "Seffi Cohen", "Liat F. Antwarg", "Morgan Sanchez"]
slug: learning-normal-representations-for-blood-biomarkers
summary_word_count: 440
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacy of fixed population reference intervals for interpreting blood biomarkers, which often overlook intra-patient variability. Current methods for personalizing interpretations based on individual testing histories can lead to overfitting, resulting in inflated false-positive rates and unnecessary follow-ups. The authors highlight that these approaches may also inadvertently include undetected or subclinical diseases, complicating clinical decision-making. 

**Method**  
The authors propose NORMA, a conditional transformer-based framework designed to generate personalized reference intervals by integrating both individual patient histories and population-level data on "normal" variations. NORMA leverages a dataset comprising nearly 2 billion longitudinal laboratory measurements from over 1.6 million individuals across diverse geographical regions, including North America, the Middle East, and East Asia. The architecture employs a transformer model that conditions on historical patient data while simultaneously referencing population-level statistics to mitigate overfitting. The training process and compute resources utilized for model training are not disclosed in the paper.

**Results**  
NORMA-derived reference intervals significantly outperform traditional personalized intervals in predicting clinical outcomes. Specifically, the model demonstrates a reduction in the classification of measurements as abnormal, with only 32% of measurements flagged compared to the 68% flagged by purely personalized methods. The authors report improved predictive performance for critical outcomes, including mortality, acute kidney injury, and chronic disease, although specific metrics (e.g., AUC, accuracy) against named baselines are not provided. The results suggest that integrating individual trajectories with population-level priors enhances clinical interpretability and reduces the risk of misclassification.

**Limitations**  
The authors acknowledge that while NORMA improves upon existing methods, it may still be susceptible to biases inherent in the population data used for conditioning. They do not address potential limitations related to the generalizability of the model across different populations or the impact of data sparsity in certain demographic groups. Additionally, the reliance on historical data may not account for rapid changes in individual health status, which could affect the accuracy of predictions.

**Why it matters**  
This work has significant implications for clinical laboratory medicine, as it challenges the prevailing reliance on purely personalized interpretations of blood biomarkers. By demonstrating that a hybrid approach—anchoring individual data to population-level norms—yields better predictive accuracy, the study advocates for a paradigm shift in how laboratory results are interpreted. The public release of the model, code, and an interactive user interface promotes transparency and accessibility, potentially facilitating broader adoption of this methodology in clinical practice. This research paves the way for future studies to explore similar hybrid approaches in other areas of personalized medicine.

Authors: Aashna P. Shah, Michelle M. Li, Yash Lal, Seffi Cohen, Liat F. Antwarg, Morgan Sanchez, James A. Diao, Chirag J. Patel et al.  
Source: arXiv:2605.18701  
URL: https://arxiv.org/abs/2605.18701v1
