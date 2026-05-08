---
title: "Online Bayesian Calibration under Gradual and Abrupt System Changes"
date: 2026-05-07 17:29:18 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06612v1"
arxiv_id: "2605.06612"
authors: ["Yang Xu", "Chiwoo Park"]
slug: online-bayesian-calibration-under-gradual-and-abrupt-system-
summary_word_count: 391
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of classical Bayesian calibration methods, which are typically offline and assume stationary data-generating processes. The authors highlight the inadequacy of existing approaches in handling nonstationary environments characterized by gradual drifts and abrupt regime shifts, particularly in the context of digital twins and computer experiments. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors introduce Bayesian Recursive Projected Calibration (BRPC), an online calibration framework designed for streaming data that accounts for systematic bias and nonstationarity. BRPC separates the calibration parameter updates from the discrepancy modeling by employing a discrepancy-free particle update for calibration parameters and a conditional Gaussian process for discrepancy estimation. This separation preserves identifiability and allows for bias-aware adaptation. To manage abrupt changes, BRPC incorporates restart mechanisms that detect regime shifts and reset the calibration process. The theoretical guarantees established include performance tracking under gradual evolution and the false-alarm and detection behavior of the restart mechanisms.

**Results**  
Empirical evaluations demonstrate that BRPC significantly enhances calibration accuracy in scenarios with gradual changes. Specifically, BRPC outperforms traditional sliding-window Bayesian calibration and data assimilation methods on synthetic and plant-simulation benchmarks. The restart-augmented version of BRPC shows further improvements in robustness and predictive performance during abrupt regime shifts. While specific numerical results are not detailed in the abstract, the authors claim substantial effect sizes compared to the baseline methods.

**Limitations**  
The authors acknowledge that BRPC's performance may be sensitive to the choice of hyperparameters in the Gaussian process and the restart mechanism's configuration. They do not address potential computational overhead associated with the online updates or the scalability of the method in high-dimensional parameter spaces. Additionally, the empirical results are based on synthetic and simulation data, which may not fully capture the complexities of real-world applications.

**Why it matters**  
The development of BRPC has significant implications for the field of online Bayesian calibration, particularly in applications where systems are subject to dynamic changes. By providing a robust framework for real-time calibration that accommodates both gradual and abrupt changes, this work paves the way for more accurate digital twins and improved decision-making in engineering and scientific applications. The theoretical foundations and empirical validation of BRPC could inspire further research into adaptive calibration techniques and their integration into broader machine learning workflows.

Authors: Yang Xu, Chiwoo Park  
Source: arXiv:2605.06612  
URL: https://arxiv.org/abs/2605.06612v1
