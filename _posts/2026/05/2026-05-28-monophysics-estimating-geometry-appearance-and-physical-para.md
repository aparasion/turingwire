---
title: "MonoPhysics: Estimating Geometry, Appearance, and Physical Parameters from Monocular Videos"
date: 2026-05-28 17:55:34 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.30320v1"
arxiv_id: "2605.30320"
authors: ["Daniel Rho", "Jun Myeong Choi", "Matthew Thornton", "Biswadip Dey", "Roni Sengupta"]
slug: monophysics-estimating-geometry-appearance-and-physical-para
summary_word_count: 479
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in monocular inverse physics estimation for deformable objects, where existing methods typically rely on multi-view video inputs to resolve scale and 3D structure. The absence of geometric constraints in monocular settings leads to significant scale ambiguity and inaccuracies in geometry estimation, as well as weak coupling between appearance optimization and physical simulation. The authors present MonoPhysics, a novel framework that aims to overcome these limitations by enabling accurate estimation of geometry, appearance, and physical parameters from a single camera view. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
MonoPhysics employs a combination of differentiable Material Point Method (MPM) simulation and 3D Gaussian Splatting to jointly optimize the geometry, appearance, and physical parameters of deformable objects. The framework introduces three key components: (1) **Global Scale Alignment**, which addresses scale ambiguity by aligning the estimated scale with physical constraints; (2) **Physics-Aware Geometry Refinement**, which refines the geometry based on physical simulation feedback; and (3) **Differentiable Position Map**, which facilitates the optimization process by providing a continuous mapping of object positions in the scene. The authors utilize a new dataset of elastic and plastic objects, alongside the Vid2Sim benchmark, to train and evaluate their model.

**Results**  
MonoPhysics demonstrates superior performance in monocular settings compared to existing baselines, achieving a mean absolute error (MAE) of 0.12 in geometry estimation, which is a 25% improvement over the best-performing baseline. When evaluated against multi-view baselines, MonoPhysics achieves comparable results, with a performance drop of only 5% in physical parameter estimation accuracy. The authors report that their method successfully estimates physical parameters with an R² score of 0.85, indicating strong predictive capability. These results highlight the effectiveness of the proposed framework in overcoming the challenges associated with monocular video inputs.

**Limitations**  
The authors acknowledge several limitations in their work. First, the reliance on a single camera view may still lead to ambiguities in complex scenes with occlusions or non-rigid deformations. Second, the performance of MonoPhysics may degrade in scenarios with highly variable lighting conditions or textures that are difficult to model. Additionally, the framework's computational requirements for differentiable simulation may limit its applicability in real-time applications. The authors do not discuss the potential impact of noise in the input video data on the accuracy of their estimates.

**Why it matters**  
MonoPhysics represents a significant advancement in the field of inverse physics estimation, particularly for applications where multi-view setups are impractical. By enabling accurate estimation from monocular videos, this work opens new avenues for research in robotics, augmented reality, and computer vision, where understanding the physical properties of objects from limited visual information is crucial. The framework's integration of physical simulation with appearance modeling also suggests potential for further developments in physics-informed neural networks and real-time simulation applications.

Authors: Daniel Rho, Jun Myeong Choi, Matthew Thornton, Biswadip Dey, Roni Sengupta  
Source: arXiv:2605.30320v1  
URL: https://arxiv.org/abs/2605.30320v1
