---
title: "EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation"
date: 2026-05-14 17:59:55 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.15199v1"
arxiv_id: "2605.15199"
authors: ["Ruozhen He", "Meng Wei", "Ziyan Yang", "Vicente Ordonez"]
slug: entitybench-towards-entity-consistent-long-range-multi-shot-
summary_word_count: 435
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of maintaining entity consistency across long-range multi-shot video generation, a gap in the current literature that has not been adequately explored. Existing benchmarks often utilize independently generated prompt sets with limited entity coverage and simplistic consistency metrics, hindering standardized comparisons. The authors present EntityBench, a comprehensive benchmark designed to evaluate entity consistency across multiple shots in video generation, which is currently unreviewed and available as a preprint.

**Method**  
The core technical contribution is the introduction of EntityBench, which consists of 140 episodes comprising 2,491 shots derived from real narrative media. The benchmark features explicit per-shot entity schedules that track characters, objects, and locations across varying difficulty tiers (easy, medium, hard) with up to 50 shots, 13 cross-shot characters, 8 cross-shot locations, and 22 cross-shot objects, including recurrence gaps of up to 48 shots. The evaluation suite is structured around three pillars: intra-shot quality, prompt-following alignment, and cross-shot consistency, with a fidelity gate that ensures only accurate entity appearances contribute to cross-shot scoring. The authors also propose EntityMem, a memory-augmented generation system that utilizes a persistent memory bank to store verified visual references for each entity prior to generation, enhancing the coherence of generated narratives.

**Results**  
The experiments reveal that existing methods exhibit a significant degradation in cross-shot entity consistency as the recurrence distance increases. In contrast, EntityMem demonstrates superior performance, achieving the highest character fidelity with a Cohen's d effect size of +2.33 compared to other evaluated methods. This indicates a substantial improvement in maintaining character presence across shots, underscoring the effectiveness of the memory-augmented approach.

**Limitations**  
The authors acknowledge that while EntityBench provides a structured framework for evaluating entity consistency, it may not encompass all possible narrative complexities found in real-world scenarios. Additionally, the benchmark's reliance on specific narrative media may limit its generalizability to other contexts. The paper does not address potential computational overhead introduced by the memory-augmented approach, which could impact scalability in real-time applications.

**Why it matters**  
The introduction of EntityBench and the EntityMem system has significant implications for the field of video generation. By providing a standardized benchmark for evaluating entity consistency, this work facilitates more rigorous comparisons between different generation methods. The findings highlight the importance of memory mechanisms in enhancing narrative coherence, paving the way for future research to explore advanced memory architectures and their applications in multi-shot video generation. This work sets a foundation for further investigations into long-range dependencies in generative models, potentially influencing the design of future architectures aimed at improving narrative consistency in AI-generated content.

Authors: Ruozhen He, Meng Wei, Ziyan Yang, Vicente Ordonez  
Source: arXiv:2605.15199  
URL: https://arxiv.org/abs/2605.15199v1
