---
title: "DARTS: Targeting Prognostic Covariates in Budget-Constrained Sequential Experiments"
date: 2026-05-07 17:27:51 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06608v1"
arxiv_id: "2605.06608"
authors: ["Kateryna Husar", "Alexander Volfovsky"]
slug: darts-targeting-prognostic-covariates-in-budget-constrained-
summary_word_count: 437
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding the integration of high-dimensional prognostic covariates in randomized controlled trials (RCTs) under budget constraints. Traditional RCTs assume that all relevant covariates are available at no cost, which is often not feasible in practice. The authors propose a novel approach to optimize the selection of covariates while adhering to a measurement budget, a problem that has not been adequately tackled in existing methodologies. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this paper is the introduction of Dynamic Adaptive Rerandomization via Thompson Sampling (DARTS). DARTS formulates the covariate acquisition process as a sequential optimization problem within a causal inference framework. The method employs a budgeted combinatorial Thompson sampler that iteratively identifies the most prognostic covariates across multiple experimental batches. Selected covariates inform the rerandomization process and regression adjustments, aimed at minimizing the variance of the average treatment effect at the batch level. The authors present a theoretical decoupling result that ensures adaptive covariate selection does not compromise randomization validity. Additionally, they derive a Bayes risk bound for the acquisition layer that aligns with the minimax lower bound, adjusted for logarithmic factors. The training compute requirements are not explicitly disclosed.

**Results**  
Empirical evaluations demonstrate that DARTS significantly enhances efficiency compared to traditional designs. The method effectively concentrates the budget on the most informative features, thereby closing the efficiency gap to oracle designs. While specific numerical results are not detailed in the abstract, the authors claim that DARTS maintains strict inferential validity while achieving substantial improvements in treatment effect estimation.

**Limitations**  
The authors acknowledge that the theoretical results are contingent on certain assumptions, such as the validity of the randomization process and the nature of the covariates. They do not address potential limitations related to the scalability of the method in extremely high-dimensional settings or the computational overhead associated with the Thompson sampling approach. Additionally, the empirical validation may be limited to specific types of data or experimental designs, which could affect generalizability.

**Why it matters**  
The implications of this work are significant for the design of RCTs in fields where data acquisition is costly and high-dimensional covariates are critical for accurate treatment effect estimation. By providing a systematic approach to covariate selection under budget constraints, DARTS enables researchers to optimize their experimental designs without sacrificing inferential validity. This advancement could lead to more efficient use of resources in clinical trials and other applications where budget limitations are a concern, ultimately improving the robustness of causal inference in practice.

Authors: Kateryna Husar, Alexander Volfovsky  
Source: arXiv:2605.06608  
URL: https://arxiv.org/abs/2605.06608v1
