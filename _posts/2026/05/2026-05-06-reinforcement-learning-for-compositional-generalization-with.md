---
title: "Reinforcement Learning for Compositional Generalization with Outcome-Level Optimization"
date: 2026-05-06 13:47:31 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.04920v1"
arxiv_id: "2605.04920"
authors: ["Xiyan Fu", "Wei Liu"]
slug: reinforcement-learning-for-compositional-generalization-with
summary_word_count: 397
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of compositional generalization in reinforcement learning (RL), specifically focusing on the limitations of existing supervised fine-tuning methods that rely on token-level training. The authors argue that these methods fail to capture the global compositional structure necessary for generalizing to novel combinations of known primitives. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach that leverages outcome-level reinforcement learning to enhance compositional generalization. They utilize Group Relative Policy Optimization (GRPO) to optimize models based on feedback derived from their final outputs rather than individual tokens. Two reward structures are explored: a simple binary outcome reward and a composite reward that incorporates additional feedback on the composition. The training process involves multiple compositional benchmarks, although specific details regarding the architecture, training compute, and dataset sizes are not disclosed.

**Results**  
The experiments demonstrate that the proposed RL approach significantly outperforms traditional supervised fine-tuning methods across various compositional benchmarks. Notably, the RL models exhibit improved performance in terms of generalization to unseen compositions, particularly for complex composition types. The authors report that supervised models tend to overfit to frequent training compositions, while the RL framework effectively reshapes the output distribution, leading to enhanced generalization capabilities. However, specific numerical results and effect sizes are not provided in the summary.

**Limitations**  
The authors acknowledge that their approach may require substantial computational resources due to the nature of reinforcement learning, which can be more demanding than supervised learning. Additionally, they do not address potential issues related to the scalability of their method to larger, more complex datasets or the generalizability of their findings across different domains. The reliance on specific reward structures may also limit the applicability of the method to other tasks that do not fit the proposed framework.

**Why it matters**  
This work has significant implications for the field of machine learning, particularly in the context of developing models that can generalize to novel situations without extensive retraining. By shifting the focus from token-level to outcome-level optimization, the authors provide a new perspective on how RL can be utilized to tackle compositional generalization. This approach could pave the way for more robust AI systems capable of understanding and generating complex combinations of elements, which is crucial for applications in natural language processing, robotics, and beyond.

Authors: Xiyan Fu, Wei Liu  
Source: arXiv:2605.04920  
URL: https://arxiv.org/abs/2605.04920v1
