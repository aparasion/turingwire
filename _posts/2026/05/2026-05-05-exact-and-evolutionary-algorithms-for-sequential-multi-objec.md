---
title: "Exact and Evolutionary Algorithms for Sequential Multi-Objective Transmission Topology Planning"
date: 2026-05-05 13:38:30 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.03753v1"
arxiv_id: "2605.03753"
authors: ["Job Groeneveld", "Miguel Mu\u00f1oz", "Jan Viebahn", "Alessandro Zocca"]
slug: exact-and-evolutionary-algorithms-for-sequential-multi-objec
summary_word_count: 402
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in sequential multi-objective optimization for day-ahead transmission topology planning and congestion management, specifically for Transmission System Operators (TSOs). The authors propose a framework that incorporates four operational objectives: worst-case line loading under N-1 security, topological depth, number of switching actions, and time spent in non-reference topologies. The work is presented as a preprint and has not undergone peer review.

**Method**  
The authors develop two algorithms: an exact enumeration method called the block algorithm and a multi-objective evolutionary algorithm based on NSGA-III. The block algorithm leverages the temporal block structure of feasible strategies to enumerate the complete Pareto front efficiently. It operates under fixed operational bounds for depth and switch count, achieving polynomial growth in evaluation count relative to the planning horizon. The evolutionary algorithm employs structure-guided initialization and problem-specific variation operators tailored to the topology-planning context. The algorithms are evaluated using real operational data from the Dutch high-voltage grid managed by TenneT TSO.

**Results**  
The block algorithm successfully computes the full Pareto front for a highly congested day in under three minutes, demonstrating its efficiency and practicality as a decision-support tool. In contrast, the evolutionary algorithm converges towards the Pareto front but does not fully recover it, indicating a trade-off between computational efficiency and optimality. The results highlight the block algorithm's capability to serve as a ground-truth benchmark for future heuristic and learning-based methods in this domain.

**Limitations**  
The authors acknowledge that the block algorithm's performance is contingent on the fixed operational bounds, which may not generalize across all scenarios. Additionally, the evolutionary algorithm's inability to recover the exact Pareto front suggests limitations in its convergence properties. The paper does not address potential scalability issues when applied to larger or more complex networks beyond the Dutch high-voltage grid.

**Why it matters**  
This work has significant implications for the field of power systems optimization, particularly in enhancing decision-making processes for TSOs. By providing both an exact method and a heuristic approach, the authors contribute valuable tools for managing transmission topology under multi-objective constraints. The block algorithm's efficiency positions it as a practical solution for real-time applications, while the evolutionary algorithm's insights can inform future research on heuristic methods in multi-objective optimization. This dual approach encourages further exploration of hybrid methodologies that could integrate exact and approximate solutions for complex operational challenges in power systems.

Authors: Job Groeneveld, Miguel Muñoz, Jan Viebahn, Alessandro Zocca  
Source: arXiv:2605.03753  
URL: [https://arxiv.org/abs/2605.03753v1](https://arxiv.org/abs/2605.03753v1)
