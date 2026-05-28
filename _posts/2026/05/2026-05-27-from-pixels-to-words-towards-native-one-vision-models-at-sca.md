---
title: "From Pixels to Words -- Towards Native One-Vision Models at Scale"
date: 2026-05-27 17:59:55 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.28820v1"
arxiv_id: "2605.28820"
authors: ["Haiwen Diao", "Jiahao Wang", "Penghao Wu", "Yuhao Dong", "Yuwei Niu", "Yue Zhu"]
slug: from-pixels-to-words-towards-native-one-vision-models-at-sca
summary_word_count: 406
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of current vision-language models (VLMs) that rely on a modular framework, which separates image encoders and language decoders. This fragmentation leads to suboptimal pixel-level signal processing and weakens early pixel-word interactions. While native VLMs have shown promise in single-image tasks, their application in multi-image, video understanding, and spatial intelligence remains underexplored. The authors propose a solution to this gap by introducing NEO-ov, a native foundation model designed to learn cross-frame and pixel-word correspondences in an end-to-end manner.

**Method**  
NEO-ov is architecturally distinct from traditional VLMs as it eliminates the need for external encoders, auxiliary adapters, or post-hoc fusion mechanisms. Instead, it integrates fine-grained spatiotemporal modeling directly within the model architecture. The authors detail their training methodology, which includes extensive architectural analyses and recipes aimed at optimizing performance for native multimodal tasks. While specific training compute details are not disclosed, the model is designed to scale effectively, suggesting a robust training regime that leverages large datasets for comprehensive learning.

**Results**  
NEO-ov demonstrates competitive performance against established modular VLMs, achieving significant improvements in fine-grained visual perception tasks. The authors report that NEO-ov narrows the performance gap with modular counterparts, although specific quantitative results (e.g., accuracy, F1 scores) against named baselines on standard benchmarks are not provided in the abstract. The model's ability to handle multi-image and video understanding tasks is highlighted, indicating a substantial advancement in the capabilities of native VLMs.

**Limitations**  
The authors acknowledge that while NEO-ov shows promise, it is still in the early stages of exploration for multi-image and video tasks. They do not address potential scalability issues related to training on extremely large datasets or the computational costs associated with deploying such a model in real-world applications. Additionally, the lack of detailed performance metrics against specific baselines limits the ability to fully assess the model's effectiveness.

**Why it matters**  
The introduction of NEO-ov has significant implications for the future of multimodal modeling. By demonstrating that native "one-vision" architectures can achieve competitive performance at scale, this work paves the way for more integrated approaches to vision-language tasks. The findings encourage further exploration into end-to-end models that can process complex spatiotemporal data without the fragmentation inherent in traditional architectures. This could lead to advancements in applications such as video analysis, interactive AI systems, and enhanced human-computer interaction.

Authors: Haiwen Diao, Jiahao Wang, Penghao Wu, Yuhao Dong, Yuwei Niu, Yue Zhu, Zhongang Cai, Weichen Fan et al.  
Source: arXiv:2605.28820  
URL: https://arxiv.org/abs/2605.28820v1
