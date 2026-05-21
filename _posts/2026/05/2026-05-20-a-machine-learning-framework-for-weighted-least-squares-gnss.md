---
title: "A Machine Learning Framework for Weighted Least Squares GNSS Positioning based on Activation Functions"
date: 2026-05-20 17:50:14 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.21461v1"
arxiv_id: "2605.21461"
authors: ["Pin-Hsun Lee", "Harry Leib"]
slug: a-machine-learning-framework-for-weighted-least-squares-gnss
summary_word_count: 423
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of Global Navigation Satellite Systems (GNSS) positioning accuracy in urban environments, where signal obstruction, non-line-of-sight (NLOS) reception, and multipath effects degrade pseudorange measurements. Existing methods, including multi-constellation GNSS, often fail to effectively filter out degraded signals, leading to significant positioning errors. The authors propose a machine learning framework that enhances the weighted least squares (WLS) algorithm by incorporating activation functions to improve the identification of poor-quality signals.

**Method**  
The core technical contribution is a machine learning framework that integrates activation functions into the WLS algorithm. The framework utilizes several signal quality indicators as features for ensemble learning algorithms, which predict quality scores for GNSS signals. These scores are then transformed into weights for the WLS positioning algorithm using activation functions. The study evaluates various activation functions, with a focus on sigmoid functions, across different machine learning models and GNSS constellation configurations. The training process leverages real-world datasets from urban areas in Hong Kong and Tokyo, although specific details on the training compute and dataset size are not disclosed.

**Results**  
The proposed framework demonstrates significant improvements in positioning accuracy compared to baseline WLS methods. The authors report substantial reductions in positioning errors for both single- and multi-constellation scenarios, with specific effect sizes not quantified in the abstract. The comparative analysis indicates that the sigmoid activation function consistently outperforms other functions across various machine learning algorithms and configurations. Additionally, the algorithm exhibits strong geographical transferability, maintaining performance levels when applied to datasets from other urbanized regions.

**Limitations**  
The authors acknowledge that their approach may be limited by the quality and representativeness of the training datasets, as well as the reliance on specific activation functions that may not generalize across all environments. They do not address potential computational overhead introduced by the machine learning components or the scalability of the framework in real-time applications. Furthermore, the study does not explore the impact of varying urban densities or the influence of different GNSS constellations beyond those tested.

**Why it matters**  
This work has significant implications for improving GNSS positioning accuracy in challenging urban environments, which is critical for applications in transportation, location-based services, and intelligent agriculture. By effectively filtering out poor-quality signals through a machine learning-enhanced WLS approach, the framework could lead to more reliable positioning solutions, thereby enhancing the performance of GNSS-dependent systems. The demonstrated geographical transferability suggests that the methodology could be adapted for use in diverse urban settings, paving the way for future research on robust GNSS positioning techniques.

Authors: Pin-Hsun Lee, Harry Leib  
Source: arXiv:2605.21461  
URL: https://arxiv.org/abs/2605.21461v1
