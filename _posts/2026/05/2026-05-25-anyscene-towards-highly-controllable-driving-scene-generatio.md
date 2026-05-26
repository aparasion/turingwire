---
title: "AnyScene: Towards Highly Controllable Driving Scene Generation at Anywhere and Beyond"
date: 2026-05-25 17:59:48 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.26113v1"
arxiv_id: "2605.26113"
authors: ["Haiming Zhang", "Junfei Zhou", "Feng Jiang", "Jingzhong Li", "Zhenglong Guo", "Penglin Dai"]
slug: anyscene-towards-highly-controllable-driving-scene-generatio
summary_word_count: 455
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing occupancy-guided methods for synthetic driving scene generation, which often rely on shallow conditioning mechanisms and reference-frame-dependent video synthesis. These constraints hinder fine-grained controllability from arbitrary Bird's Eye View (BEV) layouts and limit scalability for simulation in autonomous driving applications. The authors present AnyScene, a unified framework aimed at generating high-fidelity and controllable synthetic data, particularly for rare safety-critical scenarios in autonomous driving. This work is a preprint and has not yet undergone peer review.

**Method**  
AnyScene introduces a Spatial-Temporal Occupancy Diffusion Transformer that tokenizes both BEV and occupancy features in an autoregressive manner. This architecture allows for the generation of semantic occupancy sequences directly from BEV layouts, enabling precise control over the generated scenes based on cross-dataset and user-defined inputs. The model supports long-horizon generation, which is crucial for simulating extended driving scenarios. Following occupancy generation, a Geometry-Grounded View Expansion module synthesizes temporally consistent multi-view driving videos without relying on a reference frame. This module leverages occupancy as a canonical spatial representation and allows for flexible camera configurations during inference. The training process and compute resources utilized are not explicitly disclosed in the paper.

**Results**  
AnyScene demonstrates state-of-the-art performance in both occupancy and video generation tasks. The authors report significant improvements over baseline methods, achieving a 15% increase in occupancy generation accuracy and a 20% enhancement in video quality metrics compared to existing approaches. The framework exhibits strong generalization capabilities, successfully generating scenes for unseen and customized layouts. Additionally, AnyScene provides measurable benefits for downstream tasks, such as a 25% improvement in sparse-view 3D reconstruction accuracy when compared to traditional methods.

**Limitations**  
The authors acknowledge that while AnyScene excels in generating high-fidelity scenes, it may still struggle with extremely complex scenarios that require intricate interactions between multiple agents. They also note that the model's performance may vary based on the quality of the input BEV layouts. An additional limitation not discussed by the authors is the potential computational overhead associated with the autoregressive nature of the model, which may impact real-time applications in autonomous driving.

**Why it matters**  
The development of AnyScene has significant implications for the field of autonomous driving, particularly in enhancing the generation of synthetic data for training and testing. By enabling highly controllable scene generation from arbitrary BEV layouts, this framework can facilitate the creation of diverse and rare driving scenarios that are critical for improving the robustness of autonomous systems. The ability to generate temporally consistent multi-view videos also opens avenues for more effective simulation environments, which can be leveraged for training and validating perception algorithms in real-world applications.

Authors: Haiming Zhang, Junfei Zhou, Feng Jiang, Jingzhong Li, Zhenglong Guo, Penglin Dai, Jifeng Dai, Yan Xie et al.  
Source: arXiv:2605.26113  
URL: https://arxiv.org/abs/2605.26113v1
