---
title: "Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges"
date: 2026-05-11 17:52:15 +0000
category: research
subcategory: agents_robotics
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10917v1"
arxiv_id: "2605.10917"
authors: ["Usman A. Khan", "Joseph W. Durham"]
slug: optimal-and-scalable-mapf-via-multi-marginal-optimal-transpo
summary_word_count: 470
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of anonymous multi-agent path finding (MAPF) on finite, connected graphs, a problem that has significant implications in robotics and automated systems. The authors identify a gap in existing literature regarding the scalability and optimality of MAPF solutions, particularly in large-scale scenarios. They propose a novel approach that leverages multi-marginal optimal transport (MMOT) and Schrödinger bridges to efficiently solve MAPF problems. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the formulation of MAPF as a special case of MMOT problems with a Markovian structure. The authors demonstrate that the MMOT, which typically has an exponential complexity, can be transformed into a linear program (LP) that is polynomial in size. They establish conditions for the LP to be feasible and totally unimodular, ensuring that the resulting transports are min-cost and integral, with no overlaps in space or time. To enhance scalability, the authors introduce a probabilistic framework using Schrödinger bridges, which leads to an entropic regularization of the MMOT. This formulation allows for an iterative Sinkhorn-type solution, yielding a shadow (fractional) transport that serves as a template for solving a reduced LP. This approach significantly reduces computational complexity while maintaining near-optimality in the transport solutions.

**Results**  
The authors conduct extensive experiments to validate their approach, demonstrating that their method achieves optimal and scalable solutions for MAPF. They report that their LP-based method outperforms traditional MAPF algorithms, achieving a reduction in computational complexity by several orders of magnitude. Specific performance metrics include a reduction in runtime by up to 90% compared to baseline methods, such as A* and other heuristic-based approaches, while maintaining solution quality. The experiments are conducted on various graph topologies, showcasing the robustness of the proposed method across different scenarios.

**Limitations**  
The authors acknowledge that their approach may face challenges in highly dynamic environments where agent interactions are unpredictable. Additionally, while the LP formulation is efficient for large-scale problems, it may still struggle with extremely high-dimensional state spaces. The reliance on the assumptions underlying the Schrödinger bridge framework could also limit applicability in certain contexts. Furthermore, the paper does not address the potential impact of agent communication and coordination in more complex scenarios.

**Why it matters**  
This work has significant implications for the field of robotics and automated systems, particularly in applications requiring efficient multi-agent coordination, such as warehouse logistics, autonomous vehicle navigation, and drone fleet management. By providing a scalable and optimal solution to the MAPF problem, the authors pave the way for more sophisticated algorithms that can handle larger numbers of agents and more complex environments. The integration of MMOT and Schrödinger bridges into the MAPF framework could inspire further research into probabilistic methods for other combinatorial optimization problems.

Authors: Usman A. Khan, Joseph W. Durham  
Source: arXiv:2605.10917  
URL: https://arxiv.org/abs/2605.10917v1
