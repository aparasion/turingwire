---
title: "Integrable Elasticity via Neural Demand Potentials"
date: 2026-05-21 17:59:47 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.22820v1"
arxiv_id: "2605.22820"
authors: ["Carlos Heredia", "Daniel Roncel"]
slug: integrable-elasticity-via-neural-demand-potentials
summary_word_count: 439
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in modeling multiproduct retail demand with a focus on deriving elasticities directly from demand functions. Existing models often struggle with out-of-sample generalization and provide unstable elasticity estimates, particularly for cross-price effects. The authors propose the Integrable Context-Dependent Demand Network (ICDN) as a solution. This work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the ICDN architecture, which employs a demand-first approach to model multiproduct demand. The model learns log-demand as a smooth, context-conditioned function of log-prices, allowing for the exact derivation of elasticities from the learned demand surface. The architecture leverages neural networks to capture complex relationships between prices and demand while ensuring that the resulting demand functions are integrable. The training process involves optimizing a loss function that emphasizes the accuracy of demand predictions and the stability of elasticity estimates. The authors utilize the Dominick's beer dataset for empirical validation, although specific details regarding training compute and hyperparameter settings are not disclosed.

**Results**  
On the Dominick's beer dataset, ICDN demonstrates significant improvements in out-of-sample generalization compared to a directed log-log benchmark. The model yields more stable and economically plausible elasticity estimates, particularly for weakly identified cross-price effects. While specific numerical results are not provided in the abstract, the authors claim that ICDN outperforms the benchmark in terms of both predictive accuracy and the reliability of elasticity estimates, indicating a substantial effect size in practical applications.

**Limitations**  
The authors acknowledge that the ICDN model may still be sensitive to the choice of hyperparameters and the quality of the training data. They also note that while the model improves elasticity estimates, it may not fully capture all market dynamics, particularly in highly volatile or non-linear demand environments. An additional limitation is the reliance on a single dataset (Dominick's beer), which may restrict the generalizability of the findings to other retail contexts. The authors do not discuss potential computational inefficiencies or scalability issues that may arise when applying ICDN to larger datasets or more complex retail scenarios.

**Why it matters**  
The implications of this work are significant for both academic research and practical applications in retail analytics. By providing a robust framework for modeling multiproduct demand and deriving elasticities, ICDN can enhance pricing strategies and inventory management in retail settings. The ability to generate stable elasticity estimates is particularly valuable for firms looking to optimize their pricing in response to competitive dynamics. Furthermore, this research opens avenues for future work in demand modeling, potentially leading to more sophisticated approaches that integrate additional contextual factors or leverage larger datasets.

Authors: Carlos Heredia, Daniel Roncel  
Source: arXiv:2605.22820  
URL: https://arxiv.org/abs/2605.22820v1
