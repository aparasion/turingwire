---
title: "Why Geometric Continuity Emerges in Deep Neural Networks: Residual Connections and Rotational Symmetry Breaking"
date: 2026-05-06 14:27:18 +0000
category: research
subcategory: theory
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.04971v1"
arxiv_id: "2605.04971"
authors: ["Kyungwon Jeong", "Won-Gi Paeng", "Honggyo Suh"]
slug: why-geometric-continuity-emerges-in-deep-neural-networks-res
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the unexplained phenomenon of geometric continuity in deep neural networks, specifically the alignment of principal singular vectors of weight matrices across adjacent layers. While this property has been empirically observed, the underlying mechanisms remain inadequately understood in the literature. The authors aim to elucidate the factors contributing to this continuity, particularly in the context of residual connections and the role of symmetry-breaking nonlinearities.

**Method**  
The authors conduct experiments using toy multi-layer perceptrons (MLPs) and small transformer architectures to investigate the emergence of geometric continuity. They propose two primary mechanisms: (1) **Residual Connections**: These connections facilitate cross-layer gradient coherence, which aligns weight updates across layers, thereby promoting continuity. (2) **Symmetry-Breaking Nonlinearities**: These nonlinearities constrain the layers to a shared coordinate frame, preventing rotational drift that could disrupt weight structure. The authors demonstrate that a nonlinear activation function that preserves rotation fails to maintain continuity, indicating that symmetry breaking—not nonlinearity itself—is crucial for this property. They also differentiate the roles of activation and normalization: activation is responsible for concentrating continuity in the leading singular direction, while normalization helps distribute continuity across multiple directions. In the context of transformers, the authors find that continuity is projection-specific, with different layers (Q, K, Gate, Up) developing input-space continuity, while others (O, Down) develop output-space continuity. The layer V, which lacks an adjacent nonlinearity, exhibits only low continuity.

**Results**  
The authors provide empirical evidence showing that networks with residual connections and symmetry-breaking nonlinearities exhibit significantly higher geometric continuity compared to those without these features. While specific numerical results are not disclosed in the abstract, the findings suggest a marked improvement in continuity metrics when comparing architectures with and without the identified mechanisms. The experiments indicate that the presence of residual connections and appropriate nonlinearities leads to a more stable and coherent weight structure across layers, which is quantitatively superior to baseline models lacking these characteristics.

**Limitations**  
The authors acknowledge that their findings are based on toy models and small transformers, which may not fully capture the complexities of larger, real-world networks. Additionally, the specific impact of different types of nonlinearities beyond those tested remains unexplored. The study does not address the scalability of these mechanisms to larger architectures or their implications for training dynamics in more complex settings.

**Why it matters**  
Understanding the mechanisms behind geometric continuity has significant implications for the design and training of deep neural networks. By clarifying the roles of residual connections and symmetry-breaking nonlinearities, this work provides insights that could inform architectural choices and training strategies aimed at enhancing model stability and performance. The findings may also influence future research on the interpretability of neural network behavior and the development of more robust architectures.

Authors: Kyungwon Jeong, Won-Gi Paeng, Honggyo Suh  
Source: arXiv:2605.04971  
URL: [https://arxiv.org/abs/2605.04971v1](https://arxiv.org/abs/2605.04971v1)
