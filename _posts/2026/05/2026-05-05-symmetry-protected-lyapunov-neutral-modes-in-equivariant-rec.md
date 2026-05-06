---
title: "Symmetry-Protected Lyapunov Neutral Modes in Equivariant Recurrent Networks"
date: 2026-05-05 03:59:56 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.03338v1"
arxiv_id: "2605.03338"
authors: ["Hanson Hanxuan Mo"]
slug: symmetry-protected-lyapunov-neutral-modes-in-equivariant-rec
summary_word_count: 435
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how recurrent networks can maintain neutral modes for continuous variables like position and phase over extended time horizons. Specifically, it investigates the conditions under which these neutral directions are guaranteed by symmetry rather than merely tuned. The authors focus on equivariant recurrent networks and their ability to leverage symmetry to ensure stability in the presence of perturbations.

**Method**  
The core technical contribution is a theoretical framework that establishes conditions for the existence of symmetry-protected Lyapunov neutral modes in finite-dimensional autonomous \(C^1\) vector fields that are equivariant under a Lie group \(G\). The authors prove that for any compact invariant set with a uniformly nondegenerate group-orbit bundle and stabilizer type \(H\), there exist at least \(\dim(G/H)\) zero Lyapunov exponents at points where the Lyapunov spectrum is defined. This guarantees the presence of neutral directions that are protected by symmetry. The authors conduct controlled experiments to demonstrate the effects of explicitly breaking this symmetry, leading to the emergence of pseudo-gaps that predict finite memory lifetimes. They validate their theoretical findings through various metrics, including normalized equivariance error, direct group-tangent exponents, and principal-angle alignment. Additionally, they train an exactly equivariant recurrent cell on velocity-input \(S^1\) path integration and compare its performance against GRU, LSTM, and orthogonal-RNN baselines.

**Results**  
The learned equivariant recurrent cell achieves a step equivariance preservation of \(3.2 \times 10^{-8}\) and maintains a near-zero group-tangent exponent under zero-input conditions. In terms of performance, the equivariant cell demonstrates significant improvements in horizon, speed, and restricted-phase generalization compared to the baseline models. The authors provide quantitative results that indicate the effectiveness of their approach, although specific numerical results against named baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that their findings are contingent on the assumptions of the theoretical framework, particularly the conditions under which the Lyapunov spectrum is defined. They do not address potential scalability issues when applying their methods to higher-dimensional systems or the implications of noise in real-world applications. Additionally, the experimental validation is limited to specific configurations and may not generalize across all equivariant architectures.

**Why it matters**  
This work has significant implications for the design of recurrent neural networks, particularly in applications requiring long-term stability and memory retention, such as robotics and control systems. By establishing a theoretical foundation for symmetry-protected neutral modes, the research opens avenues for developing more robust and efficient recurrent architectures that can leverage symmetry to enhance performance. The findings could influence future research on equivariant neural networks and their applications in various domains, including physics-informed learning and dynamical systems.

Authors: Hanson Hanxuan Mo  
Source: arXiv:2605.03338  
URL: https://arxiv.org/abs/2605.03338v1
