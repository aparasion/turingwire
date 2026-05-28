---
title: "How VLAs Fail Differently: Black-Box Action Monitoring Reveals Architecture-Specific Failure Signatures"
date: 2026-05-27 16:44:55 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28726v1"
arxiv_id: "2605.28726"
authors: ["Krishnam Gupta"]
slug: how-vlas-fail-differently-black-box-action-monitoring-reveal
summary_word_count: 413
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in understanding the failure modes of Variable-Length Action (VLA) architectures in reinforcement learning, specifically at the motor-command level. Prior literature has not systematically characterized how different VLA architectures fail, nor has it provided a framework for monitoring these failures effectively. The authors aim to elucidate architecture-specific failure signatures, which is crucial for improving the robustness and safety of VLA deployments.

**Method**  
The core technical contribution is the introduction of SafeContract, a black-box action monitoring toolkit that employs conformal calibration to assess the performance of various VLA architectures. The authors evaluate three distinct architectures: VQ-BeT, Diffusion Policy, and ACT, across 450 episodes in two bimanual manipulation tasks (PushT and ALOHA 14-DOF). They analyze failure predictors such as direction reversal rates, jerk monitoring, and velocity violations. The study employs area under the receiver operating characteristic curve (AUROC) as a metric for predictive performance, revealing that direction reversal rates serve as a universal predictor across all architectures, while jerk monitoring is effective only for discrete-token architectures.

**Results**  
The findings indicate that direction reversal rates yield high AUROC scores (0.93 for VQ-BeT, 0.79 for Diffusion Policy, and 0.91 for ACT, all p<0.001), establishing it as a reliable failure predictor. Jerk monitoring shows varying effectiveness, with AUROC scores of 0.88 for VQ-BeT, 0.69 for Diffusion, and 0.41 for ACT, indicating a gradient of predictive power from discrete to continuous architectures. Conversely, velocity violations are largely non-predictive, with AUROC scores ranging from 0.41 to 0.69, and velocity monitoring provides negligible predictive signal for continuous-family VLAs (AUROC=0.52 for ACT, 0.41 for Diffusion). These results underscore the necessity for architecture-specific monitoring strategies, as no single monitor is universally applicable.

**Limitations**  
The authors acknowledge that their findings are limited to the specific architectures and tasks evaluated, which may not generalize to all VLA implementations. Additionally, the reliance on a black-box monitoring approach may obscure underlying causal mechanisms of failure. The study does not explore the implications of these findings on real-world applications or the potential for integrating these monitoring strategies into existing VLA systems.

**Why it matters**  
This work has significant implications for the design and deployment of VLA architectures in safety-critical applications. By identifying architecture-specific failure signatures and the inadequacy of universal monitoring strategies, the research provides a framework for developing more robust and reliable VLA systems. This could lead to improved safety protocols in autonomous systems, enhancing their operational reliability and trustworthiness in real-world scenarios.

Authors: Krishnam Gupta  
Source: arXiv cs.LG  
URL: [https://arxiv.org/abs/2605.28726v1](https://arxiv.org/abs/2605.28726v1)
