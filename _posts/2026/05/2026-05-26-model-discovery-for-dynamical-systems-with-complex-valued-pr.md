---
title: "Model discovery for dynamical systems with complex-valued product units"
date: 2026-05-26 15:18:47 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.27158v1"
arxiv_id: "2605.27158"
authors: ["Martin Br\u00fcckmann", "Babette Dellen", "Uwe Jaekel"]
slug: model-discovery-for-dynamical-systems-with-complex-valued-pr
summary_word_count: 434
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the discovery of governing equations for dynamical systems from observed trajectories, particularly in scenarios where analytic equations are not available. Traditional methods, such as Sparse Identification of Nonlinear Dynamical Systems (SINDy), rely on predefined libraries of candidate functions, which limits their applicability to complex systems. The authors propose a novel approach that leverages complex-valued product-unit networks to learn relevant monomials directly from data, including those with fractional or negative exponents.

**Method**  
The core technical contribution is the introduction of complex-valued product-unit networks, where each unit represents a complex monomial. The network output is a sparse linear combination of these monomials, allowing for the discovery of governing equations without a predefined function library. The training process involves at least 3000 data points from the dynamical systems under study. The architecture is designed to capture the underlying dynamics of chaotic systems effectively, and the learning mechanism is tailored to identify relevant monomials directly from the observed data.

**Results**  
The proposed method was evaluated on four chaotic benchmark systems: Lorenz63, Lorenz84, the Four-Wing attractor, and a fractional variant of Lorenz63. The authors report that they successfully recovered the exact governing equations in 90% of trials for the Lorenz63, Lorenz84, and Four-Wing attractor systems. For the fractional Lorenz63, the recovery rate was between 70-90%. Additionally, when applied to real-world human-gait accelerometer signals, the model achieved a root mean square error (RMSE) of approximately 12-14% of the signal amplitude range over a test horizon three times longer than the training interval, indicating robust performance in high-dimensional systems.

**Limitations**  
The authors acknowledge that their approach may require a substantial amount of training data (at least 3000 points) to achieve reliable results, which could be a limitation in data-scarce environments. Furthermore, while the method shows promise in chaotic systems, its performance in more complex or noisy real-world scenarios remains to be fully validated. The reliance on complex-valued units may also introduce additional computational complexity, which could be a barrier for certain applications.

**Why it matters**  
This work has significant implications for the field of dynamical systems modeling, particularly in contexts where traditional analytic methods are infeasible. By enabling the discovery of governing equations directly from data, the proposed approach could facilitate deeper insights into system dynamics, enhance predictive modeling capabilities, and broaden the applicability of machine learning techniques in scientific research. The ability to learn complex monomials directly from data opens new avenues for exploring nonlinear dynamics and could lead to advancements in various domains, including physics, biology, and engineering.

Authors: Martin Brückmann, Babette Dellen, Uwe Jaekel  
Source: arXiv:2605.27158  
URL: https://arxiv.org/abs/2605.27158v1
