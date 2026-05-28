---
title: "Expressive Power of Floating-Point Neural Networks with Arbitrary Reduction Orders and Inexact Activation Implementations"
date: 2026-05-27 16:30:41 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28704v1"
arxiv_id: "2605.28704"
authors: ["Yeachan Park", "Geonho Hwang", "Wonyeol Lee", "Sejun Park"]
slug: expressive-power-of-floating-point-neural-networks-with-arbi
summary_word_count: 447
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the literature regarding the expressivity of neural networks operating under finite-precision floating-point arithmetic. Most existing theories assume exact real arithmetic, which does not reflect practical implementations. Previous studies have focused on limited activation functions and idealized conditions, such as fixed reduction orders and correctly rounded activations. This work expands the understanding of floating-point neural networks by considering arbitrary reduction orders and inexact activation implementations with bounded unit in the last place (ulp) errors.

**Method**  
The authors introduce a general distinguishability framework to analyze the expressivity of floating-point neural networks. They establish that the ability to distinguish every pair of distinct inputs in the first layer is a necessary condition for universal representability. This framework allows for the identification of broad classes of activation functions that fail to be universal representators, extending previous findings on specific counterexamples like the correctly rounded cosine activation. The authors also demonstrate that a suitable form of distinguishability is sufficient for universal representability under mild conditions on the activation implementation. They provide universal representability results for a wide range of practical activation functions, including $\mathrm{Sigmoid}$, $\tanh$, $\mathrm{ReLU}$, $\mathrm{ELU}$, $\mathrm{SeLU}$, $\mathrm{GeLU}$, $\mathrm{Swish}$, $\mathrm{Mish}$, and $\sin$, all evaluated under more realistic floating-point execution models than previously considered.

**Results**  
The paper establishes that floating-point neural networks can represent arbitrary functions between floating-point domains exactly under the proposed framework. The authors provide specific conditions under which various activation functions achieve universal representability, significantly broadening the scope of previously known results. While exact numerical results are not provided in the abstract, the implications suggest a substantial increase in the expressivity of neural networks when using the proposed framework compared to traditional models that rely on idealized assumptions.

**Limitations**  
The authors acknowledge that their findings are contingent on the bounded ulp errors in activation implementations, which may not cover all practical scenarios. They do not address the computational overhead introduced by arbitrary reduction orders or the potential performance degradation in real-world applications due to inexact activations. Additionally, the framework's applicability to more complex architectures, such as those involving recurrent or convolutional layers, remains unexplored.

**Why it matters**  
This work has significant implications for the design and analysis of neural networks in practical applications, particularly in resource-constrained environments where floating-point arithmetic is prevalent. By elucidating the conditions under which floating-point neural networks can achieve universal representability, this research paves the way for more robust and expressive neural network architectures. It encourages further exploration into the effects of floating-point precision on model performance and opens avenues for developing new activation functions that maintain expressivity while adhering to practical implementation constraints.

Authors: Yeachan Park, Geonho Hwang, Wonyeol Lee, Sejun Park  
Source: arXiv:2605.28704  
URL: [https://arxiv.org/abs/2605.28704v1](https://arxiv.org/abs/2605.28704v1)
