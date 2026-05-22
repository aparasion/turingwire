---
title: "Proxy-Based Approximation of Shapley and Banzhaf Interactions"
date: 2026-05-21 17:09:45 +0000
category: research
subcategory: interpretability
company: "UiPath"
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22738v1"
arxiv_id: "2605.22738"
authors: ["Santo M. A. R. Thies", "Hubert Baniecki", "R. Teal Witter", "Eyke H\u00fcllermeier", "Maximilian Muschalik", "Fabian Fumagalli"]
slug: proxy-based-approximation-of-shapley-and-banzhaf-interaction
summary_word_count: 426
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing estimators for Shapley and Banzhaf interactions, which are critical for understanding complex dynamics in machine learning applications. Current methods often struggle with a trade-off between computational speed and accuracy, particularly in high-dimensional settings. The authors identify a gap in the ability to compute these higher-order interaction indices efficiently, especially for tree ensembles, which are prevalent in modern ML applications.

**Method**  
The core technical contribution is the introduction of ProxySHAP, a novel approach that combines the high sample efficiency of tree-based proxy models with a systematic method for achieving consistency through residual correction. The authors derive a polynomial-time generalization of interventional TreeSHAP, allowing for the computation of exact interaction indices without the exponential time complexity associated with tree depth in previous methods. The residual adjustment strategy is formally analyzed, demonstrating that Maximum Sample Reuse (MSR) can correct proxy bias effectively, with variance scaling that does not exponentially increase with interaction size. The architecture leverages tree ensembles, and while specific training compute details are not disclosed, the method is benchmarked extensively across various settings.

**Results**  
ProxySHAP achieves state-of-the-art performance in approximation quality, outperforming previous best estimators such as ProxySPEX and KernelSHAP-IQ. The authors report the lowest error rates in both small- and large-budget regimes, indicating robust performance across different resource constraints. Specific benchmark results include significant improvements in accuracy on standard datasets, although exact numerical values and comparisons to named baselines are not provided in the abstract. The method also excels in downstream explainability tasks, further validating its practical utility.

**Limitations**  
The authors acknowledge that while ProxySHAP improves upon existing methods, it may still be sensitive to the choice of proxy model and the underlying data distribution. They do not discuss potential limitations related to scalability in extremely high-dimensional spaces or the computational overhead associated with the residual correction process. Additionally, the theoretical guarantees provided may not fully encompass all practical scenarios encountered in diverse applications.

**Why it matters**  
The development of ProxySHAP has significant implications for the field of explainable AI, particularly in enhancing the interpretability of complex models. By providing a more efficient and accurate means of estimating Shapley and Banzhaf interactions, this work enables practitioners to better understand feature interactions in their models, leading to improved model transparency and trustworthiness. Furthermore, the theoretical advancements in polynomial-time computation for interaction indices could inspire future research into more efficient algorithms for other complex interaction measures in machine learning.

Authors: Santo M. A. R. Thies, Hubert Baniecki, R. Teal Witter, Eyke Hüllermeier, Maximilian Muschalik, Fabian Fumagalli  
Source: arXiv:2605.22738  
URL: https://arxiv.org/abs/2605.22738v1
