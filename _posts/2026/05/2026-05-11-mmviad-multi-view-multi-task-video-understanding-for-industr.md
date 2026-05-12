---
title: "MMVIAD: Multi-view Multi-task Video Understanding for Industrial Anomaly Detection"
date: 2026-05-11 16:49:38 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10833v1"
arxiv_id: "2605.10833"
authors: ["Xiran Zhao", "Jing Jin", "Yan Bai", "Zhongan Wang", "Yifeng Sun", "Yihang Lou"]
slug: mmviad-multi-view-multi-task-video-understanding-for-industr
summary_word_count: 446
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in industrial anomaly detection literature, particularly the lack of continuous multi-view video datasets that reflect real-world inspection processes. Existing datasets predominantly focus on static images or sparse views, which inadequately represent the complexities of dynamic environments in manufacturing. The authors introduce MMVIAD (Multi-view Multi-task Video Industrial Anomaly Detection), which is, to the best of their knowledge, the first dataset designed for continuous multi-view video anomaly detection and understanding. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the MMVIAD dataset, which consists of object-centric 2-second inspection clips featuring approximately 120 degrees of camera motion. The dataset encompasses 48 object categories, 14 environments, and 6 types of structural anomalies, enabling a multi-task evaluation framework that includes anomaly detection, defect classification, object classification, and anomaly visible-time localization. To enhance model performance, the authors propose a two-stage post-training pipeline. The first stage, Perception-Structured Supervised Fine-Tuning (PS-SFT), initializes perception-structured reasoning. The second stage, Visibility-grounded Industrial Structured Temporal Anomaly Group Relative Policy Optimization (VISTA-GRPO), refines the model using a semantic-gated defect reward and visibility-aware temporal reward, culminating in the final model, VISTA.

**Results**  
Systematic evaluations on the MMVIAD dataset reveal that existing commercial and open-source video multi-layered models (MLLMs) significantly underperform compared to human capabilities, particularly in fine-grained defect recognition and temporal grounding. The VISTA model demonstrates a marked improvement, achieving an average score of 57.5 on the MMVIAD-Unseen benchmark, compared to a baseline score of 45.0 from the base model. This performance surpasses that of GPT-5.4, indicating a substantial advancement in multi-task video understanding for industrial applications.

**Limitations**  
The authors acknowledge that the dataset may not encompass all possible industrial scenarios, which could limit the generalizability of the findings. Additionally, the reliance on a two-stage post-training approach may introduce complexity in model deployment and real-time application. The paper does not address potential biases in the dataset or the computational resources required for training the VISTA model, which may be significant given the complexity of the tasks involved.

**Why it matters**  
The introduction of the MMVIAD dataset and the VISTA model has significant implications for the field of industrial anomaly detection. By providing a comprehensive multi-view video dataset, this work enables more robust training and evaluation of models in real-world scenarios, potentially leading to improved quality control in manufacturing processes. The methodologies developed here could serve as a foundation for future research in multi-task learning and anomaly detection, fostering advancements in automated inspection systems and enhancing operational efficiency in industrial settings.

Authors: Xiran Zhao, Jing Jin, Yan Bai, Zhongan Wang, Yifeng Sun, Yihang Lou, Xuanyu Zhu, Tao Feng et al.  
Source: arXiv:2605.10833  
URL: [https://arxiv.org/abs/2605.10833v1](https://arxiv.org/abs/2605.10833v1)
