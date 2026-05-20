---
title: "Optimal Representation Size: High-Dimensional Analysis of Pretraining and Linear Probing"
date: 2026-05-19 16:56:56 +0000
category: research
subcategory: training_methods
company: "ServiceNow"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20105v1"
arxiv_id: "2605.20105"
authors: ["Valentina Njaradi", "Cl\u00e9mentine Domin\u00e9", "Rachel Swanson", "Marco Mondelli", "Andrew Saxe"]
slug: optimal-representation-size-high-dimensional-analysis-of-pre
summary_word_count: 483
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the interplay between representation size during pretraining and its impact on downstream task performance, particularly in high-dimensional settings. While the two-stage paradigm of pretraining followed by fine-tuning or linear probing is widely adopted, there is limited analytical insight into how representation dimensionality affects generalization, especially when balancing unlabelled and labelled data. The authors aim to formalize this relationship and provide a framework for optimizing representation size based on task-specific parameters.

**Method**  
The authors propose an analytical model that formalizes the structure extraction process as principal component analysis (PCA) applied to unlabelled data, while downstream learning is modeled as linear regression on a separate labelled dataset. They derive exact expressions for both training and generalization error in the high-dimensional regime, explicitly linking these errors to the representation dimensionality, the sizes of unlabelled and labelled datasets, and the alignment of tasks. The model reveals that the optimal representation size is contingent on the availability of pretraining data and the amount of downstream data. Specifically, they identify conditions under which compressed representations yield better generalization when pretraining data is abundant, while higher-dimensional representations are preferable when pretraining data is limited. The authors also quantify the trade-off between unlabelled and labelled data, providing a metric for how much unlabelled data can substitute for a single labelled sample.

**Results**  
The analytical results indicate that the choice of representation size significantly influences downstream generalization performance. The authors demonstrate that with abundant unlabelled data, a compressed representation minimizes generalization error, while with limited unlabelled data, a higher-dimensional representation is advantageous. They provide empirical validation of their theoretical findings by observing similar trends in autoencoders and pretrained large language models (LLMs). The exact trade-off quantified suggests that a specific ratio of unlabelled to labelled data can be established, enhancing the understanding of data efficiency in model training.

**Limitations**  
The authors acknowledge that their model is idealized and may not capture all complexities of real-world scenarios, such as the effects of noise in data or the intricacies of non-linear relationships in high-dimensional spaces. They do not address the potential computational costs associated with high-dimensional representations or the scalability of their findings to very large datasets. Additionally, the model assumes linear relationships in downstream tasks, which may not hold in all applications.

**Why it matters**  
This work has significant implications for the design of machine learning systems, particularly in scenarios where labelled data is scarce. By providing a framework for optimizing representation size based on task parameters, it informs strategies for data-efficient learning and model training. The insights into the trade-off between unlabelled and labelled data can guide practitioners in resource allocation for pretraining and fine-tuning phases, ultimately enhancing model performance in practical applications. This research lays the groundwork for future studies on representation learning and generalization in high-dimensional spaces.

Authors: Valentina Njaradi, Clémentine Dominé, Rachel Swanson, Marco Mondeli, Andrew Saxe  
Source: arXiv:2605.20105  
URL: [https://arxiv.org/abs/2605.20105v1](https://arxiv.org/abs/2605.20105v1)
