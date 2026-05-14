---
title: "Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training"
date: 2026-05-13 15:11:37 +0000
category: research
subcategory: efficiency_inference
company: "Perplexity"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13652v1"
arxiv_id: "2605.13652"
authors: ["Namrata Shivagunde", "Vijeta Deshpande", "Sherin Muckatira", "Anna Rumshisky"]
slug: beyond-perplexity-a-geometric-and-spectral-study-of-low-rank
summary_word_count: 412
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the generalization capabilities of low-rank pre-training methods for large language models compared to full-rank training. Existing literature primarily relies on validation perplexity from single-seed runs, which is an inadequate measure of model quality. The authors aim to investigate whether low-rank methods yield models that generalize comparably to full-rank training or if the rank constraint fundamentally alters the learned representations and loss landscapes.

**Method**  
The authors conduct a comprehensive evaluation of five low-rank pre-training methods: GaLore and Fira (memory-efficient optimizers), CoLA and SLTrain (architecture reparameterizations), and ReLoRA (adapter-style updates with periodic resets). They compare these methods against full-rank training across three model scales (60M, 130M, 350M). The evaluation employs 16 metrics across four dimensions: (1) 1-D loss landscape analysis along random and top-K PCA directions, (2) 1-D interpolation between checkpoints, (3) spectral analysis of weights and learned updates, and (4) activation similarity to full-rank training. This multifaceted approach allows for a detailed characterization of the solutions found by each method.

**Results**  
The findings reveal that low-rank methods do not converge to the same loss basins as full-rank training, nor do they converge similarly to one another, despite comparable validation perplexity. Specifically, full-rank training achieves a sharper basin along random directions, while low-rank methods exhibit distinct convergence patterns. Notably, GaLore maintains the closest alignment with full-rank activations, particularly in later layers. The study also indicates that validation perplexity does not consistently correlate with downstream performance across all scales, suggesting that geometric and spectral metrics provide better predictive power for model quality.

**Limitations**  
The authors acknowledge that their study is limited by the specific low-rank methods chosen for evaluation and the reliance on certain model scales. They do not explore the impact of varying hyperparameters or the potential for other low-rank methods not included in their analysis. Additionally, the study's reliance on specific metrics may not capture all aspects of model performance, particularly in diverse downstream tasks.

**Why it matters**  
This work has significant implications for the design and evaluation of low-rank pre-training methods in natural language processing. By demonstrating that low-rank methods can lead to geometrically distinct solutions that do not necessarily correlate with validation perplexity, the authors encourage a shift towards more comprehensive evaluation metrics. This could influence future research directions, prompting the development of new low-rank training techniques and evaluation frameworks that prioritize generalization and model robustness over traditional perplexity measures.

Authors: Namrata Shivagunde, Vijeta Deshpande, Sherin Muckatira, Anna Rumshisky  
Source: arXiv:2605.13652  
URL: [https://arxiv.org/abs/2605.13652v1](https://arxiv.org/abs/2605.13652v1)
