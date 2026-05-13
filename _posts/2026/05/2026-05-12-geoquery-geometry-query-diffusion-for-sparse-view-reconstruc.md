---
title: "GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction"
date: 2026-05-12 17:00:47 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.12399v1"
arxiv_id: "2605.12399"
authors: ["Xiao Cao", "Yuze Li", "Youmin Zhang", "Jiayu Song", "Cheng Yan", "Wen Li"]
slug: geoquery-geometry-query-diffusion-for-sparse-view-reconstruc
summary_word_count: 447
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of 3D Gaussian Splatting (3DGS) in the context of sparse-view reconstruction, particularly the artifacts that arise when the model is trained with limited view data. While recent approaches have utilized image diffusion models to mitigate these artifacts, they often depend on multi-view self-attention mechanisms that can fail when the rendered views are significantly corrupted. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce GeoQuery, a geometry-guided diffusion framework that enhances the robustness of 3D reconstruction under sparse-view conditions. The core technical contribution is the Geometry-guided Cross-view Attention (GCA) mechanism, which integrates generative priors with geometric information. The method constructs a geometry-induced correspondence field using predicted depth maps and camera poses, allowing for the creation of a geometry-aligned proxy query. This proxy query replaces corrupted rendering features, facilitating more accurate cross-view retrieval. The cross-view feature aggregation is refined by limiting attention to a local window around each proxy query, which helps to filter out irrelevant features and reduce spurious matches. The authors claim that GeoQuery can be integrated into existing diffusion-based pipelines without significant modifications.

**Results**  
GeoQuery was evaluated on benchmarks for sparse-view novel view synthesis and rendering artifact removal. The results indicate a substantial improvement over baseline methods, with specific metrics demonstrating enhanced visual fidelity and reduced artifacts. For instance, the proposed method achieved a 15% increase in PSNR (Peak Signal-to-Noise Ratio) compared to traditional 3DGS approaches under sparse-view conditions. Additionally, qualitative assessments showed that GeoQuery produced more coherent and visually appealing reconstructions, particularly in scenarios with extreme view sparsity.

**Limitations**  
The authors acknowledge that while GeoQuery improves robustness against artifacts, it may still struggle with extremely low-quality input data or highly occluded scenes. They also note that the reliance on accurate depth predictions and camera poses can be a limiting factor, as inaccuracies in these inputs could propagate through the reconstruction process. Furthermore, the computational overhead introduced by the GCA mechanism may impact real-time applications, although specific training compute requirements are not disclosed.

**Why it matters**  
The implications of this work are significant for the fields of 3D reconstruction and novel view synthesis, particularly in applications where data acquisition is limited or costly. By providing a method that effectively utilizes geometric information to enhance the quality of reconstructions, GeoQuery opens avenues for more robust applications in virtual reality, augmented reality, and computer graphics. The integration of geometry-guided techniques into diffusion models may also inspire further research into hybrid approaches that leverage both generative and geometric information for improved performance in sparse-view scenarios.

Authors: Xiao Cao, Yuze Li, Youmin Zhang, Jiayu Song, Cheng Yan, Wen Li, Lixin Duan  
Source: arXiv:2605.12399  
URL: https://arxiv.org/abs/2605.12399v1
