---
title: "DMGD: Train-Free Dataset Distillation with Semantic-Distribution Matching in Diffusion Models"
date: 2026-05-05 15:37:50 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.03877v1"
arxiv_id: "2605.03877"
authors: ["Qichao Wang", "Yunhong Lu", "Hengyuan Cao", "Junyi Zhang", "Min Zhang"]
slug: dmgd-train-free-dataset-distillation-with-semantic-distribut
summary_word_count: 420
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing dataset distillation methods, particularly those based on diffusion models, which often require additional fine-tuning stages and lack effective guidance mechanisms. The authors propose a novel approach, DMGD (Dual Matching Guided Diffusion), to enable dataset distillation without the need for training, thereby filling a gap in the literature regarding efficient and effective dataset distillation techniques. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The DMGD framework introduces two key components: Semantic Matching and Distribution Matching. Semantic Matching is achieved through conditional likelihood optimization, which eliminates the reliance on auxiliary classifiers typically used in previous methods. The framework employs a dynamic guidance mechanism that enhances the diversity of the generated synthetic datasets while ensuring semantic alignment with the original dataset. Additionally, the authors implement an optimal transport (OT) based Distribution Matching approach to align the generated data with the target distribution structure. To optimize computational efficiency, two strategies are introduced: Distribution Approximate Matching and Greedy Progressive Matching, which facilitate effective distribution matching guidance with minimal computational overhead.

**Results**  
The DMGD framework was evaluated on three benchmarks: ImageNet-Woof, ImageNet-Nette, and ImageNet-1K. The results indicate that DMGD outperforms state-of-the-art methods that require additional fine-tuning. Specifically, DMGD achieves average accuracy gains of 2.1% on ImageNet-Woof, 5.4% on ImageNet-Nette, and 2.4% on ImageNet-1K compared to these baselines. These improvements demonstrate the effectiveness of the proposed training-free approach in dataset distillation.

**Limitations**  
The authors acknowledge that while DMGD eliminates the need for fine-tuning, it may still be sensitive to the choice of hyperparameters in the semantic and distribution matching processes. Additionally, the paper does not explore the scalability of the method to larger datasets beyond those tested. There is also no discussion on the potential impact of noise in the original datasets on the performance of the distilled datasets, which could be a significant factor in practical applications.

**Why it matters**  
The implications of this work are substantial for the field of machine learning, particularly in scenarios where computational resources are limited or where rapid prototyping of models is required. By providing a training-free method for dataset distillation, DMGD can facilitate the development of more efficient models, enabling researchers to leverage large datasets without the associated computational burden. This could lead to broader adoption of dataset distillation techniques in various applications, including transfer learning and few-shot learning, where the availability of labeled data is often a bottleneck.

Authors: Qichao Wang, Yunhong Lu, Hengyuan Cao, Junyi Zhang, Min Zhang  
Source: arXiv:2605.03877  
URL: [https://arxiv.org/abs/2605.03877v1](https://arxiv.org/abs/2605.03877v1)
