---
title: "A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents"
date: 2026-05-19 17:54:21 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.20173v1"
arxiv_id: "2605.20173"
authors: ["Vasundra Srinivasan"]
slug: a-methodology-for-selecting-and-composing-runtime-architectu
summary_word_count: 453
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the architectural design of production-level LLM (Large Language Model) agents, specifically the integration of stochastic model outputs with deterministic software systems. The authors introduce the concept of the stochastic-deterministic boundary (SDB) as a critical architectural element that governs how LLM outputs translate into system actions. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is a structured methodology for selecting and composing runtime architecture patterns around the SDB. The authors categorize agent runtime design into three primary concerns: Coordination, State, and Control. They present a catalog of six distinct runtime patterns—hierarchical delegation, scatter-gather plus saga, event-driven sequencing, shared state machine, supervisor plus gate, and human in the loop—each tailored for different types of agents (conversational, autonomous, long-horizon). The paper traces the lineage of these patterns to established distributed-systems concepts while highlighting the implications of stochastic workers. Additionally, the authors propose a five-step methodology for selecting appropriate runtime patterns, a diagnostic procedure for mapping production failures to specific pattern weaknesses, and introduce the failure mode of replay divergence, which occurs when LLM consumers of deterministic logs yield inconsistent outputs due to model-version or prompt variations. A reliability decomposition is also provided, distinguishing between model variance and architectural momentum, emphasizing the importance of SDB strength and pattern choice as model variance diminishes.

**Results**  
The methodology is applied to five distinct workloads, demonstrating its practical utility. The authors provide a runnable reference implementation for a 90-day contract-renewal agent, although specific quantitative results (e.g., performance metrics, error rates) against named baselines are not detailed in the abstract. The implications of the proposed patterns and methodology suggest a potential for improved reliability in production LLM systems, particularly as model variance decreases.

**Limitations**  
The authors acknowledge that the proposed patterns and methodology may not cover all possible scenarios in production environments, particularly those involving highly dynamic or unpredictable contexts. They do not address the computational overhead introduced by the additional architectural complexity or the potential trade-offs in performance versus reliability. Furthermore, the reliance on specific workloads for validation may limit the generalizability of the findings.

**Why it matters**  
This work has significant implications for the design and deployment of LLM agents in production settings. By formalizing the SDB and providing a structured approach to runtime architecture, the paper lays the groundwork for more reliable and robust LLM applications. The introduction of a diagnostic framework for identifying failure modes can enhance the resilience of these systems, making them more suitable for critical applications. This research could inform future studies on hybrid systems that integrate stochastic models with deterministic processes, ultimately advancing the field of AI-driven automation.

Authors: Vasundra Srinivasan  
Source: arXiv:2605.20173v1  
URL: https://arxiv.org/abs/2605.20173v1
