---
title: "Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention"
date: 2026-05-21 17:44:57 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22791v1"
arxiv_id: "2605.22791"
authors: ["Ali Hatamizadeh", "Yejin Choi", "Jan Kautz"]
slug: gated-deltanet-2-decoupling-erase-and-write-in-linear-attent
summary_word_count: 455
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing linear attention mechanisms, specifically the challenge of effectively managing memory updates in a way that allows for both erasure and writing of information without compromising the integrity of existing data associations. Previous models, such as Gated DeltaNet and Kimi Delta Attention (KDA), utilize a single scalar gate to control both erasure and writing, which can lead to suboptimal performance. This work presents Gated DeltaNet-2, which separates these functions to enhance memory editing capabilities. The paper is a preprint and has not yet undergone peer review.

**Method**  
Gated DeltaNet-2 introduces a novel architecture that decouples the erase and write operations through the use of two distinct channel-wise gates: an erase gate \( b_t \) and a write gate \( w_t \). This design allows for more flexible and adaptive memory management. The model builds on the principles of adaptive forgetting and channel-wise decay from KDA while addressing the limitations of scalar gating. The authors derive a fast-weight update mechanism and a chunkwise WY algorithm that incorporates channel-wise decay into asymmetric erase factors. The training process is optimized with a gate-aware backward pass, ensuring efficient parallelization. The model is implemented with 1.3 billion parameters and trained on 100 billion tokens from the FineWeb-Edu dataset.

**Results**  
Gated DeltaNet-2 demonstrates superior performance across several benchmarks, including language modeling, commonsense reasoning, and retrieval tasks. It outperforms its predecessors—Mamba-2, Gated DeltaNet, KDA, and Mamba-3—achieving the best overall results. Notably, on the long-context RULER needle-in-a-haystack benchmarks, Gated DeltaNet-2 shows significant improvements in multi-key retrieval settings, indicating its robustness in both recurrent and hybrid contexts. The paper reports effect sizes that highlight the model's advantages, although specific numerical results against named baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that while Gated DeltaNet-2 improves upon previous models, it still relies on the underlying assumptions of linear attention mechanisms, which may not generalize to all types of tasks or datasets. Additionally, the model's performance on extremely long sequences or highly variable contexts has not been exhaustively tested. The paper does not discuss potential computational overhead introduced by the additional gating mechanisms, which could impact scalability in resource-constrained environments.

**Why it matters**  
The introduction of Gated DeltaNet-2 has significant implications for the development of more efficient and effective attention mechanisms in natural language processing and other sequential data tasks. By decoupling the erase and write operations, this model paves the way for future research into adaptive memory systems that can better handle complex information retrieval and reasoning tasks. The advancements in training efficiency and memory management could lead to broader applications in areas requiring long-context understanding, such as dialogue systems and knowledge retrieval.

Authors: Ali Hatamizadeh, Yejin Choi, Jan Kautz  
Source: arXiv:2605.22791  
URL: [https://arxiv.org/abs/2605.22791v1](https://arxiv.org/abs/2605.22791v1)
