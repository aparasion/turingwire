---
title: "Complex Equation Learner: Rational Symbolic Regression with Gradient Descent in Complex Domain"
date: 2026-05-05 15:08:08 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03841v1"
arxiv_id: "2605.03841"
authors: ["Sergei Garmaev", "Maurice Gauch\u00e9", "Olga Fink"]
slug: complex-equation-learner-rational-symbolic-regression-with-g
summary_word_count: 430
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing symbolic regression methods, particularly those that utilize gradient-based optimization techniques. Traditional approaches struggle with operators that introduce singularities or domain constraints, such as division, logarithms, and square roots. These methods often either avoid these operators or impose restrictions to prevent optimization failures, which constrains the hypothesis space. The authors present a preprint that proposes a novel solution to this gap by extending the Equation Learner framework to the complex domain.

**Method**  
The core technical contribution is the introduction of a complex weight extension to the Equation Learner, which allows for the optimization of symbolic expressions in the complex domain. This approach leverages complex-valued optimization to bypass real-axis degeneracies that typically hinder convergence when dealing with singularities. The architecture retains the structure of the Equation Learner but incorporates complex weights, enabling the model to utilize operations like logarithm and square root without the need for constraints on the real domain. The authors do not disclose specific details regarding the training compute or the exact architecture used, but they validate their method on standard symbolic regression benchmarks.

**Results**  
The proposed Complex Equation Learner demonstrates significant improvements over traditional symbolic regression methods. In experiments, it successfully recovers expressions with singular behavior from experimental frequency response data, which previous models failed to capture. The authors report that their method outperforms baseline models on multiple symbolic regression benchmarks, although specific numerical results and effect sizes are not detailed in the abstract. The ability to handle singularities without imposing constraints is a key highlight of the results.

**Limitations**  
The authors acknowledge that while their method improves upon existing techniques, it may still face challenges in certain edge cases where complex optimization does not translate well to real-world applications. They do not discuss potential computational overhead introduced by complex optimization or the scalability of the approach to larger datasets. Additionally, the reliance on complex numbers may introduce interpretability challenges, as the resulting equations may not always yield straightforward real-valued interpretations.

**Why it matters**  
This work has significant implications for the field of symbolic regression and interpretable machine learning. By enabling the use of previously restricted operators, the Complex Equation Learner expands the hypothesis space, allowing for the discovery of more complex and potentially more accurate models. This advancement could facilitate better modeling of physical systems where singularities are inherent, thus enhancing the applicability of symbolic regression in scientific research and engineering. Furthermore, the approach may inspire future research into complex-valued optimization techniques in other areas of machine learning.

Authors: Sergei Garmaev, Maurice Gauché, Olga Fink  
Source: arXiv:2605.03841  
URL: [https://arxiv.org/abs/2605.03841v1](https://arxiv.org/abs/2605.03841v1)
