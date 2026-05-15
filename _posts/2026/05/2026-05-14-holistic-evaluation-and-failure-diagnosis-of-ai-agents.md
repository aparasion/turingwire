---
title: "Holistic Evaluation and Failure Diagnosis of AI Agents"
date: 2026-05-14 14:12:39 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.14865v1"
arxiv_id: "2605.14865"
authors: ["Netta Madvil", "Gilad Dym", "Alon Mecilati", "Edo Dekel", "Jonatan Liberman", "Rotem Brazilay"]
slug: holistic-evaluation-and-failure-diagnosis-of-ai-agents
summary_word_count: 453
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacies in the evaluation of AI agents executing complex multi-step processes. Current methodologies primarily focus on outcome metrics that indicate success or failure without providing insights into the underlying reasons for these outcomes. Additionally, existing process-level evaluation techniques struggle to correlate specific failure types with their locations within lengthy structured traces. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a holistic evaluation framework that integrates top-down agent-level diagnosis with bottom-up span-level evaluation. This dual approach allows for the decomposition of the evaluation process into independent assessments for each span within the agent's execution trace. The framework is designed to scale to traces of arbitrary length, producing span-level rationales that elucidate the reasoning behind each verdict. The evaluation methodology leverages a frontier model, which is shown to significantly enhance localization accuracy when applied within this framework compared to its performance as a standalone evaluator over the entire trace. Specifics regarding the architecture, loss functions, and training compute are not disclosed in the abstract.

**Results**  
The proposed framework demonstrates state-of-the-art performance on the TRAIL benchmark, achieving substantial improvements over the strongest prior baselines. Key results include:
- Up to 38% relative gain in category F1 score.
- Up to 3.5x improvement in localization accuracy.
- Up to 12.5x enhancement in joint localization-categorization accuracy.
The framework outperforms other evaluators across multiple error categories, indicating its robustness and effectiveness in diagnosing failures. Notably, the frontier model's localization accuracy is several times higher when utilized within the proposed framework compared to its performance as a monolithic judge.

**Limitations**  
The authors acknowledge that their framework's performance is contingent on the quality of the underlying frontier model. If the model is suboptimal, the evaluation results may also be compromised. Additionally, the paper does not address the computational overhead introduced by the span-level evaluations, which could be a concern in real-time applications. The scalability of the framework to extremely large traces or highly complex agent behaviors is also not thoroughly examined.

**Why it matters**  
This work has significant implications for the field of AI agent evaluation, particularly in enhancing the interpretability of failure diagnoses. By providing detailed span-level insights, the framework enables developers and researchers to pinpoint specific areas of failure, facilitating targeted improvements in agent design and training. The findings suggest that the evaluation methodology itself can be a limiting factor in performance, highlighting the need for innovative approaches in assessing AI capabilities. This could lead to more robust AI systems that are better equipped to handle complex tasks in dynamic environments.

Authors: Netta Madvil, Gilad Dym, Alon Mecilati, Edo Dekel, Jonatan Liberman, Rotem Brazilay, Liron Schliesser, Max Svidlo et al.  
Source: arXiv:2605.14865  
URL: [https://arxiv.org/abs/2605.14865v1](https://arxiv.org/abs/2605.14865v1)
