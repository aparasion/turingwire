---
title: "Ternary Decision Trees with Locally-Adaptive Uncertainty Zones"
date: 2026-05-21 17:11:19 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.22740v1"
arxiv_id: "2605.22740"
authors: ["William Smits"]
slug: ternary-decision-trees-with-locally-adaptive-uncertainty-zon
summary_word_count: 476
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional decision trees, specifically the inability to account for uncertainty in predictions near decision boundaries. Standard decision trees, such as those based on the CART algorithm, assign uniform confidence to predictions regardless of their proximity to these boundaries, which can lead to suboptimal decision-making in applications where uncertainty is critical. The authors propose a novel approach, termed ternary decision trees, which introduces uncertainty zones to enhance the model's predictive reliability. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of ternary decision trees that incorporate uncertainty zones at each split node. Each node's uncertainty zone has a half-width, delta, which is computed locally based on existing statistics during the CART split finding process, eliminating the need for external noise specifications. The authors propose five methods for estimating delta: 
1. **Quality-Plateau**: Based on the plateau width of the split criterion curve.
2. **Class-Overlap**: Measures empirical overlap in class distributions.
3. **Gain-Ratio**: Evaluates split quality relative to split entropy.
4. **Node-Bootstrap**: Assesses threshold variance through node-level resampling.
5. **Margin**: Inspired by SVM, it calculates the distance to the nearest cross-class training example.

The models are trained and evaluated across 72 datasets from OpenML-CC18 using 5-fold cross-validation, with a focus on the impact of probabilistic routing in decision-making.

**Results**  
All five delta estimation methods significantly outperform standard CART in terms of decided accuracy, with statistical significance (Wilcoxon signed-rank test, p < 0.001). The margin method demonstrates the highest efficiency, achieving an accuracy gain of 0.104 per unit of boundary-uncertain flagging rate and winning on 42 out of 72 datasets. In practical applications, such as mammography, the node-bootstrap method improves decided accuracy by +0.71% while flagging 10.8% of cases as boundary-uncertain. The authors also analyze performance on three Breiman synthetic benchmarks, revealing that the margin method self-calibrates effectively on clean data, while node-bootstrap and quality-plateau methods align closely with theoretical irreducible error.

**Limitations**  
The authors acknowledge that the proposed methods may not generalize well to datasets with high noise levels or complex feature interactions, as the uncertainty zones are based on local statistics. Additionally, the reliance on empirical methods for delta estimation may introduce variability in performance across different datasets. The paper does not address the computational overhead introduced by the ternary structure compared to traditional binary decision trees.

**Why it matters**  
The introduction of ternary decision trees with locally-adaptive uncertainty zones represents a significant advancement in decision tree methodologies, particularly for applications requiring nuanced handling of uncertainty. This approach can enhance model interpretability and reliability, making it particularly relevant for fields such as healthcare and finance, where decision-making under uncertainty is paramount. The findings encourage further exploration of uncertainty-aware models in machine learning, potentially leading to improved performance in various predictive tasks.

Authors: William Smits  
Source: arXiv:2605.22740  
URL: https://arxiv.org/abs/2605.22740v1
