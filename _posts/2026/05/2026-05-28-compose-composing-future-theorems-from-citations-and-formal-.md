---
title: "COMPOSE: Composing Future Theorems from Citations and Formal Structure"
date: 2026-05-28 17:58:42 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.30333v1"
arxiv_id: "2605.30333"
authors: ["David Busbib", "Michael Werman"]
slug: compose-composing-future-theorems-from-citations-and-formal-
summary_word_count: 472
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in generating plausible future mathematical claims by integrating two critical sources of context: the scientific citation graph and the formal theorem dependency graph. Existing methodologies typically focus on either the citation context or the formal structure, leading to outputs that are either inadequately grounded in prior work or lack sufficient motivation. The authors propose a novel approach, COMPOSE, to generate future theorem-like claims that respect both the direction of prior research and the formal dependencies inherent in mathematical discourse. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
COMPOSE employs a dual-graph framework that conditions a language model on both the scientific citation context and the formal theorem structure. The architecture leverages a transformer-based language model, integrating two distinct graph representations: one for the citation network and another for the formal dependencies of theorems. The authors constructed a dataset comprising 108,000 paired examples of scientific and formal graphs sourced from arXiv and Mathlib. Additionally, they created a benchmark of 47,000 future papers projected for 2024-2025 to evaluate the model's performance. The training process and compute resources utilized are not explicitly detailed in the paper.

**Results**  
COMPOSE demonstrates superior performance compared to strong baselines in retrieving real future papers, achieving a notable improvement in the quality of generated claims. Specifically, it outperforms existing models in LLM-judge evaluations, which assess the mathematical richness and grounding of the outputs. The paper reports that COMPOSE's outputs are more aligned with plausible future theorems, indicating a significant enhancement in the generation process when both citation and formal structures are considered. However, specific quantitative metrics (e.g., accuracy, F1 scores) against named baselines are not provided in the abstract.

**Limitations**  
The authors acknowledge that the reliance on existing citation and formal structures may limit the model's creativity in generating truly novel mathematical claims. Additionally, the dataset's reliance on arXiv and Mathlib may introduce biases based on the types of papers and the mathematical domains represented. The lack of detailed information regarding the training compute and hyperparameter settings is another limitation, as it hinders reproducibility. Furthermore, the evaluation metrics used, while indicative, may not fully capture the nuances of mathematical validity and innovation.

**Why it matters**  
The implications of this work are significant for the field of automated theorem generation and mathematical discovery. By successfully integrating citation and formal dependency graphs, COMPOSE paves the way for more sophisticated models that can generate mathematically sound and contextually relevant claims. This approach could enhance collaborative research efforts, assist mathematicians in exploring new avenues of inquiry, and ultimately contribute to the advancement of mathematical knowledge. The findings suggest that future research should focus on refining the integration of diverse contextual sources to further improve the quality and creativity of generated mathematical content.

Authors: David Busbib, Michael Werman  
Source: arXiv:2605.30333  
URL: https://arxiv.org/abs/2605.30333v1
