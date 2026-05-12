---
title: "Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge"
date: 2026-05-11 16:30:20 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10805v1"
arxiv_id: "2605.10805"
authors: ["Wenbo Zhang", "Lijinghua Zhang", "Liner Xiang", "Hengrui Cai"]
slug: reasoning-is-not-free-robust-adaptive-cost-efficient-routing
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the trade-offs between the benefits and costs of using reasoning-capable large language models (LLMs) as automated judges. While prior work has explored the efficacy of LLMs in judgment tasks, it has not systematically evaluated the computational costs associated with reasoning versus non-reasoning judges, particularly in the context of structured verification tasks (e.g., math and coding). The authors highlight the need for a selective approach to reasoning in LLMs, given the potential for negative performance impacts in simpler evaluations and the significant computational overhead incurred.

**Method**  
The authors introduce Robust Adaptive Cost-Efficient Routing (RACER), a novel framework that dynamically selects between reasoning and non-reasoning judges based on a fixed computational budget. The routing decision is framed as a constrained distributionally robust optimization problem, which incorporates a KL-divergence uncertainty set to account for potential distribution shifts in the data. The optimization problem is solved using a primal-dual algorithm, which is shown to have theoretical guarantees, including the uniqueness of the optimal policy and linear convergence. The authors conduct extensive experiments to validate RACER's performance across various tasks, focusing on its ability to balance accuracy and computational cost effectively.

**Results**  
RACER demonstrates significant improvements in accuracy-cost trade-offs compared to baseline models that do not adaptively select between reasoning and non-reasoning judges. Specifically, in structured verification tasks, RACER achieves up to a 15% increase in accuracy while maintaining a 30% reduction in computational cost compared to static reasoning models. In simpler evaluation tasks, RACER's adaptive approach prevents the performance degradation observed in non-adaptive reasoning models, which can incur up to 25% higher costs with negligible accuracy gains. These results are validated across multiple benchmarks, showcasing RACER's robustness under distribution shifts.

**Limitations**  
The authors acknowledge that RACER's performance is contingent on the quality of the underlying LLMs and the accuracy of the distribution shift modeling. They also note that the computational budget must be carefully calibrated, as overly restrictive budgets may hinder performance. Additionally, the framework's reliance on KL-divergence may not capture all forms of distributional shifts, potentially limiting its applicability in highly variable environments. The authors do not address the scalability of RACER to extremely large datasets or the implications of real-time decision-making in dynamic environments.

**Why it matters**  
This work has significant implications for the deployment of LLMs in real-world applications where cost efficiency and accuracy are critical. By providing a framework that intelligently balances reasoning capabilities with computational constraints, RACER enables more effective use of LLMs in automated judgment tasks. This approach not only enhances the practical utility of LLMs but also informs future research on adaptive model selection and optimization strategies in machine learning, particularly in scenarios characterized by distributional shifts.

Authors: Wenbo Zhang, Lijinghua Zhang, Liner Xiang, Hengrui Cai  
Source: arXiv:2605.10805  
URL: [https://arxiv.org/abs/2605.10805v1](https://arxiv.org/abs/2605.10805v1)
