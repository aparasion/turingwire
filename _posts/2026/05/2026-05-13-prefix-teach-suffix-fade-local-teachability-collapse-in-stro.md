---
title: "Prefix Teach, Suffix Fade: Local Teachability Collapse in Strong-to-Weak On-Policy Distillation"
date: 2026-05-13 15:05:30 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13643v1"
arxiv_id: "2605.13643"
authors: ["Kaiyuan Liu", "Ziyuan Zhuang", "Yang Bai", "Bing Wang", "Rongxiang Weng", "Jieping Ye"]
slug: prefix-teach-suffix-fade-local-teachability-collapse-in-stro
summary_word_count: 389
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the understanding of on-policy distillation (OPD) in the context of strong-to-weak teacher-student frameworks. Prior research posits that providing dense feedback from a stronger teacher should lead to monotonically improved performance in student models. However, the authors identify a phenomenon termed "local teachability collapse," where the effectiveness of teacher feedback diminishes in later segments of generated trajectories. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a trajectory-specific release rule to mitigate local teachability collapse. This rule evaluates the teacher's margin over the student's top-$K$ candidate responses and aggregates this margin across segments tokenized by NLTK. The supervision is truncated when a downward change point, akin to Bayesian Information Criterion (BIC) detection, is identified, indicating that the teacher's feedback is no longer discriminative. The experiments utilize the Qwen3 model family, focusing on strong-to-weak distillation tasks, and compare the proposed method against standard full-trajectory OPD.

**Results**  
The proposed release rule consistently outperforms standard full-trajectory OPD across five in-domain benchmarks, demonstrating significant improvements in student model performance. Specific metrics were not disclosed in the abstract, but the authors claim that their method better preserves model capabilities on out-of-domain tasks compared to baseline distillation methods. The results suggest that the proposed approach effectively enhances the utility of teacher feedback by concentrating on the most informative segments of the trajectory.

**Limitations**  
The authors acknowledge that their approach may not generalize to all types of distillation tasks, particularly those with different teacher-student dynamics. They do not address potential computational overhead introduced by the trajectory-specific release rule, which may complicate implementation in resource-constrained environments. Additionally, the reliance on NLTK for tokenization may introduce variability depending on the language or domain of the data.

**Why it matters**  
This work has significant implications for the design of distillation strategies in machine learning, particularly in scenarios where teacher models are substantially stronger than student models. By emphasizing the importance of local utility in teacher feedback, the findings encourage a shift in focus from uniform supervision to targeted, discriminative feedback. This could lead to more efficient training processes and improved performance in both in-domain and out-of-domain tasks, ultimately enhancing the robustness of student models in practical applications.

Authors: Kaiyuan Liu, Ziyuan Zhuang, Yang Bai, Bing Wang, Rongxiang Weng, Jieping Ye  
Source: arXiv:2605.13643  
URL: [https://arxiv.org/abs/2605.13643v1](https://arxiv.org/abs/2605.13643v1)
