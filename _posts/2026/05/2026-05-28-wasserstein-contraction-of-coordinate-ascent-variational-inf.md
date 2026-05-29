---
title: "Wasserstein Contraction of Coordinate Ascent Variational Inference"
date: 2026-05-28 17:16:22 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30253v1"
arxiv_id: "2605.30253"
authors: ["Rocco Caprio", "Adrien Corenflos", "Sam Power"]
slug: wasserstein-contraction-of-coordinate-ascent-variational-inf
summary_word_count: 404
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in understanding the convergence properties of the Coordinate Ascent Variational Inference (CAVI) algorithm, particularly in terms of its Wasserstein distance contraction. The authors present a theoretical framework that provides local convergence guarantees under specific conditions, which is not extensively covered in existing literature. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution involves establishing a contraction in Wasserstein distance for the CAVI algorithm. The authors utilize a transport-information inequality at the fixed points of the algorithm, alongside a functional smoothness condition, to derive their results. The analysis is applicable to a broad class of smooth manifolds and extends to certain non-smooth spaces. The paper also explores applications of the theoretical findings to Bayesian Gaussian Mixture Models, high-dimensional Bayesian Probit Regression, and Logistic Regression with Pólya-Gamma random variables, specifically referencing Jaakkola and Jordan's algorithm. The authors do not disclose specific training compute requirements, focusing instead on the theoretical underpinnings.

**Results**  
The authors demonstrate that the CAVI algorithm exhibits contraction properties in Wasserstein distance, leading to local convergence guarantees. While specific numerical results are not provided in the abstract, the implications of the theoretical results suggest improved convergence behavior compared to traditional variational inference methods. The paper positions its findings against existing baselines in variational inference, although explicit comparisons with named benchmarks are not detailed in the abstract.

**Limitations**  
The authors acknowledge that their results are contingent upon the assumptions of smoothness and the transport-information inequality, which may not hold in all practical scenarios. Additionally, the generalizability of the findings to more complex or high-dimensional distributions is not fully explored. The lack of empirical validation in the form of experiments or simulations is a notable limitation, as the theoretical results remain untested against real-world data.

**Why it matters**  
This work has significant implications for the field of variational inference, particularly in enhancing the understanding of convergence properties of CAVI. By establishing a theoretical foundation for Wasserstein contraction, the findings could lead to more robust and efficient variational inference algorithms, especially in high-dimensional settings. The results may also inform future research on the design of variational methods that leverage Wasserstein distances, potentially improving performance in Bayesian inference tasks. The theoretical insights could pave the way for further exploration of convergence in non-smooth spaces, expanding the applicability of variational inference techniques.

Authors: Rocco Caprio, Adrien Corenflos, Sam Power  
Source: arXiv:2605.30253  
URL: [https://arxiv.org/abs/2605.30253v1](https://arxiv.org/abs/2605.30253v1)
