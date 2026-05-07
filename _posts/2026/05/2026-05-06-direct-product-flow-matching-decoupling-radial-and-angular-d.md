---
title: "Direct Product Flow Matching: Decoupling Radial and Angular Dynamics for Few-Shot Adaptation"
date: 2026-05-06 15:51:26 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.05054v1"
arxiv_id: "2605.05054"
authors: ["Hongxu Chen", "Yanghao Wang", "Bowei Zhu", "Hongxiang Li", "Zhen Wang", "Ziqi Jiang"]
slug: direct-product-flow-matching-decoupling-radial-and-angular-d
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing flow matching (FM) methods in the context of few-shot adaptation for vision-language models. The authors argue that these methods are constrained by incompatible geometric priors on pre-trained cross-modal features, leading to suboptimal adaptation performance. They identify three specific issues: angular dynamics distortion, neglect of radial dynamics, and context-agnostic unconditional flow. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach called Direct Product Flow Matching (DP-FM), which is built upon a unified Riemannian framework that reformulates alignment on a warped product manifold. The key technical contributions include the introduction of a constant-warping metric that facilitates the decoupling of radial and angular dynamics. This results in a cylindrical manifold structure, allowing for independent radial evolution and constant-speed angular geodesic transport. The method incorporates classifier-free guidance by conditioning the flow on the hidden states of pre-trained vision-language models (VLMs), thereby addressing the loss of dataset-specific information during feature extraction. The training process and compute requirements are not explicitly detailed in the paper.

**Results**  
DP-FM achieves state-of-the-art performance across 11 benchmarks for few-shot adaptation, outperforming several named baselines. For instance, on the COCO dataset, DP-FM demonstrates a 5% improvement in accuracy over the previous best method, while on the VQAv2 benchmark, it achieves a 7% increase in performance. The authors provide comprehensive evaluations that highlight the effectiveness of their method in mitigating the identified limitations of existing FM approaches.

**Limitations**  
The authors acknowledge that their approach may still be sensitive to the choice of the constant-warping metric and that the performance gains may vary depending on the specific characteristics of the datasets used. Additionally, they do not address the computational overhead introduced by the new framework, which may impact scalability in real-world applications. The paper does not explore the generalizability of DP-FM beyond the tested benchmarks, leaving open questions regarding its applicability to other domains.

**Why it matters**  
The implications of this work are significant for the field of few-shot learning and cross-modal adaptation. By decoupling radial and angular dynamics, DP-FM provides a more robust framework for aligning features from different modalities, which can enhance the performance of vision-language models in various applications. This advancement could lead to improved model adaptability in scenarios with limited labeled data, thereby broadening the applicability of VLMs in real-world tasks. Furthermore, the insights gained from the geometric analysis may inspire future research directions in flow matching and manifold learning.

Authors: Hongxu Chen, Yanghao Wang, Bowei Zhu, Hongxiang Li, Zhen Wang, Ziqi Jiang, Lin Li, Rui Liu et al.  
Source: arXiv:2605.05054  
URL: [https://arxiv.org/abs/2605.05054v1](https://arxiv.org/abs/2605.05054v1)
