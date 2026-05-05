---
title: "CARD: Coarse-to-fine Autoregressive Modeling with Radix-based Decomposition for Transferable Free Energy Estimation"
date: 2026-05-04 14:38:41 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.02657v1"
arxiv_id: "2605.02657"
authors: ["Ziyang Yu", "Yi He", "Wenbing Huang", "Wen Yan", "Yang Liu"]
slug: card-coarse-to-fine-autoregressive-modeling-with-radix-based
summary_word_count: 442
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing methods for estimating free energy differences in molecular interactions, which are critical for applications in chemistry and drug discovery. Classical computational approaches are often prohibitively expensive due to their reliance on extensive molecular dynamics simulations. Meanwhile, deep learning-based methods suffer from limited expressiveness and generalization, as they are typically constrained by input dimensions specific to particular systems. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce CARD (Coarse-to-fine Autoregressive Modeling with Radix-based Decomposition), a generative framework that utilizes a novel radix-based decomposition technique. This method bijectively transforms 3D molecular coordinates into mixed discrete-continuous sequences, facilitating a coarse-to-fine autoregressive modeling approach. The architecture is designed to model a distribution with zero free energy, allowing for the computation of absolute free energy for arbitrary molecular systems without the need for alchemical pathways. The training process and specific compute requirements are not disclosed, but the model's design emphasizes enhanced expressiveness compared to traditional methods.

**Results**  
CARD demonstrates competitive performance against classical computational methods, achieving accuracy on par with these approaches while significantly improving inference speed. The authors report an approximately 40-fold speedup in inference time compared to traditional methods. The experiments were conducted across various tasks and molecular systems with diverse topologies, showcasing CARD's ability to generalize effectively to unseen systems. Specific benchmark comparisons and numerical results are not detailed in the abstract, but the implications of the speedup and accuracy are emphasized.

**Limitations**  
The authors acknowledge that while CARD shows promise, it may still be limited by the complexity of the molecular systems it can effectively model. The reliance on a specific decomposition method may also introduce biases or limitations in certain scenarios. Additionally, the lack of peer review means that the robustness of the findings has yet to be validated by the broader scientific community. Other potential limitations not explicitly mentioned include the scalability of the model to larger systems and the need for extensive training data to achieve optimal performance.

**Why it matters**  
The implications of this work are significant for the fields of computational chemistry and drug discovery. By providing a faster and more accurate method for free energy estimation, CARD could facilitate the exploration of larger molecular spaces and enhance the efficiency of drug design processes. The ability to compute absolute free energy without relying on alchemical pathways represents a substantial advancement, potentially leading to more reliable predictions in molecular interactions. This framework may also inspire further research into generative modeling techniques in the context of molecular simulations.

Authors: Ziyang Yu, Yi He, Wenbing Huang, Wen Yan, Yang Liu  
Source: arXiv:2605.02657  
URL: [https://arxiv.org/abs/2605.02657v1](https://arxiv.org/abs/2605.02657v1)
