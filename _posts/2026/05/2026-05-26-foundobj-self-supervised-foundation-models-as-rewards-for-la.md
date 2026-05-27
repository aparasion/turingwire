---
title: "FoundObj: Self-supervised Foundation Models as Rewards for Label-free 3D Object Segmentation"
date: 2026-05-26 15:32:32 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.27178v1"
arxiv_id: "2605.27178"
authors: ["Zihui Zhang", "Zhixuan Sun", "Yafei Yang", "Jinxi Li", "Jiahao Chen", "Bo Yang"]
slug: foundobj-self-supervised-foundation-models-as-rewards-for-la
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in 3D object segmentation within complex scene point clouds, specifically focusing on the lack of reliance on scene-level human annotations during training. Existing methods are limited in their ability to identify complex objects due to insufficient object priors, which restricts their performance in diverse and challenging environments. The authors propose FoundObj, a self-supervised framework that aims to enhance the capability of 3D object segmentation without the need for labeled data, a significant advancement in the field.

**Method**  
FoundObj introduces a superpoint-based object discovery agent that incrementally merges neighboring superpoints based on semantic and geometric rewards. The architecture employs self-supervised 2D/3D foundation models to extract semantic and geometric priors, which are then utilized to provide feedback to the object discovery agent through reinforcement learning. The semantic reward module focuses on the contextual relationships between superpoints, while the geometric reward module emphasizes spatial coherence. The training process leverages a combination of these rewards to optimize the agent's performance in identifying multi-class objects. The paper does not disclose specific training compute details but emphasizes the use of extensive benchmarks for evaluation.

**Results**  
FoundObj demonstrates superior performance across multiple benchmarks compared to existing state-of-the-art methods. The authors report significant improvements in segmentation accuracy, particularly in zero-shot and long-tail scenarios, where traditional methods struggle. For instance, on the ScanNet dataset, FoundObj achieves a mean Intersection over Union (mIoU) of 65.4%, outperforming the best baseline by 5.2%. In long-tail scenarios, the method shows a 10% improvement in mIoU for underrepresented classes, highlighting its robustness and generalization capabilities.

**Limitations**  
The authors acknowledge several limitations, including the potential for the superpoint-based approach to struggle with highly occluded objects or complex geometries where superpoint merging may lead to incorrect segmentations. Additionally, the reliance on self-supervised models may introduce biases based on the pre-training data, which could affect performance in specific domains. The paper does not address the computational efficiency of the proposed method, which may be a concern for real-time applications.

**Why it matters**  
The implications of FoundObj are significant for the field of 3D object segmentation, particularly in applications where labeled data is scarce or expensive to obtain. By leveraging self-supervised learning, the framework opens avenues for scalable and efficient segmentation in diverse environments, potentially transforming how 3D data is processed in robotics, autonomous driving, and augmented reality. The ability to generalize well in zero-shot and long-tail scenarios suggests that FoundObj could serve as a foundational model for future research in unsupervised and semi-supervised learning paradigms.

Authors: Zihui Zhang, Zhixuan Sun, Yafei Yang, Jinxi Li, Jiahao Chen, Bo Yang  
Source: arXiv:2605.27178  
URL: [https://arxiv.org/abs/2605.27178v1](https://arxiv.org/abs/2605.27178v1)
