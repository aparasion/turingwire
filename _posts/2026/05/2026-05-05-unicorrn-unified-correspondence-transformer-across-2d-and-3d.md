---
title: "UniCorrn: Unified Correspondence Transformer Across 2D and 3D"
date: 2026-05-05 17:58:53 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.04044v1"
arxiv_id: "2605.04044"
authors: ["Prajnan Goswami", "Tianye Ding", "Feng Liu", "Huaizu Jiang"]
slug: unicorrn-unified-correspondence-transformer-across-2d-and-3d
summary_word_count: 379
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of a unified model for visual correspondence across multiple modalities: 2D-2D, 2D-3D, and 3D-3D. Current approaches typically employ task-specific architectures, leading to inefficiencies and limitations in generalization across different geometric matching tasks. The authors propose UniCorrn, a preprint work that aims to bridge this gap by providing a single model capable of handling all three correspondence tasks with shared weights.

**Method**  
UniCorrn leverages a Transformer-based architecture to capture cross-modal feature similarities effectively. The model consists of a dual-stream decoder that separates appearance and positional feature streams, allowing for flexible query-based correspondence estimation. The architecture incorporates modality-specific backbones, which feed into shared encoder and decoder components. This design facilitates end-to-end learning and is trained on a diverse dataset that combines pseudo point clouds generated from depth maps with real 3D correspondence annotations. The training process is optimized to enhance performance across all three tasks simultaneously.

**Results**  
UniCorrn demonstrates competitive performance in 2D-2D matching and significantly outperforms previous state-of-the-art methods in 2D-3D and 3D-3D tasks. Specifically, it achieves an 8% improvement in registration recall on the 7Scenes dataset for 2D-3D matching and a 10% improvement on the 3DLoMatch dataset for 3D-3D matching. These results indicate a substantial enhancement in the model's ability to establish correspondences across different modalities compared to existing solutions.

**Limitations**  
The authors acknowledge that while UniCorrn shows promising results, it may still be limited by the quality and diversity of the training data, particularly in scenarios with sparse or noisy point cloud data. Additionally, the reliance on Transformer architecture may introduce computational overhead, which could be a concern for real-time applications. The paper does not address potential scalability issues when applied to larger datasets or more complex scenes.

**Why it matters**  
The development of UniCorrn has significant implications for 3D vision tasks, as it provides a versatile framework that can be applied across various applications, including robotics, augmented reality, and autonomous navigation. By unifying the correspondence tasks, this work paves the way for more efficient model training and deployment, potentially leading to advancements in multi-modal perception systems. The ability to generalize across different geometric matching tasks could also inspire future research into more integrated approaches in computer vision.

Authors: Prajnan Goswami, Tianye Ding, Feng Liu, Huaizu Jiang  
Source: arXiv cs.CV  
URL: [https://arxiv.org/abs/2605.04044v1](https://arxiv.org/abs/2605.04044v1)
