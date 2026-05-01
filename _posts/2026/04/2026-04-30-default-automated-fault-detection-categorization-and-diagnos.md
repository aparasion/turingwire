---
title: "DEFault++: Automated Fault Detection, Categorization, and Diagnosis for Transformer Architectures"
date: 2026-04-30 17:07:11 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28118v1"
arxiv_id: "2604.28118"
authors: ["Sigma Jahan", "Saurabh Singh Rajput", "Tushar Sharma", "Mohammad Masudur Rahman"]
slug: default-automated-fault-detection-categorization-and-diagnos
summary_word_count: 424
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the fault diagnosis capabilities for transformer architectures, which are prevalent in critical AI applications. Existing techniques primarily focus on generic deep neural networks and lack specificity in identifying faults within transformer components. The authors present DEFault++, a novel approach that aims to detect, categorize, and diagnose faults specific to transformers, which often degrade model performance without triggering runtime errors. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
DEFault++ employs a hierarchical learning-based diagnostic framework that operates at three levels of abstraction: fault detection, fault categorization, and root cause diagnosis. The architecture utilizes a Fault Propagation Graph (FPG) that maps the relationships between transformer components, allowing for targeted analysis. The model is trained on DEFault-bench, a benchmark dataset comprising 3,739 labeled instances generated through systematic mutation testing across seven transformer models and nine downstream tasks. The mutation technique, DEForm, introduces faults specific to transformer architectures. The diagnosis process leverages prototype matching and supervised contrastive learning to produce interpretable results. The authors do not disclose specific training compute details.

**Results**  
DEFault++ achieves an area under the receiver operating characteristic curve (AUROC) of 0.96 for fault detection and a Macro-F1 score of 0.85 for both fault categorization and root cause diagnosis on the DEFault-bench. These results significantly outperform existing baselines, demonstrating the model's effectiveness in diagnosing faults in both encoder and decoder architectures. Additionally, a developer study involving 21 practitioners showed that the accuracy of selecting appropriate repair actions improved from 57.1% without DEFault++ to 83.3% with its assistance, indicating a substantial practical impact.

**Limitations**  
The authors acknowledge that DEFault++ is limited to the specific transformer architectures and tasks included in the DEFault-bench, which may not generalize to all transformer models or novel architectures. Furthermore, the reliance on systematic mutation testing may not capture all possible fault scenarios encountered in real-world applications. The study also does not address the computational overhead introduced by the diagnostic process, which could affect deployment in resource-constrained environments.

**Why it matters**  
The implications of DEFault++ are significant for the reliability and robustness of transformer-based models in critical applications. By providing a systematic approach to fault detection and diagnosis, this work enables practitioners to identify and rectify issues that could otherwise lead to degraded model performance. The framework can serve as a foundation for future research aimed at enhancing the resilience of transformer architectures, potentially influencing the design of more fault-tolerant AI systems.

Authors: Sigma Jahan, Saurabh Singh Rajput, Tushar Sharma, Mohammad Masudur Rahman  
Source: arXiv:2604.28118  
URL: [https://arxiv.org/abs/2604.28118v1](https://arxiv.org/abs/2604.28118v1)
