---
title: "Misaligned by Reward: Socially Undesirable Preferences in LLMs"
date: 2026-05-06 15:04:23 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.05003v1"
arxiv_id: "2605.05003"
authors: ["Gayane Ghazaryan", "Esra D\u00f6nmez"]
slug: misaligned-by-reward-socially-undesirable-preferences-in-llm
summary_word_count: 493
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the evaluation of reward models used for aligning large language models (LLMs) with human preferences. Existing benchmarks primarily assess instruction-following capabilities, neglecting the critical aspect of social alignment. The authors argue that this oversight can lead to the adoption of models that exhibit socially undesirable preferences, which may not be evident in traditional evaluations. By focusing on socially consequential domains—bias, safety, morality, and ethical reasoning—the paper aims to illuminate the shortcomings of current reward models in capturing socially desirable outcomes.

**Method**  
The authors propose a novel framework that transforms social evaluation datasets into pairwise preference data. This framework utilizes gold labels when available and directional bias indicators otherwise to assess the preferences of reward models. The study evaluates five publicly available reward models and two instruction-tuned models, analyzing their outputs across the four identified domains. The methodology emphasizes the systematic testing of whether these models exhibit a preference for socially undesirable responses and whether their preferences lead to biased distributions of outputs. The training compute and specific architectures of the models are not disclosed, but the focus is on the comparative performance across the domains.

**Results**  
The findings reveal substantial variability in performance across the evaluated models, with no single model consistently outperforming others across all domains. Notably, the models frequently preferred socially undesirable options, indicating a significant deficiency in social intelligence. The authors report that stronger bias avoidance mechanisms can inadvertently compromise contextual sensitivity, highlighting a critical trade-off in model alignment. The results underscore that standard reward benchmarks fail to adequately measure social alignment, necessitating the development of more targeted evaluation metrics. Specific effect sizes and quantitative comparisons to baseline models are not provided in the abstract, but the qualitative findings suggest a pervasive issue across the board.

**Limitations**  
The authors acknowledge that their framework relies on the availability of gold labels and directional bias indicators, which may not be universally applicable across all datasets. Additionally, the study does not explore the underlying reasons for the observed preferences, leaving a gap in understanding the mechanisms driving socially undesirable outputs. The lack of detailed quantitative metrics in the results section limits the ability to gauge the magnitude of the issues identified. Furthermore, the evaluation is constrained to the selected domains, which may not encompass the full spectrum of social alignment challenges.

**Why it matters**  
This work has significant implications for the development and evaluation of LLMs, particularly in contexts where social alignment is critical. By highlighting the inadequacies of current reward models in capturing socially desirable preferences, the authors advocate for a paradigm shift in how these models are assessed. The findings suggest that without rigorous evaluation frameworks that directly measure social preferences, the deployment of LLMs could perpetuate biases and ethical shortcomings. This research paves the way for future studies to refine reward model evaluations and enhance the alignment of LLMs with socially acceptable norms.

Authors: Gayane Ghazaryan, Esra Dönmez  
Source: arXiv:2605.05003  
URL: [https://arxiv.org/abs/2605.05003v1](https://arxiv.org/abs/2605.05003v1)
