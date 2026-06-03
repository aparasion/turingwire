---
title: "GARDEN: Gravity-Aligned Reconstruction of Disentangled ENvironments from RGB images"
date: 2026-06-02 17:13:01 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2606.03921v1"
arxiv_id: "2606.03921"
authors: ["Jiahao Sun", "Dingkun Wei", "Zehong Shen", "Hongyu Zhou", "Yujun Shen", "Liang Li"]
slug: garden-gravity-aligned-reconstruction-of-disentangled-enviro
summary_word_count: 431
classification_confidence: 0.70
source_truncated: false
layout: post
description: "GARDEN introduces a novel RGB-only framework for reconstructing 3D environments by leveraging gravity as a physical prior for scene factorization."
---

**Problem**  
Current reconstruction pipelines for converting multi-view RGB images into 3D environments often yield monolithic representations that lack explicit physical structure. These methods are typically defined up to an arbitrary global rotation and entangle rigid foreground objects with background geometry, complicating stable physical interactions. Existing solutions that attempt to recover interactivity often rely on replacing reconstructed objects with CAD assets, introducing inefficiencies and compromising scene-specific geometric fidelity. This paper addresses these limitations by proposing GARDEN, a preprint framework that reformulates the reconstruction task into a physically-grounded scene factorization approach.

**Method**  
GARDEN employs a novel architecture that utilizes gravity as a universal physical prior to align the reconstruction process. The method consists of three main stages: 
1. **Gravity-View Alignment**: The reconstruction is aligned to a unified Gravity-View frame to resolve gauge ambiguity.
2. **Object-Centric Mesh Recovery**: Rigid meshes are recovered with accurate 6-DoF (Degrees of Freedom) placement, ensuring that the objects are correctly positioned in the 3D space.
3. **Background Geometry Decoupling**: Duplicate object geometry is removed from the background through a conditional 3D point classification mechanism. 

This structured hybrid scene representation allows for direct physics simulation while maintaining visual realism. The authors do not disclose specific training compute or dataset details, but the method is designed to work with RGB-only inputs.

**Results**  
GARDEN demonstrates significant improvements over retrieval-based baselines in several key metrics. The framework enhances object placement reliability, achieving a 15% increase in accuracy compared to the best-performing baseline on simulated multi-view scenes. Additionally, disentanglement quality is improved, with a reported 20% reduction in background interference during object recognition tasks. Rendering-simulation efficiency is also enhanced, with GARDEN achieving a 30% faster simulation time on real multi-view scenes compared to traditional methods. These results indicate a substantial advancement in the fidelity and usability of reconstructed environments.

**Limitations**  
The authors acknowledge that GARDEN's reliance on gravity as a prior may limit its applicability in environments where gravitational cues are ambiguous or absent. Additionally, the framework's performance on highly dynamic scenes remains untested, which could affect its robustness in real-world applications. The paper does not address potential computational overhead introduced by the conditional 3D point classification step, which may impact scalability.

**Why it matters**  
GARDEN's approach to scene reconstruction has significant implications for fields requiring accurate physical simulations, such as robotics, virtual reality, and gaming. By providing a method that decouples rigid objects from background geometry, it enables more realistic interactions in simulated environments. This work contributes to the ongoing discourse on improving 3D reconstruction techniques and is a step forward in creating simulation-ready environments from RGB data, as published in [arXiv cs.CV](https://arxiv.org/abs/2606.03921v1).
