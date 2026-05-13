---
title: "Model-based Bootstrap of Controlled Markov Chains"
date: 2026-05-12 17:05:59 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12410v1"
arxiv_id: "2605.12410"
authors: ["Ziwei Su", "Imon Banerjee", "Diego Klabjan"]
slug: model-based-bootstrap-of-controlled-markov-chains
summary_word_count: 465
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding the estimation of transition kernels in finite controlled Markov chains (CMCs) under nonstationary or history-dependent control policies, particularly in the context of offline reinforcement learning (RL) where the behavior policy is unknown. The authors propose a model-based bootstrap method to provide a robust statistical framework for estimating transition dynamics, which is crucial for accurate policy evaluation and recovery in offline settings. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of a model-based bootstrap approach for estimating transition kernels in CMCs. The authors establish distributional consistency for the bootstrap transition estimator in both a single long-chain regime and an episodic offline RL regime. Key innovations include a novel bootstrap law of large numbers (LLN) for visitation counts and the application of the martingale central limit theorem (CLT) for bootstrap transition increments. The authors extend their results to offline policy evaluation (OPE) and optimal policy recovery (OPR) by demonstrating the Hadamard differentiability of Bellman operators, which allows for the derivation of asymptotically valid confidence intervals for value and Q-functions. The experiments utilize the RiverSwim problem as a benchmark to validate the proposed method.

**Results**  
The proposed bootstrap confidence intervals (CIs), particularly the percentile CIs, demonstrate superior performance compared to traditional methods such as the episodic bootstrap and plug-in CLT CIs. Specifically, the proposed method achieves nominal coverage rates of approximately 50%, 90%, and 95% across various sample sizes and episode lengths, while the baseline methods exhibit poor calibration under similar conditions. The results indicate that the model-based bootstrap provides more reliable estimates of transition dynamics, which is critical for effective policy evaluation in offline RL scenarios.

**Limitations**  
The authors acknowledge that their approach may be sensitive to the choice of model for the transition dynamics and that the performance could degrade if the model is misspecified. Additionally, the reliance on Hadamard differentiability may limit the applicability of the method to certain classes of problems. The paper does not address the computational complexity of implementing the proposed bootstrap method in large-scale applications, which could be a significant barrier in practice.

**Why it matters**  
This work has significant implications for the field of offline reinforcement learning, particularly in enhancing the reliability of policy evaluation and recovery methods. By providing a statistically sound framework for estimating transition dynamics in CMCs, the proposed model-based bootstrap can improve the robustness of offline RL algorithms, leading to better decision-making in real-world applications where data is limited or the behavior policy is unknown. The findings encourage further exploration of bootstrap methods in reinforcement learning and may inspire new approaches to tackle similar challenges in other areas of machine learning.

Authors: Ziwei Su, Imon Banerjee, Diego Klabjan  
Source: arXiv:2605.12410  
URL: https://arxiv.org/abs/2605.12410v1
