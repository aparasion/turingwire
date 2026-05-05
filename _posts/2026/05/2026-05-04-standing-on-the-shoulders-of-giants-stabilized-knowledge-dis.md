---
title: "Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection"
date: 2026-05-04 17:37:16 +0000
category: research
subcategory: other
company: "DeepSeek"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02860v1"
arxiv_id: "2605.02860"
authors: ["Mohamad Khajezade", "Fatemeh H. Fard", "Mohamed Sami Shehata"]
slug: standing-on-the-shoulders-of-giants-stabilized-knowledge-dis
summary_word_count: 418
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing methods for cross-language code clone detection (X-CCD), particularly the challenges posed by semantically equivalent programs in different programming languages that exhibit minimal surface similarity. The authors highlight the drawbacks of using large language models (LLMs) as black-box systems, including issues related to cost, reproducibility, privacy, and inconsistent output formatting. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a knowledge distillation framework that transfers reasoning capabilities from a larger model, DeepSeek-R1, to more compact open-source student models for X-CCD. The methodology involves constructing reasoning-oriented synthetic training data from cross-language code pairs sourced from Project CodeNet. The student models, Phi3 and Qwen-Coder, are fine-tuned using Low-Rank Adaptation (LoRA) adapters. To enhance model reliability, the authors introduce several response stabilization techniques: forced conclusion prompting, a binary classification head, and a contrastive classification head. The training process leverages these techniques to improve the models' predictive metrics and response rates.

**Results**  
The experimental evaluation includes comparisons across multiple language pairs: Python–Java, Rust–Java, Rust–Python, and Rust–Ruby. The results indicate that knowledge distillation significantly enhances the reliability of compact models, with notable improvements in predictive performance, particularly under distribution shifts. The introduction of classification-head variants leads to a substantial reduction in inference time compared to traditional generation-based inference methods. Specific performance metrics, such as accuracy and F1 scores, are not disclosed in the abstract, but the authors assert that their approach consistently outperforms baseline models in the context of X-CCD.

**Limitations**  
The authors acknowledge that their approach may still be limited by the inherent challenges of X-CCD, such as the diversity of programming languages and the complexity of semantic equivalence. They do not discuss potential overfitting issues that may arise from the synthetic training data or the generalizability of their findings to other language pairs not included in their experiments. Additionally, the reliance on LoRA adapters may limit the scalability of the approach to larger models or different architectures.

**Why it matters**  
This work has significant implications for the field of code clone detection, particularly in enhancing the practicality and reliability of compact models for X-CCD. By demonstrating that reasoning-oriented distillation combined with response stabilization can improve model performance, the authors provide a pathway for developing more efficient and accessible tools for software analysis. This could facilitate broader adoption of X-CCD techniques in real-world applications, where resource constraints and model interpretability are critical considerations.

Authors: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata  
Source: arXiv:2605.02860  
URL: [https://arxiv.org/abs/2605.02860v1](https://arxiv.org/abs/2605.02860v1)
