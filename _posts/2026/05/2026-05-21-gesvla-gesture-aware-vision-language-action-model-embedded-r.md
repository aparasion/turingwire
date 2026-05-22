---
title: "GesVLA: Gesture-Aware Vision-Language-Action Model Embedded Representations"
date: 2026-05-21 17:57:44 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.22812v1"
arxiv_id: "2605.22812"
authors: ["Wenxuan Guo", "Ziyuan Li", "Meng Zhang", "Yichen Liu", "Yimeng Dong", "Chuxi Xu"]
slug: gesvla-gesture-aware-vision-language-action-model-embedded-r
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing Vision-Language-Action (VLA) models, which predominantly rely on textual instructions and struggle with spatial ambiguity in complex scenes containing multiple similar objects. The authors propose a novel approach that incorporates gesture as an additional instruction modality to enhance the model's performance in robot manipulation tasks. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Gesture-aware Vision-Language-Action model (GesVLA), which integrates gesture features into the latent space of the model. This integration allows gesture representations to influence both high-level reasoning and low-level action generation. The architecture employs a dual-VLM framework that tightly couples gesture representations with action policies. To generate training data, the authors developed a scalable gesture data generation pipeline that renders hand models onto real-world scene images, effectively bridging the sim-to-real visual gap. This pipeline produces diverse motion patterns and corresponding pointing annotations. The model is trained using a two-stage strategy: the first stage focuses on gesture perception, while the second stage emphasizes action prediction, ensuring that the model learns to interpret gestures effectively and translate them into actions.

**Results**  
The GesVLA model was evaluated on various robotic tasks, including a controlled block manipulation task and more practical scenarios such as product and produce selection. The results indicate that the incorporation of gesture significantly enhances target grounding accuracy and improves human-robot interaction efficiency. Specifically, the model achieved a notable increase in performance metrics compared to baseline VLA models, particularly in complex and cluttered environments. While exact numerical results are not disclosed in the abstract, the authors emphasize the consistent improvement across tasks, suggesting a substantial effect size.

**Limitations**  
The authors acknowledge several limitations, including the potential for gesture misinterpretation in highly dynamic environments and the reliance on a specific gesture dataset that may not encompass all possible human gestures. Additionally, the model's performance may vary based on the quality of the rendered gesture data and the complexity of the scenes. An obvious limitation not explicitly mentioned is the scalability of the gesture data generation pipeline, which may require significant computational resources for large-scale deployment.

**Why it matters**  
The introduction of gesture as a parallel instruction modality in VLA models has significant implications for the field of robotic manipulation. By enhancing the model's ability to resolve spatial ambiguities and improve interaction efficiency, this work paves the way for more intuitive human-robot collaboration. The dual-VLM architecture and the gesture data generation pipeline could serve as foundational components for future research, potentially leading to more advanced models capable of understanding and executing complex tasks in real-world environments.

Authors: Wenxuan Guo, Ziyuan Li, Meng Zhang, Yichen Liu, Yimeng Dong, Chuxi Xu, Yunfei Wei, Ze Chen et al.  
Source: arXiv:2605.22812  
URL: https://arxiv.org/abs/2605.22812v1
