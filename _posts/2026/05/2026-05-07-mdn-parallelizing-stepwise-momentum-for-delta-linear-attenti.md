---
title: "MDN: Parallelizing Stepwise Momentum for Delta Linear Attention"
date: 2026-05-07 08:12:09 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.05838v1"
arxiv_id: "2605.05838"
authors: ["Yulong Huang", "Xiang Liu", "Hongxiang Huang", "Xiaopeng Lin", "Zunchang Liu", "Xiaowen Chu"]
slug: mdn-parallelizing-stepwise-momentum-for-delta-linear-attenti
summary_word_count: 408
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing linear attention (LA) models, particularly the rapid information decay and suboptimal convergence associated with naive stochastic gradient descent (SGD) updates. While recent models like Mamba2 and GDN have made strides in scaling large language models (LLMs) to handle long sequences, they do not effectively leverage momentum-based optimization techniques. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel architecture called Momentum DeltaNet (MDN), which employs a chunkwise parallel algorithm for LA with a stepwise momentum rule. The key innovation lies in geometrically reordering the update coefficients to enhance training efficiency and effectiveness. The authors analyze the momentum-based recurrence from a dynamical systems perspective, identifying it as a second-order system characterized by complex conjugate eigenvalues. This analysis informs the design of stable gating constraints that ensure robust performance. The implementation utilizes Triton kernels to optimize computational throughput, allowing MDN to maintain competitive training speeds relative to other linear models like Mamba2 and KDA.

**Results**  
MDN demonstrates significant performance improvements over established baselines, including Transformers, Mamba2, and GDN, across various downstream evaluation benchmarks. Specifically, the authors report consistent enhancements in model performance for both 400M and 1.3B parameter configurations. While exact numerical results are not provided in the abstract, the authors emphasize that MDN achieves comparable training throughput to existing linear models while outperforming them in terms of convergence and stability.

**Limitations**  
The authors acknowledge that their approach may introduce additional complexity in the training process due to the stepwise momentum rule and the need for stable gating constraints. They do not discuss potential scalability issues when applying MDN to even larger models or the computational overhead associated with the chunkwise parallelization. Furthermore, the reliance on Triton kernels may limit accessibility for practitioners not using compatible hardware or software environments.

**Why it matters**  
The development of MDN has significant implications for the future of LLMs, particularly in applications requiring the processing of long sequences. By effectively integrating momentum-based optimization into linear attention frameworks, this work paves the way for more efficient training methodologies that can handle larger datasets and more complex tasks. The insights gained from the dynamical systems analysis may also inspire further research into stability and convergence in neural network training, potentially influencing the design of future architectures.

Authors: Yulong Huang, Xiang Liu, Hongxiang Huang, Xiaopeng Lin, Zunchang Liu, Xiaowen Chu, Zeke Xie, Bojun Cheng  
Source: arXiv cs.NE  
URL: https://arxiv.org/abs/2605.05838v1
