---
title: "MoCapAnything V2: End-to-End Motion Capture for Arbitrary Skeletons"
date: 2026-04-30 17:16:38 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.28130v1"
arxiv_id: "2604.28130"
authors: ["Kehong Gong", "Zhengyu Wen", "Dao Thien Phong", "Mingxi Xu", "Weixia He", "Qi Wang"]
slug: mocapanything-v2-end-to-end-motion-capture-for-arbitrary-ske
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing factorized pipelines for arbitrary-skeleton motion capture from monocular video, which typically involve separate Video-to-Pose and inverse-kinematics (IK) stages. These methods suffer from ambiguities in joint rotations due to the non-differentiable nature of IK, which restricts the system's ability to adapt to noisy predictions and optimize for final animation objectives. The authors propose the first fully end-to-end framework that jointly learns and optimizes both Video-to-Pose and Pose-to-Rotation, filling a significant gap in the literature regarding the integration of these components. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The proposed framework introduces a novel architecture that integrates Video-to-Pose and Pose-to-Rotation into a single learnable model. The key innovation is the use of a reference pose-rotation pair from the target asset, which anchors the mapping and defines the rotation coordinate system, thus transforming the rotation prediction into a well-constrained conditional problem. The model employs a skeleton-aware Global-Local Graph-guided Multi-Head Attention (GL-GMHA) module, facilitating joint-level local reasoning and global coordination. The training process leverages a dataset of arbitrary skeletons, with a focus on optimizing both joint positions and rotations directly from video input, eliminating the need for mesh intermediates. The authors do not disclose specific training compute details.

**Results**  
The proposed method demonstrates significant improvements over existing baselines on the Truebones Zoo and Objaverse datasets. The rotation error is reduced from approximately 17 degrees to 10 degrees, and further to 6.54 degrees on unseen skeletons. Additionally, the framework achieves approximately 20 times faster inference compared to traditional mesh-based pipelines, showcasing its efficiency and robustness in real-time applications.

**Limitations**  
The authors acknowledge that the model's performance may be influenced by the quality of the reference pose-rotation pairs used for training, as well as the potential for overfitting to specific skeleton configurations. They do not address the scalability of the model to highly complex or non-standard skeletons, nor do they discuss the implications of varying video quality or occlusions on performance. Furthermore, the reliance on a single reference pose may limit generalization across diverse motion capture scenarios.

**Why it matters**  
This work has significant implications for the field of motion capture and animation, particularly in applications requiring real-time performance and adaptability to arbitrary skeletons. By providing a fully end-to-end solution, the framework enhances the robustness and efficiency of motion capture systems, paving the way for more sophisticated applications in gaming, virtual reality, and film production. The integration of learnable components also opens avenues for future research into more generalized motion capture techniques that can handle a wider variety of skeletal structures and motion dynamics.

Authors: Kehong Gong, Zhengyu Wen, Dao Thien Phong, Mingxi Xu, Weixia He, Qi Wang, Ning Zhang, Zhengyu Li et al.  
Source: arXiv:2604.28130  
URL: [https://arxiv.org/abs/2604.28130v1](https://arxiv.org/abs/2604.28130v1)
