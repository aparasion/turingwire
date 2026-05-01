---
title: "AesRM: Improving Video Aesthetics with Expert-Level Feedback"
date: 2026-04-30 16:24:07 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.28078v1"
arxiv_id: "2604.28078"
authors: ["Yujin Han", "Yujie Wei", "Yefei He", "Xinyu Liu", "Tianle Li", "Zichao Yu"]
slug: aesrm-improving-video-aesthetics-with-expert-level-feedback
summary_word_count: 428
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the evaluation and enhancement of video aesthetics, which is critical for applications like filmmaking. Existing research predominantly focuses on visual fidelity and lacks a systematic framework for assessing video aesthetics, often relying on vague definitions of visual pleasure. The authors propose a structured approach to evaluate video aesthetics through a hierarchical rubric that encompasses three dimensions: Visual Aesthetics (VA), Visual Fidelity (VF), and Visual Plausibility (VP), along with 15 fine-grained criteria. This framework facilitates the creation of a large-scale expert-annotated dataset and a benchmark for aesthetic evaluation.

**Method**  
The core technical contribution is the development of Video Aesthetic Reward Models (AesRM), specifically AesRM-Base and AesRM-CoT. AesRM-Base predicts pairwise preferences across the three aesthetic dimensions, providing efficient post-training rewards. AesRM-CoT enhances interpretability by generating Chains of Thought (CoT) aligned with the 15 criteria. The training process employs a three-stage progressive scheme:  
1. **Atomic Aesthetic Capability Learning**: Focuses on fundamental aesthetic concepts, such as shot composition.  
2. **Cold-Start**: Aligns the model with structured reasoning protocols to improve initial performance.  
3. **GRPO (Gradient Reinforcement Policy Optimization)**: Further refines evaluation accuracy.  
Additionally, self-consistency-based CoT synthesis is introduced to enhance CoT quality, and CoT-based process rewards are designed during GRPO. The training compute details are not disclosed.

**Results**  
AesRM demonstrates superior performance compared to existing aesthetic reward models across multiple benchmarks, including the newly introduced AesVideo-Bench, which consists of approximately 2500 video pairs annotated by experts. The authors report significant improvements in robustness and lower position bias, although specific numerical results and effect sizes against named baselines are not provided in the abstract.

**Limitations**  
The authors acknowledge that their framework is still in the early stages and may require further validation across diverse video genres and styles. They do not address potential biases in expert annotations or the scalability of the model to real-time applications. Additionally, the reliance on expert feedback may limit the generalizability of the model to broader audiences.

**Why it matters**  
This work has significant implications for downstream applications in video generation and editing, particularly in enhancing the aesthetic quality of generated content. By establishing a rigorous framework for evaluating video aesthetics, it paves the way for more nuanced and effective aesthetic models that can be integrated into creative tools for filmmakers and content creators. The introduction of AesRM could lead to advancements in automated video editing and generation systems, ultimately improving the quality of visual media.

Authors: Yujin Han, Yujie Wei, Yefei He, Xinyu Liu, Tianle Li, Zichao Yu, Andi Han, Shiwei Zhang et al.  
Source: arXiv:2604.28078  
URL: [https://arxiv.org/abs/2604.28078v1](https://arxiv.org/abs/2604.28078v1)
