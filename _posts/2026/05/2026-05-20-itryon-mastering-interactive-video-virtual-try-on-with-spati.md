---
title: "iTryOn: Mastering Interactive Video Virtual Try-On with Spatial-Semantic Guidance"
date: 2026-05-20 17:23:32 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.21431v1"
arxiv_id: "2605.21431"
authors: ["Jun Zheng", "Zhengze Xu", "Mengting Chen", "Jing Wang", "Jinsong Lan", "Xiaoyong Zhu"]
slug: itryon-mastering-interactive-video-virtual-try-on-with-spati
summary_word_count: 453
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the literature on Video Virtual Try-On (VVT) by introducing the Interactive Video Virtual Try-On (Interactive VVT) task. Existing VVT methods primarily focus on non-interactive scenarios, where garments are displayed without accounting for user interactions. This oversight limits the realism and applicability of virtual try-on systems in real-world contexts, where users actively engage with clothing. The authors formalize the challenges of Interactive VVT, which include resolving semantic ambiguities from standard pose data and learning complex garment deformations during brief interactive moments. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose iTryOn, a novel framework that leverages a large-scale video diffusion Transformer architecture. The core technical contributions include a multi-level interaction injection mechanism that enhances the generation of complex garment dynamics. At the spatial level, iTryOn employs a garment-agnostic 3D hand prior to provide detailed guidance for hand-garment interactions, effectively addressing spatial ambiguities. At the semantic level, the framework utilizes global captions for contextual understanding and time-stamped action captions for localized interaction guidance, synchronized through a novel Action-aware Rotational Position Embedding (A-RoPE). The training process involves extensive datasets, although specific compute resources and dataset sizes are not disclosed.

**Results**  
iTryOn demonstrates state-of-the-art performance on traditional VVT benchmarks, outperforming existing methods in both standard and interactive settings. The authors report significant improvements in metrics such as temporal consistency and interaction realism, although specific numerical results and comparisons to named baselines are not detailed in the abstract. The framework's ability to handle complex interactions marks a substantial advancement over previous approaches, indicating a commanding lead in the new interactive VVT task.

**Limitations**  
The authors acknowledge several limitations, including the potential for overfitting to the training data due to the complexity of the model and the sparsity of interactive moments in the video data. They also note that the reliance on 3D hand priors may not generalize well across diverse garment types and user interactions. Additionally, the paper does not address the computational efficiency of the model during inference, which could impact real-time applications.

**Why it matters**  
The introduction of Interactive VVT and the iTryOn framework has significant implications for the future of virtual try-on technologies. By enabling more dynamic and controllable interactions, this work paves the way for enhanced user experiences in e-commerce and fashion industries. The methodologies developed could also inspire further research into interactive machine learning applications, particularly in areas requiring real-time user feedback and engagement. The advancements in semantic and spatial guidance mechanisms may lead to broader applications in augmented reality and human-computer interaction.

Authors: Jun Zheng, Zhengze Xu, Mengting Chen, Jing Wang, Jinsong Lan, Xiaoyong Zhu, Kaifu Zhang, Bo Zheng et al.  
Source: arXiv:2605.21431  
URL: https://arxiv.org/abs/2605.21431v1
