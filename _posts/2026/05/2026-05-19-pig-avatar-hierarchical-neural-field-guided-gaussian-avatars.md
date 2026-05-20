---
title: "PiG-Avatar: Hierarchical Neural-Field-Guided Gaussian Avatars"
date: 2026-05-19 17:59:54 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.20185v1"
arxiv_id: "2605.20185"
authors: ["Julian Kaltheuner", "Jan Spindler", "Sina Kitz", "Patrick Stotko", "Reinhard Klein"]
slug: pig-avatar-hierarchical-neural-field-guided-gaussian-avatars
summary_word_count: 412
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
Existing Gaussian avatar methods are constrained by their reliance on body-template surfaces, which intertwine the representation of the avatar with the deformation of the template. This coupling limits the ability to accurately capture complex, layered, off-body, and non-rigid clothing geometries. The authors present PiG-Avatar, a novel approach that addresses this limitation by decoupling the representation from the template topology. This work is a preprint and has not yet undergone peer review.

**Method**  
PiG-Avatar employs a continuous neural field to represent avatars as Gaussians anchored in a volumetric canonical space, using the parametric body model solely for kinematic transport. This design allows for the anchors to deviate from the template surface, maintaining kinematic coherence through 3D barycentric anchor transport. The authors introduce a dual-level spatially coherent optimization strategy that combines Sobolev-preconditioned neural-field updates with a KNN-based preconditioning of canonical anchor geometry. This approach facilitates an emergent self-organization of anchor density, where anchors autonomously migrate towards regions of high curvature, appearance variation, and non-coherent motion. The architecture supports hierarchical reconstruction, enabling coarse-level supervision to propagate to finer levels through a shared field and coupled anchor graph.

**Results**  
PiG-Avatar demonstrates state-of-the-art rendering quality on established benchmarks that include subjects with complex clothing and challenging non-rigid motion. The method achieves significant improvements over existing baselines, although specific quantitative results (e.g., PSNR, SSIM) are not disclosed in the abstract. The authors claim robust generalization to imperfect body model initialization and real-time rendering capabilities across all detail levels, indicating a substantial advancement in rendering efficiency and fidelity.

**Limitations**  
The authors acknowledge that while PiG-Avatar effectively decouples representation from template topology, the reliance on a parametric body model for kinematic transport may still impose some limitations in scenarios with extreme deformations. Additionally, the optimization process may require significant computational resources, although specific training compute details are not provided. The paper does not address potential challenges in scalability or the performance of the method in highly dynamic environments.

**Why it matters**  
The implications of PiG-Avatar extend to various applications in computer graphics, virtual reality, and animation, where accurate and flexible avatar representations are crucial. By enabling the capture of complex clothing geometries and non-rigid motions without the constraints of traditional surface-based methods, this work paves the way for more realistic and adaptable digital avatars. The hierarchical reconstruction capability also suggests potential for improved detail management in real-time applications, enhancing user experience in interactive environments.

Authors: Julian Kaltheuner, Jan Spindler, Sina Kitz, Patrick Stotko, Reinhard Klein  
Source: arXiv:2605.20185v1  
URL: https://arxiv.org/abs/2605.20185v1
