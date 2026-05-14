---
title: "TRUST-TAEA: A trustworthiness-guided two-archive evolutionary algorithm with variable-grouping sparse search for large-scale multi-objective optimization"
date: 2026-05-13 10:36:02 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.13324v1"
arxiv_id: "2605.13324"
authors: ["JunYi Cui"]
slug: trust-taea-a-trustworthiness-guided-two-archive-evolutionary
summary_word_count: 434
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenges in large-scale multi-objective optimization, particularly in high-dimensional decision spaces where complex variable interactions and limited function evaluation budgets hinder the balance between convergence, diversity, and stability. Existing two-archive evolutionary algorithms often fail to leverage archive reliability and problem-structure information effectively, resulting in inefficient searches, incomplete coverage of the Pareto front, and late-stage archive drift. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose TRUST-TAEA, a trustworthiness-guided two-archive evolutionary algorithm that integrates evolutionary progress with convergence-archive maturity to define archive trustworthiness. The core technical contributions include:  
1. **Variable-Grouping Sparse Search**: This method enhances search efficiency by grouping variables based on their interactions, allowing for more focused exploration of the decision space.  
2. **Anchor-Probing Compensatory Search**: This technique is employed to probe promising areas of the search space, compensating for potential deficiencies in the archive's coverage.  
3. **Archive Stabilization**: This mechanism ensures that the archive maintains a stable representation of the Pareto front throughout the optimization process.  
The algorithm is evaluated on the LSMOP benchmark suite, which includes problems with 500 to 5000 decision variables and two or three objectives. The training compute details are not disclosed.

**Results**  
TRUST-TAEA demonstrates superior or highly competitive performance compared to existing baselines on the LSMOP benchmark suite. Specifically, it achieves the best Inverted Generational Distance (IGD$^+$) values, indicating improved convergence and diversity. In a practical application involving a three-objective day-ahead scheduling case for a grid-connected microgrid, TRUST-TAEA not only outperforms other methods in terms of IGD$^+$ but also generates a feasible dispatch strategy that effectively balances cost, emissions, and grid-power fluctuations.

**Limitations**  
The authors acknowledge that while TRUST-TAEA shows promising results, it may still be sensitive to the choice of parameters and the specific structure of the optimization problem. Additionally, the reliance on the LSMOP benchmark suite may limit the generalizability of the findings to other types of multi-objective optimization problems. The paper does not address the computational overhead introduced by the trustworthiness evaluation and variable-grouping mechanisms, which could impact scalability in extremely high-dimensional settings.

**Why it matters**  
The development of TRUST-TAEA has significant implications for the field of multi-objective optimization, particularly in applications requiring efficient exploration of large decision spaces. By effectively integrating trustworthiness into the evolutionary process, this work paves the way for more robust algorithms that can handle complex optimization tasks in real-world scenarios, such as energy management in microgrids. The methodologies introduced could inspire further research into trust-guided optimization techniques, potentially leading to advancements in both theoretical and practical aspects of evolutionary algorithms.

Authors: JunYi Cui  
Source: arXiv:2605.13324  
URL: https://arxiv.org/abs/2605.13324v1
