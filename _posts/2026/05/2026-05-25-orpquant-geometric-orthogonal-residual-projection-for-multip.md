---
title: "OrpQuant: Geometric Orthogonal Residual Projection for Multiplier-Free Power-of-Two Transformer Quantization"
date: 2026-05-25 17:52:46 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26092v1"
arxiv_id: "2605.26092"
authors: ["Maoyang Xiang", "Bo Wang", "Tao Luo"]
slug: orpquant-geometric-orthogonal-residual-projection-for-multip
summary_word_count: 424
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of deploying Large Language Models (LLMs) and Vision Transformers (ViTs) on edge devices due to memory constraints and timing bottlenecks from dense Multiply-Accumulate (MAC) operations. Specifically, it focuses on the challenges posed by logarithmic Power-of-Two (PoT) quantization in the ultra-low bit regime, particularly below 4 bits, where the Low Angular Resolution Regime leads to significant degradation in high-dimensional feature representations. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Orthogonal Residual Projection (ORP), a novel algorithm-hardware co-design framework that reformulates quantization as a dual-basis geometric projection. ORP synthesizes a higher-resolution residual lattice using only shift-and-add operations, circumventing the need for MAC operations. The method employs an analytical solver that significantly reduces the calibration time for the LLaMA-2-7B model to approximately 15 minutes, contrasting with traditional gradient-based optimization techniques. The architecture leverages a 3-bit weight and 16-bit activation quantization scheme (W3/A16) to enhance performance while maintaining hardware efficiency.

**Results**  
ORP demonstrates superior performance on the LLaMA-2-7B model, achieving a perplexity of 6.10 under the 3-bit quantization constraint. This result is notably better than conventional MAC-intensive baselines such as Adaptive Weight Quantization (AWQ), which typically rely on asymmetric scaling. Additionally, ORP maintains competitive accuracy in 4-bit quantization scenarios. At the silicon level, standard-cell RTL synthesis at a 28nm process node shows that ORP effectively alleviates timing bottlenecks associated with dense multiplier trees, indicating its practical applicability in hardware implementations.

**Limitations**  
The authors acknowledge that while ORP improves quantization efficiency and reduces calibration time, it may still face challenges in extreme low-bit scenarios beyond 3 bits, where the geometric limitations of the residual lattice could re-emerge. Additionally, the paper does not address the potential trade-offs in model interpretability or the impact of ORP on other model architectures outside of LLaMA-2-7B. The reliance on a specific hardware synthesis process (28nm) may also limit generalizability to other fabrication technologies.

**Why it matters**  
The implications of this work are significant for the deployment of LLMs and ViTs on resource-constrained edge devices. By providing a method that reduces reliance on MAC operations, ORP enables more efficient model quantization, potentially leading to faster inference times and lower power consumption. This advancement could facilitate the broader adoption of sophisticated AI models in real-time applications, such as mobile devices and IoT systems, where computational resources are limited. Furthermore, the reduction in calibration time enhances the feasibility of deploying these models in dynamic environments where rapid adaptation is crucial.

Authors: Maoyang Xiang, Bo Wang, Tao Luo  
Source: arXiv:2605.26092  
URL: https://arxiv.org/abs/2605.26092v1
