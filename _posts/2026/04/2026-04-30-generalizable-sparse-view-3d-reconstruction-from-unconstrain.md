---
title: "Generalizable Sparse-View 3D Reconstruction from Unconstrained Images"
date: 2026-04-30 17:59:55 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.28193v1"
arxiv_id: "2604.28193"
authors: ["Vinayak Gupta", "Chih-Hao Lin", "Shenlong Wang", "Anand Bhattad", "Jia-Bin Huang"]
slug: generalizable-sparse-view-3d-reconstruction-from-unconstrain
summary_word_count: 417
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of reconstructing 3D scenes from sparse, unposed images under real-world conditions, which include varying illumination and transient occlusions. Existing methods typically rely on scene-specific optimization techniques that utilize appearance embeddings or dynamic masks, necessitating extensive training for each scene. This approach limits generalization capabilities and often fails when dealing with sparse views. The authors present this work as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The core technical contribution is the GenWildSplat framework, a feed-forward architecture designed for sparse-view outdoor reconstruction. This framework eliminates the need for per-scene optimization by leveraging learned geometric priors to predict depth, camera parameters, and 3D Gaussians in a canonical space. The architecture includes an appearance adapter that modulates the predicted appearance to match target lighting conditions, and a semantic segmentation component that effectively manages transient objects. The model is trained using a curriculum learning approach on both synthetic and real datasets, enhancing its ability to generalize across diverse illumination and occlusion scenarios. The authors do not disclose specific training compute details.

**Results**  
GenWildSplat achieves state-of-the-art performance on the PhotoTourism and MegaScenes benchmarks, demonstrating superior feed-forward rendering quality compared to existing methods. The framework enables real-time inference without the need for test-time optimization, which is a significant advantage over traditional approaches. While specific quantitative results are not provided in the abstract, the authors claim that their method outperforms named baselines, indicating a substantial improvement in rendering quality and generalization capabilities.

**Limitations**  
The authors acknowledge that their approach may still struggle with highly complex scenes or extreme occlusions that were not adequately represented in the training data. Additionally, the reliance on synthetic data for curriculum learning may introduce biases that affect performance on real-world datasets. The paper does not discuss the computational efficiency of the model in terms of memory usage or the scalability of the architecture to larger datasets.

**Why it matters**  
The implications of this work are significant for downstream applications in computer vision and graphics, particularly in scenarios where 3D reconstruction is required from limited or unstructured image data. By providing a framework that generalizes well across varying conditions without the need for extensive scene-specific training, GenWildSplat opens avenues for real-time applications in augmented reality, autonomous navigation, and remote sensing. The ability to handle transient occlusions and varying lighting conditions enhances the robustness of 3D reconstruction systems, making them more applicable in dynamic environments.

Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
Source: arXiv:2604.28193  
URL: [https://arxiv.org/abs/2604.28193v1](https://arxiv.org/abs/2604.28193v1)
