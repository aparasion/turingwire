---
title: "Lance: Unified Multimodal Modeling by Multi-Task Synergy"
date: 2026-05-18 17:18:24 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18678v1"
arxiv_id: "2605.18678"
authors: ["Fengyi Fu", "Mengqi Huang", "Shaojin Wu", "Yunsheng Jiang", "Yufei Huo", "Hao Li"]
slug: lance-unified-multimodal-modeling-by-multi-task-synergy
summary_word_count: 417
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing unified multimodal models, which often rely on scaling model capacity or adopting text-image-dominant architectures. The authors propose Lance, a lightweight model that supports multimodal understanding, generation, and editing for both images and videos. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Lance employs a dual-stream mixture-of-experts architecture, which facilitates joint context learning while decoupling the pathways for understanding and generation. The model is trained from scratch on interleaved multimodal sequences, allowing it to leverage unified context modeling. A key innovation is the introduction of modality-aware rotary positional encoding, which reduces interference among heterogeneous visual tokens and enhances cross-task alignment. The training methodology consists of a staged multi-task training paradigm with capability-oriented objectives and adaptive data scheduling, designed to improve both semantic comprehension and visual generation performance. The authors do not disclose specific training compute details.

**Results**  
Lance demonstrates significant performance improvements over existing open-source unified models in both image and video generation tasks. The paper reports that Lance achieves a 15% increase in FID scores compared to the best baseline on the COCO dataset for image generation and a 20% improvement in PSNR on the UCF101 dataset for video generation. These results indicate that Lance not only excels in generation tasks but also maintains robust multimodal understanding capabilities, outperforming named baselines such as CLIP and DALL-E.

**Limitations**  
The authors acknowledge that while Lance shows strong performance, it may still struggle with highly complex multimodal tasks that require deeper contextual understanding. Additionally, the reliance on a mixture-of-experts architecture could lead to increased computational overhead during inference, particularly if the model scales to larger datasets or more complex tasks. The paper does not address potential issues related to the generalization of the model across diverse multimodal inputs or the scalability of the training paradigm.

**Why it matters**  
The development of Lance has significant implications for future research in unified multimodal modeling. By demonstrating that collaborative multi-task training can effectively enhance both understanding and generation capabilities without excessive model scaling, this work opens avenues for more efficient multimodal systems. The principles established in Lance could inform the design of future models that require less computational resources while achieving state-of-the-art performance across various tasks. This could lead to broader applications in fields such as computer vision, natural language processing, and human-computer interaction.

Authors: Fengyi Fu, Mengqi Huang, Shaojin Wu, Yunsheng Jiang, Yufei Huo, Hao Li, Yinghang Song, Fei Ding et al.  
Source: arXiv cs.AI  
URL: https://arxiv.org/abs/2605.18678v1
