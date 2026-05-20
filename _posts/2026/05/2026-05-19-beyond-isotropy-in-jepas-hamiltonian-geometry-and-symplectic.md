---
title: "Beyond Isotropy in JEPAs: Hamiltonian Geometry and Symplectic Prediction"
date: 2026-05-19 16:57:47 +0000
category: research
subcategory: theory
company: "MiniMax"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20107v1"
arxiv_id: "2605.20107"
authors: ["Robert Jenkinson Alvarez"]
slug: beyond-isotropy-in-jepas-hamiltonian-geometry-and-symplectic
summary_word_count: 399
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of Joint Embedding Predictive Architectures (JEPAs), which typically regularize one-view embeddings towards an isotropic Gaussian distribution. The authors argue that this isotropic assumption is not merely a benign default but incurs a significant cost in terms of predictive performance, particularly when the downstream geometry is structured and unknown. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a novel architecture called HamJEPA, which incorporates Hamiltonian geometry into the predictive modeling of view-to-view transitions. Instead of relying on a fixed marginal target, HamJEPA encodes each view as a phase-space state represented by position \( q \) and momentum \( p \). The model predicts transitions using a learned Hamiltonian leapfrog map, which allows for the incorporation of non-isotropic scale and spectral floors to prevent collapse. The training process leverages a minimax and maximum-entropy covariance approach under a Hamiltonian energy budget, specifically targeting the structured downstream geometry \( H \succ 0 \).

**Results**  
HamJEPA demonstrates significant improvements over the baseline model SIGReg on the CIFAR-100 dataset, achieving a gain of +4.89 kNN@20 and +3.52 linear-probe points at 30 epochs, and +6.45 kNN@20 and +10.64 linear-probe points at 80 epochs. On the ImageNet-100 dataset, HamJEPA-$q$ achieves +4.82 kNN@20 and +7.52 linear-probe points at 45 epochs. The authors conduct ablation studies that indicate the symplectic coupling mechanism is crucial for the observed gains in neighborhood geometry, as a matched MLP predictor does not replicate the performance improvements.

**Limitations**  
The authors acknowledge that their approach may not generalize well to all types of structured geometries, particularly those that are highly complex or non-Hamiltonian. Additionally, the reliance on learned Hamiltonian dynamics may introduce challenges in interpretability and stability during training. The paper does not address the computational overhead associated with the Hamiltonian leapfrog map, which may limit scalability in larger datasets or real-time applications.

**Why it matters**  
This work has significant implications for the design of predictive architectures in machine learning, particularly in scenarios where the underlying geometry of the data is complex and unknown. By moving beyond isotropic assumptions, HamJEPA opens avenues for more robust and flexible representations that can adapt to various structured geometries. This could enhance performance in a range of applications, from computer vision to reinforcement learning, where understanding the relationships between different views of data is critical.

Authors: Robert Jenkinson Alvarez  
Source: arXiv:2605.20107v1  
URL: https://arxiv.org/abs/2605.20107v1
