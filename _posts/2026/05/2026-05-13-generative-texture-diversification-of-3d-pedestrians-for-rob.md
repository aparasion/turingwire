---
title: "Generative Texture Diversification of 3D Pedestrians for Robust Autonomous Driving Perception"
date: 2026-05-13 16:35:50 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.13755v1"
arxiv_id: "2605.13755"
authors: ["Arka Bhowmick", "Enes Ozeren", "Ahmed Abdullah", "Oliver Wasenmuller"]
slug: generative-texture-diversification-of-3d-pedestrians-for-rob
summary_word_count: 403
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the availability of high-quality, diverse datasets for training 2D and 3D perception models in autonomous driving, particularly for pedestrian detection. Existing real-world datasets are often insufficient due to the high costs and time associated with large-scale annotated data collection. The authors propose a method to generate synthetic pedestrian data that maintains variability and realism, which is crucial for enhancing the robustness of perception systems in safety-critical scenarios.

**Method**  
The authors introduce a method for generating diverse 3D pedestrian instances from a single base asset. This is achieved by employing StyleGAN2 to synthesize varied facial textures and identity-level appearance variations, which are then automatically mapped onto 3D meshes. The approach allows for scalable diversification of pedestrian appearances without the need for creating new geometries for each instance. The generated assets are used to construct synthetic datasets, which are then mixed with real data to evaluate the impact on RGB-based object detection performance. The study also investigates the effects of geometry-driven distribution shifts on point cloud perception for 3D object detection.

**Results**  
The authors report that their method of controlled synthetic diversification significantly improves robustness in 2D detection tasks. While specific numerical results are not disclosed in the abstract, the findings indicate that the integration of synthetic data enhances model performance compared to using real data alone. Additionally, the experiments reveal that 3D perception models exhibit sensitivity to geometric domain gaps, suggesting that the quality of 3D data is critical for effective detection.

**Limitations**  
The authors acknowledge that their approach relies on the quality of the base 3D asset and the effectiveness of the StyleGAN2-generated textures. They do not address potential limitations related to the generalizability of the synthetic data across different environments or the computational resources required for generating and training on these datasets. Furthermore, the impact of the synthetic data on long-term model performance and real-world applicability remains unexamined.

**Why it matters**  
This work has significant implications for the development of robust autonomous driving systems. By demonstrating that generative AI can effectively create diverse pedestrian representations, the authors provide a scalable solution to the data scarcity problem in autonomous driving. The insights gained from the analysis of cross-domain training strategies can inform future research on improving the resilience of perception models to domain shifts, ultimately contributing to safer autonomous navigation in complex environments.

Authors: Arka Bhowmick, Enes Ozeren, Ahmed Abdullah, Oliver Wasenmuller  
Source: arXiv:2605.13755  
URL: [https://arxiv.org/abs/2605.13755v1](https://arxiv.org/abs/2605.13755v1)
