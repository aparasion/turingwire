---
title: "Min Generalized Sliced Gromov Wasserstein: A Scalable Path to Gromov Wasserstein"
date: 2026-05-13 16:33:10 +0000
category: research
subcategory: efficiency_inference
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13753v1"
arxiv_id: "2605.13753"
authors: ["Ashkan Shahbazi", "Xinran Liu", "Ping He", "Soheil Kolouri"]
slug: min-generalized-sliced-gromov-wasserstein-a-scalable-path-to
summary_word_count: 426
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the computational inefficiency of existing Gromov-Wasserstein (GW) solvers, particularly in high-dimensional spaces. The authors propose a novel approach, min Generalized Sliced Gromov-Wasserstein (min-GSGW), which leverages generalized slicers to enhance the scalability of the GW problem. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of generalized slicers into the sliced GW framework. The authors develop a method that learns coupled nonlinear slicers, which assign compatible push-forward values to both input measures. This allows for the construction of a transport plan that maintains monotonicity in the projected domain, which is then evaluated against the GW objective in the original spaces. The min-GSGW approach minimizes the GW cost directly in the original spaces, ensuring that the resulting transport plan is rigid-motion invariant, a property essential for applications in geometric matching and shape analysis. Additionally, the authors propose an amortized variant that replaces per-instance optimization with a learned slicer, enabling efficient processing of unseen input pairs. The training process and specific computational resources used are not disclosed.

**Results**  
The authors validate min-GSGW through experiments on three tasks: animal mesh matching, horse mesh interpolation, and ShapeNet part transfer. The results demonstrate that min-GSGW achieves meaningful geometric correspondences and GW objective values while significantly reducing computational costs compared to existing GW solvers. Although specific numerical results are not detailed in the abstract, the emphasis on "substantially lower computational cost" suggests a marked improvement over baseline methods, which typically struggle with scalability in high-dimensional settings.

**Limitations**  
The authors acknowledge that while min-GSGW improves computational efficiency, it may still be sensitive to the choice of hyperparameters in the learning process of the slicers. Additionally, the reliance on learned slicers may introduce generalization issues when applied to highly diverse datasets not represented in the training set. The paper does not discuss potential limitations related to the robustness of the learned transport plans under varying input distributions or the scalability of the method to even larger datasets.

**Why it matters**  
The introduction of min-GSGW has significant implications for geometric matching and shape analysis tasks, particularly in fields such as computer vision and graphics where efficient and accurate shape correspondence is critical. By providing a scalable solution to the GW problem, this work opens avenues for further research into more complex geometric structures and their applications in machine learning. The amortized approach also suggests potential for real-time applications where rapid processing of geometric data is required.

Authors: Ashkan Shahbazi, Xinran Liu, Ping He, Soheil Kolouri  
Source: arXiv:2605.13753  
URL: [https://arxiv.org/abs/2605.13753v1](https://arxiv.org/abs/2605.13753v1)
