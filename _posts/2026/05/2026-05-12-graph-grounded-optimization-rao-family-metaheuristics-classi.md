---
title: "Graph-Grounded Optimization: Rao-Family Metaheuristics, Classical OR, and SLM-Driven Formulation over Knowledge Graphs"
date: 2026-05-12 14:43:35 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.12204v1"
arxiv_id: "2605.12204"
authors: ["Madhulatha Mandarapu", "Sandeep Kunkunuru"]
slug: graph-grounded-optimization-rao-family-metaheuristics-classi
summary_word_count: 417
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in optimization methodologies that utilize property knowledge graphs (KGs) as the primary input modality for decision variables, constraints, and objective coefficients. Existing LLM/SLM-driven optimization systems, such as OptiMUS and Chain-of-Experts, do not leverage KGs effectively, relying instead on free-form natural language or static tabular data. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel paradigm termed "graph-grounded optimization," which integrates KGs into the optimization process through Cypher queries. They instantiate this paradigm using the open-source samyama-graph database and evaluate it across seven real-world public-domain problems, including drug repurposing and clinical-trial site selection. The optimization is performed using a portfolio of Rao-family metaheuristics (BMWR, Jaya, SAMP-Jaya, EHR-Jaya, Rao-1) and compared against Google OR-tools (CP-SAT and GLOP) as reference solvers. The evaluation focuses on the performance of these algorithms across various problem types, emphasizing the need for a portfolio approach due to the varying strengths of the Rao variants in different contexts.

**Results**  
The results indicate that no single Rao-family metaheuristic consistently outperforms the others across all problem types. Specifically, BMWR excels in discrete-with-tradeoff and high-dimensional problems, while Rao-1 is superior in continuous low- to mid-dimensional scenarios. In contrast, Google OR-tools perform well on small linear and MILP-friendly sub-problems but struggle with non-linear objectives prevalent in the evaluated real-world settings. The authors highlight that graph-grounded formulations reveal data-quality issues, such as missing properties and degenerate aggregates, which are often overlooked in traditional text-based optimization approaches.

**Limitations**  
The authors acknowledge several limitations, including the potential for data-quality issues inherent in KGs, which can affect optimization outcomes. They also note that the performance of Rao-family metaheuristics may vary significantly based on the specific characteristics of the optimization problem, suggesting that further empirical validation is necessary. Additionally, the study does not explore the scalability of the proposed methods in larger or more complex KGs, nor does it address the computational overhead introduced by querying KGs.

**Why it matters**  
This work has significant implications for the field of optimization, particularly in contexts where KGs can provide rich, structured information. By demonstrating the efficacy of graph-grounded optimization, the authors pave the way for future research that can leverage KGs to enhance decision-making processes in various domains, including healthcare, supply chain management, and environmental planning. The findings encourage the development of more sophisticated optimization frameworks that can integrate diverse data sources, ultimately leading to more robust and informed solutions.

Authors: Madhulatha Mandarapu, Sandeep Kunkunuru  
Source: arXiv:2605.12204  
URL: [https://arxiv.org/abs/2605.12204v1](https://arxiv.org/abs/2605.12204v1)
