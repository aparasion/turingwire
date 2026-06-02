---
title: "MASER: Modality-Adaptive Specialist Routing for Embodied 3D Spatial Intelligence"
date: 2026-06-01 16:36:21 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02463v1"
arxiv_id: "2606.02463"
authors: ["Hilton Raj", "Vishnuram AV"]
slug: maser-modality-adaptive-specialist-routing-for-embodied-3d-s
summary_word_count: 412
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces MASER, a framework for modality-adaptive routing in embodied agents, enhancing spatial reasoning across multiple modalities."
---

**Problem**  
Existing Vision-Language Models (VLMs) are typically fine-tuned on a single modality, which limits their effectiveness in 3D environments where questions may require reasoning across multiple modalities (e.g., natural language, RGB images, point clouds). This paper addresses the gap in capability where the semantics of a question may favor a modality different from the one the model is fine-tuned on. The authors present MASER (Modality-Adaptive Specialist Routing), a preprint work that proposes a solution to this limitation by enabling embodied agents to dynamically select the most appropriate modality for answering spatially relevant questions.

**Method**  
MASER employs a lightweight framework that consists of five modality adapters built on a shared VLM backbone. The architecture includes a frozen sentence transformer for encoding questions, which generates embeddings that are then processed through a small Multi-layer Perceptron (MLP). This MLP is trained on oracle adapter-accuracy labels to learn a neural routing policy that selects the best modality adapter during inference. The training process involves optimizing the routing policy to maximize the accuracy of the selected modality based on the specific question context. The framework is designed to make a single adapter call per question, enhancing efficiency.

**Results**  
The authors evaluate MASER on the Open3D-VQA benchmark, demonstrating that no single modality is universally optimal for all questions. Specifically, point-cloud answers are optimal in 51.5% of cases. MASER achieves an oracle agreement of 51.3%, significantly outperforming a Random-Forest ablation model, which achieved only 43.5%. These results indicate that the modality-adaptive routing effectively improves the accuracy of embodied agents in spatial reasoning tasks.

**Limitations**  
The authors acknowledge that the performance of MASER is contingent on the quality of the oracle adapter-accuracy labels used for training the MLP. Additionally, the framework's reliance on a shared VLM backbone may limit its adaptability to more complex or diverse environments not represented in the training data. The paper does not address potential scalability issues when integrating more modalities or the computational overhead associated with training multiple adapters.

**Why it matters**  
The introduction of MASER has significant implications for the development of more capable embodied agents that can navigate and reason in complex 3D environments. By enabling dynamic modality selection, MASER enhances the ability of agents to interpret and respond to spatial queries more effectively, paving the way for advancements in applications such as robotics, augmented reality, and interactive AI systems. This work contributes to the ongoing discourse in multimodal learning and spatial intelligence, as discussed in related literature, and is available on [arXiv](https://arxiv.org/abs/2606.02463v1).
