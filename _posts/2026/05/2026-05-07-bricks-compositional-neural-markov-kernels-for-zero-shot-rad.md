---
title: "BRICKS: Compositional Neural Markov Kernels for Zero-Shot Radiation-Matter Simulation"
date: 2026-05-07 17:19:31 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06591v1"
arxiv_id: "2605.06591"
authors: ["Richard Hildebrandt", "Evangelos Kourlitis", "Baran Hashemi", "Manuel B\u00fcnstorf", "Thierry Meyer", "Nikola Boskov"]
slug: bricks-compositional-neural-markov-kernels-for-zero-shot-rad
summary_word_count: 381
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in efficient simulation of radiation-matter interactions, which is critical across various fields such as particle physics, nuclear engineering, and medical physics. The authors propose a novel approach to create compositional neural surrogates that can perform zero-shot simulations of particle interactions with materials. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of a next-particle prediction kernel utilizing hybrid discrete-continuous transformer models, specifically leveraging Riemannian Flow Matching on product manifolds. This architecture allows the model to generate variable-sized, typed sets of particles and their radiation effects resulting from interactions with material volumes. The model is designed to be differentiable, enabling tractable likelihood computations for downstream applications. The training process and compute requirements are not explicitly detailed, but the authors report significant computational speed-ups on GPU compared to traditional CPU-bound mechanistic simulations.

**Results**  
The authors evaluate their model at the kernel level, demonstrating predictive stability across multi-round autoregressive rollouts. While specific numerical results are not provided in the abstract, the authors claim a substantial computational speed-up for single-kernel execution compared to existing mechanistic simulators. The paper also introduces a novel dataset comprising 20 million events of radiation-matter interactions, which is intended to facilitate further research in this domain.

**Limitations**  
The authors acknowledge that their model's performance may be limited by the quality and diversity of the training data, as well as the inherent complexity of simulating radiation-matter interactions accurately. They do not discuss potential issues related to generalization to highly complex or novel material distributions beyond those seen in the training set. Additionally, the reliance on GPU acceleration may limit accessibility for researchers without access to high-performance computing resources.

**Why it matters**  
This work has significant implications for the field of radiation-matter interaction simulations, particularly in contexts where traditional mechanistic models are computationally prohibitive. By enabling zero-shot simulations, the proposed method could accelerate research and development in various applications, including medical imaging, radiation therapy, and space exploration. The release of the 20M-event dataset also provides a valuable resource for the community, potentially fostering advancements in machine learning techniques for physical simulations.

Authors: Richard Hildebrandt, Evangelos Kourlitis, Baran Hashemi, Manuel Bünstorf, Thierry Meyer, Nikola Boskov, Michael Kagan, Dan Rosenbaum et al.  
Source: arXiv:2605.06591  
URL: [https://arxiv.org/abs/2605.06591v1](https://arxiv.org/abs/2605.06591v1)
