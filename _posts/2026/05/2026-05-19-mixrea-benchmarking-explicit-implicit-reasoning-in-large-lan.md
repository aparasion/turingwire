---
title: "MixRea: Benchmarking Explicit-Implicit Reasoning in Large Language Models"
date: 2026-05-19 17:15:08 +0000
category: research
subcategory: reasoning
company: "Cognition"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.20128v1"
arxiv_id: "2605.20128"
authors: ["Yuanqing Cai", "Ziyi Huang", "Minhao Liu", "Lixin Duan", "Wen Li", "Yanru Zhang"]
slug: mixrea-benchmarking-explicit-implicit-reasoning-in-large-lan
summary_word_count: 378
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the understanding of how large language models (LLMs) process contextual cues, particularly in high-stakes decision-making scenarios. The authors explore the phenomenon of inattentional blindness, where LLMs may overlook subtle yet critical contextual information despite explicit task instructions. This work is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The authors introduce a novel benchmark called MixRea, consisting of 2,246 multiple-choice questions categorized into nine distinct reasoning types. These questions are designed to assess explicit-implicit reasoning capabilities, focusing on the distribution of explicit and implicit information. The evaluation involves 21 advanced LLMs, including the top performer, Gemini 2.5 Pro. To address the identified limitations in reasoning, the authors propose a new prompting technique termed Potential Relation Completion Prompting (PRCP). This method aims to enhance model performance by recovering overlooked causal relationships in the reasoning process.

**Results**  
The evaluation reveals that even the best-performing model, Gemini 2.5 Pro, achieves only 42.8% consistency on the MixRea benchmark, indicating a significant prevalence of inattentional blindness across the tested models. This performance is notably low, suggesting that current LLMs struggle with tasks requiring nuanced understanding of context. The results highlight the inadequacy of existing models in handling explicit-implicit reasoning, with implications for their deployment in critical applications.

**Limitations**  
The authors acknowledge that their findings are limited to the specific reasoning tasks included in the MixRea benchmark and may not generalize to all forms of reasoning or other LLM architectures. They also note that the benchmark's design may not capture all dimensions of inattentional blindness. An additional limitation is the reliance on a single prompting strategy (PRCP) without extensive exploration of alternative methods that could further enhance reasoning capabilities.

**Why it matters**  
This research has significant implications for the development of more cognitively aligned LLMs that can better handle complex reasoning tasks. By identifying the limitations of current models in attending to critical contextual cues, the work underscores the necessity for improved training methodologies and architectures that incorporate cognitive principles. The findings may inform future research directions aimed at enhancing LLM performance in high-stakes environments, ultimately contributing to safer and more reliable AI systems.

Authors: Yuanqing Cai, Ziyi Huang, Minhao Liu, Lixin Duan, Wen Li, Yanru Zhang  
Source: arXiv:2605.20128v1  
URL: https://arxiv.org/abs/2605.20128v1
