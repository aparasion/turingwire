---
title: "Parametric Modular Answer Set Programs Made Declarative"
date: 2026-05-21 16:52:18 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22716v1"
arxiv_id: "2605.22716"
authors: ["Jorge Fandinno", "Yuliya Lierler", "Torsten Schaub"]
slug: parametric-modular-answer-set-programs-made-declarative
summary_word_count: 385
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the expressiveness and modularity of first-order Answer Set Programming (ASP) by introducing a new formalism for modular logic programs. The authors identify limitations in existing ASP frameworks, particularly in their ability to define and manage subprograms with parameters and intensionality statements. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of parametric modular logic programs, which extend traditional ASP by allowing the definition of subprograms that can accept parameters. This formalism incorporates intensionality statements, enabling a more structured approach to program design. The authors provide a theoretical foundation for this new framework, demonstrating how it can encapsulate the semantics of clingo-programs with collective control. The methodology includes formal definitions, proofs of soundness and completeness, and examples illustrating the practical application of the proposed formalism in modular ASP.

**Results**  
The authors demonstrate that parametric modular logic programs can effectively represent complex logic structures that traditional non-modular ASP cannot. While specific quantitative results or benchmarks against existing ASP systems are not provided in the abstract, the paper claims that the new formalism significantly enhances the expressiveness and usability of ASP. The authors illustrate the practical implications of their approach through examples, showing how modularity can simplify the design and instantiation of logic programs.

**Limitations**  
The authors acknowledge that their approach may introduce additional complexity in terms of understanding and implementing the new formalism, particularly for users accustomed to traditional ASP. They do not address potential performance implications of using parametric modular logic programs compared to non-modular approaches, such as increased computational overhead or the impact on solving efficiency. Additionally, the scalability of the proposed framework in large-scale applications remains unexamined.

**Why it matters**  
This work has significant implications for the development of more modular and maintainable logic programming systems. By enabling the definition of parameterized subprograms, the proposed formalism can facilitate the reuse of code and enhance collaboration in complex logic programming tasks. This advancement could lead to more efficient implementations in various domains, including knowledge representation, automated reasoning, and AI planning. The ability to structure and instantiate subprograms dynamically may also pave the way for more sophisticated applications in multi-agent systems and collective decision-making processes.

Authors: Jorge Fandinno, Yuliya Lierler, Torsten Schaub  
Source: arXiv:2605.22716  
URL: [https://arxiv.org/abs/2605.22716v1](https://arxiv.org/abs/2605.22716v1)
