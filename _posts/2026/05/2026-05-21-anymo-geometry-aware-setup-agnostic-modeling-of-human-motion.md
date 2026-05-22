---
title: "AnyMo: Geometry-Aware Setup-Agnostic Modeling of Human Motion in the Wild"
date: 2026-05-21 16:52:10 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22715v1"
arxiv_id: "2605.22715"
authors: ["Baiyu Chen", "Zechen Li", "Wilson Wongso", "Lihuan Li", "Xiachong Lin", "Hao Xue"]
slug: anymo-geometry-aware-setup-agnostic-modeling-of-human-motion
summary_word_count: 462
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of setup-dependent variability in human motion recognition using wearable inertial measurement units (IMUs). Current models struggle to generalize across different sensing setups, which include variations in body location, mounting position, sensor orientation, and device hardware. This limitation hampers the applicability of wearable IMUs in real-world scenarios and restricts their use to closed-set recognition tasks. The authors present AnyMo, a geometry-aware framework designed to enable setup-agnostic human motion modeling. This work is a preprint and has not yet undergone peer review.

**Method**  
AnyMo employs a multi-faceted approach to model human motion. It utilizes physics-grounded IMU simulation to generate diverse synthetic signals across various body-surface placements. The framework pre-trains a graph encoder using paired synthetic placement views and masked partial observations, allowing it to learn robust representations of human motion. The model tokenizes multi-position IMU data into full-body motion tokens, which are then aligned with a large language model (LLM) to facilitate motion-language understanding. The training process leverages a combination of synthetic data generation and graph-based encoding, although specific details regarding the architecture, loss functions, and training compute are not disclosed.

**Results**  
AnyMo demonstrates significant improvements across three tasks: zero-shot activity recognition, cross-modal retrieval, and wearable IMU motion captioning. On the Human Activity Recognition (HAR) benchmark, AnyMo achieves an average improvement of 11.7% in Accuracy, 11.6% in F1 score, and 22.6% in Recall at 2 (R@2) compared to baseline models. In cross-modal retrieval tasks, it increases the mean reciprocal rank (MRR) for IMU-to-text retrieval by 15.9% and for text-to-IMU retrieval by 28.6%. Additionally, the model enhances zero-shot captioning performance, achieving an 18.8% improvement in BERT-F1 score. These results indicate that AnyMo effectively generalizes across unseen datasets and modalities.

**Limitations**  
The authors acknowledge that while AnyMo shows promise, it may still be limited by the quality and diversity of the synthetic data generated. The reliance on simulated signals could introduce biases that do not fully capture the complexities of real-world motion. Furthermore, the model's performance on highly variable or extreme motion scenarios remains untested. The paper does not discuss the computational efficiency or scalability of the model in practical applications, which could be critical for deployment in resource-constrained environments.

**Why it matters**  
The development of AnyMo has significant implications for the field of wearable motion analysis. By providing a setup-agnostic framework, it opens avenues for broader applications of wearable IMUs in diverse environments, enhancing the potential for real-time human motion understanding. This work could facilitate advancements in areas such as health monitoring, sports analytics, and human-computer interaction, where accurate motion recognition is crucial. The integration of motion-language understanding also suggests potential for improved human-robot interaction and assistive technologies.

Authors: Baiyu Chen, Zechen Li, Wilson Wongso, Lihuan Li, Xiachong Lin, Hao Xue, Benjamin Tag, Flora Salim  
Source: arXiv:2605.22715  
URL: [https://arxiv.org/abs/2605.22715v1](https://arxiv.org/abs/2605.22715v1)
