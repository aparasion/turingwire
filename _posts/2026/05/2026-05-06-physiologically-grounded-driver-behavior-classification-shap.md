---
title: "Physiologically Grounded Driver Behavior Classification: SHAP-Driven Elite Feature Selection and Hybrid Gradient Boosting for Multimodal Physiological Signals"
date: 2026-05-06 16:48:57 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.05120v1"
arxiv_id: "2605.05120"
authors: ["Sahar Askari", "Mohammad Mahdi Mirza Ali Mohammadi", "Fatemeh Ensafdoust", "Amin Golnari", "Saeid Sanei"]
slug: physiologically-grounded-driver-behavior-classification-shap
summary_word_count: 423
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the classification of driver behaviors using multimodal physiological signals. Existing approaches often rely on single-modality data, which limits the robustness and interpretability of the models. The authors propose a framework that integrates electroencephalogram (EEG), electromyography (EMG), and galvanic skin response (GSR) signals to enhance the accuracy and interpretability of driving behavior classification.

**Method**  
The proposed framework consists of several key components:  
1. **Data Collection**: A large-scale dataset of synchronized EEG, EMG, and GSR signals is utilized.  
2. **Preprocessing**: Rigorous preprocessing steps are applied to clean and prepare the data for analysis.  
3. **Feature Extraction**: A domain-specific pipeline extracts features from time-domain, frequency-domain, and derived physiological indices.  
4. **Feature Selection**: SHAP (SHapley Additive exPlanations)-based elite feature selection is employed to retain the top 250 features, effectively reducing dimensionality while maintaining predictive power.  
5. **Modeling**: Hyperparameter optimization for extreme gradient boosting (XGBoost) and light gradient boosting machine (LightGBM) is performed using Bayesian optimization via Optuna.  
6. **Ensemble Learning**: A weighted soft-voting ensemble combines the predictions from both gradient boosting models to leverage their complementary strengths.

**Results**  
The ensemble model achieves a test accuracy of 80.91% and a macro-F1 score of 0.79, significantly outperforming single-modality baselines and traditional machine learning models. Specifically, the ensemble shows an 8% performance improvement over the best single modality (EEG), underscoring the effectiveness of multimodal fusion. The results indicate that the proposed method not only enhances predictive performance but also provides insights into the physiological underpinnings of driver behavior.

**Limitations**  
The authors acknowledge that the study is limited by the reliance on a specific dataset, which may not generalize across different driving contexts or populations. Additionally, while SHAP analysis provides insights into feature importance, it does not account for potential interactions between features. The computational overhead associated with the ensemble model may also pose challenges for real-time applications. Furthermore, the study does not explore the impact of varying physiological states (e.g., fatigue, stress) on model performance.

**Why it matters**  
This work has significant implications for the development of intelligent transportation systems and driver assistance technologies. By leveraging multimodal physiological signals, the proposed framework enhances the understanding of driver behavior, which can lead to improved safety measures and more responsive vehicle systems. The interpretability provided by SHAP analysis also paves the way for future research into the physiological factors influencing driving, potentially informing interventions aimed at reducing accidents caused by driver distraction or fatigue.

Authors: Sahar Askari, Mohammad Mahdi Mirza Ali Mohammadi, Fatemeh Ensafdoust, Amin Golnari, Saeid Sanei  
Source: arXiv:2605.05120  
URL: https://arxiv.org/abs/2605.05120v1
