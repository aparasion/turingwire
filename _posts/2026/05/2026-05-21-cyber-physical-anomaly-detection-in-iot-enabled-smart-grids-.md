---
title: "Cyber-Physical Anomaly Detection in IoT-Enabled Smart Grids Using Machine Learning and Metaheuristic Feature Optimization"
date: 2026-05-21 17:18:57 +0000
category: research
subcategory: other
company: "null"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22749v1"
arxiv_id: "2605.22749"
authors: ["Adis Alihod\u017ei\u0107", "Eva Tuba", "Milan Tuba"]
slug: cyber-physical-anomaly-detection-in-iot-enabled-smart-grids-
summary_word_count: 449
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in effective anomaly detection within IoT-enabled smart grids, particularly distinguishing between physical incidents and cyber-physical attacks. The increasing complexity of smart grid infrastructures, characterized by dense measurement systems and communication links, heightens vulnerability to both natural and malicious disruptions. Existing literature lacks comprehensive methods that integrate machine learning with feature optimization to enhance detection capabilities in this context.

**Method**  
The authors propose a hybrid approach that combines machine learning with a genetic algorithm (GA) for feature selection. The architecture employs several baseline models, including logistic regression, RBF-SVM, XGBoost, Random Forest, and Extra Trees, to classify events from the MSU/ORNL Power System Attack Dataset. The GA is utilized to optimize the feature set, reducing the initial 112 attributes from phasor measurement units (PMUs) and intelligent electronic devices (IEDs) to an average of 27.4 attributes across five runs. The training process leverages the full feature set to establish baseline performance metrics, which are then compared against the optimized model. The evaluation metrics include macro-F1 and ROC-AUC, providing a robust assessment of classification performance.

**Results**  
The results indicate that tree-based ensemble models outperform other baseline methods, with Extra Trees achieving the highest performance metrics. Specifically, after applying the GA for feature selection, the GA + Extra Trees model improves the macro-F1 score from 0.9118 to 0.9212 and the ROC-AUC from 0.9791 to 0.9837. This demonstrates a significant enhancement in classification accuracy while reducing the feature space, suggesting that many PMU measurements are redundant and that a compact subset can still yield reliable anomaly detection.

**Limitations**  
The authors acknowledge that the study is limited by its reliance on a single dataset, which may not encompass the full spectrum of potential cyber-physical attacks or physical incidents in diverse smart grid environments. Additionally, the generalizability of the feature selection process and the model's performance across different grid configurations and attack scenarios remains untested. The authors do not address potential overfitting due to the reduced feature set or the implications of using a genetic algorithm for feature selection in real-time applications.

**Why it matters**  
This work has significant implications for the development of robust anomaly detection systems in smart grids, particularly as the integration of IoT devices continues to expand. By demonstrating that a reduced set of features can maintain high detection accuracy, the study paves the way for more efficient monitoring systems that require less computational overhead. This could lead to faster response times in identifying and mitigating cyber-physical threats, ultimately enhancing the resilience and security of smart grid infrastructures. The findings also encourage further exploration of feature optimization techniques in other domains where high-dimensional data is prevalent.

Authors: Adis Alihodžić, Eva Tuba, Milan Tuba  
Source: arXiv:2605.22749  
URL: [https://arxiv.org/abs/2605.22749v1](https://arxiv.org/abs/2605.22749v1)
