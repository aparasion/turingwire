---
title: "Reversa: A Reverse Documentation Engineering Framework for Converting Legacy Software into Operational Specifications for AI Agents"
date: 2026-05-18 17:23:13 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18684v1"
arxiv_id: "2605.18684"
authors: ["Sanderson Oliveira de Macedo", "Ronaldo Martins da Costa"]
slug: reversa-a-reverse-documentation-engineering-framework-for-co
summary_word_count: 459
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in converting legacy software systems into operational specifications suitable for AI agents, a challenge exacerbated by the implicit nature of business rules and architectural decisions embedded in legacy code. The authors highlight the need for reliable context and correctness criteria for language-model-based coding agents to operate effectively. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Reversa framework, which employs a multi-agent pipeline to reverse engineer legacy software. The framework consists of specialized agents that perform the following tasks: mapping the project surface, analyzing modules, extracting implicit rules, synthesizing architecture, generating unit-level specifications, and reviewing claims. Key mechanisms include:
- **Traceability**: Establishing a clear link between code and specifications.
- **Confidence Marking**: Explicitly indicating the confidence level of generated claims.
- **Gap Preservation**: Identifying and preserving areas requiring human validation.

Reversa is implemented as a Node.js CLI, facilitating the installation of skills across various agent engines. It utilizes a SHA-256 manifest to maintain the integrity of modified files during updates or uninstalls. The authors also propose an evaluation protocol that includes metrics for coverage, traceability, confidence, utility, and cost.

**Results**  
The authors conducted an exploratory case study on migrating an ATM system from COBOL to Go, where the Reversa pipeline produced 517 claims classified by an internal confidence index. The results included:
- 10 identified gaps requiring human validation.
- 53 Gherkin parity scenarios developed to ensure functional equivalence.
- A reconstruction plan with 9 out of 11 tasks completed at the time of inventory.

While the study did not complete final parity validation and cutover, the results indicate a structured approach to documenting legacy systems, with a focus on traceability and confidence in the generated specifications.

**Limitations**  
The authors acknowledge that their study does not claim broad empirical superiority over existing methods. They also note that the final validation and cutover processes were not completed, which limits the practical applicability of the results. Additionally, the exploratory nature of the case study may not generalize to other legacy systems or programming languages. The evaluation metrics proposed are yet to be validated in broader contexts.

**Why it matters**  
The implications of this work are significant for the fields of reverse engineering and AI-assisted software development. By providing a structured framework for converting legacy systems into operational specifications, Reversa could enhance the reliability of AI agents in modifying existing software. This could lead to reduced risks in software maintenance and evolution, ultimately facilitating the integration of AI technologies into legacy systems. The proposed evaluation metrics also lay the groundwork for future research in assessing the effectiveness of reverse engineering methodologies.

Authors: Sanderson Oliveira de Macedo, Ronaldo Martins da Costa  
Source: arXiv:2605.18684  
URL: [https://arxiv.org/abs/2605.18684v1](https://arxiv.org/abs/2605.18684v1)
