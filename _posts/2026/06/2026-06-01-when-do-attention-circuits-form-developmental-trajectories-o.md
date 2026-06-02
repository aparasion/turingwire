---
title: "When Do Attention Circuits Form? Developmental Trajectories of Capability and Attention-Sink Emergence Across Three 1B-ClassArchitectures"
date: 2026-06-01 15:26:23 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.02378v1"
arxiv_id: "2606.02378"
authors: ["Yongzhong Xu"]
slug: when-do-attention-circuits-form-developmental-trajectories-o
summary_word_count: 424
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper investigates the developmental trajectories of attention-head circuits in 1B-class language models, revealing distinct patterns of emergence and capability formation."
---

**Problem**  
This work addresses the gap in understanding the developmental trajectories of attention-head circuits in large language models, specifically focusing on the formation of attention mechanisms across different architectures and pretraining corpora. The authors highlight that existing literature lacks a comprehensive analysis of how attention circuits emerge during training, particularly in 1B-class models. This preprint is unreviewed, indicating that the findings are preliminary and subject to further validation.

**Method**  
The authors analyze three 1B-class language models: Pythia 1B, OLMo 1B-0724-hf, and OLMoE 1B-7B-0924, which represent two architecture families (dense transformer and mixture-of-experts) and two pretraining datasets (The Pile and DCLM). They conduct 30 mechanistic-interpretability runs, applying a participation-ratio (PR) spectral signal and a capability-specific selectivity screen to track the emergence of induction, previous-token, and BOS-attractor heads across 10 log-spaced revisions per model. The study identifies five key findings regarding the emergence patterns of these attention circuits.

**Results**  
The findings reveal several significant patterns:  
- **F1**: Layers 0 and 1 consistently produce zero BOS-classified heads across all revisions and models, indicating this is an architectural property rather than a learned behavior.  
- **F2**: The emergence of the whole-model BOS-attractor fraction varies: Pythia 1B shows a gradual ramp, OLMo 1B exhibits a sharp phase transition (from 7% to 70% between adjacent checkpoints), and OLMoE 1B-7B follows a gradual ramp.  
- **F3**: In DCLM models, induction-circuit formation occurs 10-20 times earlier than BOS-attractor formation, suggesting that these transitions are distinct rather than simultaneous.  
- **F4**: The capability-specific screen converges to the final induction circuit within 0.3-2% of total training tokens, indicating that circuit identification can occur before the model reaches its final state.  
- **F5**: For every final-checkpoint induction head sampled, the per-head PR is elevated at or before the first revision where the head crosses its capability-selectivity threshold.

**Limitations**  
The authors note that their findings are based on a limited set of models and pretraining datasets, which may not generalize to all architectures or training regimes. Additionally, the study does not explore the implications of these findings on downstream tasks or the potential for transfer learning. The lack of peer review also raises questions about the robustness of the conclusions.

**Why it matters**  
Understanding the developmental trajectories of attention circuits is crucial for advancing the interpretability and efficiency of large language models. The distinct emergence patterns identified in this study could inform future model designs and training strategies, particularly in optimizing attention mechanisms. This work contributes to the broader discourse on model interpretability and capability development, as discussed in related literature (as published in [arXiv cs.LG](https://arxiv.org/abs/2606.02378v1)).
