---
title: "Attractor-Vascular Coupling Theory: Formal Grounding and Empirical Validation for AAMI-Standard Cuffless Blood Pressure Estimation from Smartphone Photoplethysmography"
date: 2026-05-11 17:24:42 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10871v1"
arxiv_id: "2605.10871"
authors: ["Timothy Oladunni", "Farouk Ganiyu Adewumi"]
slug: attractor-vascular-coupling-theory-formal-grounding-and-empi
summary_word_count: 462
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in accurate cuffless blood pressure (BP) estimation using smartphone photoplethysmography (PPG). Existing methods often rely on multiple sensors or invasive techniques, which limits accessibility and convenience. The authors propose the Attractor-Vascular Coupling Theory (AVCT) as a novel mathematical framework that leverages cardiac attractor geometry to encode BP information, aiming to meet the AAMI standards for BP estimation without the need for traditional cuff methods.

**Method**  
The core technical contribution is the AVCT, which is grounded in Cardiac Stability Theory. The authors operationalize this theory using Takens delay embedding to extract attractor morphology features from PPG signals. They derive two theorems, one proposition, and one corollary that justify the use of PPG attractor features for BP estimation and predict the importance hierarchy of these features. A LightGBM model is trained on pulse transit time (PTT) and Cardiac Stability Index (CSI) features, employing a single-point calibration approach. The model is evaluated using strict leave-one-subject-out cross-validation (LOSO-CV) on a dataset comprising 46 subjects, with a total of 29,684 windows of data.

**Results**  
The LightGBM model achieved a mean absolute error (MAE) of 2.05 mmHg for systolic BP (SBP) and 1.67 mmHg for diastolic BP (DBP), with correlation coefficients of r = 0.990 and r = 0.991, respectively. These results satisfy the AAMI/IEEE SP10 requirement of MAE below 5 mmHg. The median per-subject MAE was 1.87 mmHg for SBP and 1.54 mmHg for DBP, with 70% and 76% of subjects meeting AAMI criteria individually. Notably, a PPG-only model using nine smartphone attractor features achieved results within 0.05 mmHg of the ECG+PPG model, indicating that high-quality BP tracking is feasible using only a smartphone camera. The authors report a 91.5% error reduction from uncalibrated to calibrated estimation, confirming all four AVCT predictions quantitatively.

**Limitations**  
The authors acknowledge that their study is limited by the relatively small sample size (46 subjects) and the specific demographic of the dataset, which may not generalize across broader populations. Additionally, while the model demonstrates high accuracy, the reliance on a single-point calibration may introduce variability in real-world applications. The authors do not address potential confounding factors such as variations in PPG signal quality due to motion artifacts or skin tone differences.

**Why it matters**  
This work has significant implications for the development of non-invasive, accessible BP monitoring technologies. By demonstrating that clinical-grade BP estimation can be achieved using only smartphone cameras, the research paves the way for widespread adoption of cuffless BP monitoring in both clinical and home settings. The grounding of BP estimation in nonlinear dynamical systems theory also opens avenues for further research into the application of AVCT in other physiological measurements, potentially enhancing the robustness and interpretability of machine learning models in healthcare.

Authors: Timothy Oladunni, Farouk Ganiyu Adewumi  
Source: arXiv:2605.10871  
URL: https://arxiv.org/abs/2605.10871v1
