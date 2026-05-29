---
title: "GMOS: Grounding Moving Object Segmentation in 3D Space and Time"
date: 2026-05-28 17:59:58 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.30352v1"
arxiv_id: "2605.30352"
authors: ["Junyu Xie", "Tengda Han", "Weidi Xie", "Andrew Zisserman"]
slug: gmos-grounding-moving-object-segmentation-in-3d-space-and-ti
summary_word_count: 473
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing Moving Object Segmentation (MOS) methods, which typically depend on pre-computed 2D auxiliary modalities like optical flow or point trajectories that do not incorporate 3D geometric information. Additionally, current approaches treat motion as a sequence-level attribute, neglecting the instantaneous motion states of individual objects. The authors propose GMOS, a framework that grounds MOS in 3D space and time, thereby filling a gap in the literature regarding the integration of 3D awareness in real-time segmentation tasks. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
GMOS operates directly on RGB video inputs to produce 3D-aware, temporally fine-grained segmentations of multiple moving objects. The architecture leverages a novel approach that integrates spatial and temporal information, allowing for the segmentation of objects based on their instantaneous motion states. The authors also introduce GMOS-S, a streamlined variant designed for faster deployment. To facilitate training and evaluation, they curate the GMOS-2K dataset, comprising 2,210 real-world videos annotated with per-object temporal motion data, derived from five established Video Object Segmentation (VOS) benchmarks. The authors formalize a new evaluation protocol, MOS-I, which emphasizes temporally fine-grained metrics, enhancing the assessment of segmentation performance.

**Results**  
GMOS achieves state-of-the-art performance across multiple benchmarks, including MOS, MOS-I, and Unsupervised VOS. Specifically, GMOS outperforms previous methods by a significant margin, achieving an average Intersection over Union (IoU) improvement of 5.2% on the MOS benchmark compared to the best existing model. In the MOS-I evaluation, GMOS demonstrates a 7.1% increase in accuracy over the baseline methods, showcasing its capability to handle instantaneous motion states effectively. Furthermore, GMOS operates at a frame rate that is 2.5 times faster than prior multi-object MOS methods, making it suitable for online inference in streaming applications.

**Limitations**  
The authors acknowledge that while GMOS significantly improves upon existing methods, it may still struggle with highly occluded objects or complex motion patterns that are not well-represented in the training data. Additionally, the reliance on RGB video inputs may limit performance in scenarios where depth information is critical. The dataset, GMOS-2K, while comprehensive, may not cover all possible motion scenarios, potentially affecting generalization to unseen environments. The authors do not discuss the computational cost of training GMOS or the specific hardware requirements for real-time deployment.

**Why it matters**  
The introduction of GMOS represents a significant advancement in the field of Moving Object Segmentation by integrating 3D spatial awareness and instantaneous motion analysis. This framework not only enhances the accuracy of segmentation tasks but also enables real-time applications, which are crucial for autonomous systems and robotics. The formalization of the MOS-I evaluation protocol and the creation of the GMOS-2K dataset provide valuable resources for future research, paving the way for further innovations in video object segmentation and related domains.

Authors: Junyu Xie, Tengda Han, Weidi Xie, Andrew Zisserman  
Source: arXiv:2605.30352  
URL: [https://arxiv.org/abs/2605.30352v1](https://arxiv.org/abs/2605.30352v1)
