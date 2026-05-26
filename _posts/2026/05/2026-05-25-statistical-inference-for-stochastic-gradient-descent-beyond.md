---
title: "Statistical Inference for Stochastic Gradient Descent Beyond Finite Variance"
date: 2026-05-25 16:18:39 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.26000v1"
arxiv_id: "2605.26000"
authors: ["Jose Blanchet", "Peter Glynn", "Wenhao Yang"]
slug: statistical-inference-for-stochastic-gradient-descent-beyond
summary_word_count: 419
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in statistical inference methodologies for Stochastic Gradient Descent (SGD) when dealing with stochastic gradients that exhibit infinite variance. Traditional approaches to inference using SGD iterates are hindered by the dependence on unknown nuisance parameters in the limiting distributions. The authors propose a model-agnostic methodology that is applicable in both finite- and infinite-variance scenarios, which is particularly relevant given the increasing prevalence of SGD in large-scale statistical learning and stochastic optimization. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is a novel approach to constructing confidence regions from SGD trajectories. The methodology leverages a joint weak convergence result for the Polyak-Ruppert averaged estimator, combined with an empirical second-moment normalizer derived from the stochastic gradients along the SGD path. This joint limit results in a self-normalized statistic where the leading tail-dependent scaling terms cancel out, facilitating the construction of confidence regions without the need for explicit estimation of tail indices or stable-law parameters. The authors implement a subsampling calibration scheme to estimate critical values, ensuring the method remains computationally efficient and straightforward to apply. The proposed approach is asymptotically valid in both finite- and infinite-second-moment regimes.

**Results**  
The authors validate their methodology through extensive simulation studies, demonstrating reliable coverage of the constructed confidence regions across various settings. While specific numerical results are not detailed in the abstract, the simulations indicate that the proposed method outperforms traditional inference techniques that do not account for infinite variance, thus providing a robust tool for uncertainty quantification in stochastic optimization tasks.

**Limitations**  
The authors acknowledge that their method, while effective, may still be sensitive to the choice of subsampling parameters and the underlying assumptions regarding the stochastic gradients. They do not address potential computational overhead in high-dimensional settings or the implications of model misspecification. Additionally, the performance of the method in real-world applications remains to be thoroughly evaluated, as the simulations are conducted in controlled environments.

**Why it matters**  
This work has significant implications for the field of machine learning, particularly in scenarios where SGD is employed for large-scale optimization problems. By providing a reliable method for statistical inference in the presence of infinite variance, the authors enhance the toolkit available for practitioners, enabling better uncertainty quantification and more robust decision-making in stochastic optimization contexts. This advancement could lead to improved performance in various applications, including deep learning and reinforcement learning, where SGD is a fundamental algorithm.

Authors: Jose Blanchet, Peter Glynn, Wenhao Yang  
Source: arXiv:2605.26000  
URL: [https://arxiv.org/abs/2605.26000v1](https://arxiv.org/abs/2605.26000v1)
