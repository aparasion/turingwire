---
title: "Accelerating Bayesian inverse design in computational fluid dynamics using neural operators"
date: 2026-05-25 17:18:18 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.26059v1"
arxiv_id: "2605.26059"
authors: ["Bipin Tiwari", "Omer San"]
slug: accelerating-bayesian-inverse-design-in-computational-fluid-
summary_word_count: 443
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the significant computational burden associated with Bayesian inverse design in computational fluid dynamics (CFD), particularly when using gradient-based Markov chain Monte Carlo (MCMC) methods. The authors highlight the limitations of existing surrogate models in accurately capturing posterior geometry and uncertainty, especially in shock-dominated flows, which are critical in aerodynamic applications. The gap lies in the integration of effective surrogate models within the MCMC framework to enhance computational efficiency while maintaining fidelity in uncertainty quantification.

**Method**  
The core technical contribution is the integration of neural operator surrogates into the MCMC inference loop for Bayesian inverse design. The authors utilize a fully Bayesian formulation of quasi-one-dimensional nozzle flow, employing cubic B-splines for geometry parameterization to improve identifiability and posterior conditioning. A Deep Operator Network (DON) is trained on CFD-generated data and replaces the traditional CFD solver within a No-U-Turn Sampler (NUTS). The likelihood model, priors, and sampling configuration remain unchanged, allowing for a direct comparison with high-fidelity CFD simulations. The surrogate model enables rapid inference, reducing total computation time to under one second, achieving a speedup of over three orders of magnitude compared to conventional methods.

**Results**  
The surrogate-based inference successfully reproduces the posterior geometry and uncertainty trends observed in the CFD reference across varying observation regimes, from sparse to fully observed data. The authors report that the integration of the neural operator leads to a significant reduction in inference time while preserving the integrity of the posterior estimates. The results indicate that the method can achieve a speedup exceeding 1000x compared to traditional MCMC approaches, demonstrating its effectiveness in practical applications.

**Limitations**  
The authors acknowledge that the performance of the neural operator surrogates may vary with different flow conditions and geometries, particularly in more complex scenarios beyond the quasi-one-dimensional nozzle flow studied. They also note that while the method shows promise for aerodynamic applications, its generalizability to other domains in CFD remains to be validated. Additionally, the reliance on high-quality training data for the neural operator is a potential limitation, as insufficient data could lead to inaccurate surrogate predictions.

**Why it matters**  
This work has significant implications for the field of aerodynamic design and uncertainty quantification. By enabling rapid, uncertainty-aware inverse design workflows, the proposed method can facilitate real-time decision-making in engineering applications. The integration of neural operators within the MCMC framework not only enhances computational efficiency but also opens avenues for further research into the application of deep learning techniques in other areas of CFD and inverse problems. This approach could lead to more robust design methodologies that account for uncertainty, ultimately improving the performance and reliability of aerodynamic systems.

Authors: Bipin Tiwari, Omer San  
Source: arXiv:2605.26059  
URL: [https://arxiv.org/abs/2605.26059v1](https://arxiv.org/abs/2605.26059v1)
