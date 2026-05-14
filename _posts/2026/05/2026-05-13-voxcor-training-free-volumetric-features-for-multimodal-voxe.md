---
title: "VoxCor: Training-Free Volumetric Features for Multimodal Voxel Correspondence"
date: 2026-05-13 17:20:26 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.13798v1"
arxiv_id: "2605.13798"
authors: ["Guney Tombak", "Ertunc Erdil", "Ender Konukoglu"]
slug: voxcor-training-free-volumetric-features-for-multimodal-voxe
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in cross-modal 3D medical image analysis, specifically the need for voxelwise representations that maintain anatomical consistency across different imaging modalities, scanners, and acquisition protocols. Existing methods often rely on frozen 2D Vision Transformer (ViT) models but typically extract features along a single anatomical axis, limiting their applicability to new volumes and failing to leverage complementary viewing directions. The authors propose VoxCor, a training-free method that enhances the reusability of volumetric feature representations derived from frozen ViT models. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
VoxCor employs a fit-transform approach that integrates triplanar ViT inference with a compact closed-form weighted partial least squares (WPLS) projection. During the offline fitting phase, it establishes voxel correspondences to identify modality-stable anatomical directions in the triplanar feature space. The method does not require fine-tuning or registration during the transform phase; instead, it utilizes linear projection and triplanar ViT inference to map new volumes. Voxel correspondences can be queried via nearest-neighbor search, facilitating efficient retrieval of anatomical features. The authors provide implementation details and publicly available code on GitHub.

**Results**  
VoxCor was evaluated on two tasks: intra-subject Abdomen MR–CT and inter-subject HCP T2w–T1w. The results demonstrate that VoxCor significantly improves performance in challenging cross-subject, cross-modality transfer scenarios. Specifically, it achieves competitive registration performance compared to both handcrafted descriptors and learned 3D features. The method reduces encoder sensitivity for dense correspondence transfer, indicating robustness in various settings. While specific numerical results are not detailed in the abstract, the authors claim substantial improvements over baseline methods in the aforementioned tasks.

**Limitations**  
The authors acknowledge that VoxCor's performance may be contingent on the quality of the frozen ViT models used, as well as the specific anatomical structures being analyzed. They do not address potential limitations related to the scalability of the method to other imaging modalities or the generalizability of the learned representations across diverse datasets. Additionally, the reliance on nearest-neighbor search may introduce computational overhead in large-scale applications.

**Why it matters**  
VoxCor's training-free approach to volumetric feature extraction has significant implications for downstream multimodal analysis, particularly in medical imaging where rapid and accurate voxel correspondence is critical. By enabling reusable feature representations that are modality-stable, VoxCor can facilitate more efficient workflows in clinical settings, enhance the robustness of cross-modal analyses, and potentially improve diagnostic outcomes. This work opens avenues for further research into the integration of frozen foundation models in medical imaging tasks, paving the way for advancements in automated image analysis and interpretation.

Authors: Guney Tombak, Ertunc Erdil, Ender Konukoglu  
Source: arXiv:2605.13798  
URL: [https://arxiv.org/abs/2605.13798v1](https://arxiv.org/abs/2605.13798v1)
