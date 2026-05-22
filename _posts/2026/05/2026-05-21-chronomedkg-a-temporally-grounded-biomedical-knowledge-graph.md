---
title: "ChronoMedKG: A Temporally-Grounded Biomedical Knowledge Graph and Benchmark for Clinical Reasoning"
date: 2026-05-21 17:04:28 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.22734v1"
arxiv_id: "2605.22734"
authors: ["Md Shamim Ahmed", "Farzaneh Firoozbakht", "Lukas Galke Poech", "Jan Baumbach", "Richard R\u00f6ttger"]
slug: chronomedkg-a-temporally-grounded-biomedical-knowledge-graph
summary_word_count: 459
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the existing biomedical knowledge graph (KG) literature, specifically the lack of temporal grounding in disease associations. Current KGs, such as PrimeKG, Hetionet, and iKraph, treat disease associations as static entities, failing to account for the temporal dynamics of clinical symptoms and disease progression. This limitation hampers their utility in longitudinal clinical reasoning and retrieval tasks. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce ChronoMedKG, a temporally-grounded biomedical knowledge graph comprising 460,497 evidence-linked triples derived from a raw dataset of 13 million extractions. The graph encompasses 13,431 diseases, with each association linked to temporal components such as onset windows and progression stages. The construction of ChronoMedKG employs a disease-autonomous multi-agent pipeline, where multiple frontier large language models (LLMs) independently extract knowledge from PubMed and PMC literature. The final relations retained in the graph are those that achieve consensus across multiple models, pass credibility filtering, and align with established ontologies. A multi-signal credibility score is also integrated to enhance the reliability of the extracted information.

**Results**  
ChronoMedKG demonstrates a 92.7% agreement rate with Orphadata, indicating high fidelity in its disease associations. Notably, it introduces temporal grounding for 6,250 diseases that are not represented in existing resources like HPOA, Orphadata, and Phenopackets, including 1,657 rare diseases coded by Orphanet. The authors also present ChronoTQA, a benchmark consisting of 3,341 questions across eight task types (six temporal and two static controls), with an additional 12-question supplementary probe. When evaluated, frontier LLMs exhibit a performance drop of approximately 30 points when transitioning from static to temporal questions. However, retrieval using ChronoMedKG mitigates this decline, recovering 47-65% of long-tail failures, compared to only 17-29% recovery for HPOA-RAG.

**Limitations**  
The authors acknowledge that while ChronoMedKG significantly enhances temporal reasoning capabilities, it is still limited by the quality and comprehensiveness of the underlying literature from which it extracts data. Additionally, the reliance on multi-agent consensus may introduce biases based on the models used. The temporal aspects of the graph may also not cover all possible clinical scenarios, particularly in complex cases with overlapping symptoms across different age groups. Furthermore, as a preprint, the findings await validation through peer review.

**Why it matters**  
ChronoMedKG represents a pivotal advancement in the integration of temporal information into biomedical knowledge graphs, which is essential for improving clinical reasoning and decision-making processes. By providing a temporal axis for retrieval-augmented clinical systems, it opens avenues for more accurate diagnostics and personalized medicine approaches. The introduction of the ChronoTQA benchmark further facilitates the evaluation of temporal reasoning capabilities in LLMs, setting a foundation for future research in this domain.

Authors: Md Shamim Ahmed, Farzaneh Firoozbakht, Lukas Galke Poech, Jan Baumbach, Richard Röttger  
Source: arXiv:2605.22734  
URL: [https://arxiv.org/abs/2605.22734v1](https://arxiv.org/abs/2605.22734v1)
