---
title: "On the Influence of the Feature Computation Budget on Per-Instance Algorithm Selection for Black-Box Optimization"
date: 2026-05-06 14:15:34 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.04954v1"
arxiv_id: "2605.04954"
authors: ["Koen van der Blom", "Diederick Vermetten"]
slug: on-the-influence-of-the-feature-computation-budget-on-per-in
summary_word_count: 446
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a gap in the literature regarding the efficiency of per-instance algorithm selection (PIAS) in black-box optimization (BBO) when considering the computational budget allocated for feature extraction. Specifically, it investigates the threshold at which the computational cost of feature extraction becomes justified in improving algorithm selection performance. The authors aim to quantify the tradeoff between the accuracy of features derived from the instances and the performance of the selected algorithms, which has not been systematically explored in prior work.

**Method**  
The authors conduct an extensive empirical study comparing PIAS with varying budgets for feature computation against a baseline of the single best-performing algorithm across multiple scenarios. The study encompasses two portfolio sizes, three distinct problem sets, four dimensionalities, and ten target budgets, allowing for a comprehensive analysis of the impact of feature computation on algorithm selection. The PIAS framework is evaluated by measuring its performance relative to the virtual best solver, with a focus on how different fractions of the total budget influence the effectiveness of the feature computation. The authors employ a systematic approach to assess the tradeoff between feature accuracy and PIAS performance, providing insights into optimal budget allocation.

**Results**  
The findings indicate that PIAS remains viable in the majority of tested scenarios, even when up to 25% of the total optimization budget is allocated to feature computation. The results reveal that the optimal fraction of the budget dedicated to feature extraction varies significantly across different algorithm selection scenarios. On average, the study shows that approximately 20% of the performance loss of PIAS compared to the virtual best solver can be attributed to the budget spent on feature computation. This quantification underscores the critical role of budget management in enhancing the efficacy of PIAS in BBO tasks.

**Limitations**  
The authors acknowledge that the effectiveness of PIAS is highly scenario-dependent, which may limit the generalizability of their findings. They do not explore the implications of feature computation on real-time applications or the potential overhead introduced by feature extraction in dynamic environments. Additionally, the study does not consider the impact of varying feature extraction methods or the potential for feature redundancy, which could further influence the results.

**Why it matters**  
This work has significant implications for the design of algorithm selection frameworks in BBO, particularly in contexts where computational resources are constrained. By elucidating the relationship between feature computation budgets and PIAS performance, the study provides a foundational understanding that can guide future research in optimizing algorithm selection strategies. The insights gained can inform practitioners on how to allocate computational resources effectively, potentially leading to more efficient optimization processes in various applications.

Authors: Koen van der Blom, Diederick Vermetten  
Source: arXiv:2605.04954  
URL: [https://arxiv.org/abs/2605.04954v1](https://arxiv.org/abs/2605.04954v1)
