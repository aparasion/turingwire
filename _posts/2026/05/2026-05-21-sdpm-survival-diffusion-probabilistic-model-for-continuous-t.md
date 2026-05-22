---
title: "SDPM: Survival Diffusion Probabilistic Model for Continuous-Time Survival Analysis"
date: 2026-05-21 17:33:47 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22776v1"
arxiv_id: "2605.22776"
authors: ["Stanislav R. Kirpichenko", "Andrei V. Konstantinov", "Lev V. Utkin"]
slug: sdpm-survival-diffusion-probabilistic-model-for-continuous-t
summary_word_count: 436
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing survival analysis methods that either impose structural assumptions on the hazard function or discretize the time axis, which can lead to reduced flexibility and approximation errors. The authors propose the Survival Diffusion Probabilistic Model (SDPM) as a novel generative approach for continuous-time survival analysis. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
SDPM utilizes a denoising diffusion model to model the conditional distribution of survival outcomes, specifically the joint distribution of observed time and censoring indicator, denoted as $\mathbb{P}(T,δ\mid \mathbf{x})$. The model operates in a transformed target space, employing standardized log-times and a continuous Gaussian-mixture representation for the censoring indicator. By assuming conditionally independent censoring, the model generates conditional samples that can be transformed into survival function estimates using the Kaplan-Meier estimator. The training process involves optimizing a loss function tailored for diffusion models, although specific details on the loss formulation and training compute are not disclosed.

**Results**  
The authors evaluate SDPM on ten real survival datasets, comparing its performance against five strong baselines, including tree-based models, boosting-based models, and neural survival models. SDPM demonstrates competitive predictive performance, achieving notable results across several metrics: C-index, integrated time-dependent AUC, and integrated Brier score. In a synthetic study using Cox-Weibull data, SDPM outperforms a strong nonparametric baseline in accurately recovering the shape of the underlying continuous survival distribution when a sufficient number of samples are generated. An ablation study highlights the significance of the proposed target-space transformations, which enhance event-rate calibration, minimize invalid generated times, and yield consistent improvements in predictive discrimination.

**Limitations**  
The authors acknowledge that the assumption of conditionally independent censoring may not hold in all practical scenarios, potentially affecting the model's applicability. Additionally, while the model shows strong performance on the evaluated datasets, its generalizability to other types of survival data or extreme censoring scenarios remains untested. The paper does not provide detailed information on the computational resources required for training or the scalability of the model to larger datasets.

**Why it matters**  
The introduction of SDPM represents a significant advancement in survival analysis by providing a flexible, non-parametric approach that avoids the pitfalls of traditional methods. Its ability to model continuous-time survival outcomes without discretization opens new avenues for research in survival analysis, particularly in fields where time-to-event data is prevalent, such as healthcare and reliability engineering. The model's performance on various benchmarks suggests that it could serve as a robust alternative to existing methods, potentially influencing future work in generative modeling for survival data.

Authors: Stanislav R. Kirpichenko, Andrei V. Konstantinov, Lev V. Utkin  
Source: arXiv:2605.22776  
URL: [https://arxiv.org/abs/2605.22776v1](https://arxiv.org/abs/2605.22776v1)
