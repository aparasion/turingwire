---
title: "Shields to Guarantee Probabilistic Safety in MDPs"
date: 2026-05-11 17:33:01 +0000
category: research
subcategory: safety_alignment
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10888v1"
arxiv_id: "2605.10888"
authors: ["Linus Heck", "Filip Mac\u00e1k", "Roman Andriushchenko", "Milan \u010ce\u0161ka", "Sebastian Junges"]
slug: shields-to-guarantee-probabilistic-safety-in-mdps
summary_word_count: 450
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding the application of shielding techniques to ensure probabilistic safety in Markov Decision Processes (MDPs). While classical shielding methods provide strong guarantees on safety and permissiveness, extending these guarantees to scenarios where violations are permissible with a certain probability has not been adequately explored. The authors highlight the challenges in maintaining these guarantees in probabilistic settings and present a formal framework to tackle this issue. This work is a preprint and has not yet undergone peer review.

**Method**  
The authors propose a formal framework that extends classical shielding to accommodate probabilistic safety. They demonstrate the theoretical impossibility of achieving strong guarantees on both safety and permissiveness in this context. The framework includes the development of two types of shields: natural shields with weaker guarantees and both offline and online shield constructions that ensure strong safety guarantees. The offline shields are designed to be computed prior to deployment, while the online shields adaptively modify the agent's policy during operation. The paper does not disclose specific details regarding the architecture, loss functions, or training compute used in the empirical evaluations, focusing instead on the theoretical underpinnings and practical implementations of the shielding methods.

**Results**  
The empirical evaluation demonstrates the effectiveness of the proposed shielding methods against established baselines in probabilistic safety scenarios. The authors report significant improvements in safety metrics, although specific numerical results and effect sizes are not detailed in the summary. The evaluation includes comparisons with classical shielding approaches, highlighting the computational feasibility and practical advantages of the new shields in maintaining safety while allowing for controlled risk.

**Limitations**  
The authors acknowledge that the guarantees provided by the proposed shields are weaker than those of classical shielding methods, which may limit their applicability in scenarios requiring stringent safety assurances. Additionally, the computational complexity of the online shield construction may pose challenges in real-time applications. The paper does not address potential scalability issues when applied to larger state spaces or more complex MDPs, nor does it explore the impact of varying levels of permissible risk on the performance of the shields.

**Why it matters**  
This work has significant implications for the design of autonomous systems that operate under uncertainty, such as robotics and autonomous vehicles. By providing a framework for probabilistic safety, the authors enable the development of agents that can make informed decisions while managing risk, thus enhancing their operational robustness. The findings could inform future research on safety-critical applications, where balancing safety and permissiveness is essential for practical deployment. The proposed shielding methods may also inspire further exploration into adaptive safety mechanisms in dynamic environments.

Authors: Linus Heck, Filip Macák, Roman Andriushchenko, Milan Češka, Sebastian Junges  
Source: arXiv:2605.10888  
URL: [https://arxiv.org/abs/2605.10888v1](https://arxiv.org/abs/2605.10888v1)
