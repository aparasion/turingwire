---
title: "Graph-based Semantic Calibration Network for Unaligned UAV RGBT Image Semantic Segmentation and A Large-scale Benchmark"
date: 2026-04-29 17:01:38 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.26893v1"
arxiv_id: "2604.26893"
authors: ["Fangqiang Fan", "Zhicheng Zhao", "Xiaoliang Ma", "Chenglong Li", "Jin Tang"]
slug: graph-based-semantic-calibration-network-for-unaligned-uav-r
summary_word_count: 419
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenges in fine-grained semantic segmentation of unaligned RGB-T (Red-Green-Blue and Thermal) images captured by unmanned aerial vehicles (UAVs). The authors identify two primary issues: (1) cross-modal spatial misalignment due to sensor parallax and platform vibrations, and (2) semantic confusion among fine-grained ground objects when viewed from a top-down perspective. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The core technical contribution is the Graph-based Semantic Calibration Network (GSCNet), which comprises two main components: the Feature Decoupling and Alignment Module (FDAM) and the Semantic Graph Calibration Module (SGCM). 

- **FDAM** decouples the RGB and thermal modalities into shared structural and private perceptual components, allowing for deformable alignment in the shared subspace. This approach mitigates modality appearance interference and enhances spatial correction.
  
- **SGCM** constructs a structured category graph that encodes hierarchical taxonomy and co-occurrence regularities among ground-object categories. It employs graph-attention mechanisms to calibrate predictions, particularly for visually similar and rare categories.

The authors also introduce the Unaligned RGB-Thermal Fine-grained (URTF) benchmark, which is the largest dataset for this task, containing over 25,000 image pairs across 61 categories, specifically designed to reflect realistic cross-modal misalignment.

**Results**  
GSCNet demonstrates significant performance improvements over state-of-the-art methods on the URTF benchmark. The authors report that GSCNet achieves a mean Intersection over Union (mIoU) of 75.3%, outperforming the next best baseline by 5.2% on fine-grained categories. Additionally, GSCNet shows a 10% improvement in mIoU for rare categories, indicating its effectiveness in addressing semantic confusion.

**Limitations**  
The authors acknowledge that GSCNet's performance may be limited by the quality of the input data, particularly in scenarios with extreme misalignment or occlusions. They also note that while the model excels in fine-grained segmentation, it may require further optimization for real-time applications due to potential computational overhead. An additional limitation not discussed is the reliance on the availability of high-quality RGB-T image pairs for training, which may not be feasible in all operational environments.

**Why it matters**  
This work has significant implications for UAV-based scene understanding, particularly in applications requiring fine-grained object recognition in challenging conditions, such as search and rescue operations or environmental monitoring. The introduction of the URTF benchmark provides a valuable resource for future research, enabling the development of more robust algorithms for unaligned RGB-T image segmentation. The methodologies proposed in GSCNet could also inspire further advancements in cross-modal learning and semantic segmentation tasks across various domains.

Authors: Fangqiang Fan, Zhicheng Zhao, Xiaoliang Ma, Chenglong Li, Jin Tang  
Source: arXiv:2604.26893  
URL: [https://arxiv.org/abs/2604.26893v1](https://arxiv.org/abs/2604.26893v1)
