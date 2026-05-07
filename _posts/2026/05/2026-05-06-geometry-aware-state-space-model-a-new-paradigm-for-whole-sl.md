---
title: "Geometry-Aware State Space Model: A New Paradigm for Whole-Slide Image Representation"
date: 2026-05-06 17:33:30 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.05164v1"
arxiv_id: "2605.05164"
authors: ["Enhui Chai", "Sicheng Chen", "Tianyi Zhang", "Chad Wong", "Kecheng Huang", "Zeyu Liu"]
slug: geometry-aware-state-space-model-a-new-paradigm-for-whole-sl
summary_word_count: 402
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing Multiple Instance Learning (MIL) approaches in histopathological image analysis, particularly in the context of Whole-Slide Images (WSIs). Current methods typically embed patch representations in homogeneous Euclidean spaces, which fails to capture the hierarchical organization and regional heterogeneity of pathological tissues. This gap restricts the models' ability to effectively represent global tissue architecture and fine-grained cellular morphology. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel hybrid hyperbolic-Euclidean representation for WSI features, which allows for the complementary modeling of hierarchical tissue structures and local morphological details. The core technical contribution is the BatMIL framework, which integrates this dual geometric representation. BatMIL employs a structured state space sequence model (S4) as its backbone, enabling efficient encoding of patch sequences with linear computational complexity. Additionally, a chunk-level mixture-of-experts (MoE) module is introduced to group patches into regions, dynamically routing them to specialized subnetworks. This design enhances representational capacity while minimizing redundant computations. The training process and specific loss functions are not detailed in the abstract.

**Results**  
The authors conducted extensive experiments across seven WSI datasets encompassing six cancer types. BatMIL consistently outperformed state-of-the-art MIL methods in slide-level classification tasks. While specific numerical results are not provided in the abstract, the authors claim significant improvements over existing approaches, indicating that the geometry-aware representation leads to enhanced performance in computational pathology.

**Limitations**  
The authors acknowledge that their approach may still be limited by the inherent complexity of pathological tissue structures, which could introduce challenges in generalization across diverse datasets. They do not discuss potential issues related to the scalability of the mixture-of-experts module or the computational overhead associated with the dual geometric representation. Additionally, the reliance on a structured state space model may limit the framework's applicability to other domains outside of histopathology.

**Why it matters**  
This work has significant implications for the field of computational pathology, as it introduces a new paradigm for WSI representation that leverages geometric properties to improve classification accuracy. The hybrid representation and efficient modeling of long-range dependencies could pave the way for more sophisticated analysis techniques in medical imaging, potentially enhancing diagnostic capabilities and treatment planning. Furthermore, the findings may inspire future research into geometry-aware learning frameworks across various domains in machine learning.

Authors: Enhui Chai, Sicheng Chen, Tianyi Zhang, Chad Wong, Kecheng Huang, Zeyu Liu, Fei Xia  
Source: arXiv:2605.05164  
URL: [https://arxiv.org/abs/2605.05164v1](https://arxiv.org/abs/2605.05164v1)
