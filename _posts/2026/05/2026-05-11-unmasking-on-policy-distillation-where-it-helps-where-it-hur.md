---
title: "Unmasking On-Policy Distillation: Where It Helps, Where It Hurts, and Why"
date: 2026-05-11 17:33:28 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10889v1"
arxiv_id: "2605.10889"
authors: ["Mohammadreza Armandpour", "Fatih Ilhan", "David Harrison", "Ajay Jaiswal", "Duc N. M Hoang", "Fartash Faghri"]
slug: unmasking-on-policy-distillation-where-it-helps-where-it-hur
summary_word_count: 452
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the conditions under which on-policy distillation is beneficial or detrimental for training reasoning models. While on-policy distillation provides dense supervision, the authors highlight the ambiguity surrounding the choice of teacher models and the contexts for self-distillation. Existing methods often rely on extensive training runs that yield aggregate performance metrics, obscuring the dynamics at the token level. This work aims to clarify these dynamics through a novel diagnostic framework.

**Method**  
The authors propose a training-free diagnostic framework that evaluates distillation effectiveness at a granular level—per token, per question, and per teacher model. They derive an ideal per-node gradient, which represents the parameter update that maximally increases the student's probability of success. To estimate this gradient efficiently, they introduce a scalable targeted-rollout algorithm capable of handling long chains of intermediate thoughts. The core metric introduced is the gradient alignment score, defined as the cosine similarity between the ideal gradient and any given distillation gradient. This score quantifies how closely a specific distillation configuration approximates the ideal signal, allowing for a detailed analysis of distillation effectiveness across various settings.

**Results**  
The authors conduct experiments across multiple self-distillation scenarios and with external teacher models. They find that distillation guidance shows significantly higher alignment with the ideal gradient on incorrect rollouts compared to correct ones, indicating that the teacher's signal becomes noisy when the student model already performs well. Additionally, the optimal context for distillation is shown to depend on both the student model's capacity and the specific target task, with no single configuration proving universally effective. These insights are supported by quantitative evaluations, although specific numerical results and comparisons to named baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that their framework does not provide a one-size-fits-all solution for distillation, as the optimal configurations vary significantly based on task and model capacity. They also note that their approach is diagnostic rather than prescriptive, meaning it does not directly improve model performance but rather informs future distillation strategies. An additional limitation is the absence of empirical results in the abstract, which may hinder the assessment of practical applicability.

**Why it matters**  
This work has significant implications for the design of distillation strategies in machine learning, particularly in reasoning tasks. By providing a framework for per-task, per-token analysis, it encourages researchers to adopt a more nuanced approach to distillation, moving away from generic configurations. The findings suggest that understanding the dynamics of distillation at a granular level can lead to more effective training methodologies, ultimately enhancing model performance in complex reasoning tasks.

Authors: Mohammadreza Armandpour, Fatih Ilhan, David Harrison, Ajay Jaiswal, Duc N. M Hoang, Fartash Faghri, Yizhe Zhang, Minsik Cho et al.  
Source: arXiv:2605.10889  
URL: https://arxiv.org/abs/2605.10889v1
