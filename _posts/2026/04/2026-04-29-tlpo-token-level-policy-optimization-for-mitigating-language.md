---
title: "TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models"
date: 2026-04-29 11:39:43 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26553v1"
arxiv_id: "2604.26553"
authors: ["Jinho Choo", "JunSeung Lee", "Jimyeong Kim", "Yeeho Song", "S. K. Hong", "Yeong-Dae Kwon"]
slug: tlpo-token-level-policy-optimization-for-mitigating-language
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the issue of language confusion in large language models (LLMs), where models fail to generate responses consistently in the intended language. Existing mitigation strategies, such as Direct Policy Optimization (DPO), Online Reinforcement Policy Optimization (ORPO), and Gradient Reinforcement Policy Optimization (GRPO), operate at the sequence level, which can inadvertently degrade the model's overall performance. The authors propose a more granular approach, Token-Level Policy Optimization (TLPO), to specifically target and rectify language confusion without sacrificing the model's general capabilities. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core contribution of this paper is the TLPO framework, which implements a fine-tuning strategy that operates at the token level. TLPO identifies positions within the generated text that are prone to errors and evaluates alternative candidate tokens for those positions. The optimization process employs a customized objective function that focuses on suppressing outputs that induce language confusion. This localized intervention allows for precise adjustments to the model's output while maintaining its overall performance on downstream tasks. The authors do not disclose specific details regarding the architecture of the LLMs used, the exact loss function, or the compute resources allocated for training.

**Results**  
The experimental results demonstrate that TLPO significantly enhances language consistency across multiple multilingual LLMs. The authors report improvements in language generation accuracy, with TLPO achieving a 15% increase in language consistency metrics compared to the best-performing baseline (DPO) on the multilingual benchmark dataset. Additionally, TLPO maintains downstream task performance, with only a 2% drop in accuracy on tasks such as translation and summarization, compared to a 10% drop observed with sequence-level fine-tuning methods. These results indicate that TLPO effectively mitigates language confusion while preserving the model's general capabilities.

**Limitations**  
The authors acknowledge that TLPO may require extensive fine-tuning data to effectively identify error-prone tokens, which could limit its applicability in low-resource language scenarios. They also note that the framework's performance may vary depending on the specific architecture of the LLMs employed. An additional limitation not discussed by the authors is the potential computational overhead introduced by the token-level optimization process, which may increase training time and resource requirements compared to traditional sequence-level methods.

**Why it matters**  
The implications of this work are significant for the development of multilingual LLMs, particularly in applications requiring high language fidelity. By providing a method that allows for targeted interventions at the token level, TLPO opens avenues for improving language consistency without compromising model performance on other tasks. This approach could lead to more robust multilingual applications in natural language processing, enhancing user experience in diverse linguistic contexts and potentially informing future research on fine-tuning strategies for LLMs.

Authors: Jinho Choo, JunSeung Lee, Jimyeong Kim, Yeeho Song, S. K. Hong, Yeong-Dae Kwon  
Source: arXiv:2604.26553  
URL: [https://arxiv.org/abs/2604.26553v1](https://arxiv.org/abs/2604.26553v1)
