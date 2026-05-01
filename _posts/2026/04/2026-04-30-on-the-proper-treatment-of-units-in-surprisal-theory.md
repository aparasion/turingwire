---
title: "On the Proper Treatment of Units in Surprisal Theory"
date: 2026-04-30 17:33:58 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.28147v1"
arxiv_id: "2604.28147"
authors: ["Samuel Kiegeland", "V\u00e9steinn Sn\u00e6bjarnarson", "Tim Vieira", "Ryan Cotterell"]
slug: on-the-proper-treatment-of-units-in-surprisal-theory
summary_word_count: 417
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the empirical application of surprisal theory within computational linguistics. Specifically, it critiques the common practice of using linguistically motivated units (e.g., words) for experimental stimuli while relying on pretrained language models that operate on a fixed token alphabet. This misalignment leads to conflated modeling choices regarding the definition of the unit of analysis and the regions of interest for predictions. The authors argue that this lack of clarity undermines the validity of surprisal-based predictors and calls for a more rigorous treatment of units in this context.

**Method**  
The authors propose a unified framework that disentangles the choices of unit definition and regions of interest in surprisal analysis. They introduce a formalism that allows for the specification of arbitrary unit inventories, enabling researchers to explicitly define the units of analysis in their models. The framework emphasizes that tokenization should be treated as an implementation detail rather than a fundamental aspect of the scientific inquiry into surprisal. The paper does not disclose specific architectures, loss functions, or training compute, as it primarily focuses on theoretical contributions rather than empirical implementations.

**Results**  
The paper does not present empirical results or quantitative comparisons against named baselines, as it is primarily a theoretical exploration. Instead, it provides a conceptual foundation for future empirical work that could leverage the proposed framework. The authors suggest that by clarifying the treatment of units, subsequent studies can yield more reliable and interpretable results in the context of surprisal theory.

**Limitations**  
The authors acknowledge that their framework is primarily theoretical and does not include empirical validation or case studies demonstrating its application. They do not address potential challenges in implementing the framework in existing models or the computational implications of adopting a more flexible unit inventory. Additionally, the paper does not explore how this framework might interact with various language modeling paradigms or the implications for models trained on different tokenization schemes.

**Why it matters**  
This work has significant implications for downstream research in computational linguistics and psycholinguistics. By providing a clearer framework for the treatment of units in surprisal theory, it encourages more rigorous experimental designs and analyses. This clarity can lead to improved understanding of human language processing and the development of more effective language models. Furthermore, it opens avenues for future research to empirically validate the proposed framework, potentially leading to advancements in how language models are evaluated and applied in real-world tasks.

Authors: Samuel Kiegeland, Vésteinn Snæbjarnarson, Tim Vieira, Ryan Cotterell  
Source: arXiv:2604.28147  
URL: https://arxiv.org/abs/2604.28147v1
