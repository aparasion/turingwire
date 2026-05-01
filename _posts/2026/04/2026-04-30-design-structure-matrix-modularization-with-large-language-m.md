---
title: "Design Structure Matrix Modularization with Large Language Models"
date: 2026-04-30 15:38:38 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28018v1"
arxiv_id: "2604.28018"
authors: ["Shuo Jiang", "Jianxi Luo"]
slug: design-structure-matrix-modularization-with-large-language-m
summary_word_count: 400
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in modularization techniques for Design Structure Matrices (DSMs) in engineering design, specifically focusing on the limitations of traditional graph optimization methods that lack contextual understanding of the engineering systems involved. The authors highlight that existing approaches do not leverage the capabilities of Large Language Models (LLMs) for this combinatorial challenge. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors propose a novel approach that utilizes LLMs for DSM modularization, building on previous research that applied LLMs to DSM sequencing. The method involves partitioning system elements into cohesive modules using three different backbone LLMs. The training process is conducted over 30 iterations, achieving near-reference quality without the need for specialized optimization code. The authors introduce the "semantic-alignment hypothesis," which posits that the effectiveness of domain knowledge in LLMs is contingent upon the alignment between the model's functional priors and the structural optimization objectives. The paper includes ablation studies to determine optimal input representations, objective formulations, and solution pool designs for practical applications.

**Results**  
The proposed LLM-based modularization method demonstrates significant performance improvements over traditional graph-based approaches. The authors report achieving near-reference quality in modularization tasks across five case studies, although specific numerical results and comparisons to named baselines are not detailed in the abstract. The findings suggest that while domain knowledge can enhance performance in simpler DSMs, it may hinder outcomes in more complex scenarios due to semantic misalignment.

**Limitations**  
The authors acknowledge that the reliance on LLMs may introduce challenges related to semantic misalignment, particularly in complex DSMs where domain knowledge does not translate effectively into the optimization objectives. They do not address potential scalability issues or the computational costs associated with deploying LLMs in large-scale engineering design tasks. Additionally, the paper does not provide extensive empirical validation across diverse engineering domains, which may limit the generalizability of the findings.

**Why it matters**  
This research has significant implications for the integration of LLMs in engineering design optimization, particularly in modularization tasks where traditional methods fall short. By establishing a framework that leverages LLMs, the study opens avenues for more context-aware and efficient design processes. The introduction of the semantic-alignment hypothesis provides a new lens through which to evaluate the effectiveness of knowledge integration in LLM applications, potentially guiding future research in both LLM development and engineering design methodologies.

Authors: Shuo Jiang, Jianxi Luo  
Source: arXiv:2604.28018  
URL: [https://arxiv.org/abs/2604.28018v1](https://arxiv.org/abs/2604.28018v1)
