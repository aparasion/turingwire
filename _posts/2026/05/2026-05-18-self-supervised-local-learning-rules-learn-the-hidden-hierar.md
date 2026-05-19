---
title: "Self-supervised local learning rules learn the hidden hierarchical structure of high-dimensional data"
date: 2026-05-18 15:37:28 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.18557v1"
arxiv_id: "2605.18557"
authors: ["Ariane Delrocq", "Wu S. Zihan", "Guillaume Bellec", "Wulfram Gerstner"]
slug: self-supervised-local-learning-rules-learn-the-hidden-hierar
summary_word_count: 457
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how biologically plausible learning rules can effectively capture the hierarchical structure inherent in high-dimensional sensory data. While deep neural networks (DNNs) have demonstrated success in various tasks, the plasticity mechanisms that facilitate such learning in biological systems remain largely unexplored. The authors investigate local learning rules within the framework of the Random Hierarchy Model (RHM), an artificial dataset designed to simulate the hierarchical nature of real-world data.

**Method**  
The study evaluates two categories of local learning rules. The first category employs direct feedback signals to approximate error propagation from the output layer, which is a common approach in traditional DNN training. The second category utilizes layerwise self-supervised learning techniques, including both contrastive and non-contrastive loss functions, that do not rely on explicit error approximation at the output layer. The authors conduct experiments to assess the performance of these learning rules on the RHM tasks, focusing on their ability to learn the underlying hierarchical structure efficiently. The training compute details are not disclosed, but the emphasis is on the data efficiency of the second type of learning rules compared to supervised backpropagation.

**Results**  
The results indicate that the first category of learning rules fails to solve the RHM tasks, primarily due to input-specific nonlinearities, referred to as "masking," which are critical for learning complex tasks in full backpropagation. In contrast, the second category of self-supervised learning rules successfully learns the hierarchical structure of the RHM tasks. Notably, these algorithms demonstrate data efficiency comparable to that of supervised backpropagation, suggesting that they can achieve similar performance with potentially less labeled data. The authors do not provide specific numerical results or effect sizes against named baselines, which limits the quantitative assessment of their findings.

**Limitations**  
The authors acknowledge that the first type of learning rules is inadequate for the tasks at hand, attributing this to the absence of essential nonlinearities present in backpropagation. However, they do not discuss the scalability of their proposed methods to more complex or real-world datasets beyond the RHM. Additionally, the reliance on self-supervised learning raises questions about the generalizability of these rules to tasks requiring explicit supervision. The lack of detailed training compute metrics also limits the reproducibility of their results.

**Why it matters**  
This work has significant implications for the development of biologically inspired learning algorithms that can operate efficiently in high-dimensional spaces. By demonstrating that self-supervised local learning rules can effectively capture hierarchical structures, the findings may inform future research on neural network architectures that mimic biological learning processes. This could lead to advancements in unsupervised and semi-supervised learning paradigms, potentially reducing the dependency on labeled data in machine learning applications.

Authors: Ariane Delrocq, Wu S. Zihan, Guillaume Bellec, Wulfram Gerstner  
Source: arXiv:2605.18557  
URL: https://arxiv.org/abs/2605.18557v1
