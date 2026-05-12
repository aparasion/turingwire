---
title: "DGPO: Beyond Pairwise Preferences with Directional Consistent Groupwise Optimization"
date: 2026-05-11 17:10:44 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10863v1"
arxiv_id: "2605.10863"
authors: ["Mengyi Deng", "Zhiwei Li", "Xin Li", "Tingyu Zhu", "Yulan Yuan", "Zhijiang Guo"]
slug: dgpo-beyond-pairwise-preferences-with-directional-consistent
summary_word_count: 405
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing preference optimization methods in Large Language Models (LLMs), particularly their inability to maintain directional consistency while ensuring reasoning diversity. The authors highlight that current approaches primarily focus on pairwise comparisons, which may not effectively capture the complexity of reasoning paths. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Directional-Groupwise Preference Optimization (DGPO), a novel framework that aggregates supervision signals at the group level. DGPO organizes question-answer instances into structured sets, allowing for multi-candidate comparisons that enhance the model's ability to discern direction-aware alignment. The core technical contribution is a margin-based likelihood objective that optimizes the separation of coherent reasoning paths from inconsistent alternatives. This group-wise formulation is designed to leverage richer relative information compared to traditional pairwise objectives. The training process involves constructing reverse data to reinforce the model's understanding of reasoning consistency across diverse pathways.

**Results**  
DGPO demonstrates significant empirical improvements across five benchmarks, achieving an average accuracy increase of 3.2% with the introduction of reverse data. When compared to baseline models, DGPO yields further enhancements, with average accuracy improvements of up to 3.6% across multiple datasets and model families. These results indicate that DGPO not only outperforms existing pairwise preference optimization methods but also provides a more robust framework for reasoning consistency.

**Limitations**  
The authors acknowledge that while DGPO improves directional consistency and reasoning diversity, it may still be limited by the quality and diversity of the training data used for constructing the structured sets. Additionally, the framework's reliance on group-wise comparisons may introduce computational overhead, which could affect scalability in larger datasets. The authors do not discuss potential challenges related to the interpretability of the model's decisions or the generalizability of the results across different domains.

**Why it matters**  
The implications of DGPO are significant for future research in preference optimization and LLM alignment. By moving beyond pairwise comparisons to a group-wise approach, DGPO sets a precedent for more nuanced models that can better capture the complexities of human reasoning. This work could inspire further exploration into multi-candidate optimization strategies and enhance the development of LLMs that are more aligned with human-like reasoning patterns. The framework's ability to maintain consistency across diverse reasoning pathways may also lead to advancements in applications requiring robust decision-making capabilities.

Authors: Mengyi Deng, Zhiwei Li, Xin Li, Tingyu Zhu, Yulan Yuan, Zhijiang Guo, Wei Wang  
Source: arXiv:2605.10863  
URL: https://arxiv.org/abs/2605.10863v1
