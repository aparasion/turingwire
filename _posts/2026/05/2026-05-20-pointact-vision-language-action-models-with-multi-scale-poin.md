---
title: "PointACT: Vision-Language-Action Models with Multi-Scale Point-Action Interaction"
date: 2026-05-20 17:10:31 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.21414v1"
arxiv_id: "2605.21414"
authors: ["Shizhe Chen", "Paul Pacaud", "Cordelia Schmid"]
slug: pointact-vision-language-action-models-with-multi-scale-poin
summary_word_count: 393
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing Vision-Language-Action (VLA) models that predominantly utilize 2D visual representations, which hinder their ability to effectively reason about fine-grained geometry and spatial grounding necessary for precise robotic manipulation in 3D environments. The authors propose PointACT, a dual-system VLA model that integrates 3D point cloud representations into the action decoding process. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
PointACT introduces a multi-scale point-action interaction mechanism that leverages hierarchical 3D point cloud data. The architecture employs efficient bottleneck window self-attention, allowing evolving action tokens to attend to both local geometric details and the global scene structure. The model is trained on the LIBERO and RLBench benchmarks, with a focus on comparing its performance against both monolithic and dual-system VLA baselines, including those augmented with point cloud inputs. The training process involves fine-tuning a pretrained vision-language backbone, as well as training an action expert from scratch, particularly emphasizing the integration of 3D geometry with 2D semantic representations.

**Results**  
PointACT demonstrates significant performance improvements over state-of-the-art pretrained VLA models. Specifically, it achieves a 10% increase in success rates on the RLBench-10Tasks suite compared to existing baselines. The model shows even larger performance gains when the vision-language backbone is frozen, indicating the effectiveness of training the action expert independently. The results are consistent across both LIBERO and RLBench benchmarks, underscoring the robustness of the proposed architecture.

**Limitations**  
The authors acknowledge that while PointACT shows improved performance, it may still be limited by the quality and resolution of the input point cloud data. Additionally, the reliance on pretrained models may introduce biases from the training data, which could affect generalization to novel tasks. The paper does not address potential computational overhead associated with processing 3D point clouds, which may impact real-time applications in robotic manipulation.

**Why it matters**  
The implications of this work are significant for the development of more capable robotic systems that require nuanced understanding and interaction with 3D environments. By demonstrating the effectiveness of integrating hierarchical 3D representations with VLA models, PointACT paves the way for future research into more sophisticated robotic manipulation strategies. This approach could enhance the performance of robots in complex tasks, leading to advancements in fields such as autonomous navigation, human-robot interaction, and general-purpose robotic applications.

Authors: Shizhe Chen, Paul Pacaud, Cordelia Schmid  
Source: arXiv:2605.21414  
URL: [https://arxiv.org/abs/2605.21414v1](https://arxiv.org/abs/2605.21414v1)
