---
title: "MEME: Multi-entity & Evolving Memory Evaluation"
date: 2026-05-12 17:55:10 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12477v1"
arxiv_id: "2605.12477"
authors: ["Seokwon Jung", "Alexander Rubinstein", "Arnas Uselis", "Sangdoo Yun", "Seong Joon Oh"]
slug: meme-multi-entity-evolving-memory-evaluation
summary_word_count: 485
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing benchmarks for evaluating memory systems in large language model (LLM)-based agents, particularly in persistent environments where agents must manage multi-entity information over time. Prior work has primarily focused on single-entity updates, neglecting complex scenarios involving dependency reasoning and the evolution of memory states. The authors introduce the MEME benchmark, which includes six tasks that span multi-entity and evolving memory capabilities, with a specific focus on Cascade, Absence, and Deletion tasks that have not been previously evaluated. This work is presented as a preprint and has not undergone peer review.

**Method**  
The MEME benchmark consists of six distinct tasks designed to evaluate memory systems across three paradigms: static retrieval, dynamic updates, and evolving memory states. The authors assess six different memory systems over 100 controlled episodes. The evaluation metrics focus on accuracy in handling dependency reasoning tasks, specifically measuring performance in Cascade (3% average accuracy) and Absence (1% average accuracy) tasks. The authors explore various configurations, including prompt optimization, deeper retrieval mechanisms, and reduced filler noise, to enhance performance. Notably, they identify that only a file-based agent utilizing Claude Opus 4.7 as its internal LLM shows partial improvement, albeit at a significantly higher computational cost (~70x the baseline).

**Results**  
The results indicate a stark performance drop in dependency reasoning tasks across all evaluated memory systems, with average accuracies of 3% for Cascade and 1% for Absence tasks. In contrast, static retrieval performance remains adequate, suggesting a disconnect between static and dynamic memory capabilities. The authors highlight that even advanced configurations and stronger LLMs fail to bridge this performance gap, underscoring the challenges in evolving memory management. The file-based agent with Claude Opus 4.7 demonstrates some improvement, but the cost implications render it impractical for large-scale applications.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a controlled environment that may not fully capture the complexities of real-world applications. They also note that the performance improvements observed with the file-based agent come at a prohibitive computational cost, which may hinder practical deployment. Additionally, the benchmark does not account for the potential impact of different LLM architectures or training methodologies on memory performance, which could be explored in future work. The tasks defined in MEME may also require further refinement to better align with real-world scenarios.

**Why it matters**  
The introduction of the MEME benchmark is significant for advancing the evaluation of memory systems in LLM-based agents, particularly in applications requiring persistent memory management. By highlighting the inadequacies of current benchmarks and demonstrating the challenges in dependency reasoning, this work lays the groundwork for future research aimed at developing more robust memory architectures. The findings emphasize the need for innovative solutions that can effectively manage multi-entity information in evolving contexts, which is crucial for the deployment of LLMs in complex, real-world environments.

Authors: Seokwon Jung, Alexander Rubinstein, Arnas Uselis, Sangdoo Yun, Seong Joon Oh  
Source: arXiv cs.LG  
URL: https://arxiv.org/abs/2605.12477v1
