---
title: "VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction"
date: 2026-05-14 17:59:04 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.15186v1"
arxiv_id: "2605.15186"
authors: ["Kaixin Zhu", "Yiwen Tang", "Yifan Yang", "Renrui Zhang", "Bohan Zeng", "Ziyu Guo"]
slug: vggt-edit-feed-forward-native-3d-scene-editing-with-residual
summary_word_count: 409
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing 3D scene editing methods that rely on 2D-lifting strategies, which often result in blurry textures and inconsistent geometry due to a lack of spatial awareness. The authors highlight that while high-quality 3D scene reconstruction has advanced, current models struggle to respond effectively to dynamic human instructions, limiting their applicability in interactive environments. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this paper is VGGT-Edit, a feed-forward framework designed for text-conditioned native 3D scene editing. The architecture incorporates depth-synchronized text injection, which aligns semantic guidance with the spatial poses of the backbone model. This alignment is crucial for stable instruction grounding. The framework employs a residual transformation head that predicts 3D geometric displacements directly, allowing for scene deformation while maintaining background stability. The training process utilizes a multi-term objective function that enforces geometric accuracy and cross-view consistency. The authors also introduce the DeltaScene Dataset, a large-scale dataset generated through an automated pipeline with 3D agreement filtering to ensure high-quality ground truth.

**Results**  
VGGT-Edit demonstrates significant improvements over traditional 2D-lifting baselines. The authors report sharper object details and enhanced multi-view consistency, with near-instant inference speeds. While specific quantitative results are not detailed in the abstract, the qualitative improvements suggest a substantial effect size in terms of visual fidelity and structural integrity when compared to existing methods.

**Limitations**  
The authors acknowledge that their approach may still face challenges in handling highly complex scenes or extreme editing scenarios that require nuanced understanding beyond the current model's capabilities. Additionally, the reliance on a large-scale dataset may introduce biases based on the dataset's composition, which could affect generalization to unseen environments. The paper does not discuss potential computational costs associated with training or inference, which could be a concern for deployment in resource-constrained settings.

**Why it matters**  
The implications of VGGT-Edit are significant for the field of interactive 3D applications, such as virtual reality, gaming, and architectural visualization. By enabling more responsive and accurate scene editing based on natural language instructions, this work paves the way for more intuitive user interfaces and enhances the realism of generated environments. The introduction of a dedicated dataset also contributes to the community by providing a benchmark for future research in 3D scene understanding and editing.

Authors: Kaixin Zhu, Yiwen Tang, Yifan Yang, Renrui Zhang, Bohan Zeng, Ziyu Guo, Ruichuan An, Zhou Liu et al.  
Source: arXiv:2605.15186  
URL: https://arxiv.org/abs/2605.15186v1
