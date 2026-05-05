---
title: "Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation"
date: 2026-05-04 15:57:07 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.02757v1"
arxiv_id: "2605.02757"
authors: ["Chenyu Hui", "Xiaodi Huang", "Siyu Xu", "Yunke Wang", "Shan You", "Fei Wang"]
slug: seeing-realism-from-simulation-efficient-video-transfer-for-
summary_word_count: 479
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the significant gap in the capability of Vision-Language-Action (VLA) models, which typically depend on large-scale real-world video datasets for effective training. The authors highlight the limitations of simulated data, which, while cost-effective and easily generated, often suffers from a pronounced visual domain gap and lacks environmental diversity. This results in poor generalization to real-world scenarios, necessitating a method to enhance the utility of simulated videos for training VLA models.

**Method**  
The authors propose a novel video augmentation framework that transforms simulated VLA videos into realistic training videos while maintaining task semantics and action trajectories. The core components of the method include:

1. **Video Semantic Segmentation and Captioning**: The framework extracts structured conditions from the simulated videos, enabling the identification of key elements within the video content.
2. **Caption Diversification**: Captions are rewritten to introduce variability in the environmental context, enhancing the diversity of the training data.
3. **Conditional Video Transfer Model**: This model synthesizes realistic videos based on the extracted conditions and diversified captions.
4. **Diffusion Feature-Reuse Mechanism**: This mechanism accelerates video generation by reusing video tokens across adjacent timesteps, significantly improving computational efficiency.
5. **Coreset Sampling Strategy**: This strategy identifies a compact, non-redundant subset of data for augmentation, optimizing the use of limited computational resources.

The authors do not disclose specific training compute requirements, but the methods are designed to be practical for large-scale applications.

**Results**  
The proposed framework demonstrates substantial improvements over baseline models across multiple benchmarks. Notable results include:

- An 8% improvement in RDT-1B performance on the Robotwin 2.0 benchmark.
- A 5.1% increase in performance on the more challenging LIBERO-Plus benchmark.

These results indicate a significant enhancement in the generalization capabilities of VLA models trained with the augmented data compared to traditional methods.

**Limitations**  
The authors acknowledge that their approach may still be limited by the inherent quality of the simulated data and the effectiveness of the video transfer model. They do not address potential issues related to the scalability of the method in extremely diverse environments or the computational overhead associated with the initial data extraction and captioning processes. Additionally, the reliance on the quality of the semantic segmentation and captioning could introduce biases if the underlying models are not robust.

**Why it matters**  
This work has important implications for the development of VLA models, particularly in scenarios where real-world data is scarce or difficult to obtain. By effectively bridging the gap between simulated and real-world data, the proposed framework can enhance the training of VLA models, leading to better performance in practical applications such as robotics and interactive AI systems. The ability to generate realistic training data from simulations could also reduce the reliance on costly real-world data collection, making it a valuable contribution to the field.

Authors: Chenyu Hui, Xiaodi Huang, Siyu Xu, Yunke Wang, Shan You, Fei Wang, Tao Huang, Chang Xu  
Source: arXiv:2605.02757  
URL: https://arxiv.org/abs/2605.02757v1
