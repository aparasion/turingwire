---
title: "NeuroTrain: Surveying Local Learning Rules for Spiking Neural Networks with an Open Benchmarking Framework"
date: 2026-05-14 16:50:15 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.15058v1"
arxiv_id: "2605.15058"
authors: ["Alessio Caviglia", "Filippo Marostica", "Roberta Bardini", "Alessandro Savino", "Stefano Di Carlo"]
slug: neurotrain-surveying-local-learning-rules-for-spiking-neural
summary_word_count: 439
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of a unified taxonomy and benchmarking framework for spiking neural networks (SNNs) training algorithms. Despite the rapid development of various training methods, there is no systematic organization that clarifies their relationships and biological inspirations. This gap hinders reproducibility and comparative analysis in the field. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a comprehensive taxonomy of SNN training algorithms, categorizing them into several classes: surrogate-gradient backpropagation, local and three-factor learning rules, biologically inspired plasticity mechanisms, ANN-to-SNN conversion pipelines, and non-standard optimization strategies. Each class is analyzed based on computational principles, learning signals, and locality properties. To facilitate reproducible research, they introduce NeuroTrain, an open-source framework built on snnTorch. NeuroTrain implements a representative set of SNN training algorithms in a modular and extendable manner, allowing for consistent benchmarking across various datasets, architectures, and training regimes. The framework is designed to support the evaluation of different learning rules and their performance in a standardized environment.

**Results**  
While specific quantitative results are not provided in the abstract, the authors emphasize that NeuroTrain enables systematic benchmarking, which can lead to the identification of effective training algorithms for SNNs. The framework's modularity allows researchers to easily compare the performance of different algorithms across multiple datasets and architectures, potentially leading to improved performance metrics in future studies. The authors highlight that the consolidation of fragmented literature through their taxonomy and framework will facilitate more informed comparisons and evaluations.

**Limitations**  
The authors acknowledge that the taxonomy may not encompass all existing SNN training algorithms, particularly those that are emerging or less well-documented. Additionally, the performance metrics derived from NeuroTrain depend on the selected datasets and architectures, which may not represent all possible use cases in SNN applications. The framework's reliance on snnTorch may also limit its accessibility to researchers unfamiliar with this specific library. Furthermore, as a preprint, the findings and methodologies have not yet been validated through peer review, which may affect their credibility.

**Why it matters**  
This work is significant as it provides a structured approach to understanding and comparing SNN training algorithms, which is crucial for advancing the field. By offering a comprehensive taxonomy and a reproducible benchmarking framework, the authors lay the groundwork for future research that can build on these findings. The identification of common patterns and open challenges will guide researchers in developing more efficient and scalable SNN training methods. Ultimately, this could lead to enhanced performance in applications such as neuromorphic computing, robotics, and real-time processing tasks.

Authors: Alessio Caviglia, Filippo Marostica, Roberta Bardini, Alessandro Savino, Stefano Di Carlo  
Source: arXiv:2605.15058  
URL: [https://arxiv.org/abs/2605.15058v1](https://arxiv.org/abs/2605.15058v1)
