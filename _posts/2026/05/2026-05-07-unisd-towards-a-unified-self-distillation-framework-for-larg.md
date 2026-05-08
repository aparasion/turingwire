---
title: "UniSD: Towards a Unified Self-Distillation Framework for Large Language Models"
date: 2026-05-07 17:22:11 +0000
category: research
subcategory: training_methods
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06597v1"
arxiv_id: "2605.06597"
authors: ["Yiqiao Jin", "Yiyang Wang", "Lucheng Fu", "Yijia Xiao", "Yinyi Luo", "Haoxin Liu"]
slug: unisd-towards-a-unified-self-distillation-framework-for-larg
summary_word_count: 428
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of self-distillation (SD) in autoregressive large language models (LLMs), particularly the challenges posed by free-form self-generated trajectories, task-dependent correctness, and the instability of plausible rationales as supervision. The authors note that existing research primarily focuses on isolated design choices, leaving a gap in understanding the effectiveness, roles, and interactions of various components in self-distillation. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose UniSD, a unified self-distillation framework that integrates several mechanisms to enhance supervision reliability, representation alignment, and training stability. Key components of UniSD include:

- **Multi-teacher agreement**: Utilizes multiple teacher models to provide diverse supervision signals.
- **Exponential Moving Average (EMA) teacher stabilization**: Stabilizes the teacher model's predictions over time to reduce noise.
- **Token-level contrastive learning**: Encourages the model to differentiate between correct and incorrect token predictions.
- **Feature matching**: Aligns the feature representations of the student and teacher models.
- **Divergence clipping**: Mitigates the impact of outlier predictions during training.

The authors construct an integrated pipeline, termed UniSDfull, which combines these components to achieve optimal performance. The training compute details are not explicitly disclosed, but the framework is evaluated across six benchmarks and six models from three different model families.

**Results**  
UniSDfull demonstrates significant improvements over both the base model and existing baselines. Specifically, it achieves an average performance increase of +5.4 points over the base model and +2.8 points over the strongest baseline across the evaluated benchmarks. The paper provides detailed comparisons against named baselines, although specific benchmark names are not listed in the abstract.

**Limitations**  
The authors acknowledge that while UniSD improves self-distillation efficacy, the framework's reliance on multiple components may introduce complexity in model training and deployment. They do not address potential scalability issues when applying UniSD to larger or more diverse datasets. Additionally, the paper does not explore the computational overhead introduced by the multi-teacher setup or the EMA stabilization process.

**Why it matters**  
The implications of this work are significant for the field of LLM adaptation. By demonstrating that self-distillation can be a practical and effective method for adapting LLMs without the need for stronger external teachers, the authors pave the way for more efficient model training strategies. The insights gained from the interactions of various components within the UniSD framework can inform future research on self-supervised learning and model distillation techniques, potentially leading to more robust and adaptable LLMs.

Authors: Yiqiao Jin, Yiyang Wang, Lucheng Fu, Yijia Xiao, Yinyi Luo, Haoxin Liu, B. Aditya Prakash, Josiah Hester et al.  
Source: arXiv:2605.06597  
URL: [https://arxiv.org/abs/2605.06597v1](https://arxiv.org/abs/2605.06597v1)
