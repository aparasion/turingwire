---
title: "TOC-SR: Task-Optimal Compact diffusion for Image Super Resolution"
date: 2026-05-04 16:06:24 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02767v1"
arxiv_id: "2605.02767"
authors: ["Sowmya Vajrala", "Akshay Bankar", "Manjunath Arveti", "Shreyas Pandith", "Sravanth Kodavanti", "Subhajit Sanyal"]
slug: toc-sr-task-optimal-compact-diffusion-for-image-super-resolu
summary_word_count: 408
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the efficiency of diffusion models for image super-resolution (SR), particularly their large model sizes and computational demands during iterative sampling. The authors propose TOC-SR, a framework aimed at creating compact, one-step super-resolution models. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of TOC-SR involves the development of a compact diffusion backbone through a two-step process. Initially, a sixteen-channel latent diffusion model serves as the foundation. The authors employ feature-wise generative distillation to create parameter-efficient surrogate blocks, which are then optimized using epsilon-constrained Bayesian Optimization. This optimization aims to minimize model complexity while preserving generative fidelity. The resulting compact diffusion backbone achieves a 6.6x reduction in parameters and a 2.8x reduction in GMACs (Giga Multiply-Accumulate operations) compared to the original expanded diffusion model. Subsequently, this backbone is adapted for super-resolution tasks, and the diffusion process is distilled into a single-step generator, significantly enhancing computational efficiency.

**Results**  
The proposed TOC-SR framework demonstrates competitive performance on standard benchmarks for image super-resolution. While specific numerical results are not detailed in the abstract, the authors claim that their method maintains strong reconstruction quality despite the significant reductions in model size and computational requirements. The efficiency gains are particularly notable when compared to traditional diffusion models, which typically require multiple sampling steps to achieve high-quality outputs.

**Limitations**  
The authors acknowledge that while TOC-SR achieves substantial reductions in model size and computational load, there may be trade-offs in terms of the fidelity of generated images compared to larger, more complex models. Additionally, the reliance on Bayesian Optimization for architecture discovery may introduce variability in results depending on the optimization parameters and initial conditions. The paper does not address potential limitations related to the generalizability of the model across diverse datasets or its performance in real-time applications.

**Why it matters**  
The implications of this work are significant for the field of image processing and computer vision, particularly in applications requiring real-time performance and low-latency processing, such as mobile devices and embedded systems. By demonstrating that it is possible to achieve high-quality super-resolution with a compact model, TOC-SR paves the way for further research into efficient architectures in generative modeling. This could lead to broader adoption of diffusion models in practical applications where computational resources are constrained.

Authors: Sowmya Vajrala, Akshay Bankar, Manjunath Arveti, Shreyas Pandith, Sravanth Kodavanti, Subhajit Sanyal, Amit Unde, Srinivas Soumitri Miriyala  
Source: arXiv:2605.02767  
URL: [https://arxiv.org/abs/2605.02767v1](https://arxiv.org/abs/2605.02767v1)
