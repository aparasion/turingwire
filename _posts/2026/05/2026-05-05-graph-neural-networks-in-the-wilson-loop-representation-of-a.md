---
title: "Graph Neural Networks in the Wilson Loop Representation of Abelian Lattice Gauge Theories"
date: 2026-05-05 15:55:21 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03901v1"
arxiv_id: "2605.03901"
authors: ["Ali Rayat", "Gia-Wei Chern"]
slug: graph-neural-networks-in-the-wilson-loop-representation-of-a
summary_word_count: 447
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the application of graph neural networks (GNNs) to Abelian lattice gauge theories, particularly in the context of local gauge structures that are prevalent in condensed matter systems and synthetic quantum platforms. Existing methods often fail to incorporate gauge invariance effectively, leading to inefficiencies in modeling strongly correlated phases and dynamics. The authors propose a novel GNN architecture that explicitly enforces gauge invariance, which is crucial for accurately capturing the physics of these systems.

**Method**  
The authors introduce a gauge-invariant GNN architecture that utilizes local gauge-invariant inputs, specifically Wilson loops, to represent the gauge structure of the lattice models. The architecture is designed to preserve gauge invariance throughout the message-passing process, effectively eliminating redundant gauge degrees of freedom while maintaining expressive power. The model is trained on both $\mathbb{Z}_2$ and $\mathrm{U}(1)$ lattice gauge models, focusing on predicting global observables and spatially resolved quantities. The training process leverages a dataset generated from the underlying gauge theories, although specific details regarding the training compute and hyperparameters are not disclosed. The GNN is shown to serve as an efficient surrogate for semiclassical dynamics in $\mathrm{U}(1)$ quantum link models, enabling stable time evolution without the need for repeated fermionic diagonalization.

**Results**  
The proposed GNN architecture demonstrates significant performance improvements over traditional methods. In benchmarks against established baselines for both $\mathbb{Z}_2$ and $\mathrm{U}(1)$ lattice gauge models, the GNN achieves high accuracy in predicting global observables and local dynamics. The authors report that their model can effectively capture nonlocal correlations induced by gauge-matter coupling, outperforming conventional approaches in terms of both accuracy and computational efficiency. Specific effect sizes and quantitative results are not detailed in the abstract, but the authors emphasize the model's ability to reproduce statistical correlations and local dynamics faithfully.

**Limitations**  
The authors acknowledge that their approach may be limited by the complexity of the underlying gauge theories and the potential for overfitting in high-dimensional parameter spaces. They do not address the scalability of the model to non-Abelian gauge theories, which may present additional challenges. Furthermore, the reliance on Wilson loops as inputs may restrict the model's applicability to other gauge-invariant representations.

**Why it matters**  
This work has significant implications for the simulation and understanding of strongly correlated quantum systems. By establishing a gauge-invariant framework for GNNs, the authors provide a pathway for more accurate and efficient modeling of lattice gauge theories, which are fundamental to both theoretical physics and practical applications in quantum computing. The ability to simulate semiclassical dynamics without extensive computational overhead opens new avenues for research in quantum many-body systems and could enhance the development of quantum algorithms that leverage gauge invariance.

Authors: Ali Rayat, Gia-Wei Chern  
Source: arXiv:2605.03901  
URL: https://arxiv.org/abs/2605.03901v1
