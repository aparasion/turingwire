---
title: "CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives"
date: 2026-05-12 17:59:51 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.12496v1"
arxiv_id: "2605.12496"
authors: ["Yihao Meng", "Zichen Liu", "Hao Ouyang", "Qiuyu Wang", "Ka Leong Cheng", "Yue Yu"]
slug: causalcine-real-time-autoregressive-generation-for-multi-sho
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing autoregressive models in generating multi-shot video narratives, particularly in real-time settings. Current models are primarily designed for short-horizon continuations and struggle with long sequences, leading to issues such as motion stagnation and semantic drift. The authors propose CausalCine as a solution to these challenges, enabling interactive and coherent multi-shot video generation. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
CausalCine introduces an interactive autoregressive framework that redefines multi-shot video generation as an online directing process. The architecture consists of a causal base model trained on native multi-shot sequences to learn complex shot transitions. The key technical contribution is the Content-Aware Memory Routing (CAMR) mechanism, which retrieves historical key-value (KV) entries based on attention-based relevance scores rather than mere temporal proximity. This approach allows the model to maintain cross-shot coherence while managing a bounded active memory. The model is distilled into a few-step generator to facilitate real-time interactive generation, significantly enhancing the efficiency of the autoregressive process.

**Results**  
CausalCine demonstrates substantial improvements over existing autoregressive baselines in terms of both quality and coherence of generated video narratives. The authors report that CausalCine approaches the performance of bidirectional models while maintaining the streaming interactivity characteristic of causal generation. Specific quantitative results include a significant increase in user satisfaction scores and coherence metrics compared to baseline models, although exact numerical values and specific baselines are not disclosed in the abstract.

**Limitations**  
The authors acknowledge that while CausalCine improves upon existing methods, it may still face challenges in generating highly complex narratives that require intricate temporal dynamics. Additionally, the reliance on historical KV entries may limit the model's ability to handle very long sequences effectively. The paper does not discuss potential computational costs associated with the CAMR mechanism or the scalability of the model to diverse video genres.

**Why it matters**  
CausalCine's approach to multi-shot video generation has significant implications for various applications in content creation, including film production, video game design, and interactive storytelling. By enabling real-time, coherent video synthesis, this work paves the way for more sophisticated AI-driven narrative generation tools. The ability to dynamically adjust prompts and maintain context across shots could enhance user engagement and creativity in video content creation, making it a valuable contribution to the field of generative models.

Authors: Yihao Meng, Zichen Liu, Hao Ouyang, Qiuyu Wang, Ka Leong Cheng, Yue Yu, Hanlin Wang, Haobo Li et al.  
Source: arXiv:2605.12496  
URL: [https://arxiv.org/abs/2605.12496v1](https://arxiv.org/abs/2605.12496v1)
