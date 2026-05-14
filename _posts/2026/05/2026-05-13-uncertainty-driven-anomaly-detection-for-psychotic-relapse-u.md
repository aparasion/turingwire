---
title: "Uncertainty-Driven Anomaly Detection for Psychotic Relapse Using Smartwatches: Forecasting and Multi-Task Learning Fusion"
date: 2026-05-13 17:43:07 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13816v1"
arxiv_id: "2605.13816"
authors: ["Nikolaos Tsalkitzis", "Panagiotis P. Filntisis", "Petros Maragos", "Niki Efthymiou"]
slug: uncertainty-driven-anomaly-detection-for-psychotic-relapse-u
summary_word_count: 433
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in capability for early detection of psychotic relapse through continuous monitoring using digital phenotyping. Existing literature lacks robust frameworks that effectively integrate diverse physiological signals from wearable devices, particularly smartwatches, to predict relapses. The authors aim to enhance the predictive accuracy of relapse detection by leveraging cardiac, motion, and sleep data, which have not been sufficiently combined in prior studies.

**Method**  
The authors propose two distinct frameworks for anomaly detection based on smartwatch data. The first framework utilizes a forecasting approach to predict cardiac dynamics, flagging deviations between predicted and observed features as indicators of potential relapse. The second framework employs a multi-task learning paradigm that integrates sleep, motion, and cardiac signals, utilizing Transformer encoders to learn time-aware embeddings and predict measurement timing. Both frameworks output a daily anomaly score derived from predictive uncertainty, estimated via an ensemble of multilayer perceptrons, which enhances robustness against variability inherent in real-world wearable data. A late-fusion strategy is then applied to combine the anomaly scores from both frameworks, resulting in a unified decision score.

**Results**  
The proposed fused model was evaluated on the 2nd e-Prevention Grand Challenge dataset, achieving an 8% relative improvement over the previous competition-winning baseline. The authors conducted extensive ablation studies to validate the contributions of each component, demonstrating that the integration of diverse digital phenotypes significantly enhances the fidelity of psychotic relapse detection. The results indicate that the complementary nature of the physiological signals captured by the two frameworks leads to improved predictive performance.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a specific dataset, which may not generalize across different populations or settings. Additionally, the performance of the models may be influenced by the quality and consistency of the data collected from smartwatches, which can vary among users. The study does not address the potential for real-time implementation challenges in clinical settings, nor does it explore the interpretability of the model outputs, which could be critical for clinical adoption.

**Why it matters**  
This work has significant implications for the field of mental health monitoring and intervention. By demonstrating the effectiveness of integrating multiple physiological signals for anomaly detection, it paves the way for more accurate and timely interventions for individuals at risk of psychotic relapse. The methodologies developed could be adapted for other mental health conditions, potentially leading to broader applications of digital phenotyping in clinical practice. Furthermore, the findings underscore the importance of leveraging ensemble approaches and multi-task learning in the development of robust predictive models in healthcare.

Authors: Nikolaos Tsalkitzis, Panagiotis P. Filntisis, Petros Maragos, Niki Efthymiou  
Source: arXiv:2605.13816  
URL: [https://arxiv.org/abs/2605.13816v1](https://arxiv.org/abs/2605.13816v1)
