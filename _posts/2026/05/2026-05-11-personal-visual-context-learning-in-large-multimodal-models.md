---
title: "Personal Visual Context Learning in Large Multimodal Models"
date: 2026-05-11 17:59:17 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.10936v1"
arxiv_id: "2605.10936"
authors: ["Zihui Xue", "Ami Baid", "Sangho Kim", "Mi Luo", "Kristen Grauman"]
slug: personal-visual-context-learning-in-large-multimodal-models
summary_word_count: 457
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the capability of Large Multimodal Models (LMMs) to effectively utilize personalized visual context for individual users, particularly in the context of wearable devices like smart glasses. The authors introduce the concept of Personal Visual Context Learning (Personal VCL), which is the ability of LMMs to leverage user-specific visual information to resolve personalized queries. The work is presented as a preprint and has not yet undergone peer review. The authors also highlight the lack of systematic evaluation in this area, leading to the development of Personal-VCL-Bench, a benchmark designed to assess the personal visual context across various dimensions, including persons, objects, and behaviors.

**Method**  
The core technical contribution is the introduction of the Agentic Context Bank, which serves as a memory structure that organizes a user's visual context into a self-refining bank. This architecture allows for query-adaptive evidence selection, enabling the model to dynamically choose relevant visual information based on the specific query at hand. The authors evaluate their method against standard context prompting regimes across multiple tasks and LMM backbones, although specific details regarding the architecture, loss functions, and training compute are not disclosed in the abstract. The benchmark, Personal-VCL-Bench, is designed to systematically assess the performance of LMMs in utilizing personal visual context.

**Results**  
The authors report that their Agentic Context Bank consistently outperforms standard context prompting methods across various tasks and evaluated LMM backbones. While specific numerical results and effect sizes are not detailed in the abstract, the consistent improvement indicates a significant enhancement in the models' ability to leverage personalized visual context. The results suggest that the proposed method effectively narrows the context utilization gap identified in existing LMMs.

**Limitations**  
The authors acknowledge that the mechanisms for leveraging visual evidence and aggregating multiple observations remain underexplored. They do not discuss potential limitations related to the scalability of the Agentic Context Bank, the computational overhead introduced by maintaining a self-refining memory bank, or the generalizability of their findings across diverse user populations and contexts. Additionally, the lack of peer review may imply that the methodology and results require further validation.

**Why it matters**  
This work has significant implications for the development of personalized LMMs, particularly in applications involving wearable technology. By formalizing Personal VCL and providing a benchmark for evaluation, the authors lay the groundwork for future research aimed at enhancing the personalization capabilities of LMMs. The introduction of the Agentic Context Bank could lead to more effective user interactions with AI systems, ultimately improving the utility of personal assistants in real-world scenarios. This research could catalyze further exploration into personalized AI, driving advancements in user-centric design and contextual understanding in multimodal systems.

Authors: Zihui Xue, Ami Baid, Sangho Kim, Mi Luo, Kristen Grauman  
Source: arXiv:2605.10936  
URL: https://arxiv.org/abs/2605.10936v1
