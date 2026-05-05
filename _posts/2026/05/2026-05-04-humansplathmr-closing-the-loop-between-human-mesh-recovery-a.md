---
title: "HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar"
date: 2026-05-04 16:26:11 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.02784v1"
arxiv_id: "2605.02784"
authors: ["Yeheng Zong", "Pou-Chun Kung", "Yike Pan", "Seth Isaacson", "Yizhou Chen", "Ram Vasudevan"]
slug: humansplathmr-closing-the-loop-between-human-mesh-recovery-a
summary_word_count: 418
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing methods for human mesh recovery (HMR) and avatar generation from video, particularly in the context of 3D geometry accuracy. Current approaches, including ViT-based models, often overfit to 2D views and fail to generalize well to novel poses. Additionally, NeRF and Gaussian Splatting techniques treat pose and appearance separately, which hampers rendering performance in dynamic scenarios. The authors propose HumanSplatHMR as a solution to these issues, presenting a preprint that has not yet undergone peer review.

**Method**  
HumanSplatHMR introduces a joint optimization framework that integrates 3D human pose refinement with high-fidelity avatar learning. The architecture leverages a differentiable renderer to backpropagate losses—specifically photometric, segmentation, and depth losses—directly to pose parameters and global positions. This approach allows for real-time adjustments to the 3D pose based on image-level feedback, enhancing the accuracy of pose recovery. The model utilizes a state-of-the-art human pose estimator to generate initial mesh estimates, which are then iteratively refined through the optimization process. The training compute details are not disclosed, but the method emphasizes the importance of coupling geometric pose estimation with rendering to improve overall performance.

**Results**  
The authors report significant improvements in pose recovery accuracy and rendering quality compared to baseline methods. Specifically, HumanSplatHMR outperforms traditional pose recovery techniques that do not incorporate image-level refinement, as well as avatar generation methods that decouple pose estimation from mesh reconstruction. While exact numerical results are not provided in the abstract, the paper claims consistent enhancements across various benchmarks, indicating a robust performance against established baselines.

**Limitations**  
The authors acknowledge that their method relies on the initial human mesh estimates provided by the pose estimator, which may introduce inaccuracies if the estimator performs poorly. Additionally, the paper does not address the computational efficiency of the proposed framework, which could be a concern for real-time applications. The reliance on differentiable rendering may also limit the approach's applicability in scenarios where such rendering is computationally prohibitive.

**Why it matters**  
HumanSplatHMR has significant implications for applications in motion capture, virtual reality, and digital twinning, where accurate human representation is crucial. By effectively closing the loop between pose estimation and rendering, this work paves the way for more realistic and adaptable human avatars in dynamic environments. The integration of image-level feedback into the pose refinement process could inspire future research in related fields, potentially leading to advancements in real-time 3D reconstruction and interactive applications.

Authors: Yeheng Zong, Pou-Chun Kung, Yike Pan, Seth Isaacson, Yizhou Chen, Ram Vasudevan, Katherine A. Skinner  
Source: arXiv:2605.02784  
URL: https://arxiv.org/abs/2605.02784v1
