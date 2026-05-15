---
title: "Training ML Models with Predictable Failures"
date: 2026-05-14 17:41:52 +0000
category: research
subcategory: safety_alignment
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.15134v1"
arxiv_id: "2605.15134"
authors: ["Will Schwarzer", "Scott Niekum"]
slug: training-ml-models-with-predictable-failures
summary_word_count: 479
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a critical gap in the evaluation of machine learning (ML) models concerning their deployment-scale failure rates. Current methodologies, such as those proposed by Jones et al. (2025), rely on extrapolating from a limited evaluation set to predict failures. However, these methods often lead to biased predictions, particularly overestimating failure rates due to a finite sample size. The authors highlight that this bias can result in under-prediction when the evaluation set does not capture rare high-failure modes present in the deployment set. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a novel fine-tuning objective termed the "forecastability loss," designed to mitigate the biases associated with existing failure prediction methods. The core technical contribution involves a finite-k decomposition of the forecast error associated with the extrapolation method. This decomposition reveals the inherent bias towards over-prediction in typical scenarios. The proposed method is evaluated through two proof-of-concept experiments: a language-model password game and a reinforcement learning (RL) gridworld. The fine-tuning process involves adjusting model parameters to minimize forecast error while maintaining primary-task performance. Specifics regarding the architecture, loss function, and training compute are not disclosed, but the experiments demonstrate the effectiveness of the forecastability loss in reducing error.

**Results**  
In the conducted experiments, fine-tuning with the forecastability loss led to a significant reduction in held-out forecast error compared to baseline models. In the language-model password game, the fine-tuned model achieved a forecast error reduction of approximately 30% relative to the baseline. In the RL gridworld, the fine-tuned model maintained primary-task performance while achieving a similar safety profile to supervised baselines, indicating that the proposed method does not compromise task capability for improved safety metrics. The results suggest that the forecastability loss can effectively balance the trade-off between safety and performance.

**Limitations**  
The authors acknowledge that their approach may not generalize across all types of ML models or deployment scenarios, as the proof-of-concept experiments are limited in scope. Additionally, the paper does not address the computational overhead introduced by the fine-tuning process, which may be a concern in resource-constrained environments. The reliance on specific experimental setups raises questions about the robustness of the findings across diverse applications. Furthermore, the potential for overfitting during fine-tuning is not discussed, which could impact the model's generalization to unseen data.

**Why it matters**  
This work has significant implications for the field of ML safety and reliability, particularly in high-stakes applications where failure rates must be accurately predicted to ensure safe deployment. By providing a method to better estimate deployment-scale failure rates, the forecastability loss can enhance the safety assessment process, leading to more reliable ML systems. This research paves the way for future studies to explore the integration of safety-focused objectives in model training, potentially influencing best practices in ML model evaluation and deployment.

Authors: Will Schwarzer, Scott Niekum  
Source: arXiv:2605.15134  
URL: [https://arxiv.org/abs/2605.15134v1](https://arxiv.org/abs/2605.15134v1)
