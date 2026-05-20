---
title: "CaMo: Camera Motion Grounded Evaluation and Training for Vision-Language Models"
date: 2026-05-19 17:50:25 +0000
category: research
subcategory: evaluation_benchmarks
company: "Cognition"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.20165v1"
arxiv_id: "2605.20165"
authors: ["Hsiang-Wei Huang", "Junbin Lu", "Kuang-Ming Chen", "Jianxu Shangguan", "Cheng-Yen Yang", "Jenq-Neng Hwang"]
slug: camo-camera-motion-grounded-evaluation-and-training-for-visi
summary_word_count: 465
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of Vision-Language Models (VLMs) concerning their understanding of camera motion, which is crucial for spatial cognition. Existing spatial VLMs demonstrate high accuracy on spatial question answering benchmarks, but the authors argue that these metrics do not adequately reflect the models' spatial intelligence. They introduce the Spatial Narrative Score (SNS) as a novel evaluation framework that requires VLMs to generate spatial narratives that incorporate both scene semantics and camera motion. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose CaMo, a camera motion grounded VLM designed to enhance the spatial reasoning capabilities of existing models. CaMo integrates a mechanism for generating explicit spatial narratives that detail camera motion alongside scene semantics. The architecture details are not fully disclosed, but the model is trained on a dataset that emphasizes camera motion understanding. The training process involves leveraging a frozen proxy LLM to reason about the generated narratives, thereby ensuring that the model's outputs are grounded in both spatial and motion contexts. The authors provide their code, data, and model for public access, facilitating reproducibility and further research.

**Results**  
CaMo demonstrates a marked improvement in performance when evaluated using the SNS framework compared to state-of-the-art spatial VLMs. Specifically, while existing models show significant performance degradation under SNS, CaMo maintains consistent performance across both SNS evaluation and traditional spatial question answering tasks. The paper reports that CaMo achieves a 15% increase in SNS scores over the best-performing baseline VLMs, which highlights the effectiveness of grounding VLMs in camera motion understanding. The results underscore the necessity of evaluating VLMs with a focus on spatial narrative generation to ensure robust spatial reasoning capabilities.

**Limitations**  
The authors acknowledge that the SNS framework may not capture all aspects of spatial reasoning and that further refinements could enhance its robustness. Additionally, the reliance on a frozen proxy LLM for reasoning may limit the adaptability of CaMo to dynamic contexts where real-time reasoning is required. The paper does not address potential biases in the training data or the generalizability of the model across diverse spatial scenarios, which could affect its applicability in real-world tasks.

**Why it matters**  
This work has significant implications for the development of VLMs, particularly in applications requiring nuanced spatial understanding, such as robotics, augmented reality, and autonomous navigation. By emphasizing the importance of camera motion in spatial reasoning, the authors pave the way for future research that integrates motion dynamics into VLM architectures. The introduction of the SNS framework also sets a new standard for evaluating VLMs, encouraging the community to adopt more comprehensive metrics that reflect true spatial intelligence rather than superficial accuracy.

Authors: Hsiang-Wei Huang, Junbin Lu, Kuang-Ming Chen, Jianxu Shangguan, Cheng-Yen Yang, Jenq-Neng Hwang  
Source: arXiv cs.CV  
URL: [https://arxiv.org/abs/2605.20165v1](https://arxiv.org/abs/2605.20165v1)
