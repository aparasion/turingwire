---
title: "RoSHAP: A Distributional Framework and Robust Metric for Stable Feature Attribution"
date: 2026-05-14 17:51:09 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.15154v1"
arxiv_id: "2605.15154"
authors: ["Lanxin Xiang", "Liang Shi", "Youhui Ye", "Boyu Jiang", "Dawei Zhou", "Feng Guo"]
slug: roshap-a-distributional-framework-and-robust-metric-for-stab
summary_word_count: 436
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the stochastic variability inherent in feature attribution measures, which can lead to inconsistent feature rankings across different model training runs, data splits, or random seeds. The authors highlight that existing methods often fail to provide stable and reliable feature attributions, which is critical for interpretability in machine learning models. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce RoSHAP, a robust metric for feature attribution that builds upon the SHAP (SHapley Additive exPlanations) framework. RoSHAP incorporates a distributional approach to feature attribution by modeling the distribution of attribution scores through bootstrap resampling and kernel density estimation. The framework is designed to aggregate feature attributions into a single score that reflects the stability and strength of the features. Under mild regularity conditions, the authors demonstrate that the aggregated scores converge to an asymptotically Gaussian distribution, which significantly reduces the computational burden associated with distribution estimation. The RoSHAP metric rewards features that are not only active and strong but also stable across different model configurations.

**Results**  
The authors validate RoSHAP through both simulation studies and real-data experiments. They report that RoSHAP outperforms standard single-run attribution measures in identifying significant features. Specifically, models constructed using features selected by RoSHAP achieve predictive performance comparable to those using the full feature set while utilizing substantially fewer predictors. The paper provides quantitative comparisons, although specific numerical results and effect sizes are not detailed in the abstract.

**Limitations**  
The authors acknowledge that while RoSHAP improves stability and interpretability, it still relies on the underlying assumptions of the SHAP framework, which may not hold in all scenarios. Additionally, the computational efficiency, while improved, may still be a concern for very large datasets or high-dimensional feature spaces. The paper does not address potential biases introduced by the bootstrap resampling method or the choice of kernel density estimation parameters, which could affect the robustness of the feature rankings.

**Why it matters**  
The development of RoSHAP has significant implications for the field of interpretable machine learning. By providing a more stable and robust method for feature attribution, this work enhances the reliability of insights drawn from machine learning models, which is crucial for applications in sensitive domains such as healthcare, finance, and autonomous systems. The ability to consistently identify important features can lead to better model performance and more informed decision-making processes. Furthermore, this framework opens avenues for future research into improving feature selection methodologies and understanding the stochastic nature of model interpretability.

Authors: Lanxin Xiang, Liang Shi, Youhui Ye, Boyu Jiang, Dawei Zhou, Feng Guo  
Source: arXiv cs.LG  
URL: [https://arxiv.org/abs/2605.15154v1](https://arxiv.org/abs/2605.15154v1)  
arXiv ID: 2605.15154
