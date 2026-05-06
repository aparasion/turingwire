---
title: "Physics-Grounded Multi-Agent Architecture for Traceable, Risk-Aware Human-AI Decision Support in Manufacturing"
date: 2026-05-05 17:24:53 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.04003v1"
arxiv_id: "2605.04003"
authors: ["Danny Hoang", "Ryan Matthiessen", "Christopher Miller", "Nasir Mannan", "Ruby ElKharboutly", "David Gorsich"]
slug: physics-grounded-multi-agent-architecture-for-traceable-risk
summary_word_count: 446
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing large language model (LLM) assistants in executing risk-constrained multi-step numerical workflows and providing auditable provenance for high-stakes decisions in high-precision CNC machining of aerospace components. The authors highlight the need for a robust decision-support system that integrates inspection, simulation, and process knowledge to ensure safety and traceability in manufacturing environments. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel architecture called Multi-Agent Knowledge Analysis (MAKA), which is designed to facilitate human-in-the-loop decision support. MAKA comprises several components: intent routing, tools-only quantitative analysis, knowledge graph retrieval, and critic-based verification. The architecture enforces physical plausibility, safety bounds, and completeness of provenance before recommendations are presented for human approval. MAKA is instantiated on a Ti-6Al-4V rotor blade machining testbed, integrating data from virtual machining path-tracking error fields, cutting-force and deflection simulations, and scan-based 3D inspection deviation maps from 16 blades. The analysis decomposes deviations into four components: evidence-linked pathing, a drift-based wear proxy, a residual systematic compliance term, and a variability proxy for instability-aware escalation. The system is evaluated through a three-level tool-orchestration benchmark, which includes single-step and multi-step stateful sequences.

**Results**  
MAKA demonstrates a significant improvement in successful tool execution, achieving up to an 87.5 percentage point increase compared to an unstructured single-model interaction pattern with the same tool access. In digital twin what-if studies, MAKA effectively coordinates traceable compensation candidates, reducing predicted surface deviation from approximately \(10^{-2}\) inches to around \(\pm 10^{-3}\) inches across most of the blade within the simulation environment. These results indicate a substantial enhancement in risk-aware decision-making capabilities for human operators.

**Limitations**  
The authors acknowledge that the MAKA architecture is still in the experimental phase and may require further validation in real-world manufacturing settings. They do not address potential scalability issues when applied to more complex machining tasks or the integration of additional data sources. Furthermore, the reliance on simulation data may limit the generalizability of the findings to other materials or machining processes.

**Why it matters**  
The development of MAKA has significant implications for the field of human-AI collaboration in manufacturing. By providing a structured, traceable, and risk-aware decision support system, this architecture can enhance the reliability and safety of CNC machining processes. The ability to decompose deviations and provide evidence-linked recommendations could lead to more informed human decision-making, ultimately improving manufacturing efficiency and product quality. This work lays the groundwork for future research into integrating AI systems with physical manufacturing processes, potentially influencing the design of next-generation decision support tools.

Authors: Danny Hoang, Ryan Matthiessen, Christopher Miller, Nasir Mannan, Ruby ElKharboutly, David Gorsich, Matthew P. Castanier, Farhad Imani  
Source: arXiv:2605.04003  
URL: [https://arxiv.org/abs/2605.04003v1](https://arxiv.org/abs/2605.04003v1)
