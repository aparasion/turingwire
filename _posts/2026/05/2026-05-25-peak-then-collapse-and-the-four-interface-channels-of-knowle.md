---
title: "Peak-Then-Collapse and the Four Interface Channels of Knowledge-Graph Tool Use"
date: 2026-05-25 17:05:35 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.26037v1"
arxiv_id: "2605.26037"
authors: ["Tianda Sun", "Dimitar Kazakov"]
slug: peak-then-collapse-and-the-four-interface-channels-of-knowle
summary_word_count: 445
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing reinforcement learning-based tool-use methodologies, specifically the GRPO (Generalized Reinforcement Policy Optimization) framework, when applied to a minimal knowledge-graph tool API. The authors investigate the performance of this framework on the Qwen2.5-7B-Instruct model using a restricted set of Freebase navigation verbs over the Complex WebQuestions dataset. The study highlights a significant gap in understanding the dynamics of tool-use performance, particularly the observed "peak-then-collapse" behavior in the model's ability to generate tool-grounded answers.

**Method**  
The authors employ a reinforcement learning approach using GRPO to train the Qwen2.5-7B-Instruct model on a knowledge-graph tool API with four navigation verbs. The training involves a self-verifiable retrieval reward mechanism, where the model's performance is evaluated based on its ability to produce tool-grounded answers. The study systematically explores seven different reward designs to identify failure modes, revealing that simply increasing the density or specificity of proxy rewards does not resolve the underlying issues. The authors also conduct an oracle ablation study to assess the impact of injecting gold relations during retrieval, finding minimal improvements in exact-match accuracy. A novel mitigation strategy, one-iteration self-distillation, is introduced, achieving a 40.0% exact-match (EM) accuracy, demonstrating that the model's performance is largely interface-bound within the tested capacity range of 7B to 14B parameters.

**Results**  
The model's tool-grounded answer rate initially improves from 3.8% to 9.6% over 250 training steps but subsequently collapses to 0% within a 50-step window, indicating a critical failure in sustained performance. The one-iteration self-distillation method achieves a peak EM of 40.0% at 7B parameters, with only a marginal increase of 0.25 percentage points when the model capacity is doubled to 14B. The authors note that 95.4% of retrieval-dependent errors stem from retrieval-composition failures rather than answer-extraction failures, underscoring the challenges in effective tool use.

**Limitations**  
The authors acknowledge several limitations, including the narrow focus on a minimal knowledge-graph API, which may not generalize to more complex interfaces. They also note that the observed peak-then-collapse pattern may not be fully understood, and the study does not explore the effects of different model architectures or larger datasets. Additionally, the reliance on a single model (Qwen2.5-7B-Instruct) limits the generalizability of the findings.

**Why it matters**  
This work has significant implications for the design of reinforcement learning systems that utilize external tools, particularly in the context of knowledge graphs. The findings suggest that interface feedback plays a crucial role in tool-use performance, highlighting the need for more robust reward mechanisms that account for the unique characteristics of knowledge-graph APIs. The study also opens avenues for future research into mitigating retrieval-composition failures and improving the stability of tool-grounded answer generation.

Authors: Tianda Sun, Dimitar Kazakov  
Source: arXiv:2605.26037  
URL: https://arxiv.org/abs/2605.26037v1
