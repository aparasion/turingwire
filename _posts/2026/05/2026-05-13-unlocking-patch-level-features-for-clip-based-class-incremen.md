---
title: "Unlocking Patch-Level Features for CLIP-Based Class-Incremental Learning"
date: 2026-05-13 17:56:23 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.13835v1"
arxiv_id: "2605.13835"
authors: ["Hao Sun", "Zi-Jun Ding", "Da-Wei Zhou"]
slug: unlocking-patch-level-features-for-clip-based-class-incremen
summary_word_count: 440
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing Class-Incremental Learning (CIL) approaches that leverage CLIP (Contrastive Language-Image Pretraining) models. While prior work has focused on aligning global image embeddings (specifically the [CLS] token) with text prompts (the [EOS] token), it neglects the rich patch-level semantic information encoded in CLIP's architecture. This gap is particularly critical as local features can provide essential cues for object recognition, which are often overlooked in current methodologies. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework called SPA (Semantic-guided Patch-level Alignment) to enhance CLIP-based CIL by utilizing local representations. The method involves several key steps: 
1. **Visual Guidance Generation**: For each class, diverse visual samples are generated and processed through GPT-5 to create class-wise semantic descriptions.
2. **Patch Selection**: These descriptions guide the selection of discriminative patch-level visual features from the CLIP encoder.
3. **Cross-Modal Alignment**: Optimal transport is employed to align the selected patch tokens with the semantic tokens derived from the class-wise descriptions, facilitating a structured cross-modal alignment.
4. **Task-Specific Projectors**: The framework incorporates projectors tailored for specific tasks to adapt the model effectively to incremental learning scenarios.
5. **Calibration of Old-Class Representations**: Pseudo-features are sampled from stored class-wise Gaussian statistics to mitigate catastrophic forgetting, ensuring that previously learned classes retain their representations.

**Results**  
SPA demonstrates significant improvements over existing baselines on standard CIL benchmarks. The authors report state-of-the-art performance metrics, although specific numbers and comparisons to named baselines are not detailed in the provided text. The effectiveness of the proposed method is underscored by its ability to leverage local features, which enhances recognition accuracy in incremental learning tasks.

**Limitations**  
The authors acknowledge that their approach may introduce additional complexity in terms of computational overhead due to the integration of patch-level features and the use of GPT-5 for semantic description generation. They do not discuss potential scalability issues or the impact of varying the number of classes on performance. Additionally, the reliance on optimal transport may pose challenges in terms of computational efficiency, particularly in real-time applications.

**Why it matters**  
The implications of this work are significant for the field of CIL, particularly in applications where continuous learning from new classes is essential. By unlocking patch-level features, SPA not only enhances the performance of CLIP-based models but also sets a precedent for future research to explore local feature utilization in other architectures. This could lead to more robust models capable of retaining knowledge over time while adapting to new information, thereby advancing the state of the art in incremental learning.

Authors: Hao Sun, Zi-Jun Ding, Da-Wei Zhou  
Source: arXiv:2605.13835  
URL: https://arxiv.org/abs/2605.13835v1
