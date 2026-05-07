---
title: "Preference-Based Self-Distillation: Beyond KL Matching via Reward Regularization"
date: 2026-05-06 15:31:50 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.05040v1"
arxiv_id: "2605.05040"
authors: ["Xin Yu", "Liuchen Liao", "Yiwen Zhang", "Yingchen Yu", "Lingzhou Xue", "Qinzhen Guo"]
slug: preference-based-self-distillation-beyond-kl-matching-via-re
summary_word_count: 409
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing on-policy self-distillation methods in reinforcement learning, particularly the reliance on KL divergence matching with a context-augmented teacher model. The authors highlight that this approach can lead to training instability and degradation in reasoning performance over time. Furthermore, the lack of exploratory diversity from a genuine external teacher hampers the learning process. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework called Preference-Based Self-Distillation (PBSD), which shifts the focus from fixed-teacher KL matching to a reward-regularized learning objective. The core technical contribution involves deriving a reward-regularized objective that targets a reward-reweighted teacher distribution, which is analytically shown to be superior to the original teacher distribution. PBSD optimizes the preference gaps between teacher and student samples while maintaining on-policy sampling for the student. The framework is supported by a statistical analysis that formalizes the conditions under which on-policy self-distillation is more advantageous than learning from an external teacher. The architecture specifics, loss functions, and training compute details are not disclosed in the abstract.

**Results**  
Experiments conducted on mathematical reasoning and tool-use benchmarks demonstrate that PBSD outperforms existing self-distillation methods. The authors report that PBSD achieves the strongest average performance across multiple model scales when compared to named baselines, although specific numerical results and effect sizes are not provided in the abstract. The framework is noted for improved training stability and token efficiency, indicating a significant enhancement over prior self-distillation approaches.

**Limitations**  
The authors acknowledge that their approach may still be sensitive to the choice of reward functions and the design of the teacher-student interaction. They do not discuss potential scalability issues or the generalizability of PBSD to other domains outside of mathematical reasoning and tool use. Additionally, the lack of peer review raises questions about the robustness of their findings.

**Why it matters**  
The implications of PBSD are significant for the field of reinforcement learning and self-distillation. By moving beyond traditional KL matching, this work opens avenues for more stable and efficient training methodologies that leverage on-policy learning. The reward-regularized perspective could inspire further research into preference-based learning frameworks, potentially leading to advancements in areas requiring complex reasoning and decision-making. This approach may also encourage the exploration of new architectures and training paradigms that prioritize exploratory diversity, enhancing the overall performance of self-distillation techniques.

Authors: Xin Yu, Liuchen Liao, Yiwen Zhang, Yingchen Yu, Lingzhou Xue, Qinzhen Guo  
Source: arXiv:2605.05040  
URL: https://arxiv.org/abs/2605.05040v1
