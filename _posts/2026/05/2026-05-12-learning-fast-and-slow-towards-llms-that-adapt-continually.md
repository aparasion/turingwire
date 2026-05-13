---
title: "Learning, Fast and Slow: Towards LLMs That Adapt Continually"
date: 2026-05-12 17:58:20 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12484v1"
arxiv_id: "2605.12484"
authors: ["Rishabh Tiwari", "Kusha Sareen", "Lakshya A Agrawal", "Joseph E. Gonzalez", "Matei Zaharia", "Kurt Keutzer"]
slug: learning-fast-and-slow-towards-llms-that-adapt-continually
summary_word_count: 483
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of current large language models (LLMs) in continual learning scenarios, specifically the issues of catastrophic forgetting and the trade-off between in-context learning and parameter updates. Traditional methods either update model parameters, leading to loss of generalization, or rely solely on in-context learning, which lacks the performance of parameter updates. The authors propose a framework that integrates both approaches, inspired by human cognitive learning processes, to enhance LLM adaptability without sacrificing foundational reasoning capabilities.

**Method**  
The authors introduce a Fast-Slow Training (FST) framework, where model parameters are treated as "slow" weights and optimized context as "fast" weights. The fast weights are designed to learn from textual feedback, allowing the model to adapt to task-specific requirements while maintaining the generalization capabilities of the slow weights. The training process involves a dual mechanism where fast weights are updated rapidly based on immediate task feedback, while slow weights are updated less frequently, preserving the model's foundational knowledge. The authors report that FST is up to 3x more sample-efficient than traditional reinforcement learning (RL) methods and achieves a higher performance asymptote. The training compute details are not disclosed, but the architecture remains consistent with existing LLM frameworks.

**Results**  
FST demonstrates significant improvements over traditional RL methods across various reasoning tasks. The models trained with FST exhibit up to 70% less Kullback-Leibler (KL) divergence from the base LLM compared to those trained solely with RL, indicating reduced catastrophic forgetting. In continual learning scenarios, FST models effectively adapt to new tasks without performance degradation, outperforming parameter-only RL models, which tend to stall in learning new tasks. The authors provide quantitative results showing that FST-trained models consistently achieve higher accuracy on benchmark tasks, although specific numerical results and baseline comparisons are not detailed in the abstract.

**Limitations**  
The authors acknowledge that while FST improves sample efficiency and reduces catastrophic forgetting, it may still be sensitive to the quality of the textual feedback used for fast weight updates. Additionally, the framework's performance in highly dynamic environments with rapid task shifts remains to be fully evaluated. The paper does not address potential computational overhead introduced by maintaining two sets of weights, nor does it explore the implications of fast weight updates on model interpretability.

**Why it matters**  
The proposed FST framework has significant implications for the development of more robust and adaptable LLMs, particularly in applications requiring continual learning and adaptation to new tasks. By effectively balancing the trade-offs between in-context and parameter-based learning, this approach could lead to advancements in AI systems that require ongoing learning in dynamic environments, such as conversational agents, personalized recommendation systems, and adaptive educational tools. The integration of fast and slow learning mechanisms may also inspire future research into hybrid learning paradigms in machine learning.

Authors: Rishabh Tiwari, Kusha Sareen, Lakshya A Agrawal, Joseph E. Gonzalez, Matei Zaharia, Kurt Keutzer, Inderjit S Dhillon, Rishabh Agarwal et al.  
Source: arXiv:2605.12484  
URL: https://arxiv.org/abs/2605.12484v1
