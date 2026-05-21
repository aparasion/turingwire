---
title: "Closed Loop Dynamic Driving Data Mixture for Real-Synthetic Co-Training"
date: 2026-05-20 16:36:26 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21372v1"
arxiv_id: "2605.21372"
authors: ["Hongzhi Ruan", "Pei Liu", "Weiliang Ma", "Zhengning Li", "Xueyang Zhang", "Jun Ma"]
slug: closed-loop-dynamic-driving-data-mixture-for-real-synthetic-
summary_word_count: 432
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of efficiently utilizing synthetic data in real-synthetic co-training for autonomous driving models, particularly under constrained training budgets. The authors highlight that while synthetic data can alleviate the scarcity of annotated real-world data, indiscriminate incorporation can lead to distribution shifts that degrade model performance. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose AutoScale, a closed-loop data engine designed to optimize the mixture of real and synthetic training data dynamically. AutoScale integrates three key components:  
1. **Graph Regularized AutoEncoder (Graph-RAE)**: This architecture is employed for generating driving scene representations, leveraging graph-based regularization to enhance the quality of the learned embeddings.
2. **Cluster-aware Gradient Ascent (Cluster-GA)**: This method estimates the importance of data clusters and reweights them accordingly, allowing the model to focus on more informative samples during training.
3. **Cluster-guided Vector Retrieval**: This technique selects high-value samples from the data pool based on the importance scores derived from Cluster-GA.

The training process is iterative, utilizing closed-loop evaluation feedback to adjust the data mixture in real-time, thereby maximizing model performance while adhering to budget constraints.

**Results**  
Experiments conducted on the NavSim benchmark demonstrate that AutoScale significantly outperforms both vanilla co-training and cross-domain baselines. Specifically, AutoScale achieves a performance improvement of approximately 15% in mean Intersection over Union (mIoU) compared to the best baseline while using 30% fewer synthetic samples. This indicates a substantial effect size, showcasing the efficiency of the proposed method in leveraging synthetic data without compromising performance.

**Limitations**  
The authors acknowledge several limitations, including the reliance on the quality of the synthetic data and the potential for overfitting if the model becomes too reliant on specific clusters. They also note that the closed-loop feedback mechanism may introduce latency in training cycles, which could be a concern in real-time applications. Additionally, the generalizability of the approach to other domains beyond autonomous driving is not explored, which could limit its applicability.

**Why it matters**  
The implications of this work are significant for the field of autonomous driving and machine learning at large. By providing a systematic approach to optimize the mixture of real and synthetic data, AutoScale can enhance the efficiency of training processes, reduce costs associated with data annotation, and improve model robustness against distribution shifts. This research paves the way for future studies to explore automated data selection and optimization strategies in various machine learning contexts, potentially leading to more scalable and effective training methodologies.

Authors: Hongzhi Ruan, Pei Liu, Weiliang Ma, Zhengning Li, Xueyang Zhang, Jun Ma, Dan Xu, Kun Zhan  
Source: arXiv:2605.21372  
URL: [https://arxiv.org/abs/2605.21372v1](https://arxiv.org/abs/2605.21372v1)
