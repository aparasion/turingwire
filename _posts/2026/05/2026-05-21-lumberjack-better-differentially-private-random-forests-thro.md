---
title: "Lumberjack: Better Differentially Private Random Forests through Heavy Hitter Detection in Trees"
date: 2026-05-21 17:23:04 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.22756v1"
arxiv_id: "2605.22756"
authors: ["Christian Janos Lebeda", "David Erb", "Tudor Cebere", "Aur\u00e9lien Bellet"]
slug: lumberjack-better-differentially-private-random-forests-thro
summary_word_count: 435
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing differentially private (DP) random forest algorithms, which often suffer from significant utility degradation when applied to sensitive tabular data. The authors highlight that current methods fail to balance privacy guarantees with model performance, rendering them impractical for real-world applications. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this paper is the introduction of Lumberjack, a differentially private random forest algorithm that leverages a novel $(\varepsilon, \delta)$-DP heavy hitter detection mechanism tailored for hierarchical data structures. The heavy hitter detection algorithm achieves an error bound of $O_{\varepsilon, \delta}(\sqrt{\log h})$, where $h$ is the height of the decision tree. This allows for the construction of deeper trees than previously feasible, enhancing the model's expressiveness while adhering to privacy constraints. The pruning process is aggressive, retaining only nodes that are sufficiently populated, which contributes to improved utility. The authors provide empirical results based on benchmark datasets, demonstrating that Lumberjack outperforms existing DP random forest methods.

**Results**  
Lumberjack establishes a new state of the art in the privacy-utility trade-off for DP random forests. The empirical evaluation shows that Lumberjack consistently outperforms prior methods across various benchmarks, achieving substantial improvements in utility metrics. Specific performance metrics are not disclosed in the abstract, but the authors claim that their approach significantly narrows the utility gap compared to existing techniques, particularly for practical privacy budgets. The results suggest that the proposed method can effectively balance the competing demands of privacy and model performance.

**Limitations**  
The authors acknowledge that while Lumberjack improves upon existing methods, it may still be sensitive to the choice of hyperparameters, particularly those related to the heavy hitter detection algorithm. Additionally, the scalability of the method to extremely large datasets or high-dimensional feature spaces is not thoroughly evaluated. The paper does not address potential computational overhead introduced by the heavy hitter detection process, which could impact training times in resource-constrained environments.

**Why it matters**  
The implications of this work are significant for the field of privacy-preserving machine learning, particularly in applications involving sensitive data. By demonstrating that it is possible to construct differentially private random forests with improved utility, the authors open up new avenues for research in privacy-preserving algorithms. This work encourages further exploration of deep decision trees in the context of differential privacy, suggesting that enhanced expressiveness can be achieved without compromising privacy guarantees. The findings may influence future designs of machine learning models that require stringent privacy protections while maintaining high performance.

Authors: Christian Janos Lebeda, David Erb, Tudor Cebere, Aurélien Bellet  
Source: arXiv:2605.22756  
URL: https://arxiv.org/abs/2605.22756v1
