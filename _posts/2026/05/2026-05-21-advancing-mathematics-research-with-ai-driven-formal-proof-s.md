---
title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
date: 2026-05-21 17:24:57 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22763v1"
arxiv_id: "2605.22763"
authors: ["George Tsoukalas", "Anton Kovsharov", "Sergey Shirobokov", "Anja Surina", "Moritz Firsching", "Gergely B\u00e9rczi"]
slug: advancing-mathematics-research-with-ai-driven-formal-proof-s
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the application of AI-driven formal proof search in mathematics research, particularly focusing on the limitations of large language models (LLMs) in generating reliable mathematical proofs. The authors highlight the unreliability of LLMs in mathematical reasoning, which restricts their utility in solving open mathematical problems. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach that leverages LLMs to generate formal proofs in the Lean proof assistant. They conduct a large-scale evaluation of this method, employing a two-tiered agent architecture. The primary agent autonomously generates proofs for mathematical conjectures, while a secondary agent utilizes Lean for verification. The evaluation encompasses 353 open Erdős problems and 492 OEIS conjectures. The computational cost for the most capable agent is reported to be a few hundred dollars per problem. The training compute specifics are not disclosed, but the architecture's design emphasizes the interplay between LLM-based generation and formal verification.

**Results**  
The most capable agent successfully resolved 9 out of 353 open Erdős problems, achieving a success rate of approximately 2.5%. Additionally, it proved 44 out of 492 OEIS conjectures, translating to a success rate of about 8.9%. A baseline agent that alternated between LLM generation and Lean verification replicated the Erdős problem successes but incurred higher costs, particularly on more challenging problems. These results demonstrate a significant advancement in AI-aided formal proof search, showcasing the potential of LLMs in mathematical research.

**Limitations**  
The authors acknowledge several limitations, including the reliance on LLMs, which may still produce unreliable outputs despite verification. The cost-effectiveness of the proposed method is also flagged, particularly for harder problems where the verification process becomes more expensive. Additionally, the evaluation is limited to specific mathematical domains, and the generalizability of the findings to other areas of mathematics remains uncertain. The authors do not address potential biases in the training data of the LLMs or the implications of these biases on the generated proofs.

**Why it matters**  
This research has significant implications for the future of mathematical research, particularly in the automation of proof generation and verification. By demonstrating the effectiveness of AI-driven formal proof search, the work paves the way for further exploration of LLMs in other mathematical domains and potentially in interdisciplinary applications. The findings could lead to enhanced collaboration between mathematicians and AI systems, fostering new methodologies for tackling open problems in mathematics. Furthermore, the insights into agent design may inform future developments in AI-assisted theorem proving.

Authors: George Tsoukalas, Anton Kovsharov, Sergey Shirobokov, Anja Surina, Moritz Firsching, Gergely Bérczi, Francisco J. R. Ruiz, Arun Suggala et al.  
Source: arXiv:2605.22763  
URL: https://arxiv.org/abs/2605.22763v1
