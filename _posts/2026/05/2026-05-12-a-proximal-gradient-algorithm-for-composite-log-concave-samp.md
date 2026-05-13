---
title: "A proximal gradient algorithm for composite log-concave sampling"
date: 2026-05-12 17:48:09 +0000
category: research
subcategory: sampling_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12461v1"
arxiv_id: "2605.12461"
authors: ["Linghai Liu", "Sinho Chewi"]
slug: a-proximal-gradient-algorithm-for-composite-log-concave-samp
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of sampling from composite log-concave distributions of the form \( \pi \propto e^{-f-g} \) in \( \mathbb{R}^d \), where \( f \) is a smooth function and \( g \) is a potentially non-smooth function. The authors propose a proximal gradient algorithm that requires gradient evaluations of \( f \) and access to a restricted Gaussian oracle (RGO) for \( g \). This work is a preprint and has not yet undergone peer review, indicating that the findings should be interpreted with caution.

**Method**  
The proposed algorithm leverages the proximal operator associated with the function \( g \) to facilitate sampling. Specifically, the RGO allows for efficient sampling from the density \( \text{RGO}_{g,h,y}(x) \propto \exp(-g(x) - \frac{1}{2h}||y-x||^2) \). The algorithm achieves an \( \varepsilon \) error in total variation distance in \( \widetilde{\mathcal{O}}(κ\sqrt{d} \log^4(1/\varepsilon)) \) iterations, where \( κ = \frac{β}{α} \) with \( α \) being the strong convexity parameter of \( f + g \) and \( β \) the smoothness parameter of \( f \). The authors extend their results to scenarios where \( \pi \) is non-log-concave but adheres to a Poincaré or log-Sobolev inequality, as well as cases where \( f \) is non-smooth but Lipschitz continuous.

**Results**  
The algorithm matches the state-of-the-art results for the case where \( g = 0 \), achieving the same convergence rate of \( \widetilde{\mathcal{O}}(κ\sqrt{d} \log^4(1/\varepsilon)) \). The authors demonstrate that their method is effective in both log-concave and non-log-concave settings, providing a robust framework for sampling from a broader class of distributions. However, specific numerical results or comparisons against named baselines on established benchmarks are not provided in the abstract, which limits the ability to quantify the performance improvements over existing methods.

**Limitations**  
The authors acknowledge that their algorithm's performance is contingent on the strong convexity and smoothness assumptions of \( f \) and \( g \). They do not address potential computational overhead associated with the RGO, nor do they explore the implications of high-dimensional settings beyond the theoretical guarantees. Additionally, the lack of empirical validation or comparison against other sampling methods in practical scenarios is a notable gap.

**Why it matters**  
This work contributes to the field of probabilistic sampling by providing a novel algorithm that extends the capabilities of existing methods to a wider class of composite log-concave distributions. The implications are significant for applications in optimization, Bayesian inference, and machine learning, where sampling from complex distributions is often required. The ability to handle non-smooth functions and non-log-concave distributions opens new avenues for research and practical applications, particularly in high-dimensional spaces.

Authors: Linghai Liu, Sinho Chewi  
Source: arXiv:2605.12461  
URL: https://arxiv.org/abs/2605.12461v1
