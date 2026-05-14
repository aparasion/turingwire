---
title: "FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping"
date: 2026-05-13 06:42:40 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.13071v1"
arxiv_id: "2605.13071"
authors: ["Jongmin Choi", "Joon Son Chung"]
slug: fits-interpretable-spiking-neurons-via-frequency-selectivity
summary_word_count: 398
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in understanding how individual spiking neurons can specialize within Spiking Neural Networks (SNNs) for improved temporal processing. While previous research has enhanced temporal modeling through complex neuron dynamics and network-level mechanisms, the specific roles of individual neurons in frequency selectivity and temporal shaping remain underexplored. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors introduce FiTS, a novel spiking neuron architecture that decomposes temporal computation into two distinct modules: Frequency Selectivity (FS) and Temporal Shaping (TS). The FS module is designed to parameterize each neuron's target frequency, optimizing it to maximize the subthreshold magnitude response. The TS module modulates the timing of frequency components contributing to membrane voltage accumulation through group-delay modulation. The architecture is implemented in simple feedforward SNNs without recurrence or network-level delays. The training process and specific datasets used for evaluation are not disclosed, but the focus is on auditory benchmarks where frequency and timing are critical.

**Results**  
FiTS demonstrates consistent improvements over a plain Leaky Integrate-and-Fire (LIF) baseline across various auditory benchmarks. The paper reports that FiTS achieves a significant increase in performance metrics, although specific numerical results and effect sizes are not detailed in the abstract. It is noted that FiTS remains competitive with established temporal SNN baselines, suggesting that the proposed architecture effectively captures the necessary temporal dynamics for auditory processing tasks.

**Limitations**  
The authors acknowledge that while FiTS provides interpretable neuron-level summaries of frequency and timing organization, the architecture's performance may be limited by the absence of recurrent connections and network-level delays, which are often critical in complex temporal tasks. Additionally, the lack of detailed training compute and dataset specifics may hinder reproducibility and broader applicability. The paper does not address potential scalability issues or the generalization of the model to non-auditory tasks.

**Why it matters**  
The introduction of FiTS has significant implications for the design of interpretable SNNs, particularly in applications requiring precise temporal processing, such as auditory signal processing. By elucidating the roles of frequency selectivity and temporal shaping at the neuron level, this work paves the way for more sophisticated SNN architectures that can leverage these insights for improved performance in real-world tasks. The interpretability aspect also opens avenues for understanding and debugging SNNs, which is crucial for their deployment in safety-critical applications.

Authors: Jongmin Choi, Joon Son Chung  
Source: arXiv:2605.13071  
URL: [https://arxiv.org/abs/2605.13071v1](https://arxiv.org/abs/2605.13071v1)
