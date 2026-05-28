---
title: "Internally Referenced Low-Light Enhancement"
date: 2026-05-27 15:20:35 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.28605v1"
arxiv_id: "2605.28605"
authors: ["Peiyuan He", "Hainuo Wang", "Hengxing Liu", "Mingjia Li", "Xiaojie Guo"]
slug: internally-referenced-low-light-enhancement
summary_word_count: 409
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of self-supervised low-light image enhancement (LLIE) methods, which typically rely on external paired datasets for training. The authors highlight that the absence of external references leads to difficulties in disentangling illumination, textures, and noise in low-light images. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The proposed Internally Referenced LLIE framework introduces several novel components to enhance low-light images without external data. Key contributions include:

1. **Local Exposure-Simulated Scheme**: This technique generates a low-frequency pseudo ground-truth from the degraded input image, serving as an internal physical reference for global illumination estimation and color cast correction.

2. **Dual-Domain Preservation Strategy**: This strategy employs two loss functions:
   - **Illumination-Aligned Perceptual Loss**: This loss preserves global structures while accounting for illumination variations.
   - **Shift-Invariant Spectral Correlation Loss**: This loss captures fine-grained local structures and mitigates high-frequency noise.

3. **Gain-Adaptive Feature Modulation (GAFM)**: This mechanism addresses spatially-variant residual noise by transforming the self-estimated illumination map into an internal spatial gain prior. GAFM dynamically guides a blind-spot network for spatially-aware denoising.

The authors do not disclose specific training compute details but emphasize the self-supervised nature of their approach, which eliminates the need for external datasets.

**Results**  
The proposed method demonstrates state-of-the-art performance on benchmark datasets, achieving significant improvements in noise suppression and textural fidelity compared to existing LLIE methods. The authors report quantitative metrics, although specific numbers and baseline comparisons are not detailed in the abstract. The results indicate that their approach effectively enhances low-light images while maintaining structural integrity and reducing noise artifacts.

**Limitations**  
The authors acknowledge that their method may still struggle with extreme low-light conditions where the internal references may not be sufficiently reliable. Additionally, the reliance on self-generated references could introduce biases in scenarios with complex lighting conditions. The paper does not discuss the computational efficiency or real-time applicability of the proposed framework, which could be a concern for practical deployment.

**Why it matters**  
This work has significant implications for the field of computer vision, particularly in applications requiring low-light image processing, such as surveillance, photography, and autonomous driving. By eliminating the dependency on external datasets, the proposed framework opens avenues for further research into self-supervised learning techniques in image enhancement. The innovative use of internal references and dual-domain strategies may inspire future methodologies aimed at improving image quality in challenging conditions.

Authors: Peiyuan He, Hainuo Wang, Hengxing Liu, Mingjia Li, Xiaojie Guo  
Source: arXiv:2605.28605  
URL: https://arxiv.org/abs/2605.28605v1
