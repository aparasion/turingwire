---
title: "NoRIN: Backbone-Adaptive Reversible Normalization for Time-Series Forecasting"
date: 2026-05-11 16:42:52 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10823v1"
arxiv_id: "2605.10823"
authors: ["Shun Zhang", "Yuyang Xiao"]
slug: norin-backbone-adaptive-reversible-normalization-for-time-se
summary_word_count: 446
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing reversible normalization techniques, specifically Reversible Instance Normalization (RevIN) and its variants (Dish-TS, SAN, FAN), in time-series forecasting. These methods utilize a strictly affine transformation, which restricts their ability to reshape the underlying data distribution, leaving issues such as heavy tails and skewness uncorrected. The authors propose NoRIN, a novel approach that introduces non-linear reversible normalization to overcome these limitations. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
NoRIN employs the arcsinh-form Johnson $S_U$ transform, which incorporates two shape parameters, $(δ, ε)$, that control the tailedness and skewness of the data distribution. The method allows for the recovery of the linear $Z$-score normalization used in RevIN when $δ \to \infty$. The training process involves jointly optimizing $(δ, ε)$ with the backbone model using gradient descent. The authors identify a phenomenon termed the "degeneration problem," where the forecasting loss is locally indifferent to the shape of the distribution, allowing high-capacity backbones to compensate for monotonic reparameterizations. To mitigate this issue, NoRIN decouples the shape selection from gradient training: $(δ, ε)$ are initialized using a closed-form Slifker-Shapiro quantile fit and subsequently refined through Bayesian optimization based on validation objectives. The inner training loop remains consistent with standard RevIN training.

**Results**  
The authors conducted experiments across six different backbone architectures, five real-world datasets, and three prediction horizons, resulting in a total of 90 configurations. The decoupled shape optimization process yielded $(δ^\star, ε^\star)$ values that consistently deviated from the linear limit, demonstrating that different backbone architectures necessitate distinct normalization parameters for optimal performance. The paper reports significant improvements in forecasting accuracy compared to baseline methods, although specific numerical results and effect sizes are not detailed in the abstract.

**Limitations**  
The authors acknowledge that the proposed method may still be sensitive to the initialization of the shape parameters and the choice of backbone architecture. Additionally, while the decoupling of shape optimization from gradient training is a novel approach, it may introduce additional complexity in model training and hyperparameter tuning. The paper does not address the computational overhead introduced by the Bayesian optimization process for refining $(δ, ε)$.

**Why it matters**  
The introduction of NoRIN has significant implications for time-series forecasting, particularly in scenarios where data distributions exhibit heavy tails and skewness. By enabling more flexible normalization that adapts to the specific characteristics of different backbone architectures, NoRIN can enhance the robustness and accuracy of forecasting models. This work opens avenues for further research into adaptive normalization techniques and their integration into various machine learning frameworks, potentially leading to improved performance across a range of applications in time-series analysis.

Authors: Shun Zhang, Yuyang Xiao  
Source: arXiv:2605.10823  
URL: https://arxiv.org/abs/2605.10823v1
