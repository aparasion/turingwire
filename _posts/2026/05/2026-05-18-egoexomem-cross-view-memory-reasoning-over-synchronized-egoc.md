---
title: "EgoExoMem: Cross-View Memory Reasoning over Synchronized Egocentric and Exocentric Videos"
date: 2026-05-18 17:54:55 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.18734v1"
arxiv_id: "2605.18734"
authors: ["Ruiping Liu", "Junwei Zheng", "Yufan Chen", "Di Wen", "Shaofang Quan", "Chengzhi Wu"]
slug: egoexomem-cross-view-memory-reasoning-over-synchronized-egoc
summary_word_count: 442
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in capability for spatial-temporal reasoning in embodied intelligence, specifically focusing on the limitations of egocentric memory alone. The authors introduce EgoExoMem, a novel benchmark for cross-view memory reasoning that utilizes synchronized egocentric and exocentric videos. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the EgoExoMem benchmark, which comprises 2,600 high-quality multiple-choice questions (MCQs) across eight categories of temporal, spatial, and cross-view question-answering (QA) types. To facilitate dual-view retrieval, the authors propose E²-Select, a training-free frame selection method designed for synchronized ego-exo video pairs. E²-Select employs a combination of relevance-based budget allocation and per-view k-DPP (Determinantal Point Process) sampling to address view asymmetry and ensure cross-view temporal consistency. This method allows for effective selection of frames that maximize the utility of both egocentric and exocentric perspectives without requiring extensive training.

**Results**  
The experiments reveal that the integration of ego and exo views provides complementary memory cues, enhancing the reasoning capabilities over existing models. The best-performing model on the benchmark achieves an accuracy of 55.3%, while E²-Select surpasses this with a state-of-the-art performance of 58.2%. This performance is measured against frame-selection and retrieval-augmented generation (RAG)-based memory baselines, indicating a significant improvement in handling the complexities of cross-view memory reasoning. The authors also highlight systematic view-preference conflicts that arise between the framing of questions and the grounding of answers, which presents a unique challenge in this domain.

**Limitations**  
The authors acknowledge that the benchmark is still in its infancy and that existing models, including the best-performing ones, are far from fully solving the tasks presented. They note the inherent challenges in reconciling the differences in perspective between egocentric and exocentric views, which can lead to conflicts in memory retrieval. Additionally, the reliance on a training-free method may limit the adaptability of E²-Select in more complex scenarios where fine-tuning could yield better results. Other potential limitations not explicitly mentioned include the generalizability of the benchmark to real-world applications and the scalability of the proposed methods to larger datasets.

**Why it matters**  
The introduction of EgoExoMem and the E²-Select method has significant implications for advancing research in embodied intelligence and memory reasoning. By providing a structured framework for evaluating cross-view memory tasks, this work lays the groundwork for future studies that can explore more sophisticated models and techniques. The findings underscore the importance of integrating multiple perspectives in memory reasoning, which could lead to improved performance in various applications, including robotics, augmented reality, and human-computer interaction.

Authors: Ruiping Liu, Junwei Zheng, Yufan Chen, Di Wen, Shaofang Quan, Chengzhi Wu, Jiaming Zhang, Kailun Yang et al.  
Source: arXiv:2605.18734  
URL: https://arxiv.org/abs/2605.18734v1
