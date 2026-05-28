---
title: "Multi-Mixer Models: Flexible Sequence Modeling with Shared Representations"
date: 2026-05-27 17:26:09 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28769v1"
arxiv_id: "2605.28769"
authors: ["Kevin Y. Li", "Asher Trockman", "Ananda Theertha Suresh", "Ziteng Sun"]
slug: multi-mixer-models-flexible-sequence-modeling-with-shared-re
summary_word_count: 437
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing linear recurrent models and hybrid architectures in handling long-context retrieval and in-context learning tasks. While linear attention and state space models offer linear compute and constant memory advantages, they still fall short in performance compared to traditional softmax attention models, particularly in scenarios requiring extensive context. The authors propose a novel approach to hybrid modeling that allows for dynamic switching between different token mixing methods throughout the sequence, which has not been extensively explored in the literature. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of Oryx, a hybrid model that flexibly alternates between different mixers—specifically, quadratic attention for rich context utilization and linear recurrent models for efficient generation. Oryx is designed to share at least 90% of its parameters across these mixers, allowing both attention and recurrent modes to operate on shared internal representations. The authors validate Oryx using Mamba-2 and Gated DeltaNet variants, scaling up to 1.4 billion parameters. The training employs a mixed-training strategy under fixed token budgets, optimizing for both efficiency and performance.

**Results**  
Oryx demonstrates competitive performance against single-mixer baselines across various benchmarks. At the 1.4B parameter scale, Oryx outperforms its respective baselines by a minimum of 0.7 percentage points on averaged language modeling tasks. In retrieval tasks, Oryx achieves performance on par with the Transformer baseline while processing less than 10% of the tokens in attention mode. These results indicate that Oryx effectively leverages the strengths of both attention and linear recurrent models, achieving a balance between efficiency and contextual richness.

**Limitations**  
The authors acknowledge that while Oryx shows improved performance, it may still not fully bridge the gap in tasks requiring extensive long-context retrieval compared to pure attention models. Additionally, the reliance on shared parameters may introduce constraints on the model's ability to specialize in certain tasks. The paper does not address potential scalability issues or the impact of varying the proportion of tokens processed in attention mode on overall performance.

**Why it matters**  
The implications of this work are significant for the development of future sequence models. By demonstrating that attention and linear recurrent models can effectively share internal representations, the authors open new avenues for hybrid model architectures that can adaptively optimize for different tasks within a single framework. This approach could lead to more efficient models capable of handling a wider range of applications, particularly in natural language processing and other sequence-based tasks, where both context and efficiency are critical.

Authors: Kevin Y. Li, Asher Trockman, Ananda Theertha Suresh, Ziteng Sun  
Source: arXiv:2605.28769  
URL: [https://arxiv.org/abs/2605.28769v1](https://arxiv.org/abs/2605.28769v1)
