---
title: "VISReg: Variance-Invariance-Sketching Regularization for JEPA training"
date: 2026-06-01 17:58:01 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2606.02572v1"
arxiv_id: "2606.02572"
authors: ["Haiyu Wu", "Randall Balestriero", "Morgan Levine"]
slug: visreg-variance-invariance-sketching-regularization-for-jepa
summary_word_count: 401
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces VISReg, a novel regularization technique for self-supervised learning that enhances embedding stability and performance on out-of-distribution datasets."
---

**Problem**  
This work addresses the limitations of existing self-supervised learning methods, particularly those that utilize covariance-based regularization, such as VICReg. While VICReg effectively prevents embedding collapse through variance and covariance objectives, it only captures second-order statistics, which inadequately enforces the full distributional shape necessary for stable training. The authors highlight that current sketching-based methods, like SIGReg, improve upon this by aligning embeddings to an isotropic Gaussian but suffer from a lack of flexibility and experience vanishing gradients during collapse. This paper is a preprint and has not undergone peer review.

**Method**  
The authors propose Variance-Invariance-Sketching Regularization (VISReg), which innovatively replaces the covariance term in VICReg with a Sliced-Wasserstein-based sketching objective. This approach enforces a more comprehensive distributional shape while maintaining a variance term for scale control. By decoupling scale and shape, VISReg combines the flexibility of VICReg with the robustness of sketching methods. The architecture leverages standard self-supervised learning frameworks, and the training process is designed to be computationally efficient, scaling linearly with respect to the dataset size. The authors provide code and project details at https://haiyuwu.github.io/visreg.

**Results**  
VISReg demonstrates superior performance on low-quality datasets compared to existing regularization techniques. Specifically, when pre-trained on ImageNet-1K, VISReg achieves state-of-the-art results on out-of-distribution datasets. Notably, when pre-trained on ImageNet-22K, VISReg matches the out-of-distribution performance of DINOv2, despite DINOv2 utilizing ten times more data (LVD-142M). The authors report significant improvements in embedding stability and robustness across various training conditions, particularly in long-tailed and low-rank regimes.

**Limitations**  
The authors acknowledge that while VISReg improves upon existing methods, it may still be sensitive to hyperparameter tuning, particularly in the choice of the Sliced-Wasserstein distance metric. Additionally, the paper does not extensively evaluate VISReg across a wide range of datasets beyond ImageNet, which may limit generalizability. The authors also do not address potential computational overhead introduced by the Sliced-Wasserstein objective, which could impact scalability in very large datasets.

**Why it matters**  
The introduction of VISReg has significant implications for the field of self-supervised learning, particularly in enhancing the stability and performance of embeddings in challenging training scenarios. By effectively addressing the shortcomings of existing regularization techniques, VISReg paves the way for more robust self-supervised models that can generalize better to out-of-distribution data. This advancement is crucial for applications in real-world scenarios where data distributions can vary significantly. The findings and methodologies presented in this paper contribute to ongoing research in self-supervised learning, as published in [arXiv cs.CV](https://arxiv.org/abs/2606.02572v1).
