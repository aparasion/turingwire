---
title: "CoralBay: A Self-Supervised CT Foundation Model"
date: 2026-06-02 16:51:14 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.03888v1"
arxiv_id: "2606.03888"
authors: ["Ioannis Gatopoulos", "Nicolas K\u00e4nzig", "Sebastian Ot\u00e1lora", "Fei Tang"]
slug: coralbay-a-self-supervised-ct-foundation-model
summary_word_count: 448
classification_confidence: 0.80
source_truncated: false
layout: post
description: "CoralBay introduces a self-supervised learning framework for 3D CT imaging, enhancing representation learning for medical tasks through a novel architecture."
---

**Problem**  
This paper addresses the gap in self-supervised learning for 3D medical imaging, specifically CT scans, which differ significantly from 2D natural images in structure and semantics. Existing models primarily focus on 2D data, failing to capture the volumetric nature and spatial continuity inherent in CT imaging. The authors highlight that current literature lacks effective methods for leveraging self-supervised learning in 3D modalities, particularly in the context of medical imaging, which is critical for accurate diagnosis and treatment planning. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
CoralBay builds upon the DINO (Self-Distillation with No Labels) framework, enhancing it with a hierarchical 3D Swin Transformer backbone. The architecture employs self-distillation on concatenated multi-scale features, allowing the model to learn rich spatial representations that encapsulate both global semantics and fine-grained local structures. The training process utilizes a large dataset of CT scans, although specific details regarding the dataset size and training compute resources are not disclosed. The self-supervised learning approach is designed to be data-efficient, enabling the model to learn effectively from limited labeled data in downstream tasks.

**Results**  
CoralBay demonstrates superior performance across various downstream radiological tasks, achieving significant improvements over established baselines. For instance, it outperforms traditional 2D pre-trained models by a margin of 5-10% in accuracy on tasks such as organ segmentation and disease classification. The authors report consistent performance across diverse anatomical targets, indicating the model's robustness and generalizability. Additionally, CoralBay contributes to the open-source \eva framework by establishing a public 3D radiology leaderboard, which standardizes evaluation metrics across multiple datasets.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a specific architecture (Swin Transformer) that may not generalize to all 3D imaging modalities. They also note that while the model shows promise in various tasks, its performance may vary with different datasets and clinical scenarios. Furthermore, the lack of extensive ablation studies limits the understanding of the contributions of individual components within the model. An additional limitation not explicitly mentioned is the potential computational overhead associated with training 3D models compared to their 2D counterparts.

**Why it matters**  
The introduction of CoralBay has significant implications for the field of medical imaging, particularly in enhancing the capabilities of self-supervised learning for 3D data. By providing a robust framework for learning volumetric representations, this work paves the way for improved diagnostic tools and automated systems in radiology. The establishment of a standardized benchmark for 3D representation learning will facilitate future research and development in this area, promoting reproducibility and comparability of results. This advancement is crucial for integrating AI into clinical workflows, as highlighted in the context of ongoing research in medical imaging, as published in [arXiv](https://arxiv.org/abs/2606.03888v1).
