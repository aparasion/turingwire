---
title: "The Distillation Game: Adaptive Attacks & Efficient Defenses"
date: 2026-05-21 17:09:21 +0000
category: research
subcategory: alignment_safety
company: "MiniMax"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22737v1"
arxiv_id: "2605.22737"
authors: ["Youssef Allouah", "Mahdi Haghifam", "Sanmi Koyejo", "Reza Shokri"]
slug: the-distillation-game-adaptive-attacks-efficient-defenses
summary_word_count: 473
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the vulnerability of machine learning models to distillation attacks, which exploit the outputs of models to create imitative versions. The authors highlight a significant gap in the literature regarding the trade-off between model utility and susceptibility to such attacks. They propose a novel framework to analyze this trade-off through a minimax game involving a utility-constrained teacher model and an adaptive student model. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of a minimax game framework that facilitates the interaction between the teacher and the student models. The authors derive two key components: an adaptive evaluation rule for the student that reweights examples based on their value, and a teacher-side defense mechanism that suppresses outputs that are most beneficial for distillation. The defense mechanism, termed Product-of-Experts (PoE), operates as a forward-pass-only approach, combining the teacher model with a proxy student during the generation phase. The authors utilize a proxy for example value to inform the adaptive evaluation, allowing for efficient computation during training and inference.

**Results**  
The empirical evaluation reveals a substantial passive-adaptive gap, indicating that adaptive students can recover significantly more capability than what passive evaluation suggests. Specifically, on the GSM8K and MATH benchmarks, the authors demonstrate that adaptive evaluation leads to a narrowing of the robustness gap between expensive defenses and the PoE method. While the PoE defense remains computationally cheaper, it also preserves higher-quality reasoning traces compared to traditional defenses. The results suggest that the effectiveness of antidistillation strategies should be assessed against adaptive students rather than passive ones, as the latter may underestimate the true capabilities of adaptive attacks.

**Limitations**  
The authors acknowledge that their framework primarily focuses on the interaction between a single teacher and a single adaptive student, which may not generalize to more complex multi-student scenarios. Additionally, the reliance on a proxy for example value may introduce biases that could affect the robustness of the proposed defenses. The paper does not extensively explore the scalability of the PoE defense in larger model architectures or diverse datasets beyond GSM8K and MATH, which could limit its applicability in real-world scenarios.

**Why it matters**  
This work has significant implications for the development of robust machine learning models, particularly in contexts where model outputs are publicly accessible. By framing the problem as a game between teacher and student, the authors provide a structured approach to understanding and mitigating distillation attacks. The findings suggest that existing defenses may be less effective than previously thought when faced with adaptive attacks, prompting a reevaluation of current strategies in model deployment. This research could inform future work on designing more resilient models and defenses against imitation attacks, ultimately enhancing the security of AI systems.

Authors: Youssef Allouah, Mahdi Haghifam, Sanmi Koyejo, Reza Shokri  
Source: arXiv:2605.22737  
URL: https://arxiv.org/abs/2605.22737v1
