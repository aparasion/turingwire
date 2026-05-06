---
title: "A Closed-Form Adaptive-Landmark Kernel for Certified Point-Cloud and Graph Classification"
date: 2026-05-05 17:59:18 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.04046v1"
arxiv_id: "2605.04046"
authors: ["Sushovan Majhi", "Atish Mitra", "\u017diga Virk", "Pramita Bagchi"]
slug: a-closed-form-adaptive-landmark-kernel-for-certified-point-c
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing point-cloud and graph classification methods, particularly in the context of adaptive landmark selection and kernel-based classification. The authors introduce PALACE (Persistence Adaptive-Landmark Analytic Classification Engine) as a data-adaptive alternative to PLACE, which is constrained by a fixed grid structure. The work is presented as a preprint and has not undergone peer review, indicating that the findings should be interpreted with caution.

**Method**  
PALACE employs a cover-theoretic approach, utilizing the Lebesgue-number criterion to establish a landmark cover that adapts to the data. The method incorporates three hyperparameters (budget, radii, bandwidth), each with a maximum of five choices, allowing for a small cross-validation tier. Key contributions include:

1. A structural lower distortion bound \(λ(τ;ν)\) on the dataset \(\mathcal{D}_n\) under cross-diagram non-interference, achieving a budget reduction of \((D/L)^2\) compared to uniform grids when data diagrams are concentrated.
2. The use of equal weights \(w_k = K^{-1/2}\) to maximize \(λ\) and the implementation of farthest-point sampling to approximate the optimal \(k\)-center covering radius, both derived solely from training labels without gradient-based training.
3. A kernel-RKHS classification rate of \(O((k-1)\sqrt{K}/(γ\sqrt{m_{\min}}))\) with a binary necessity threshold \(m = Ω(\sqrt K/γ)\), supported by a matching Le Cam lower bound and a closed-form filtration-selection rule.
4. The introduction of a per-prediction certificate in both non-asymptotic Pinelis and asymptotic Gaussian forms, eliminating the need for a calibration split.

**Results**  
PALACE demonstrates superior performance on several benchmarks. It achieves an accuracy of \(91.3 \pm 1.0\%\) on the Orbit5k dataset, matching the performance of Persformer. Additionally, it outperforms all diagram-based competitors on the COX2 and MUTAG datasets and remains competitive on DHFR, with performance within 1 percentage point of the ECP baseline. Notably, under an \(8\times\) domain inflation, PALACE maintains a classification accuracy of \(94\%\), while the uniform grid method collapses to chance performance at \(25\%\) on a 4-class dataset.

**Limitations**  
The authors acknowledge that the method's performance is contingent on the choice of hyperparameters and the underlying data distribution. They do not address potential scalability issues with very large datasets or the computational overhead associated with the closed-form calculations. Additionally, the reliance on training labels for landmark selection may limit applicability in scenarios with sparse or noisy labels.

**Why it matters**  
The introduction of PALACE represents a significant advancement in adaptive kernel methods for point-cloud and graph classification, providing a framework that balances computational efficiency with classification accuracy. Its closed-form guarantees and empirical performance suggest that it could serve as a robust tool for researchers and practitioners in fields requiring high-dimensional data analysis, such as cheminformatics and computer vision. The implications of this work extend to the development of more efficient algorithms that leverage data characteristics for improved model performance.

Authors: Sushovan Majhi, Atish Mitra, Žiga Virk, Pramita Bagchi  
Source: arXiv:2605.04046  
URL: https://arxiv.org/abs/2605.04046v1
