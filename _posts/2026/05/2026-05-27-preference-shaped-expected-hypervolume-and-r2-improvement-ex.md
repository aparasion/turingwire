---
title: "Preference-Shaped Expected Hypervolume and R2 Improvement: Exact Computation and Monotonicity"
date: 2026-05-27 17:02:28 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28746v1"
arxiv_id: "2605.28746"
authors: ["Michael T. M. Emmerich"]
slug: preference-shaped-expected-hypervolume-and-r2-improvement-ex
summary_word_count: 453
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in understanding the geometric properties and computational aspects of preference-shaped expected improvement criteria in Bayesian multiobjective optimization. Specifically, it investigates the differences between two commonly used indicators: the hypervolume indicator and the R2 indicator. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contributions include a detailed analysis of the hypervolume indicator and the R2 indicator, focusing on their geometric properties and computational methods. The authors revisit the expected hypervolume improvement (EHVI) using the Deng representation and introduce product-density weighted EHVI in desirability coordinates. They also discuss the implications of linear cone transformations on cone-based EHVI and differentiate it from truncated EHVI, where variance monotonicity may not hold. For the R2 indicator, the authors prove that the exact integral R2 improvement does not equate to an ordinary objective-space weighted hypervolume due to lower-dimensional obstructions. They establish that the exact integral R2 improvement corresponds to the measure of the Tchebycheff shadow between the incumbent scalarization envelope and the reference envelope. This leads to the development of finite-sum ER2I algorithms for discrete R2, quadrature methods for exact integral R2, and a Gaussian surrogate formulation where ER2I is represented as an integral of scalar Gaussian expected improvements.

**Results**  
The paper provides theoretical results demonstrating the conditions under which preference transformations preserve exact computation, Pareto compatibility, and monotonicity. While specific numerical results are not detailed in the abstract, the implications of the findings suggest that the proposed methods can yield more accurate and computationally efficient approaches to multiobjective optimization compared to existing baselines. The authors emphasize the importance of understanding the geometric differences between the hypervolume and R2 indicators, which can significantly impact optimization outcomes.

**Limitations**  
The authors acknowledge that the exact integral R2 improvement may not always align with traditional hypervolume measures, particularly in lower-dimensional cases where certain boundary contributions are overlooked. They do not explicitly address the computational complexity of the proposed algorithms or their scalability in high-dimensional spaces, which could be a concern for practical applications. Additionally, the reliance on Gaussian surrogates may limit the applicability of the methods in scenarios where the underlying objective functions do not conform to Gaussian assumptions.

**Why it matters**  
This work has significant implications for the field of Bayesian multiobjective optimization, particularly in enhancing the understanding of how different preference indicators can be utilized effectively. By clarifying the geometric properties and computational methods associated with hypervolume and R2 indicators, the findings can inform the design of more robust optimization algorithms. This could lead to improved performance in various applications, including engineering design, resource allocation, and decision-making processes where multiple conflicting objectives must be balanced.

Authors: Michael T. M. Emmerich  
Source: arXiv:2605.28746  
URL: https://arxiv.org/abs/2605.28746v1
