---
title: "Using Aristotle API for AI-Assisted Theorem Proving in Lean 4: A Formalisation Case Study of the Grasshopper Problem"
date: 2026-05-19 17:08:58 +0000
category: research
subcategory: theory
company: "ServiceNow"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.20120v1"
arxiv_id: "2605.20120"
authors: ["Gabriel Rongyang Lau"]
slug: using-aristotle-api-for-ai-assisted-theorem-proving-in-lean-
summary_word_count: 469
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the formal verification of AI-assisted theorem proving, specifically within the context of Lean 4. It presents a case study on the Grasshopper problem, originally posed as IMO 2009 Problem 6, highlighting the limitations of current AI tools in generating fully verified mathematical proofs. The authors note that while substantial Lean developments can be generated, the evidential status of these developments is contingent on the verification of the underlying declarations. This work is a preprint and has not undergone peer review.

**Method**  
The core technical contribution involves the use of the Aristotle API to assist in the formalization of the Grasshopper problem within Lean 4. The generated artifact includes a generalized version of the theorem and four verified helper lemmas that support a maximality and adjacent-swap exchange strategy. The lemmas establish critical properties such as the equality of final and total sums, the localized impact of adjacent transpositions on intermediate sums, and the implications of maximality on forbidden-set membership. However, the main theorem remains unresolved due to an unaddressed global counting step, which is necessary to demonstrate that the membership facts yield at least \( n \) distinct forbidden values, contradicting the cardinality assumption \( |M| < n \). The authors provide a reproducible Lean artifact and a detailed analysis of both verified and unverified components of the proof.

**Results**  
The paper does not present quantitative results in the form of performance metrics or effect sizes against named baselines, as it primarily focuses on the qualitative aspects of the formalization process. The key takeaway is the identification of a significant limitation in AI-assisted theorem proving: while local proof searches can yield verified components, the overarching combinatorial reasoning required for complete theorem verification remains unresolved. This case study serves as an illustrative example of the challenges faced in the field.

**Limitations**  
The authors acknowledge the limitation that local proof search can succeed while global combinatorial reasoning remains unaddressed. They do not explicitly discuss the potential for scalability issues or the generalizability of their findings to other mathematical problems. Additionally, the reliance on the Aristotle API may introduce dependencies that could affect the reproducibility of results across different theorem proving environments.

**Why it matters**  
This work has significant implications for the development of AI-assisted theorem proving systems. It underscores the necessity for advancements in global combinatorial reasoning capabilities to complement local proof search techniques. The findings highlight the current limitations of AI tools in producing fully verified mathematical proofs, which is critical for applications in formal verification, automated reasoning, and the broader field of mathematical logic. By providing a reproducible artifact and a clear analysis of the proof's structure, this study lays the groundwork for future research aimed at enhancing the efficacy of AI in formal mathematics.

Authors: Gabriel Rongyang Lau  
Source: arXiv:2605.20120v1  
URL: https://arxiv.org/abs/2605.20120v1
