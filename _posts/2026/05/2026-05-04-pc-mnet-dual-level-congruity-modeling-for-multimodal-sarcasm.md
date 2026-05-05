---
title: "PC-MNet: Dual-Level Congruity Modeling for Multimodal Sarcasm Detection via Polarity-Modulated Attention"
date: 2026-05-04 10:47:17 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02447v1"
arxiv_id: "2605.02447"
authors: ["Maoheng Li", "Ling Zhou", "Xiaohua Huang", "Rubing Huang", "Wenming Zheng", "Guoying Zhao"]
slug: pc-mnet-dual-level-congruity-modeling-for-multimodal-sarcasm
summary_word_count: 390
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in multimodal sarcasm detection, specifically the limitations of existing methods that rely on simplistic similarity-based attention mechanisms and uniform late fusion strategies. The authors highlight that traditional late fusion approaches suffer from functional entanglement, which restricts their effectiveness in capturing the nuanced incongruities between verbal and nonverbal cues. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose PC-MNet, a novel architecture that employs a dual-level congruity modeling approach. The core technical contribution includes a scalar congruity routing mechanism and a prior-guided contextual graph, which together facilitate the identification of incongruities in a more structured manner. The model operates through a two-stage asymmetric optimization process driven by inconsistency-aware contrastive learning. This allows for selective fusion of the most discriminative multi-granularity evidence, effectively isolating atomic, composition, and contextual conflicts. The training process and compute requirements are not explicitly detailed in the paper.

**Results**  
PC-MNet achieves state-of-the-art performance on the MUStARD benchmark, surpassing the strongest multimodal baseline by 3.14% in Macro-F1 score. The authors provide extensive experimental results that demonstrate the effectiveness of their approach across various configurations and datasets, including those designed to mitigate spurious correlations. The results indicate a significant improvement in the model's ability to detect sarcasm compared to previous methods, showcasing the advantages of their dual-level congruity modeling.

**Limitations**  
The authors acknowledge that their approach may still be limited by the quality and diversity of the training data, as well as the inherent challenges in modeling sarcasm, which can be context-dependent and culturally nuanced. They do not address potential scalability issues or the computational overhead introduced by the dual-level modeling, which may affect real-time applications. Additionally, the reliance on a specific benchmark (MUStARD) raises questions about generalizability to other datasets or real-world scenarios.

**Why it matters**  
This work has significant implications for downstream applications in natural language processing and multimodal understanding, particularly in enhancing the robustness of sarcasm detection systems. By providing a decoupled paradigm for modeling pragmatic incongruities, PC-MNet could improve the performance of conversational agents, sentiment analysis tools, and social media monitoring systems. The introduction of inconsistency-aware contrastive learning may also inspire future research into more sophisticated attention mechanisms and fusion strategies in multimodal contexts.

Authors: Maoheng Li, Ling Zhou, Xiaohua Huang, Rubing Huang, Wenming Zheng, Guoying Zhao  
Source: arXiv:2605.02447  
URL: [https://arxiv.org/abs/2605.02447v1](https://arxiv.org/abs/2605.02447v1)
