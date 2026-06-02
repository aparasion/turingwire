---
title: "LLM-Evolved Pattern Generators for Optimal Classical Planning"
date: 2026-06-01 16:10:20 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02438v1"
arxiv_id: "2606.02438"
authors: ["Windy Phung", "Dominik Drexler", "Arnaud Lequen", "Jendrik Seipp"]
slug: llm-evolved-pattern-generators-for-optimal-classical-plannin
summary_word_count: 457
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces a novel method for learning admissible heuristics in optimal classical planning using LLM-driven evolutionary program synthesis."
---

**Problem**  
The paper addresses a significant gap in the literature regarding the development of admissible heuristics for optimal classical planning. While recent advancements in learned heuristics have improved search guidance in satisficing planning, they do not guarantee admissibility, rendering them unsuitable for optimal solutions. This work presents the first approach that ensures the learned heuristics are admissible by design, thus maintaining the optimality guarantees of A* search. The authors highlight that existing methods primarily focus on domain-independent heuristics, which lack the specificity required for optimal planning tasks.

**Method**  
The authors propose a framework that leverages large language models (LLMs) within an evolutionary program-synthesis paradigm to learn domain-dependent heuristics. Instead of directly mapping states to heuristic values, the method constructs abstractions that yield admissible heuristics. The process involves generating a program for each planning domain that produces a collection of patterns applicable to any task within that domain. These patterns are then combined using saturated cost partitioning to ensure admissibility. The framework is designed to run with negligible overhead during inference, making it efficient for practical applications. The training process and specific architectures used for the LLMs are not disclosed, but the focus on program synthesis indicates a novel integration of AI techniques with classical planning methodologies.

**Results**  
Empirical evaluations demonstrate that the proposed method achieves heuristic coverage comparable to state-of-the-art domain-independent baselines across multiple planning domains. The authors report that their learned heuristics evaluate states significantly faster than traditional methods while maintaining admissibility. Specific performance metrics, such as the speedup factor or percentage improvement over baselines, are not detailed in the abstract, but the results indicate a substantial enhancement in efficiency and effectiveness in optimal planning scenarios.

**Limitations**  
The authors acknowledge that their approach is contingent on the quality of the LLMs used for program synthesis, which may vary across different domains. Additionally, while the method is designed to be efficient, the overhead associated with the initial program generation phase is not quantified. The paper does not address potential scalability issues when applied to larger or more complex planning domains, nor does it explore the robustness of the learned heuristics in the presence of noisy or incomplete data.

**Why it matters**  
This work has significant implications for the field of AI planning, particularly in enhancing the efficiency and effectiveness of optimal planning algorithms. By ensuring that learned heuristics are admissible, the proposed method preserves the foundational guarantees of classical search algorithms like A*. This advancement could lead to more robust applications in various domains, including robotics, logistics, and automated reasoning. The integration of LLMs into the planning process also opens avenues for future research in combining deep learning with traditional AI techniques, as discussed in related works on heuristic learning and program synthesis, as published in [arXiv](https://arxiv.org/abs/2606.02438v1).
