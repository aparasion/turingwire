---
title: "Neural Negative Binomial Regression for Weekly Seismicity Forecasting: Per-Cell Dispersion Estimation and Tail Risk Assessment"
date: 2026-05-20 17:27:27 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.21437v1"
arxiv_id: "2605.21437"
authors: ["Alim Igilik"]
slug: neural-negative-binomial-regression-for-weekly-seismicity-fo
summary_word_count: 398
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacy of standard Poisson-based models for forecasting weekly seismicity, particularly in Central Asia from 2010 to 2024. The authors demonstrate that the Poisson distribution's assumption of a single global dispersion parameter is systematically violated in this context, as evidenced by a likelihood-ratio test with boundary correction yielding a p-value less than \(10^{-179}\). This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the EarthquakeNet architecture, which employs a neural network to estimate the overdispersion parameter \(\alpha\) on a per-cell basis. This architecture integrates spatial embeddings with a multi-layer perceptron (MLP) to capture spatial heterogeneity in seismic clustering without requiring explicit spatial covariance specifications. Unlike traditional negative binomial regression models that assume a uniform \(\alpha\) across the spatial grid, EarthquakeNet allows for localized dispersion estimates, enhancing the model's ability to generate probabilistic risk-aware alerts through quantiles of the predicted distribution.

**Results**  
The authors conducted a walk-forward evaluation from 2018 to 2023 across four systems, achieving an 8.6% reduction in mean pinball deviation (MPD) compared to a negative binomial generalized linear model (GLM) baseline. Notably, the model demonstrated a 12.5% improvement in the continuous ranked probability score (CRPS) for extreme events (where \(Y \geq 5\)), indicating superior calibration in tail risk forecasting. These results suggest that the EarthquakeNet architecture significantly enhances predictive performance in the context of seismicity forecasting.

**Limitations**  
The authors acknowledge that their model's reliance on neural network architectures may introduce challenges related to interpretability and computational resource requirements. Additionally, the model's performance is contingent on the quality and granularity of the input data, which may vary across different regions. The paper does not address potential overfitting issues that could arise from the increased model complexity or the generalizability of the findings to other seismic regions outside Central Asia.

**Why it matters**  
This work has significant implications for the field of seismology and risk assessment. By providing a framework that accommodates spatial heterogeneity in seismic events, the EarthquakeNet architecture can improve the accuracy of earthquake forecasts and enhance the reliability of risk assessments. This advancement could lead to more effective early warning systems and disaster preparedness strategies, ultimately contributing to reduced societal impacts of seismic events. The methodology may also inspire further research into the application of neural networks for other types of spatially distributed phenomena.

Authors: Alim Igilik  
Source: arXiv:2605.21437  
URL: [https://arxiv.org/abs/2605.21437v1](https://arxiv.org/abs/2605.21437v1)
