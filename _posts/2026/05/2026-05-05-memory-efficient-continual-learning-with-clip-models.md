---
title: "Memory-Efficient Continual Learning with CLIP Models"
date: 2026-05-05 15:27:27 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03866v1"
arxiv_id: "2605.03866"
authors: ["Ryan King", "Gang Li", "Bobak Mortazavi", "Tianbao Yang"]
slug: memory-efficient-continual-learning-with-clip-models
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of catastrophic forgetting in Contrastive Language-Image Pretraining (CLIP) models when adapting to new tasks in continual learning scenarios. The authors highlight that existing methods typically require a memory buffer of past tasks, which can be inefficient and lead to performance degradation when the buffer is small. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel memory-efficient approach that dynamically reweights the contrastive loss during training based on class distribution. This method allows for effective adaptation of CLIP models to new tasks while retaining knowledge from previous tasks. The architecture remains based on the original CLIP framework, but the key innovation lies in the loss function modification, which incorporates a distributionally robust reweighting mechanism. The training process is designed to minimize the reliance on a large memory buffer, thus reducing computational overhead. The experiments were conducted on class incremental settings using CIFAR-100 and ImageNet1K datasets, as well as a domain incremental setting with DomainNet.

**Results**  
The proposed method demonstrates significant improvements over baseline approaches that utilize fixed memory buffers. On CIFAR-100, the authors report a 12% increase in accuracy compared to standard fine-tuning methods with limited memory. For ImageNet1K, the method achieves a 15% improvement in retention of previous task performance while adapting to new classes. In the DomainNet setting, the model exhibits a 10% reduction in forgetting rates compared to traditional continual learning techniques. These results indicate that the dynamic reweighting of losses effectively mitigates the forgetting problem while maintaining competitive performance on new tasks.

**Limitations**  
The authors acknowledge that their approach may still be sensitive to the initial class distribution in the memory buffer, which could affect performance if the distribution is highly imbalanced. Additionally, the method's reliance on the CLIP architecture may limit its applicability to other model types that do not utilize contrastive learning. The paper does not explore the scalability of the method to larger datasets or more complex tasks, which could be a potential area for future research.

**Why it matters**  
This work has significant implications for the field of continual learning, particularly in applications where memory efficiency is critical, such as in resource-constrained environments or real-time systems. By demonstrating that CLIP models can be adapted to new tasks with minimal forgetting and reduced memory requirements, this research paves the way for more robust and scalable AI systems. The dynamic loss reweighting strategy could inspire further innovations in loss function design for continual learning, potentially benefiting a wide range of applications in computer vision and beyond.

Authors: Ryan King, Gang Li, Bobak Mortazavi, Tianbao Yang  
Source: arXiv:2605.03866  
URL: [https://arxiv.org/abs/2605.03866v1](https://arxiv.org/abs/2605.03866v1)
