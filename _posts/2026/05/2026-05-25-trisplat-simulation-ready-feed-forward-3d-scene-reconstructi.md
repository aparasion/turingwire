---
title: "TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction"
date: 2026-05-25 17:59:53 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.26115v1"
arxiv_id: "2605.26115"
authors: ["Weijie Wang", "Zimu Li", "Jinchuan Shi", "Zeyu Zhang", "Botao Ye", "Marc Pollefeys"]
slug: trisplat-simulation-ready-feed-forward-3d-scene-reconstructi
summary_word_count: 446
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing feed-forward 3D reconstruction methods that primarily utilize Gaussian primitives, which do not directly yield usable meshes for downstream applications such as simulation, physics reasoning, or embodied interaction. The authors highlight that current approaches necessitate costly post-processing steps to extract meshes, particularly in pose-free scenarios where both scene structure and camera parameters must be inferred from sparse observations. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce TriSplat, a novel feed-forward reconstruction network that employs oriented triangle primitives to represent 3D scenes. The architecture predicts local 3D point maps, triangle attributes, camera poses, and optional intrinsics in a single forward pass. Instead of treating triangle orientation as an unconstrained latent variable, TriSplat constructs geometry normals from the predicted point maps and refines them using an image-conditioned normal head. This process generates stable local frames for triangle parameterization. The training employs a mono-normal bootstrap schedule to enhance stability during early training phases, while opacity and blur scheduling progressively sharpens the surface representation, facilitating direct mesh extraction. The network is trained on datasets RealEstate10K and DL3DV, although specific training compute details are not disclosed.

**Results**  
TriSplat demonstrates superior performance compared to Gaussian feed-forward baselines, achieving more geometry-faithful reconstructions while maintaining competitive novel-view rendering quality. The authors report quantitative improvements on the RealEstate10K and DL3DV benchmarks, although specific numerical results and effect sizes are not detailed in the abstract. The direct output of triangle primitives allows for immediate integration into physics engines and rendering pipelines, underscoring the practical utility of the method.

**Limitations**  
The authors acknowledge that while TriSplat improves upon existing methods, it may still face challenges in handling highly complex scenes or occlusions, which are common in real-world environments. Additionally, the reliance on specific datasets (RealEstate10K and DL3DV) may limit the generalizability of the results. The paper does not discuss the computational efficiency of the model during inference or the scalability of the approach to larger datasets.

**Why it matters**  
TriSplat represents a significant advancement in the field of 3D scene reconstruction by providing a feed-forward solution that directly outputs simulation-ready meshes. This capability eliminates the need for post-hoc processing, streamlining workflows in applications such as robotics, virtual reality, and game development. The integration of oriented triangle primitives enhances the fidelity of reconstructions, making it a valuable contribution for researchers and engineers focused on real-time 3D rendering and simulation tasks. The implications of this work extend to improving the efficiency of 3D scene understanding and interaction in various domains.

Authors: Weijie Wang, Zimu Li, Jinchuan Shi, Zeyu Zhang, Botao Ye, Marc Pollefeys, Donny Y. Chen, Bohan Zhuang  
Source: arXiv:2605.26115  
URL: https://arxiv.org/abs/2605.26115v1
