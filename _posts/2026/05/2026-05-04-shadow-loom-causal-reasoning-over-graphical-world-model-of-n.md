---
title: "Shadow-Loom: Causal Reasoning over Graphical World Model of Narratives"
date: 2026-05-04 11:18:14 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02475v1"
arxiv_id: "2605.02475"
authors: ["David Wilmot"]
slug: shadow-loom-causal-reasoning-over-graphical-world-model-of-n
summary_word_count: 425
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the capability of existing narrative models to perform causal reasoning and structural analysis of stories. While previous works have explored narrative comprehension, they often lack a formalized approach to causal relationships and reader engagement metrics. The authors present Shadow-Loom as an experimental framework that integrates causal reasoning with narrative physics, enabling a more nuanced understanding of how stories function. Notably, this work is a preprint and has not undergone peer review.

**Method**  
Shadow-Loom employs a dual-engine architecture. The first engine implements a causal physics model based on Judea Pearl's ladder of causation, allowing for causal inference and counterfactual reasoning through Ancestral Multi-World Networks. The second engine, termed narrative physics, evaluates the narrative structure against four reader states: mystery, dramatic irony, suspense, and surprise. This evaluation is grounded in Sternberg's triad of curiosity, suspense, and surprise, with suspense formalized through structural-affect theories of story comprehension. The framework utilizes large language models (LLMs) primarily for boundary tasks such as extraction, rendering, and auditing, while core reasoning and interventions are executed in typed code over the graphical representation of the narrative. The authors provide the entire system as an open-source research artifact, including code and fixtures.

**Results**  
The paper does not present quantitative results or benchmark comparisons against established models, as it is positioned more as a conceptual framework than a performance-driven NLP model. The authors emphasize the framework's potential for enabling complex causal reasoning and narrative analysis rather than providing specific performance metrics. This lack of empirical validation may limit immediate applicability but opens avenues for future research.

**Limitations**  
The authors acknowledge that the framework is experimental and may not yet be suitable for practical applications without further validation. They do not provide empirical results or comparisons to existing narrative models, which could help contextualize its effectiveness. Additionally, the reliance on LLMs for boundary tasks may introduce biases inherent to those models, which are not addressed in the paper. The framework's complexity may also pose challenges for broader adoption in narrative analysis.

**Why it matters**  
Shadow-Loom has significant implications for the fields of narrative understanding and causal reasoning in AI. By formalizing the interplay between causal structures and reader engagement, it paves the way for more sophisticated narrative generation and analysis tools. This could enhance applications in storytelling, game design, and interactive media, where understanding user engagement and narrative dynamics is crucial. Furthermore, the open-source nature of the framework encourages collaboration and further exploration in the intersection of causal reasoning and narrative comprehension.

Authors: David Wilmot  
Source: arXiv:2605.02475  
URL: [https://arxiv.org/abs/2605.02475v1](https://arxiv.org/abs/2605.02475v1)
