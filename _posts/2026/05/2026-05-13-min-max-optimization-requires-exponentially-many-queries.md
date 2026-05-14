---
title: "Min-Max Optimization Requires Exponentially Many Queries"
date: 2026-05-13 17:34:24 +0000
category: research
subcategory: other
company: "Oracle"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13806v1"
arxiv_id: "2605.13806"
authors: ["Martino Bernasconi", "Matteo Castiglioni", "Andrea Celli", "Alexandros Hollender"]
slug: min-max-optimization-requires-exponentially-many-queries
summary_word_count: 436
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the understanding of query complexity in min-max optimization, particularly for nonconvex-nonconcave functions. The authors demonstrate that existing algorithms for finding approximate stationary points in this context require an exponential number of queries relative to the precision parameter \( \varepsilon \) and the dimensionality \( d \). This work is presented as a preprint and has not yet undergone peer review, indicating that the findings are preliminary and subject to validation.

**Method**  
The authors analyze the query complexity of algorithms tasked with locating \( \varepsilon \)-approximate stationary points of a nonconvex-nonconcave function \( f: [0,1]^d \times [0,1]^d \to \mathbb{R} \). They establish that any algorithm with oracle access to both the function \( f \) and its gradient \( \nabla f \) must make a number of queries that scales exponentially with respect to \( 1/\varepsilon \) or the dimension \( d \). The proof leverages a reduction from the problem of finding stationary points to a lower bound on the number of queries required, employing techniques from complexity theory to substantiate their claims.

**Results**  
The core result indicates that the query complexity for finding an \( \varepsilon \)-approximate stationary point is \( \Omega\left(\exp\left(\frac{1}{\varepsilon}\right)\right) \) or \( \Omega\left(\exp(d)\right) \). This finding is significant when compared to existing algorithms that may not account for such exponential growth in query requirements. The authors do not provide specific baseline algorithms or benchmarks for comparison, but the implications of their results suggest that previously proposed methods may be inefficient in high-dimensional or high-precision scenarios.

**Limitations**  
The authors acknowledge that their results are specific to the class of nonconvex-nonconcave functions and do not extend to other types of optimization problems. They also note that the exponential query complexity may not be universally applicable across all algorithmic approaches, particularly those that leverage additional structural properties of the function \( f \). An obvious limitation not discussed by the authors is the practical applicability of their findings; real-world scenarios may involve approximations or heuristics that could mitigate the exponential growth in query complexity.

**Why it matters**  
This work has significant implications for the field of optimization, particularly in machine learning contexts where min-max problems frequently arise, such as in adversarial training and generative adversarial networks (GANs). Understanding the inherent limitations in query complexity can guide researchers in developing more efficient algorithms or in setting realistic expectations for performance in high-dimensional settings. Furthermore, the results may prompt further investigation into alternative optimization strategies that could circumvent the exponential query requirements identified in this study.

Authors: Martino Bernasconi, Matteo Castiglioni, Andrea Celli, Alexandros Hollender  
Source: arXiv:2605.13806  
URL: https://arxiv.org/abs/2605.13806v1
