---
title: "Agent-Agnostic Evaluation of SQL Accuracy in Production Text-to-SQL Systems"
date: 2026-04-30 15:59:28 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28049v1"
arxiv_id: "2604.28049"
authors: ["Taslim Jamal Arif", "Kuldeep Singh"]
slug: agent-agnostic-evaluation-of-sql-accuracy-in-production-text
summary_word_count: 398
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of Text-to-SQL (T2SQL) systems in production environments, highlighting that existing benchmarks rely on ground-truth queries and structured database schemas, which are often unavailable in real-world applications. The authors note that this limitation results in a lack of effective evaluation mechanisms for T2SQL agents, leading to undetected quality degradation over time. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce the Schema-agnostic Text-to-SQL Evaluation Framework (STEF), which evaluates T2SQL systems using only natural language inputs, enriched reformulations, and generated SQL queries, without requiring access to database schemas or reference queries. STEF employs a composite metric that integrates three components: filter alignment, semantic verdict, and evaluator confidence, producing an interpretable accuracy score ranging from 0 to 100. Key technical contributions include:
- Enriched question quality validation as a primary evaluation signal.
- Configurable application-specific rule injection through prompt templating.
- Robust normalization techniques that handle GROUP BY tolerances, ORDER BY defaults, and LIMIT heuristics, ensuring that evaluations are resilient to common SQL variations.

**Results**  
The empirical evaluation demonstrates that STEF facilitates continuous monitoring of T2SQL systems in production, enabling feedback loops for agent improvement. While specific numerical results are not disclosed in the abstract, the authors assert that STEF's schema-agnostic nature allows for scalable structured query evaluation, which is a notable advancement over existing methods that are schema-dependent.

**Limitations**  
The authors acknowledge that STEF's reliance on natural language inputs may introduce variability in evaluation accuracy, as the quality of the input questions can significantly affect the results. Additionally, the framework's performance in highly complex SQL queries or those requiring intricate schema knowledge is not explicitly tested. The paper does not address potential biases in the semantic extraction process or the implications of using a composite metric that may obscure individual component performance.

**Why it matters**  
The introduction of STEF has significant implications for the development and deployment of T2SQL systems in real-world applications. By enabling schema-agnostic evaluation, STEF allows for continuous assessment and improvement of T2SQL agents, which is crucial for maintaining high-quality performance in production settings. This framework could lead to more robust T2SQL systems that adapt to user queries without the constraints of traditional evaluation methodologies, ultimately enhancing the reliability and effectiveness of natural language interfaces for database interactions.

Authors: Taslim Jamal Arif, Kuldeep Singh  
Source: arXiv:2604.28049  
URL: [https://arxiv.org/abs/2604.28049v1](https://arxiv.org/abs/2604.28049v1)
