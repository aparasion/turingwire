---
title: "DALight-3D: A Lightweight 3D U-Net for Brain Tumor Segmentation from Multi-Modal MRI"
date: 2026-05-06 05:54:44 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.04518v1"
arxiv_id: "2605.04518"
authors: ["Nand Kumar Mishra", "Dhruv Mishra", "Dr Manu Pratap Singh"]
slug: dalight-3d-a-lightweight-3d-u-net-for-brain-tumor-segmentati
summary_word_count: 452
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in efficient brain tumor segmentation from multi-modal MRI scans, a task that remains computationally intensive with existing volumetric models. The authors present DALight-3D, a lightweight architecture designed to reduce the computational burden while maintaining segmentation accuracy. This work is a preprint and has not yet undergone peer review.

**Method**  
DALight-3D is a compact variant of the 3D U-Net architecture, incorporating several innovative techniques to enhance performance while minimizing parameter count. Key components include:
- **Depthwise Separable 3D Convolutions**: These convolutions reduce the number of parameters and computational load by separating spatial and channel-wise operations.
- **Identifier-Conditioned Normalization**: This normalization technique adapts the feature scaling based on the input identifiers, improving model robustness.
- **Cross-Slice Attention (CSA)**: This mechanism allows the model to focus on relevant slices of the MRI data, enhancing contextual understanding across the volumetric input.
- **Adaptive Skip Fusion Block (SSFB)**: This block dynamically fuses features from different layers, optimizing the information flow and improving segmentation accuracy.

The model was trained for 50 epochs on the Medical Segmentation Decathlon Task01 BrainTumour benchmark, with a focus on matched optimization settings against established baselines, including standard 3D U-Net, Attention U-Net, Residual 3D U-Net, and V-Net.

**Results**  
DALight-3D achieved a mean Dice score of 0.727 with only 2.22 million parameters. In comparison, the Residual 3D U-Net, which has 3.20 million parameters, achieved a mean Dice score of 0.710. This indicates a significant improvement in segmentation performance relative to the increase in model efficiency. The authors also conducted component-wise ablation studies, demonstrating consistent performance degradation when any of the key components (SepConv, identifier-conditioned normalization, CSA, or SSFB) were removed, underscoring their importance in the architecture.

**Limitations**  
The authors acknowledge that while DALight-3D shows promise, its performance is evaluated solely on the Medical Segmentation Decathlon Task01 BrainTumour benchmark, which may limit generalizability to other datasets or clinical scenarios. Additionally, the model's lightweight nature may not capture all complex tumor morphologies, potentially affecting segmentation accuracy in more challenging cases. The paper does not discuss the model's inference speed or real-time applicability in clinical settings, which are critical for practical deployment.

**Why it matters**  
The development of DALight-3D has significant implications for the field of medical image analysis, particularly in enhancing the efficiency of brain tumor segmentation tasks. By reducing the computational cost associated with volumetric models, this architecture could facilitate broader adoption in clinical environments where rapid and accurate segmentation is crucial. Furthermore, the techniques introduced, such as depthwise separable convolutions and cross-slice attention, may inspire future research into lightweight architectures for other medical imaging tasks, potentially leading to advancements in automated diagnostics and treatment planning.

Authors: Nand Kumar Mishra, Dhruv Mishra, Dr Manu Pratap Singh  
Source: arXiv:2605.04518  
URL: [https://arxiv.org/abs/2605.04518v1](https://arxiv.org/abs/2605.04518v1)
