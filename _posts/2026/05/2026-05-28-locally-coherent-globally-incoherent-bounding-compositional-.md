---
title: "Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents"
date: 2026-05-28 17:58:55 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30335v1"
arxiv_id: "2605.30335"
authors: ["Anany Kotawala"]
slug: locally-coherent-globally-incoherent-bounding-compositional-
summary_word_count: 467
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the compositional coherence of multi-component large language model (LLM) agents. Specifically, it highlights the phenomenon where components of an LLM agent, while locally coherent, can produce globally incoherent outputs that violate fundamental probability axioms. The authors formalize this issue through the concept of compositional residual \( \epsilon^* \), which quantifies the deviation of the composed output from a joint coherent polytope. This work is crucial as it provides a theoretical framework for diagnosing and mitigating incoherence in multi-LLM systems, which is a significant concern in the deployment of ensemble models.

**Method**  
The authors introduce a formalism for measuring compositional incoherence using the L2 distance \( \epsilon^* \) from the composed output to the joint coherent polytope, which can be computed at runtime based on system outputs and cross-component coupling constraints. They establish a product-structure dichotomy that delineates conditions under which local coherence is sufficient for global coherence. A Rayleigh-quotient prediction is proposed to estimate \( \epsilon^* \), achieving a match within 7% across three of four relation classes. To address the incoherence, they propose a hierarchical Boyle-Dykstra projection that deterministically repairs the composition. Additionally, they introduce an anytime-valid e-process for sequential coherence monitoring. The empirical evaluation involves 1,876 ensemble cliques from a four-LLM mid-tier panel, assessing the performance of the proposed methods against the baseline incoherence.

**Results**  
The findings reveal that \( \epsilon^* > 0 \) is observed in 33-94% of cliques, indicating significant compositional incoherence across the evaluated ensembles. This incoherence translates to an average regret of +0.115 nats per bet on 1,770 resolved bets under the proportional allocation rule. Notably, this gain diminishes to +0.006 when considering bettors that themselves apply coherence strategies. The authors also evaluate three intuitive mitigation strategies—retrieval, partition-aware prompting, and aggregator-LLM—each of which fails to improve coherence or results in regression.

**Limitations**  
The authors acknowledge that their approach relies on the assumption of accurate cross-component coupling constraints, which may not always hold in practice. Additionally, the empirical results are limited to a specific set of LLM configurations and may not generalize to other architectures or larger-scale systems. The reliance on L2 distance as a measure of incoherence may also overlook other forms of compositional errors that could be relevant in different contexts.

**Why it matters**  
This work has significant implications for the design and deployment of multi-component LLM systems. By formalizing the concept of compositional incoherence and providing methods for its quantification and mitigation, it lays the groundwork for future research aimed at enhancing the reliability and coherence of ensemble models. The insights gained from this study can inform the development of more robust LLM architectures and improve the interpretability of their outputs, which is critical for applications in sensitive domains such as healthcare and finance.

Authors: Anany Kotawala  
Source: arXiv:2605.30335  
URL: https://arxiv.org/abs/2605.30335v1
