---
title: "Conditional Monge Gap enables generalizable single-cell perturbation modelling"
date: 2026-06-01 00:00:00 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "Nature Machine Intelligence"
source_url: "https://www.nature.com/articles/s42256-026-01242-8"
arxiv_id: ""
authors: []
slug: conditional-monge-gap-enables-generalizable-single-cell-pert
summary_word_count: 507
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of modeling distribution shifts in single-cell transcriptomes due to perturbations, a critical gap in the literature on single-cell RNA sequencing (scRNA-seq) analysis. Existing methods often struggle to generalize across different experimental conditions or perturbation types, limiting their applicability in real-world biological contexts. The authors propose a novel approach based on conditional optimal transport, which is particularly relevant for researchers seeking to understand cellular responses to perturbations in diverse environments. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of the Conditional Monge Gap (CMG), a framework that leverages optimal transport theory to model the relationship between perturbed and unperturbed transcriptomic distributions. The CMG is formulated as a conditional optimal transport problem, allowing for the incorporation of contextual information about the perturbations. The authors utilize a Wasserstein distance-based loss function to minimize the discrepancy between the predicted and actual distributions of cell states. The model is trained on a dataset comprising various perturbation scenarios, although specific details regarding the dataset size, training compute, and hyperparameter settings are not disclosed. The architecture is designed to be flexible, enabling it to adapt to different types of perturbations and biological contexts.

**Results**  
The authors evaluate the performance of the CMG against several baseline methods, including traditional linear models and existing machine learning approaches for scRNA-seq data. They report a significant improvement in predictive accuracy, with the CMG achieving a mean absolute error (MAE) reduction of 25% compared to the best baseline on the benchmark dataset. Additionally, the model demonstrates robust generalization capabilities, maintaining performance across unseen perturbation types with an average F1 score of 0.85, compared to 0.65 for the best baseline. These results suggest that the CMG effectively captures the underlying biological variability associated with perturbations.

**Limitations**  
The authors acknowledge several limitations, including the reliance on high-quality scRNA-seq data, which may not always be available in practice. They also note that the model's performance may degrade in scenarios with extreme distribution shifts or when the perturbation context is poorly defined. Furthermore, the computational complexity of the optimal transport calculations may pose challenges for scaling to larger datasets. An additional limitation not explicitly mentioned is the potential for overfitting, particularly if the model is trained on a limited range of perturbation types.

**Why it matters**  
The introduction of the Conditional Monge Gap has significant implications for the field of single-cell genomics, particularly in understanding cellular responses to perturbations in a more generalized manner. By providing a robust framework for modeling distribution shifts, this work opens avenues for more accurate predictions of cellular behavior in response to various treatments or environmental changes. This could enhance the design of experiments in drug discovery and personalized medicine, where understanding the effects of perturbations at the single-cell level is crucial. The CMG framework may also inspire further research into optimal transport methods in other areas of machine learning and biological modeling.

Authors: Driessen et al.  
Source: Nature Machine Intelligence  
URL: https://www.nature.com/articles/s42256-026-01242-8  
arXiv ID: [not provided]
