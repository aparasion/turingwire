---
title: "Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection"
date: 2026-04-30 17:16:33 +0000
category: research
subcategory: alignment_safety
company: "UiPath"
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28129v1"
arxiv_id: "2604.28129"
authors: ["Prashant Kulkarni"]
slug: latent-adversarial-detection-adaptive-probing-of-llm-activat
summary_word_count: 459
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the detection of multi-turn prompt injection attacks on large language models (LLMs), specifically focusing on covert attacks where individual turns appear benign. Existing text-level defenses are inadequate for identifying these attacks, which follow a structured path of trust-building, pivoting, and escalation. The authors propose a novel approach to detect these attacks by analyzing the activation patterns of LLMs, which they term "adversarial restlessness." This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of five scalar trajectory features that capture the activation-level signatures indicative of adversarial restlessness. These features are derived from the model's residual stream, which reflects the cumulative effect of the attack path on the model's activations. The authors evaluate their method across four model families, ranging from 24B to 70B parameters, and emphasize that the probing mechanisms are model-specific and do not generalize across different architectures. The training process involves a synthetic dataset designed to include three-phase turn-level labels (benign, pivoting, adversarial), which are critical for effective detection. The authors report that using binary conversation-level labels results in significantly higher false positive rates (50-59%).

**Results**  
The proposed method achieves a detection accuracy of 93.8% on synthetic held-out data, a substantial improvement from the baseline of 76.2%. In terms of real-world applicability, the model demonstrates detection rates of 47-71% on the LMSYS dataset when its distribution is included in the training set. A combined training approach using three distinct sources results in an overall detection accuracy of 89.4% with a false positive rate of only 2.4% on a mixed held-out set. The leave-one-source-out evaluation reveals that each dataset captures unique attack distributions, underscoring the importance of diverse training data.

**Limitations**  
The authors acknowledge that the model-specific nature of the probing mechanisms limits the transferability of their approach across different architectures. Additionally, the reliance on synthetic datasets for training may not fully capture the complexities of real-world interactions. The generalization of the model's performance to unseen attack types or novel adversarial strategies remains untested. Furthermore, the paper does not explore the computational costs associated with training and deploying the proposed detection mechanism.

**Why it matters**  
This work has significant implications for enhancing the security of LLMs against sophisticated adversarial attacks. By establishing adversarial restlessness as a reliable signal for detection, the findings pave the way for more robust defenses in conversational AI systems. The emphasis on activation-level analysis could inspire further research into model interpretability and adversarial robustness, potentially leading to the development of more resilient architectures. The insights gained from the distinct attack distributions across different datasets highlight the necessity for diverse training paradigms in the ongoing battle against adversarial manipulation.

Authors: Prashant Kulkarni  
Source: arXiv:2604.28129  
URL: [https://arxiv.org/abs/2604.28129v1](https://arxiv.org/abs/2604.28129v1)
