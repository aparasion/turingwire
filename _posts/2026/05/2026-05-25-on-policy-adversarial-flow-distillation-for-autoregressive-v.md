---
title: "On-Policy Adversarial Flow Distillation for Autoregressive Video Generation"
date: 2026-05-25 17:58:12 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.26105v1"
arxiv_id: "2605.26105"
authors: ["Yang Luo", "Shengju Qian", "Xiaohang Tang", "Zirui Zhu", "Yong Liu", "Xin Wang"]
slug: on-policy-adversarial-flow-distillation-for-autoregressive-v
summary_word_count: 469
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of distilling knowledge from heterogeneous black-box video generators into autoregressive (AR) models. Existing methods struggle with the constraints of off-policy learning, where the student model must learn from its own rollout distribution while the teacher provides only completed video prompts. This gap complicates the application of traditional supervised fine-tuning and score-based distillation techniques, which are not suitable for the unique requirements of video generation. The authors propose a novel approach, Adversarial Flow Distillation (AFD), to facilitate on-policy distillation without relying on teacher scores or complex alignment processes. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core contribution of this paper is the AFD framework, which operates on an on-policy basis. AFD involves querying the teacher model and rolling out the student model on the same prompts, allowing for direct comparison. The method employs a prompt-paired Bradley-Terry discriminator to estimate the discrepancy between the teacher's clean samples and the student's outputs. This discrepancy is then transformed into flow-matching updates for the student's noised states, effectively providing dense supervision for the student's learning process. Notably, AFD does not require teacher scores, latent variables, denoising trajectories, or reverse-chain reinforcement learning, making it a streamlined approach for video distillation. The authors conduct experiments using two families of causal AR student models, demonstrating the versatility of AFD.

**Results**  
The experimental results indicate that AFD significantly enhances the performance of AR video generation models. Specifically, the method shows improvements in motion and physics-sensitive generation while maintaining overall video quality. The authors report that AFD outperforms baseline methods, although specific quantitative metrics and comparisons to named baselines are not detailed in the abstract. Ablation studies further confirm the effectiveness of adaptive on-policy feedback and the importance of forward-process credit assignment in the distillation process.

**Limitations**  
The authors acknowledge that AFD's reliance on clean teacher videos and student rollouts may limit its applicability in scenarios where such data is not readily available. Additionally, while the method improves performance, the paper does not provide extensive quantitative comparisons against a wide range of existing state-of-the-art methods, which could provide a clearer context for its effectiveness. The lack of peer review also raises questions about the robustness of the findings.

**Why it matters**  
The implications of this work are significant for the field of video generation, particularly in applications requiring efficient and effective distillation of complex models. AFD offers a practical solution for leveraging proprietary or heterogeneous video generators, potentially enabling the development of more capable AR models for streaming, long-horizon, and interactive applications. By addressing the limitations of existing distillation techniques, this research paves the way for future advancements in autoregressive video generation and related domains.

Authors: Yang Luo, Shengju Qian, Xiaohang Tang, Zirui Zhu, Yong Liu, Xin Wang, Yang You  
Source: arXiv:2605.26105  
URL: https://arxiv.org/abs/2605.26105v1
