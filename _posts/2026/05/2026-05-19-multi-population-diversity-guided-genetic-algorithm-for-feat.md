---
title: "Multi-population Diversity-guided Genetic Algorithm for Feature Selection in Network Intrusion Detection"
date: 2026-05-19 13:57:28 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.19864v1"
arxiv_id: "2605.19864"
authors: ["Chunzhen Li"]
slug: multi-population-diversity-guided-genetic-algorithm-for-feat
summary_word_count: 433
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing Genetic Algorithm (GA)-based feature selection methods in the context of Network Intrusion Detection Systems (NIDS). Specifically, it highlights the challenges of maintaining population diversity and the lack of guidance in evolutionary operators when dealing with high-dimensional and redundant traffic features. The authors propose a novel approach, the Multi-Population Diversity-Guided Genetic Algorithm (MPDGGA), to overcome these issues. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this study is the MPDGGA, which employs a chained multi-population evolutionary structure. This architecture allows for the simultaneous evolution of multiple populations, enhancing the exploration of the feature space. A key innovation is the introduction of a diversity-guided operator that leverages the information gain ratio to inform the selection of features. This operator aims to maintain diversity within the populations while guiding the evolutionary process towards more informative features. The training process involves standard GA operations such as selection, crossover, and mutation, but with the added complexity of managing multiple populations and the diversity-guided operator.

**Results**  
The MPDGGA was evaluated on three benchmark datasets: NSL-KDD, UNSW-NB15, and nine datasets from the UCI repository. The results indicate that MPDGGA significantly outperforms four other advanced multi-population feature selection models. Specifically, it achieved the highest accuracy on 10 out of the 11 datasets tested, with a minimum feature selection rate of 2.26%. The paper provides detailed performance metrics, including accuracy, precision, recall, and F1-score, demonstrating substantial improvements over baseline models, although exact numerical comparisons are not specified in the abstract.

**Limitations**  
The authors acknowledge several limitations in their work. First, the reliance on the information gain ratio may not generalize well across all types of datasets, particularly those with non-linear relationships among features. Additionally, the computational complexity of managing multiple populations may limit scalability to very large datasets. The paper does not address the potential for overfitting due to the high dimensionality of the feature space, nor does it explore the impact of varying population sizes on performance.

**Why it matters**  
The implications of this research are significant for the field of cybersecurity, particularly in enhancing the efficacy of NIDS through improved feature selection methods. By addressing the challenges of population diversity and operator guidance in GAs, the MPDGGA presents a promising approach that could lead to more robust and efficient intrusion detection systems. This work lays the groundwork for future research into multi-population evolutionary algorithms and their applications in high-dimensional feature selection tasks, potentially influencing the design of more adaptive and intelligent cybersecurity solutions.

Authors: Chunzhen Li  
Source: arXiv:2605.19864  
URL: [https://arxiv.org/abs/2605.19864v1](https://arxiv.org/abs/2605.19864v1)
