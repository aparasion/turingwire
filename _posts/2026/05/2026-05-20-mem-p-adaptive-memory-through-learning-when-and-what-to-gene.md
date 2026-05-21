---
title: "Mem-$π$: Adaptive Memory through Learning When and What to Generate"
date: 2026-05-20 17:51:05 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21463v1"
arxiv_id: "2605.21463"
authors: ["Xiaoqiang Wang", "Chao Wang", "Hadi Nekoei", "Christopher Pal", "Alexandre Lacoste", "Spandana Gella"]
slug: mem-p-adaptive-memory-through-learning-when-and-what-to-gene
summary_word_count: 404
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing memory-augmented agents that rely on static, similarity-based retrieval from external memory stores. These agents often fail to provide contextually relevant guidance, leading to misalignment with the current task. The authors propose Mem-$\pi$, a framework that generates adaptive memory on demand, rather than retrieving pre-stored information. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Mem-$\pi$ employs a dedicated language or vision-language model, distinct from the downstream agent, to generate context-specific guidance. The architecture is designed to condition the generation of guidance on the current context of the agent, allowing it to dynamically decide both when to generate guidance and what form that guidance should take. The training employs a decision-content decoupled reinforcement learning (RL) objective, which enables the model to abstain from generating guidance when it would not be beneficial. This approach contrasts with traditional memory systems that rely on fixed entries, enhancing the adaptability of the agent in complex tasks.

**Results**  
Mem-$\pi$ demonstrates significant performance improvements across various agentic benchmarks, including web navigation, terminal-based tool use, and text-based embodied interaction. The framework achieves over 30% relative improvement on web navigation tasks compared to retrieval-based and prior RL-optimized memory baselines. Specific performance metrics and comparisons to named baselines are not detailed in the abstract, but the reported effect sizes indicate a substantial enhancement in task performance.

**Limitations**  
The authors acknowledge that while Mem-$\pi$ improves adaptability and context alignment, it may still face challenges in scenarios where the model's generative capabilities are insufficient to produce high-quality guidance. Additionally, the reliance on a separate model for guidance generation could introduce overhead in terms of computational resources and latency. The paper does not address potential issues related to the scalability of the model or its performance in highly dynamic environments where context changes rapidly.

**Why it matters**  
The implications of Mem-$\pi$ extend to the development of more sophisticated LLM agents capable of handling complex tasks with greater contextual awareness. By moving away from static memory retrieval to on-demand generation, this framework could enhance the efficiency and effectiveness of AI systems in real-world applications, such as autonomous agents in web navigation and interactive environments. The approach also opens avenues for further research into adaptive memory systems and their integration into various AI architectures.

Authors: Xiaoqiang Wang, Chao Wang, Hadi Nekoei, Christopher Pal, Alexandre Lacoste, Spandana Gella, Bang Liu, Perouz Taslakian  
Source: arXiv:2605.21463  
URL: https://arxiv.org/abs/2605.21463v1
