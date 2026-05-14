---
title: "Dense vs Sparse Pretraining at Tiny Scale: Active-Parameter vs Total-Parameter Matching"
date: 2026-05-13 16:48:24 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13769v1"
arxiv_id: "2605.13769"
authors: ["Abdalrahman Wael"]
slug: dense-vs-sparse-pretraining-at-tiny-scale-active-parameter-v
summary_word_count: 421
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the performance trade-offs between dense and sparse transformer architectures, specifically in the context of tiny-scale pretraining. The authors investigate how mixture-of-experts (MoE) models compare to dense models when both are constrained to similar parameter budgets, focusing on active versus total parameter matching. This exploration is particularly relevant given the increasing interest in efficient model architectures for resource-constrained environments.

**Method**  
The study employs a shared LLaMA-style decoder training recipe to evaluate both dense and MoE transformers. The dense models are modified to match either the active or total parameter counts of the MoE models. The MoE architecture utilizes four experts with top-2 routing, Switch-style load balancing, and a router z-loss to optimize performance. The training setup maintains fixed conditions across tokenizer, data, optimizer, schedule, depth, context length, normalization style, and evaluation protocol. The experiments are conducted with a three-seed full-data comparison, ensuring robustness in the results.

**Results**  
The results indicate that the dense active-match model achieves a best validation loss of 1.6545 ± 0.0012, while the MoE model reaches 1.5788 ± 0.0020, and the dense total-match model achieves 1.5608 ± 0.0025. This results in a matched-active gap favoring the MoE of 0.0758 ± 0.0021 and a matched-total gap favoring the dense model of 0.0180 ± 0.0020. Notably, the matched-active advantage for the MoE increases over the course of training, while the matched-total advantage for the dense model diminishes significantly. These findings suggest that in the sub-25M-parameter regime, MoE models can outperform dense models in terms of validation loss when focusing on active parameters, but do not exceed dense models when total parameter counts are equal.

**Limitations**  
The authors acknowledge that their study is limited to a specific parameter regime (sub-25M) and may not generalize to larger models or different architectures. Additionally, the reliance on a single training recipe and fixed experimental conditions may limit the applicability of the findings across diverse datasets or tasks. The paper does not explore the computational efficiency or inference speed of the models, which are critical factors in practical applications.

**Why it matters**  
This research has significant implications for the design of efficient transformer architectures, particularly in scenarios where computational resources are limited. The findings suggest that while MoE models can provide advantages in certain configurations, dense models still hold merit in terms of total capacity. This insight can guide future work in model selection and architecture design, especially for applications in edge computing or mobile devices where parameter efficiency is paramount.

Authors: Abdalrahman Wael  
Source: arXiv:2605.13769  
URL: [https://arxiv.org/abs/2605.13769v1](https://arxiv.org/abs/2605.13769v1)
