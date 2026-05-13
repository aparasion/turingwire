---
title: "Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing"
date: 2026-05-12 09:22:45 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.11835v1"
arxiv_id: "2605.11835"
authors: ["Alex Fulleda-Garcia", "Saray Soldado-Magraner", "Josep Maria Margarit-Taul\u00e9"]
slug: multi-timescale-conductance-spiking-networks-a-sparse-gradie
summary_word_count: 418
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing spiking neural networks (SNNs) in terms of gradient-based trainability, dynamical richness, and activity sparsity, particularly in regression tasks. Many state-of-the-art SNNs utilize simple phenomenological dynamics and surrogate gradients, which restrict their ability to control spiking diversity and sparsity. The authors propose a novel framework, the multi-timescale conductance spiking networks (MCSNs), to overcome these challenges. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of multi-timescale conductance spiking networks, which utilize a gradient-trainable framework where neural dynamics are shaped by tuning fast, slow, and ultra-slow conductances. This approach allows for systematic control over excitability and enables rich firing dynamics, including tonic, phasic, and bursting responses, all within a single model. The authors derive a discrete-time formulation of these differentiable dynamics, facilitating direct backpropagation through time without relying on surrogate-gradient methods. The training process is evaluated using feedforward networks of these neurons, specifically targeting the predictability limit of the Mackey-Glass time-series regression task.

**Results**  
The MCSNs were benchmarked against baseline leaky integrate-and-fire (LIF) and state-of-the-art adaptive leaky integrate-and-fire (AdLIF) networks. The results indicate that MCSNs outperform both LIF and AdLIF networks in terms of accuracy and sparsity of activity. The authors report a significant reduction in activity levels, which enhances both communication efficiency and computational resource utilization. While specific numerical results are not detailed in the abstract, the performance improvements suggest a substantial effect size, particularly in the context of regression tasks.

**Limitations**  
The authors acknowledge that while the MCSNs provide enhanced control over spiking dynamics and improved performance, the framework may still be limited by the inherent challenges of SNNs, such as the complexity of training and the need for careful tuning of conductance parameters. Additionally, the paper does not address the scalability of the proposed model to larger, more complex datasets or tasks beyond the Mackey-Glass time series. The potential for overfitting in high-dimensional spaces is also not discussed.

**Why it matters**  
The introduction of multi-timescale conductance spiking networks represents a significant advancement in the design of SNNs, particularly for applications requiring low-power, event-driven computation in temporally rich environments. The ability to achieve rich firing dynamics while maintaining gradient-based trainability opens new avenues for energy-efficient neural computation and neuromorphic hardware implementation. This work lays the groundwork for future research into more complex temporal processing tasks and could influence the development of next-generation spiking neural architectures.

Authors: Alex Fulleda-Garcia, Saray Soldado-Magraner, Josep Maria Margarit-Taulé  
Source: arXiv:2605.11835  
URL: [https://arxiv.org/abs/2605.11835v1](https://arxiv.org/abs/2605.11835v1)
