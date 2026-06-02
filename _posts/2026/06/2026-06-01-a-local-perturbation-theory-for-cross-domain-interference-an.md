---
title: "A Local Perturbation Theory for Cross-Domain Interference and Recovery in Multi-Domain RL"
date: 2026-06-01 15:44:56 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.02398v1"
arxiv_id: "2606.02398"
authors: ["Lei Yang", "Siyu Ding", "Deyi Xiong"]
slug: a-local-perturbation-theory-for-cross-domain-interference-an
summary_word_count: 428
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces a local perturbation theory to explain cross-domain interference in multi-domain reinforcement learning and proposes recovery strategies."
---

**Problem**  
This work addresses the gap in understanding the mechanisms behind cross-domain interference in multi-domain reinforcement learning (RL), particularly in large language models (LLMs). Existing literature primarily attributes performance degradation to catastrophic forgetting or global gradient conflicts, which are insufficient to explain the observed phenomena. The authors highlight that substantial interference can occur even when gradients are nearly orthogonal, indicating a need for a more nuanced theoretical framework. This paper is a preprint and has not undergone peer review.

**Method**  
The authors propose a local perturbation model to analyze multi-domain RL, focusing on the sparse, small-magnitude parameter edits that occur during single-domain training. They demonstrate that while different domains share significant active computation routes, the updates can either synergize or conflict based on the parameter changes. The model identifies a second-order damage term as the primary mechanism through which training on a later domain negatively impacts an earlier one, concentrating in a low-dimensional shared conflict subspace. The authors also introduce a domain refresh strategy that mitigates this harmful component, allowing for selective recovery with minimal collateral damage. Empirical validation includes a brief Re-Math refresh after a sequence of domain trainings (Code → Math → QA → CW), which effectively recovers Math performance.

**Results**  
The proposed method yields significant performance improvements on the Math domain, with scores increasing from 57.66 to 66.04 after the Re-Math refresh, while maintaining performance across other domains. The average score across all domains reached 66.39, outperforming baseline methods that do not utilize the local perturbation approach. Additionally, a training-free rollback on a sparse proxy conflict coordinate set for the Math-QA pair demonstrated partial restoration of Math performance, providing empirical support for the localized damage hypothesis.

**Limitations**  
The authors acknowledge that their model primarily focuses on the second-order damage term and may not account for all forms of interference in multi-domain RL. They also note that the effectiveness of the domain refresh strategy may vary across different domain pairs and training sequences. Furthermore, the empirical results are based on specific domain configurations, which may limit generalizability to other multi-domain scenarios.

**Why it matters**  
This work provides a mechanistic understanding of interference and recovery in multi-domain RL, which is crucial for developing robust LLMs that can perform well across diverse tasks without significant performance degradation. The insights gained from the local perturbation theory can inform future research on mitigating interference in multi-task learning settings, enhancing the adaptability of models in real-world applications. This is particularly relevant as the field moves towards more generalized AI systems capable of handling multiple domains simultaneously, as published in [arXiv cs.LG](https://arxiv.org/abs/2606.02398v1).
