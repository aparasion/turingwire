---
title: "Disentangling Generation and Regression in Stochastic Interpolants for Controllable Image Restoration"
date: 2026-05-20 16:41:32 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.21381v1"
arxiv_id: "2605.21381"
authors: ["Yi Liu", "Jia Ma", "Wengen Li", "Jihong Guan", "Shuigeng Zhou", "Yichao Zhang"]
slug: disentangling-generation-and-regression-in-stochastic-interp
summary_word_count: 435
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing image restoration (IR) methods, particularly the trade-offs between generative models, which excel in texture synthesis but suffer from slow inference and pixel fidelity issues, and classical regression-based methods, which provide high fidelity but lack generative capabilities. The authors propose a novel framework, DiSI, to bridge this gap by disentangling the stochastic interpolant process into independent generation and regression components. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
DiSI introduces a unified framework that separates the generation and regression processes, allowing for a flexible transition between the two. The authors implement this framework using two specific sampling trajectories and a unified sampler designed for high-quality, few-step inference across arbitrary trajectories. The architecture features a dual-branch U-Net style transformer network operating in pixel space, where one branch is dedicated to enhancing conditional guidance. The training process leverages a combination of loss functions tailored to optimize both generative and regression outputs, although specific details on the loss formulation and training compute are not disclosed.

**Results**  
DiSI demonstrates competitive performance across various IR tasks, achieving state-of-the-art results on benchmarks such as the Set14 and BSD500 datasets. The authors report that DiSI outperforms traditional regression methods by a significant margin, achieving PSNR improvements of up to 2 dB in certain scenarios. Additionally, the framework allows for adjustable distortion-perception trade-offs, enabling users to control the balance between fidelity and generative quality within a single model. The results indicate that DiSI can effectively operate in both high-fidelity and generative modes, showcasing its versatility.

**Limitations**  
The authors acknowledge that while DiSI provides a novel approach to IR, it may still be limited by the inherent complexities of disentangling generation and regression processes. They do not address potential computational overhead introduced by the dual-branch architecture or the implications of model size on deployment in resource-constrained environments. Furthermore, the paper does not explore the generalizability of the framework across diverse image types or restoration tasks beyond those tested.

**Why it matters**  
The implications of this work are significant for the field of image restoration, as it offers a flexible framework that can adapt to varying requirements for fidelity and generative quality. By enabling a controllable transition between regression and generation, DiSI opens avenues for future research into hybrid models that can leverage the strengths of both approaches. This could lead to advancements in applications such as real-time image enhancement, video restoration, and other domains where both high fidelity and generative capabilities are essential.

Authors: Yi Liu, Jia Ma, Wengen Li, Jihong Guan, Shuigeng Zhou, Yichao Zhang  
Source: arXiv:2605.21381  
URL: [https://arxiv.org/abs/2605.21381v1](https://arxiv.org/abs/2605.21381v1)
