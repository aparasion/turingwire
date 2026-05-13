---
title: "Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation"
date: 2026-05-12 17:59:34 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12492v1"
arxiv_id: "2605.12492"
authors: ["Kexuan Shi", "Hanxuan Li", "Zeju Qiu", "Yandong Wen", "Simon Buchholz", "Weiyang Liu"]
slug: pion-a-spectrum-preserving-optimizer-via-orthogonal-equivale
summary_word_count: 433
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing additive optimizers, such as Adam and Muon, in the context of large language model (LLM) training. Specifically, it identifies the gap in maintaining the spectral properties of weight matrices during optimization, which can lead to instability and suboptimal convergence. The authors propose Pion, a spectrum-preserving optimizer based on orthogonal equivalence transformation, to mitigate these issues. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Pion employs a novel update mechanism that utilizes left and right orthogonal transformations to update weight matrices, thereby preserving their singular values throughout the training process. The core technical contribution lies in the derivation of the Pion update rule, which is designed to maintain a fixed spectral norm while modulating the geometry of the weight matrices. The authors systematically analyze the design choices involved in Pion, including the implications of orthogonal transformations on convergence behavior. The optimizer is evaluated in the context of both LLM pretraining and finetuning, with a focus on its stability and performance compared to traditional optimizers.

**Results**  
Empirical evaluations demonstrate that Pion achieves competitive performance against standard optimizers on various benchmarks for LLMs. While specific numerical results are not detailed in the abstract, the authors report that Pion provides a stable optimization trajectory and improved convergence rates compared to Adam and Muon. The paper suggests that Pion's ability to preserve spectral properties leads to enhanced training stability, although exact effect sizes and performance metrics against named baselines are not explicitly provided in the abstract.

**Limitations**  
The authors acknowledge that while Pion shows promise, it may not universally outperform all existing optimizers across all tasks and datasets. They also note that the computational overhead associated with orthogonal transformations could be a potential drawback, particularly in resource-constrained environments. Additionally, the paper does not address the scalability of Pion in extremely large models or its performance in diverse training scenarios beyond LLMs.

**Why it matters**  
The introduction of Pion has significant implications for the optimization landscape in deep learning, particularly for LLMs. By preserving the spectral properties of weight matrices, Pion could lead to more stable training dynamics and potentially faster convergence, which is critical for large-scale model training. This work opens avenues for further exploration of orthogonal transformations in optimization and may inspire the development of new optimizers that leverage similar principles. The findings could also influence future research on the interplay between optimization techniques and model architecture, particularly in the context of large-scale neural networks.

Authors: Kexuan Shi, Hanxuan Li, Zeju Qiu, Yandong Wen, Simon Buchholz, Weiyang Liu  
Source: arXiv:2605.12492  
URL: [https://arxiv.org/abs/2605.12492v1](https://arxiv.org/abs/2605.12492v1)
