---
title: "Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation"
date: 2026-05-18 17:57:04 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18740v1"
arxiv_id: "2605.18740"
authors: ["Qianhao Yuan", "Jie Lou", "Xing Yu", "Hongyu Lin", "Le Sun", "Xianpei Han"]
slug: vision-opd-learning-to-see-fine-details-for-multimodal-llms-
summary_word_count: 428
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in fine-grained visual understanding in Multimodal Large Language Models (MLLMs), particularly the regional-to-global perception gap. The authors note that MLLMs perform better on fine-grained tasks when provided with evidence-centered image crops rather than full images. This suggests that the primary issue is not the model's ability to recognize local features but rather its difficulty in focusing on relevant evidence within a broader context. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose Vision-OPD (Vision On-Policy Distillation), a self-distillation framework that facilitates the transfer of regional perception capabilities from a crop-conditioned teacher model to a full-image-conditioned student model. Vision-OPD operates by instantiating two conditional policies from the same MLLM: the teacher model processes image crops, while the student model processes full images. The training involves generating on-policy rollouts from the student and minimizing the token-level divergence between the next-token distributions of the teacher and student during these rollouts. This approach allows the model to learn the advantages of focusing on specific regions of an image without relying on external teacher models, ground-truth labels, or additional inference-time tools.

**Results**  
Vision-OPD demonstrates competitive or superior performance on several fine-grained visual understanding benchmarks compared to larger models, including both open-source and closed-source alternatives, as well as "Thinking-with-Images" agentic models. Specific performance metrics are not disclosed in the abstract, but the authors claim that their method outperforms existing models, indicating a significant improvement in the ability to leverage fine-grained visual details for multimodal tasks.

**Limitations**  
The authors acknowledge that their approach may be limited by the inherent capabilities of the underlying MLLM architecture. Additionally, the reliance on self-distillation may not generalize well to all types of visual tasks, particularly those requiring external contextual information or complex reasoning beyond visual cues. The paper does not address potential computational overhead associated with the dual-policy training process or the scalability of the method to larger datasets or more complex multimodal tasks.

**Why it matters**  
The implications of this work are significant for the development of MLLMs, particularly in applications requiring nuanced visual understanding, such as image captioning, visual question answering, and interactive AI systems. By improving the ability of MLLMs to focus on relevant visual evidence, Vision-OPD could enhance the performance of these models in real-world applications where fine details are critical. This research opens avenues for further exploration of self-distillation techniques and their potential to bridge perception gaps in multimodal learning.

Authors: Qianhao Yuan, Jie Lou, Xing Yu, Hongyu Lin, Le Sun, Xianpei Han, Yaojie Lu  
Source: arXiv:2605.18740  
URL: [https://arxiv.org/abs/2605.18740v1](https://arxiv.org/abs/2605.18740v1)
