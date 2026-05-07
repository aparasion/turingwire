---
title: "Self-Attention as Transport: Limits of Symmetric Spectral Diagnostics"
date: 2026-05-06 13:25:13 +0000
category: research
subcategory: interpretability
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.04893v1"
arxiv_id: "2605.04893"
authors: ["Dominik Dahlem", "Diego Maniloff", "Mac Misiura"]
slug: self-attention-as-transport-limits-of-symmetric-spectral-dia
summary_word_count: 451
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing spectral methods used to analyze attention mechanisms in large language models (LLMs). Specifically, it highlights that traditional symmetric spectral diagnostics of the degree-normalized attention operator are orientation-blind, meaning they cannot discern the directionality of information flow within the model. This gap in capability limits the understanding of how attention mechanisms contribute to model performance and failure modes, particularly in the context of hallucinations in LLMs.

**Method**  
The authors introduce a novel framework that combines spectral analysis with a bipartite-Cheeger landscape tailored for canonical causal architectures. They establish that the asymmetry coefficient \( G \) serves as the unique control parameter for detecting information flow direction. The study evaluates two types of attention mechanisms: uniform causal attention and window attention. The authors derive a closed-form expression for the transport capacity of these mechanisms, demonstrating that uniform causal attention maintains a floor of \( φ \ge 1/5 \) with a worst cut at \( t^\ast/n \approx 0.32 \), while window attention exhibits a diminishing capacity of \( O(w/n) \). The proposed two-axis diagnostic framework utilizes \( φ \) for capacity and \( G \) for directionality, allowing for falsifiable predictions regarding the polarity of attention mechanisms.

**Results**  
The authors report significant findings from their evaluations on models with up to 8 billion parameters. The transport features yield interpretable signals, with the length-controlled evaluation achieving a LC-AUROC improvement from 0.62 to 0.84. The polarity predictions are validated through comparative analysis between benchmarks: HaluEval and MedHallu, where the polarity reverses as anticipated. This indicates that models exhibiting bottleneck-dominated attention and diffuse-dominated attention demonstrate opposite polarity in their performance metrics.

**Limitations**  
The authors acknowledge that their approach is limited to the analysis of causal architectures and may not generalize to other model types. Additionally, the reliance on specific benchmarks (HaluEval and MedHallu) may restrict the applicability of their findings across diverse datasets and tasks. The study does not explore the implications of varying model sizes beyond 8 billion parameters, which could affect the generalizability of the results. Furthermore, the focus on spectral diagnostics may overlook other critical factors influencing attention behavior.

**Why it matters**  
This work has significant implications for the understanding and diagnosis of attention mechanisms in LLMs. By establishing a framework that can differentiate between the directionality of information flow and transport capacity, it provides a more nuanced approach to analyzing model behavior. The findings could inform the design of more robust attention mechanisms and contribute to the development of models that mitigate hallucination issues. Furthermore, the proposed diagnostics could serve as a foundation for future research aimed at enhancing interpretability and performance in LLMs.

Authors: Dominik Dahlem, Diego Maniloff, Mac Misiura  
Source: arXiv:2605.04893  
URL: https://arxiv.org/abs/2605.04893v1
