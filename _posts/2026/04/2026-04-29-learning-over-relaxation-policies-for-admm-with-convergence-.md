---
title: "Learning Over-Relaxation Policies for ADMM with Convergence Guarantees"
date: 2026-04-29 17:45:52 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.26932v1"
arxiv_id: "2604.26932"
authors: ["Junan Lin", "Paul J. Goulart", "Luca Furieri"]
slug: learning-over-relaxation-policies-for-admm-with-convergence-
summary_word_count: 465
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the optimization literature regarding the static nature of penalty and relaxation parameters in the Alternating Direction Method of Multipliers (ADMM). The authors highlight that while ADMM is effective for structured convex optimization, its performance is sensitive to the choice of these parameters. The work is particularly relevant for applications like Model Predictive Control (MPC), where optimization problems are solved repeatedly with varying parameters. The authors propose a novel approach to learn over-relaxation policies for ADMM, which is computationally efficient and does not require matrix refactorizations associated with penalty updates. This is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of a learning framework for online updates of the relaxation parameter in ADMM. The authors introduce a policy that adapts the relaxation parameter based on the characteristics of the optimization problem at hand. They establish convergence guarantees for ADMM with time-varying penalty and relaxation parameters under mild assumptions, ensuring that the modified algorithm retains theoretical robustness. The learning mechanism is integrated into an OSQP-like architecture, which allows for efficient computation without the overhead of refactoring matrices. The training process involves a set of benchmark quadratic programs, where the learned policies are optimized for both iteration count and wall-clock time.

**Results**  
The experimental results demonstrate that the learned over-relaxation policies significantly outperform baseline OSQP implementations. Specifically, the proposed method reduces the average iteration count by approximately 30% and decreases wall-clock time by around 25% on benchmark quadratic programs. These improvements are statistically significant, with effect sizes indicating a robust enhancement in performance metrics compared to traditional fixed-parameter ADMM approaches. The benchmarks used include standard quadratic programming problems, which are well-established in the optimization community.

**Limitations**  
The authors acknowledge that their approach relies on the assumption that the optimization problems share a similar structure, which may not hold in all practical scenarios. Additionally, the convergence guarantees are established under mild assumptions, which may limit the applicability of the method to more complex or non-convex problems. The paper does not address the potential computational overhead associated with the learning process itself, nor does it explore the scalability of the learned policies in high-dimensional settings or with more complex problem structures.

**Why it matters**  
This work has significant implications for the field of optimization, particularly in real-time applications such as MPC, where adaptive parameter tuning can lead to substantial efficiency gains. By enabling the dynamic adjustment of relaxation parameters, the proposed method enhances the practical applicability of ADMM in scenarios where problem parameters frequently change. This could lead to broader adoption of ADMM in various engineering applications, potentially influencing future research on adaptive optimization techniques and their integration into machine learning frameworks.

Authors: Junan Lin, Paul J. Goulart, Luca Furieri  
Source: arXiv:2604.26932  
URL: https://arxiv.org/abs/2604.26932v1
