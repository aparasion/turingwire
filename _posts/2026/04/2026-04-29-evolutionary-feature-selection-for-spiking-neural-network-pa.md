---
title: "Evolutionary feature selection for spiking neural network pattern classifiers"
date: 2026-04-29 13:21:09 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2604.26654v1"
arxiv_id: "2604.26654"
authors: ["Michal Valko", "Nuno C. Marques", "Marco Castelani"]
slug: evolutionary-feature-selection-for-spiking-neural-network-pa
summary_word_count: 433
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of traditional multi-layer perceptron (MLP) models in handling noisy data for classification tasks. Specifically, it explores the gap in feature selection methodologies when applied to biologically inspired spiking neural networks (SNNs), particularly the JASTAP model. The authors aim to demonstrate that evolutionary algorithms can enhance feature selection and network training in SNNs, which have not been extensively studied in this context.

**Method**  
The core technical contribution is the integration of an evolutionary feature selection algorithm with the JASTAP spiking neural network model. The JASTAP model is characterized by its biologically realistic neuron dynamics, which differ from the activation functions used in MLPs. The evolutionary procedure involves a genetic algorithm that optimizes both the selection of input features and the parameters of the JASTAP model. The authors utilize the IRIS dataset for preliminary experiments, focusing on the model's ability to maintain classification accuracy while reducing network size and improving robustness to noise. The training compute specifics are not disclosed, but the evolutionary approach suggests a potentially higher computational cost due to the iterative nature of genetic algorithms.

**Results**  
The results indicate that the JASTAP model, when combined with the evolutionary feature selection, achieves comparable classification accuracy to traditional MLPs while utilizing fewer neurons. Specifically, the authors report that their approach can handle a higher level of noise in the data without significant degradation in performance. While exact numerical results are not provided in the abstract, the implication is that the evolutionary method leads to a more efficient model in terms of both size and robustness, outperforming standard MLPs under noisy conditions.

**Limitations**  
The authors acknowledge that their study is preliminary and limited to the IRIS dataset, which may not fully represent the complexities of real-world data. They do not address the scalability of their approach to larger datasets or more complex classification tasks. Additionally, the computational overhead introduced by the evolutionary algorithm is not quantified, which could be a significant factor in practical applications. The reliance on a single dataset limits the generalizability of the findings.

**Why it matters**  
This work has implications for the development of more efficient and robust spiking neural networks, particularly in applications where data is noisy or incomplete. By demonstrating that evolutionary algorithms can enhance feature selection in SNNs, the authors open avenues for further research into biologically inspired models that can compete with traditional deep learning architectures. This could lead to advancements in neuromorphic computing and applications in robotics, sensory processing, and other fields where real-time data handling is critical.

Authors: Michal Valko, Nuno C. Marques, Marco Castelani  
Source: arXiv:2604.26654  
URL: [https://arxiv.org/abs/2604.26654v1](https://arxiv.org/abs/2604.26654v1)
