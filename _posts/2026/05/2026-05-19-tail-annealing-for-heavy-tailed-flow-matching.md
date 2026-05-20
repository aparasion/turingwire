---
title: "Tail Annealing for Heavy-Tailed Flow Matching"
date: 2026-05-19 16:22:03 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20068v1"
arxiv_id: "2605.20068"
authors: ["Jean Pachebat"]
slug: tail-annealing-for-heavy-tailed-flow-matching
summary_word_count: 420
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of standard generative models in handling heavy-tailed data distributions, which are prevalent in various real-world applications. Existing architectures, particularly those based on Lipschitz constraints, fail to generate power-law tails from Gaussian noise effectively. Additionally, the challenge of interpolating between heavy-tailed and Gaussian data is identified as ill-posed. The authors propose a novel approach to mitigate these issues, presenting a preprint that has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of a soft-log transform, defined as \( φ(x) = \mathrm{sign}(x) \cdot \log(1 + |x|) \), applied coordinate-wise to the data prior to training. This transformation compresses heavy tails into a range conducive to standard flow matching techniques. After generating samples, the authors exponentiate the outputs to revert to the original scale. A Hill diagnostic is employed to determine whether to apply the transformation on a per-coordinate basis, ensuring that light-tailed margins remain unaffected. The theoretical underpinning suggests that the log-transform effectively maps Pareto tails to exponential distributions, facilitating a form of tail annealing through power transformations. The method does not require modifications to the underlying architecture or the use of heavy-tailed base distributions.

**Results**  
The proposed method, referred to as Log-FM, was evaluated on a comprehensive benchmark comprising 144 configurations, including three copulas and dimensions up to 100 with four tail indices. Log-FM outperformed specialized baselines across multiple metrics, including Wasserstein distance \( W_1 \), Conditional Value at Risk at the 99th percentile (CVaR$_{99}$), and extreme-quantile metrics. Notably, Log-FM achieved zero severe divergences across 2,880 runs, indicating robust performance and stability compared to existing methods.

**Limitations**  
The authors acknowledge that their approach may not generalize to all forms of heavy-tailed distributions, particularly those with complex structures beyond the scope of their benchmark. They do not address potential computational overhead introduced by the Hill diagnostic, which may affect scalability in high-dimensional settings. Additionally, the reliance on the soft-log transform may limit the method's applicability to datasets that do not conform to the assumptions underlying the transformation.

**Why it matters**  
This work has significant implications for the field of generative modeling, particularly in applications involving heavy-tailed data such as finance, telecommunications, and environmental science. By providing a straightforward yet effective method for handling heavy-tailed distributions, the authors pave the way for more accurate and reliable generative models. The concept of tail annealing through power transformations could inspire further research into adaptive transformations for various data types, potentially leading to advancements in generative modeling techniques.

Authors: Jean Pachebat  
Source: arXiv:2605.20068  
URL: https://arxiv.org/abs/2605.20068v1
