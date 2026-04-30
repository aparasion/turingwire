---
title: "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising"
date: 2026-04-29 14:01:54 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26694v1"
arxiv_id: "2604.26694"
authors: ["Jun Guo", "Qiwei Li", "Peiyan Li", "Zilong Chen", "Nan Sun", "Yifei Su"]
slug: unified-4d-world-action-modeling-from-video-priors-with-asyn
summary_word_count: 432
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing unified world models, particularly those like UWM, which only operate in 2D pixel-space and struggle to balance action efficiency with high-quality world modeling. The authors propose X-WAM, a Unified 4D World Model that integrates real-time robotic action execution with high-fidelity 4D world synthesis, encompassing both video and 3D reconstruction. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
X-WAM leverages pretrained video diffusion models to predict multi-view RGB-D videos, enhancing spatial information retrieval through a lightweight structural adaptation. This adaptation involves replicating the final layers of the pretrained Diffusion Transformer into a dedicated depth prediction branch, facilitating the reconstruction of future spatial data. The core innovation is the Asynchronous Noise Sampling (ANS) technique, which optimizes both generation quality and action decoding efficiency. ANS employs a specialized asynchronous denoising schedule during inference, allowing for rapid action decoding with fewer steps while dedicating the full sequence of steps to generate high-fidelity video. This method samples from the joint distribution of timesteps during training to align with the inference distribution, thus improving the model's performance.

**Results**  
X-WAM was pretrained on over 5,800 hours of robotic data and demonstrated impressive performance on the RoboCasa and RoboTwin 2.0 benchmarks. It achieved an average success rate of 79.2% on RoboCasa and 90.7% on RoboTwin 2.0. In addition to these success rates, X-WAM produced high-fidelity 4D reconstructions that surpassed existing methods in both visual and geometric metrics, indicating a significant improvement over prior models.

**Limitations**  
The authors acknowledge that while X-WAM improves upon previous models, it may still face challenges in generalization across diverse environments and tasks, particularly those not represented in the training data. Additionally, the reliance on pretrained video diffusion models may limit the model's adaptability to scenarios where such priors are not available. The paper does not discuss potential computational costs associated with the training and inference of the model, which could be a concern for real-time applications.

**Why it matters**  
The development of X-WAM has significant implications for the fields of robotics and computer vision, particularly in applications requiring real-time decision-making and high-fidelity environmental modeling. By unifying action execution and world synthesis, this work paves the way for more sophisticated robotic systems capable of operating in complex, dynamic environments. The integration of asynchronous denoising techniques could also inspire future research into efficient model architectures that balance performance and computational efficiency, potentially influencing the design of next-generation robotic systems.

Authors: Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang et al.  
Source: arXiv:2604.26694  
URL: [https://arxiv.org/abs/2604.26694v1](https://arxiv.org/abs/2604.26694v1)
