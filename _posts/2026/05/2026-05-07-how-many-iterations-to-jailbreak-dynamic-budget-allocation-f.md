---
title: "How Many Iterations to Jailbreak? Dynamic Budget Allocation for Multi-Turn LLM Evaluation"
date: 2026-05-07 17:25:15 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06605v1"
arxiv_id: "2605.06605"
authors: ["Shai Feldman", "Yaniv Romano"]
slug: how-many-iterations-to-jailbreak-dynamic-budget-allocation-f
summary_word_count: 408
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of efficiently evaluating large language models (LLMs) in multi-turn conversational settings, particularly in detecting rare events such as jailbreaks or successful task completions. Existing methods rely on static budget allocation, which is inefficient for multi-turn interactions and may lead to unobserved key events under computational constraints. The authors present a preprint work that introduces a dynamic budget allocation framework, filling a gap in the literature regarding effective evaluation strategies for LLMs in these contexts.

**Method**  
The core technical contribution is the Dynamic Allocation via PRojected Optimization (DAPRO) framework, which allows for dynamic budget allocation in multi-turn evaluations. DAPRO is theoretically validated to satisfy budget constraints while providing distribution-free, finite-sample coverage guarantees. Unlike previous conformal survival frameworks that assume conditional independence between censoring and event times, DAPRO does not require this assumption. A significant theoretical advancement is the introduction of a novel coverage bound that scales with the square root of the mean censoring weight, leading to tighter guarantees compared to prior methods. The framework enables unbiased, low-variance estimates of population-level metrics, such as jailbreak rates, even under limited computational resources.

**Results**  
The authors conducted comprehensive experiments using LLMs like Llama 3.1 and Qwen 2.5 across various tasks, including agentic task success, adversarial jailbreak detection, toxic content generation, and retrieval-augmented generation (RAG) hallucinations. DAPRO demonstrated improved performance over static baselines, achieving coverage levels closer to the nominal level with lower variance. Specific effect sizes were not disclosed, but the results indicate a significant enhancement in efficiency and reliability of event detection compared to traditional methods.

**Limitations**  
The authors acknowledge that while DAPRO provides tighter coverage guarantees, it may still be sensitive to the choice of hyperparameters in the optimization process. Additionally, the framework's performance in extremely low-event-rate scenarios remains to be fully explored. The paper does not address potential computational overhead introduced by the dynamic allocation process itself, which could offset some efficiency gains in certain contexts.

**Why it matters**  
The implications of this work are substantial for downstream applications involving LLMs, particularly in safety-critical domains where understanding model behavior in multi-turn interactions is essential. By providing a robust framework for dynamic budget allocation, DAPRO enhances the ability to detect rare but significant events, thereby improving the reliability of LLM evaluations. This advancement could lead to more effective monitoring and mitigation strategies for undesirable model behaviors, fostering safer deployment of LLMs in real-world applications.

Authors: Shai Feldman, Yaniv Romano  
Source: arXiv:2605.06605  
URL: https://arxiv.org/abs/2605.06605v1
