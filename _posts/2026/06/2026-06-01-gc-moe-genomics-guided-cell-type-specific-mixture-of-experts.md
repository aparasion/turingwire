---
title: "GC-MoE: Genomics-Guided Cell-Type-Specific Mixture of Experts for Histology-Based Single-Cell Spatial Transcriptomics"
date: 2026-06-01 16:01:44 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02424v1"
arxiv_id: "2606.02424"
authors: ["Kaito Shiku", "Ahtisham Fazeel Abbasi", "Ryoma Bise", "Yuichiro Iwashita", "Kazuya Nishimura", "Andreas Dengel"]
slug: gc-moe-genomics-guided-cell-type-specific-mixture-of-experts
summary_word_count: 392
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces GC-MoE, a novel framework for predicting cell-type-specific gene expression from histopathological images in single-cell spatial transcriptomics."
---

**Problem**  
The paper addresses the gap in existing methodologies for histology-based single-cell spatial transcriptomics (ST), which typically predict gene expression profiles at the spot level, aggregating multiple cells. This approach fails to capture the cell-to-cell expression variability that is crucial for accurate gene expression estimation. The authors highlight that current models do not adequately account for the structured nature of gene expression variability across different cell types. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose the Genomics-Guided Cell-Type-Specific Mixture-of-Experts (GC-MoE) framework, which utilizes a routing network to estimate cell-type probabilities and combines outputs from cell-type-specific experts for gene expression prediction. The architecture includes a Cell-Type-Specific Co-Expression-Aware Predictor (CAP) that encodes gene programs specific to each cell type. Additionally, a lightweight Cell-to-Cell Interaction Attention (C2CA) module is integrated to incorporate contextual information from neighboring cells, enhancing the model's ability to capture local interactions. The training process leverages public single-cell ST datasets, although specific details on training compute are not disclosed.

**Results**  
GC-MoE demonstrates significant performance improvements over existing single-cell and adapted spot-level baselines. The authors report consistent enhancements in predictive accuracy across various public datasets, although specific metrics and comparisons to named baselines are not detailed in the abstract. The results indicate that the proposed model effectively captures the nuanced expression variability among different cell types, outperforming traditional methods.

**Limitations**  
The authors acknowledge that their model's performance is contingent on the quality and diversity of the training datasets. They also note that while GC-MoE improves upon existing methods, it may still struggle with highly heterogeneous tissue samples where cell types are not well-defined. Additionally, the reliance on a routing network introduces complexity that may affect interpretability. The paper does not address potential computational overhead associated with the mixture-of-experts architecture.

**Why it matters**  
The introduction of GC-MoE has significant implications for advancing the field of spatial transcriptomics, particularly in applications where single-cell measurements are prohibitively expensive or logistically challenging. By improving the accuracy of gene expression predictions from histological images, this work could facilitate more effective analyses of tissue microenvironments and disease states. The findings contribute to the growing body of literature on integrating machine learning with genomics, as published in [arXiv](https://arxiv.org/abs/2606.02424v1). This framework may serve as a foundation for future research aimed at enhancing the resolution and interpretability of spatial transcriptomic data.
