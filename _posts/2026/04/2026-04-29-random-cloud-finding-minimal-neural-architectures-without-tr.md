---
title: "Random Cloud: Finding Minimal Neural Architectures Without Training"
date: 2026-04-29 15:57:01 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26830v1"
arxiv_id: "2604.26830"
authors: ["Javier Gil Bl\u00e1zquez"]
slug: random-cloud-finding-minimal-neural-architectures-without-tr
summary_word_count: 451
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in neural architecture search (NAS) methodologies that require extensive training cycles, particularly the inefficiencies associated with post-training pruning techniques. The proposed method, Random Cloud, is a training-free approach that seeks to discover minimal feedforward network architectures without the need for backpropagation or retraining, which is a common limitation in existing NAS frameworks. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of Random Cloud lies in its stochastic exploration and progressive structural reduction of neural architectures. The method begins with randomly initialized networks and evaluates their performance without any training. It employs a systematic approach to reduce the network topology by removing less significant connections, thereby identifying minimal architectures. Only the best-performing candidate from this exploration is subjected to training, which significantly reduces the computational overhead associated with traditional NAS methods. The paper does not disclose specific details regarding the architecture of the networks used or the exact training compute required for the final candidate, focusing instead on the efficiency of the search process itself.

**Results**  
Random Cloud was evaluated on seven classification benchmarks, where it was compared against magnitude pruning and random pruning baselines. The results indicate that Random Cloud matches or outperforms both baselines in six out of seven datasets. Notably, on the Sonar dataset, it achieved a statistically significant improvement of +4.9 percentage points in accuracy (p=0.017) while also achieving an 87% reduction in parameters. Furthermore, the method demonstrated superior efficiency, being faster than both pruning baselines in four out of five datasets, with a training cost ranging from 0.67 to 0.94 times that of full training.

**Limitations**  
The authors acknowledge that the Random Cloud method may not generalize well to all types of neural architectures, particularly more complex or specialized models. Additionally, the reliance on random initialization may lead to variability in results, which could affect reproducibility. The paper does not address potential limitations related to the scalability of the method for larger datasets or more complex tasks, nor does it explore the implications of the reduced parameter count on model performance in real-world applications.

**Why it matters**  
The implications of this work are significant for the field of neural architecture search, as it presents a novel approach that circumvents the computationally expensive training cycles typically associated with architecture optimization. By demonstrating that effective architectures can be identified without full training, Random Cloud opens avenues for more efficient NAS methodologies, potentially accelerating the development of lightweight models suitable for deployment in resource-constrained environments. This could lead to broader applications in areas such as edge computing and mobile AI, where computational resources are limited.

Authors: Javier Gil Blázquez  
Source: arXiv:2604.26830  
URL: [https://arxiv.org/abs/2604.26830v1](https://arxiv.org/abs/2604.26830v1)
