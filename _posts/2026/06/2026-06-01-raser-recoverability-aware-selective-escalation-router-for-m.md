---
title: "RASER: Recoverability-Aware Selective Escalation Router for Multi-Hop Question Answering"
date: 2026-06-01 16:59:36 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02488v1"
arxiv_id: "2606.02488"
authors: ["Yuyang Li", "Zihe Yan", "Tobias K\u00e4fer"]
slug: raser-recoverability-aware-selective-escalation-router-for-m
summary_word_count: 395
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper presents RASER, a cost-effective routing mechanism for multi-hop question answering that optimizes retrieval actions based on recoverability."
---

**Problem**  
Multi-hop question-answering (QA) systems typically incur high computational costs due to repeated retrieval actions for each question, often relying on large language models (LLMs) to decompose queries. This paper addresses the inefficiency of these methods, particularly when many multi-hop questions can be answered correctly with a single retrieval action. The authors highlight that existing literature does not adequately explore selective escalation strategies that minimize unnecessary retrievals, especially under tight LLM token budgets. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors introduce RASER (Recoverability-Aware Selective Escalation Router), which comprises two variants: RASER-2 and RASER-3. RASER-2 employs a binary decision-making process to either stop further retrieval or escalate to an additional retrieval action termed PRUNE. RASER-3 extends this by selecting among three options: one-shot retrieval using RAG (Retrieval-Augmented Generation), PRUNE, and iterative retrieval (IRCoT). Both routers utilize six features derived from the one-shot RAG framework to inform their decisions, but notably, neither variant requires additional LLM calls for decision-making. The training compute details are not disclosed, but the focus is on optimizing retrieval efficiency while maintaining competitive performance.

**Results**  
The performance of RASER-2 and RASER-3 is evaluated across six LLMs and three multi-hop QA benchmarks. Both routers achieve competitive F1 scores compared to state-of-the-art (SOTA) baselines while utilizing only 41-49% of the tokens consumed by the always-prune strategy. This demonstrates a significant reduction in token usage without sacrificing accuracy, indicating that RASER effectively balances cost and performance in multi-hop QA tasks.

**Limitations**  
The authors acknowledge that RASER's performance may vary depending on the specific characteristics of the multi-hop questions and the underlying LLMs used. They do not address potential limitations related to the generalizability of the feature set across different domains or the scalability of the approach to larger datasets. Additionally, the reliance on a single-shot retrieval mechanism may not be optimal for all question types, particularly those requiring deeper contextual understanding.

**Why it matters**  
The introduction of RASER has significant implications for the design of efficient multi-hop QA systems, particularly in resource-constrained environments. By reducing the reliance on expensive retrieval actions, RASER can facilitate the deployment of multi-hop QA in applications where computational resources are limited. This work contributes to the ongoing discourse on optimizing LLM usage in practical applications, as discussed in related literature on retrieval strategies and efficiency in AI systems, as published in [arXiv](https://arxiv.org/abs/2606.02488v1).
