---
title: "Sense Representations Are Inducible Interfaces"
date: 2026-05-27 16:04:35 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.28669v1"
arxiv_id: "2605.28669"
authors: ["Jan Christian Blaise Cruz", "Alham Fikri Aji"]
slug: sense-representations-are-inducible-interfaces
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitation of existing language models (LMs) that require pretraining with integrated sense structures to effectively utilize sense representations for tasks such as disambiguation and cross-lingual alignment. The authors propose a novel method, ACROS, which allows for the induction of explicit sense pathways into a frozen pretrained decoder LM, thus enabling the use of sense representations without the need for extensive retraining. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this paper is the ACROS architecture, which employs a gated residual addition mechanism to integrate sense representations into a frozen pretrained LM. This approach allows the model to maintain its original performance while enabling the induction of sense pathways. The authors utilize the SmolLM2-360M as their base model. The training process involves leveraging the existing capabilities of the pretrained LM, thus minimizing additional compute requirements. The induced sense representations are then applied in three distinct tasks: zero-shot word-sense disambiguation, low-KL lexical steering, and cross-lingual adaptation through SENSIA.

**Results**  
ACROS demonstrates competitive performance across multiple benchmarks. For zero-shot word-sense disambiguation, it achieves an F1 score of 64.95 on the Raganato ALL dataset, which is comparable to the WordNet first-sense heuristic. In the low-KL lexical steering task, ACROS shows that a simple non-oracle proxy can recover approximately 90% of positive shifts across 5,161 CoInCo cases. For cross-lingual adaptation, the model achieves a mean R@1 of 0.988 and a target FLORES perplexity (PPL) of 7.94, indicating strong performance in aligning representations across languages.

**Limitations**  
The authors acknowledge that while ACROS effectively induces sense representations, the reliance on a frozen pretrained LM may limit the adaptability of the model to certain nuanced tasks that require more dynamic adjustments. Additionally, the performance metrics, while competitive, may not fully capture the potential of sense representations in more complex linguistic scenarios. The paper does not address the scalability of the approach to larger models or its performance in low-resource languages.

**Why it matters**  
The introduction of ACROS as an inducible interface for sense representations has significant implications for the field of natural language processing (NLP). By enabling the integration of sense pathways into existing pretrained models, this work opens avenues for improved disambiguation, enhanced steering capabilities, and more effective cross-lingual applications without the need for extensive retraining. This could lead to more efficient use of computational resources and facilitate the development of more versatile NLP systems that leverage the rich semantic structures inherent in language.

Authors: Jan Christian Blaise Cruz, Alham Fikri Aji  
Source: arXiv:2605.28669  
URL: [https://arxiv.org/abs/2605.28669v1](https://arxiv.org/abs/2605.28669v1)
