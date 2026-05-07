---
title: "UFAL-CUNI at SemEval-2026 Task 11: An Efficient Modular Neuro-symbolic Method for Syllogistic Reasoning"
date: 2026-05-06 14:10:06 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.04941v1"
arxiv_id: "2605.04941"
authors: ["Ivan Kart\u00e1\u010d", "Krist\u00fdna Onderkov\u00e1", "Jan Bronec", "Zden\u011bk Kasner", "Mateusz Lango", "Ond\u0159ej Du\u0161ek"]
slug: ufal-cuni-at-semeval-2026-task-11-an-efficient-modular-neuro
summary_word_count: 447
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of disentangling content and formal reasoning in large language models (LLMs) within the context of syllogistic reasoning, as outlined in SemEval-2026 Task 11. The authors highlight a gap in existing methodologies that effectively integrate symbolic reasoning with LLMs, particularly in achieving efficient and accurate reasoning without the extensive computational overhead typically associated with larger models. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The proposed system employs a modular neuro-symbolic architecture that integrates a symbolic prover with small LLMs (4 billion parameters). The architecture consists of several components: 
1. An LLM-based parser that converts natural language syllogisms into first-order logic (FOL) representations.
2. An automated theorem prover that processes these FOL representations to derive conclusions.
3. Two optional modules: a machine translation component for handling multilingual inputs and a symbolic retrieval module that identifies relevant premises from a knowledge base. 

The training methodology and compute resources utilized for the LLMs are not explicitly detailed, but the authors emphasize the efficiency of their approach compared to larger models.

**Results**  
The system demonstrates competitive accuracy across various subtasks in the SemEval-2026 benchmark, outperforming zero-shot baselines using LLMs of similar parameter sizes. Specific performance metrics are not disclosed in the abstract, but the authors indicate a relatively low content effect, suggesting that the system's reasoning capabilities are not heavily influenced by the specific content of the syllogisms. The ablation studies reveal that while the modular approach enhances performance, the small LLMs exhibit limited multilingual capabilities, indicating a trade-off between model size and linguistic versatility.

**Limitations**  
The authors acknowledge the limited multilingual capabilities of their small LLMs, which may restrict the system's applicability in diverse linguistic contexts. Additionally, they discuss the main ranking metric used in the task and its limitations, although specific details are not provided in the abstract. An obvious limitation not mentioned by the authors is the potential scalability of the approach; while the modular design is efficient, it may not generalize well to more complex reasoning tasks or larger datasets without further optimization.

**Why it matters**  
This work contributes to the growing field of neuro-symbolic AI by demonstrating a viable method for integrating symbolic reasoning with LLMs, particularly in the domain of syllogistic reasoning. The findings suggest that smaller models can achieve competitive performance without the computational burden of larger architectures, which has implications for resource-constrained environments. Furthermore, the modular design allows for flexibility in incorporating additional functionalities, such as multilingual support and symbolic retrieval, paving the way for future research in enhancing reasoning capabilities in LLMs.

Authors: Ivan Kartáč, Kristýna Onderková, Jan Bronec, Zdeněk Kasner, Mateusz Lango, Ondřej Dušek  
Source: arXiv:2605.04941  
URL: [https://arxiv.org/abs/2605.04941v1](https://arxiv.org/abs/2605.04941v1)
