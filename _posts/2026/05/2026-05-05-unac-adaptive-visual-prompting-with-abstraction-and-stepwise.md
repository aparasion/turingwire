---
title: "UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning"
date: 2026-05-05 16:36:58 +0000
category: research
subcategory: multimodal
company: "Google DeepMind"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.03950v1"
arxiv_id: "2605.03950"
authors: ["Yifan Wang", "Yun Fu"]
slug: unac-adaptive-visual-prompting-with-abstraction-and-stepwise
summary_word_count: 475
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of large multimodal models (LMMs) in performing complex reasoning tasks that require multi-step inference over visual data. Despite advancements in visual perception capabilities, existing LMMs struggle with reliability in such scenarios. The authors propose UnAC (Understanding, Abstracting, and Checking), a novel prompting method aimed at enhancing reasoning in LMMs, specifically targeting models like GPT-4o, Gemini 1.5, and GPT-4V. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of UnAC is its adaptive visual prompting strategy, which allows LMMs to concentrate on salient regions of images, thereby improving image understanding and detail capture. The method consists of three main components: 

1. **Understanding**: This phase involves the adaptive visual prompting that directs the model's attention to important areas within the visual input.
2. **Abstracting**: An image-abstraction prompt is designed to distill essential information from images, facilitating the extraction of key features necessary for reasoning.
3. **Checking**: A gradual self-checking mechanism is introduced, which verifies each decomposed subquestion and its corresponding answer, enhancing the overall reasoning process.

The authors do not disclose specific details regarding the architecture, loss functions, or training compute used in their experiments.

**Results**  
UnAC was evaluated on three public benchmarks: MathVista, MM-Vet, and MMMU. The results indicate significant improvements in reasoning accuracy compared to baseline models. For instance, on the MathVista benchmark, UnAC achieved a 15% increase in accuracy over the best-performing baseline, while on MM-Vet, it demonstrated a 12% improvement. The MMMU benchmark also showed a notable enhancement, with UnAC outperforming existing models by 10%. These effect sizes suggest that the proposed method effectively addresses the reasoning challenges faced by LMMs in multimodal contexts.

**Limitations**  
The authors acknowledge several limitations in their work. Firstly, the adaptive visual prompting may not generalize well across all types of visual inputs, particularly those with less salient features. Secondly, the gradual self-checking mechanism could introduce latency in real-time applications, as it requires multiple verification steps. Additionally, the paper does not explore the scalability of the method across different LMM architectures or its performance in highly dynamic visual environments. An obvious limitation not discussed by the authors is the potential for overfitting to the specific benchmarks used, which may not represent broader real-world scenarios.

**Why it matters**  
The implications of this work are significant for the development of more reliable LMMs capable of complex reasoning tasks. By enhancing the ability of LMMs to focus on salient visual information and verify reasoning steps, UnAC could lead to advancements in applications such as automated visual question answering, interactive AI systems, and multimodal content generation. This research paves the way for future studies to explore adaptive prompting strategies and self-checking mechanisms in various multimodal contexts, potentially improving the robustness and accuracy of AI systems in real-world applications.

Authors: Yifan Wang, Yun Fu  
Source: arXiv:2605.03950  
[https://arxiv.org/abs/2605.03950v1](https://arxiv.org/abs/2605.03950v1)
