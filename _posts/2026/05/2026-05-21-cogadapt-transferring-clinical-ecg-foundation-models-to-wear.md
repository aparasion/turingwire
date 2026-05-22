---
title: "CogAdapt: Transferring Clinical ECG Foundation Models to Wearable Cognitive Load Assessment via Lead Adaptation"
date: 2026-05-21 17:33:35 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22774v1"
arxiv_id: "2605.22774"
authors: ["Amir Mousavi", "Mohammad Sadegh Sirjani", "Erfan Nourbakhsh", "Mimi Xie", "Rocky Slavin", "Leslie Neely"]
slug: cogadapt-transferring-clinical-ecg-foundation-models-to-wear
summary_word_count: 396
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of real-time cognitive load assessment using wearable devices, which is hindered by limited labeled data and poor generalization across subjects. The authors highlight that existing ECG foundation models, pre-trained on extensive clinical datasets, cannot be directly utilized for wearable applications due to discrepancies in sensor configurations and task-specific requirements. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this work is the CogAdapt framework, which consists of two main components: LeadBridge and ProFine. LeadBridge is a learnable adapter that transforms 3-lead ECG signals from wearable devices into anatomically consistent 12-lead representations, effectively bridging the gap between clinical and wearable data formats. ProFine is a progressive fine-tuning strategy that incrementally unfreezes layers of the encoder to adapt the pre-trained model while mitigating the risk of catastrophic forgetting. The authors employ a leave-one-subject-out cross-validation strategy for training and evaluation, ensuring robust performance across different subjects.

**Results**  
CogAdapt demonstrates significant improvements over baseline models trained from scratch on two public datasets: CLARE and CL-Drive. The macro-F1 scores achieved are 0.626 and 0.768, respectively, indicating a substantial enhancement in performance. These results suggest that the adaptation of foundation models can effectively facilitate subject-independent cognitive load assessment using wearable sensors, outperforming traditional training approaches.

**Limitations**  
The authors acknowledge several limitations, including the reliance on specific datasets (CLARE and CL-Drive), which may not fully represent the diversity of real-world scenarios. Additionally, the performance of CogAdapt may be influenced by the quality and characteristics of the input data from wearable devices. The paper does not address the potential computational overhead introduced by the LeadBridge adapter or the scalability of the ProFine strategy to larger datasets or more complex tasks.

**Why it matters**  
The implications of this work are significant for the field of adaptive human-computer interaction, as it paves the way for more accurate and generalizable cognitive load assessments using wearable technology. By leveraging pre-trained ECG foundation models, this research opens avenues for further exploration into the adaptation of other clinical models for various real-time applications in health monitoring and cognitive assessment. The findings could lead to improved user experiences in adaptive systems, enhancing the responsiveness and personalization of interactions based on cognitive load.

Authors: Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, Mimi Xie, Rocky Slavin, Leslie Neely, John Davis, John Quarles  
Source: arXiv:2605.22774  
URL: [https://arxiv.org/abs/2605.22774v1](https://arxiv.org/abs/2605.22774v1)
