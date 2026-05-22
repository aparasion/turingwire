---
title: "SEGA: Spectral-Energy Guided Attention for Resolution Extrapolation in Diffusion Transformers"
date: 2026-05-21 16:09:01 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.22668v1"
arxiv_id: "2605.22668"
authors: ["Javad Rajabi", "Kimia Shaban", "Koorosh Roohi", "David B. Lindell", "Babak Taati"]
slug: sega-spectral-energy-guided-attention-for-resolution-extrapo
summary_word_count: 451
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of diffusion transformers (DiTs) in generating high-resolution images beyond their training resolution. Existing training-free methods, which modify inference-time attention behavior, often rely on uniform scaling of Rotary Position Embeddings (RoPE) that fails to account for the distinct frequency characteristics of different components. This results in a compromise between maintaining global structure and recovering fine details. The authors present SEGA, a novel approach that dynamically adjusts attention scaling based on the spatial-frequency structure of the latent representation during each denoising step. This work is a preprint and has not yet undergone peer review.

**Method**  
SEGA introduces a training-free mechanism that adapts attention scaling across RoPE components according to the spatial-frequency characteristics of the latent representation. The core technical contribution lies in the dynamic scaling of attention, which is informed by the frequency content of the latent at each denoising step. This method contrasts with previous approaches that apply a uniform scaling, thereby allowing for a more nuanced recovery of both global structures and fine details in high-resolution image synthesis. The authors do not disclose specific details regarding the architecture, loss functions, or training compute, as the method is designed to be applied during inference rather than training.

**Results**  
The authors demonstrate that SEGA significantly enhances high-resolution image synthesis across various target resolutions. In comparative experiments against state-of-the-art training-free baselines, SEGA achieves notable improvements in both structural coherence and fine-detail fidelity. While specific numerical results are not provided in the abstract, the authors claim consistent performance gains across multiple benchmarks, indicating a robust advantage over existing methods.

**Limitations**  
The authors acknowledge that SEGA is a training-free method, which may limit its applicability in scenarios where training-based approaches could yield superior results. Additionally, the paper does not explore the computational overhead introduced by the dynamic scaling mechanism, which could impact inference speed. Another potential limitation is the reliance on the quality of the latent representation; if the latent is poorly constructed, the benefits of SEGA may be diminished. The authors do not address the scalability of their method to extremely high resolutions or its performance in diverse image domains.

**Why it matters**  
The introduction of SEGA has significant implications for the field of text-to-image generation, particularly in enhancing the capabilities of diffusion transformers to produce high-resolution outputs. By addressing the shortcomings of existing training-free methods, SEGA paves the way for more effective image synthesis techniques that can maintain both structural integrity and fine details. This advancement could influence future research directions in generative models, particularly in applications requiring high fidelity and resolution, such as digital art, virtual reality, and other creative industries.

Authors: Javad Rajabi, Kimia Shaban, Koorosh Roohi, David B. Lindell, Babak Taati  
Source: arXiv:2605.22668  
URL: [https://arxiv.org/abs/2605.22668v1](https://arxiv.org/abs/2605.22668v1)
