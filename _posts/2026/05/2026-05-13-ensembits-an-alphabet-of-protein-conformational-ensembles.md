---
title: "ENSEMBITS: an alphabet of protein conformational ensembles"
date: 2026-05-13 17:08:41 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13789v1"
arxiv_id: "2605.13789"
authors: ["Kaiwen Shi", "Carlos Oliver"]
slug: ensembits-an-alphabet-of-protein-conformational-ensembles
summary_word_count: 390
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in protein structure tokenization by introducing Ensembits, the first tokenizer specifically designed for protein conformational ensembles. Existing protein structure tokenizers (PSTs) primarily focus on static structures and fail to capture the dynamics and correlated motions inherent in protein ensembles. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Ensembits employs a Residual Vector Quantized Variational Autoencoder (VQ-VAE) architecture, utilizing a frame distillation objective to derive informative geometric descriptors from a large corpus of molecular dynamics simulations. The method tackles several challenges: it encodes variable-size ensembles with permutation invariance, addresses sparsity in dynamics data, and generates a discrete vocabulary for protein dynamics. The training process leverages a substantial dataset of molecular dynamics trajectories, allowing the model to learn effective representations of protein conformational states.

**Results**  
Ensembits demonstrates superior performance on several benchmarks compared to existing methods. It achieves state-of-the-art results in Root Mean Square Fluctuation (RMSF) prediction, outperforming all related methods. In a token-conditioned ANOVA test assessing per-residue motion amplitude, Ensembits is the strongest standalone structural tokenizer. Furthermore, it matches or exceeds the performance of static tokenizers in tasks such as enzyme commission (EC) prediction, Gene Ontology (GO) classification, binding site/affinity prediction, and zero-shot mutation-effect prediction, all while utilizing significantly less pretraining data. The distillation objective allows Ensembits to predict dynamics tokens from a single predicted structure, effectively mitigating the issue of data sparsity in dynamics.

**Limitations**  
The authors acknowledge that Ensembits, while effective, is still a preprint and has not been validated through peer review. Additionally, the reliance on a large molecular dynamics corpus may limit its applicability to systems with less available data. The model's performance in highly complex or atypical protein systems remains to be evaluated, and the generalizability of the learned representations across diverse protein families is not fully explored.

**Why it matters**  
The introduction of Ensembits marks a significant advancement in the field of protein language modeling by integrating dynamics into the tokenization process. As the focus shifts from static structure prediction to ensemble generation, Ensembits provides a necessary framework for incorporating dynamic information into protein design and function prediction. This work has implications for enhancing the accuracy of predictive models in computational biology and could facilitate more effective drug design and protein engineering efforts.

Authors: Kaiwen Shi, Carlos Oliver  
Source: arXiv:2605.13789  
URL: [https://arxiv.org/abs/2605.13789v1](https://arxiv.org/abs/2605.13789v1)
