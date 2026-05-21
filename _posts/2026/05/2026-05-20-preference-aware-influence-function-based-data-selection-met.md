---
title: "Preference-aware Influence-function-based Data Selection Method for Efficient Fine-Tuning"
date: 2026-05-20 17:15:43 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.21422v1"
arxiv_id: "2605.21422"
authors: ["Qihao Lin", "Guanxu Chen", "Dongrui Liu", "Jing Shao"]
slug: preference-aware-influence-function-based-data-selection-met
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiency in data selection methods for fine-tuning large language models (LLMs), particularly in the context of allocating limited training resources to samples that best enhance target behaviors. Existing approaches typically treat target examples uniformly, neglecting the varying relevance of these examples to the model's current state. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors introduce PRISM (PReference-aware Influence-function-based Data Selection Method for Efficient Fine-Tuning), which innovatively incorporates the model's current preferences to weight target examples. This is achieved by constructing a preference-aware target representation that reflects the model's existing behavior. The method employs influence functions to score candidate training samples based on their alignment with this representation. The theoretical foundation of PRISM suggests that this preference weighting provides a more effective first-order direction for enhancing the model's alignment with the target behavior. The authors do not disclose specific details regarding the architecture of the models used, the loss functions, or the exact compute resources allocated for training.

**Results**  
PRISM demonstrates significant improvements in both efficient fine-tuning and safety-oriented supervised fine-tuning (SFT) repair across various model families and scales. The paper reports that PRISM outperforms baseline methods, although specific numerical results and effect sizes are not detailed in the abstract. The authors emphasize that the precise characterization of target behaviors is crucial for achieving budget-efficient data selection, suggesting that PRISM can lead to more effective training outcomes compared to traditional methods.

**Limitations**  
The authors acknowledge that their approach may be limited by the quality of the initial model's preferences and the representativeness of the target examples. They do not address potential scalability issues when applying PRISM to extremely large datasets or the computational overhead introduced by calculating influence functions. Additionally, the generalizability of the method across different domains or tasks remains unexamined.

**Why it matters**  
The implications of this work are significant for the field of machine learning, particularly in the context of fine-tuning LLMs. By demonstrating that a preference-aware approach to data selection can lead to more efficient training, this research paves the way for future studies to explore similar methodologies in other areas of model training and optimization. The findings suggest that enhancing the characterization of target behaviors can lead to more effective use of training budgets, which is critical as LLMs continue to scale and the demand for efficient training methods increases.

Authors: Qihao Lin, Guanxu Chen, Dongrui Liu, Jing Shao  
Source: arXiv:2605.21422  
URL: [https://arxiv.org/abs/2605.21422v1](https://arxiv.org/abs/2605.21422v1)
