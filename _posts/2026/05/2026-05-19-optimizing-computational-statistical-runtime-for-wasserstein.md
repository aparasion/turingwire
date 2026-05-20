---
title: "Optimizing Computational-Statistical Runtime for Wasserstein Distance Estimation"
date: 2026-05-19 17:10:47 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20122v1"
arxiv_id: "2605.20122"
authors: ["Peter Matthew Jacobs", "Jeff M. Phillips"]
slug: optimizing-computational-statistical-runtime-for-wasserstein
summary_word_count: 472
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the computational inefficiency in estimating the squared Wasserstein distance between empirical measures derived from random samples, particularly in low-dimensional Euclidean spaces (d ∈ {2,3}). Existing algorithms exhibit poor scaling in runtime with respect to both the sample size \( n \) and the desired precision \( ε \). The authors propose a solution to this gap by focusing on the computational-statistical runtime, which aims to achieve \( ε \)-additive error in expectation while allowing for \( O(1) \) computational cost for sample collection. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a novel Sample-Sketch-Solve paradigm that employs a regular Cartesian grid sketch of the samples. This approach allows for data compression without increasing the asymptotic error, which is crucial for maintaining accuracy while improving computational efficiency. The method is particularly effective for \( α \)-Hölder smooth distributions, where the Wasserstein distance \( W_2^2(P,Q) \) can be approximated within \( ε \) error in a time complexity of \( ε^{-\max(2,\frac{d+1+o(1)}{1+α})} \). For distributions with \( α > 1/2 \) in two dimensions, the method achieves an optimal time complexity of \( Θ(ε^{-2}) \), and it approaches optimality as \( α \) approaches 1 in three dimensions.

**Results**  
The proposed method demonstrates significant improvements over traditional algorithms. Specifically, it achieves the desired \( ε \)-additive error in \( Θ(ε^{-2}) \) time for \( α > 1/2 \) in \( d = 2 \) and nearly optimal performance as \( α \to 1 \) in \( d = 3 \). The authors benchmark their approach against existing algorithms, although specific baseline comparisons and numerical results are not detailed in the abstract. The implications of these results suggest a substantial reduction in computational overhead for Wasserstein distance estimation, particularly in applications involving large datasets.

**Limitations**  
The authors acknowledge that their method is primarily tailored for \( α \)-Hölder smooth distributions, which may limit its applicability to other types of distributions. Additionally, the performance gains are contingent on the smoothness parameter \( α \), and the method may not generalize well to distributions that do not meet these criteria. The paper does not address potential trade-offs in accuracy versus computational efficiency when applied to non-smooth distributions or higher dimensions beyond \( d = 3 \).

**Why it matters**  
This work has significant implications for fields that rely on Wasserstein distance for distribution comparison, such as machine learning, statistics, and optimal transport. By optimizing the computational-statistical runtime, the proposed method enables more efficient processing of large-scale data, facilitating real-time applications and enhancing the feasibility of Wasserstein-based metrics in practical scenarios. The findings could inspire further research into efficient algorithms for other distance metrics and broaden the applicability of Wasserstein distance in various domains.

Authors: Peter Matthew Jacobs, Jeff M. Phillips  
Source: arXiv:2605.20122  
URL: https://arxiv.org/abs/2605.20122v1
