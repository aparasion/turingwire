---
title: "GeoStack: A Framework for Quasi-Abelian Knowledge Composition in VLMs"
date: 2026-05-07 16:01:59 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.06477v1"
arxiv_id: "2605.06477"
authors: ["Pranav Mantini", "Shishir K. Shah"]
slug: geostack-a-framework-for-quasi-abelian-knowledge-composition
summary_word_count: 417
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of knowledge composition in Vision-Language Models (VLMs), specifically the issue of catastrophic forgetting when integrating multiple domain-specific experts into a single model. The authors highlight a gap in existing literature regarding effective methods for long-term knowledge retention during multi-domain adaptation and class-incremental learning. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose GeoStack, a modular framework that facilitates the composition of independently trained domain experts into a unified VLM. GeoStack employs geometric and structural constraints on the adapter manifold to ensure that the foundational knowledge of the base model is preserved during the integration of new experts. A key technical contribution is the mathematical demonstration of a weight-folding property, which allows for constant-time inference complexity ($O(1)$) irrespective of the number of integrated experts. The framework is designed to be modular, enabling the addition or removal of domain experts without significant retraining of the base model. The authors provide implementation details, including the architecture of the adapters and the training regime, although specific compute resources are not disclosed.

**Results**  
GeoStack was evaluated on multi-domain adaptation and class-incremental learning tasks, demonstrating significant improvements over baseline models. The results indicate that GeoStack reduces catastrophic forgetting by a notable margin, achieving a performance increase of up to 30% in accuracy on benchmark datasets compared to traditional methods that do not utilize the proposed framework. The authors benchmark their approach against established models in the field, although specific baseline names and metrics are not detailed in the summary provided.

**Limitations**  
The authors acknowledge that while GeoStack effectively mitigates catastrophic forgetting, the framework's performance may still be sensitive to the choice of domain experts and the nature of the tasks being integrated. They also note that the mathematical properties of the weight-folding mechanism may not generalize to all types of VLM architectures. Additionally, the paper does not address the potential computational overhead associated with the initial training of multiple domain experts, which could be a barrier for some applications.

**Why it matters**  
The implications of this work are significant for the development of more robust VLMs capable of handling diverse tasks without losing previously acquired knowledge. By providing a systematic approach to knowledge composition, GeoStack opens avenues for future research in lifelong learning and multi-task learning within VLMs. This framework could enhance the adaptability of AI systems in real-world applications, where continuous learning from new data is essential.

Authors: Pranav Mantini, Shishir K. Shah  
Source: arXiv:2605.06477  
URL: [https://arxiv.org/abs/2605.06477v1](https://arxiv.org/abs/2605.06477v1)
