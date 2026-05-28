---
title: "Applications of temporal graph learning for predicting the dynamics of biological systems"
date: 2026-05-27 15:57:40 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28659v1"
arxiv_id: "2605.28659"
authors: ["Manuel Dileo", "Andrea Sottoriva"]
slug: applications-of-temporal-graph-learning-for-predicting-the-d
summary_word_count: 463
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This work-in-progress paper addresses the gap in existing literature regarding the modeling of temporal dynamics in biological systems, specifically in single-cell transcriptomics. While previous approaches have leveraged transformer architectures for static gene-expression matrices, they fail to account for the temporal evolution of cellular states during development and disease progression. The authors propose a temporal graph-based framework to represent and predict these dynamics, which is not adequately covered in current methodologies. This paper is a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a temporal graph learning framework that models cellular states as evolving graph structures based on pseudotime-resolved gene regulatory networks. The methodology involves several key steps: 
1. **Data Preparation**: Starting from single-cell transcriptomic data, pseudotime trajectories are inferred to discretize cells into developmental snapshots.
2. **Network Reconstruction**: A gene regulatory network is reconstructed for each snapshot, capturing the regulatory interactions at that specific developmental stage.
3. **Modeling**: Temporal graph neural networks (TGNNs) are employed to forecast biological states across these snapshots. The architecture details, including specific layers or hyperparameters, are not disclosed in the abstract.
4. **Tasks**: The framework is evaluated on three tasks: gene-expression forecasting, link prediction, and out-degree centrality prediction, using two publicly available mouse developmental datasets: erythroid gastrulation and pancreatic endocrinogenesis.

**Results**  
The results indicate that the proposed temporal graph-based models outperform established foundation models such as scGPT and scFoundation across the evaluated tasks. Specifically, the authors report significant improvements in predictive accuracy for gene-expression forecasting, link prediction, and out-degree centrality prediction, although exact numerical performance metrics (e.g., accuracy, F1 scores) are not provided in the abstract. The temporal graph learning approach effectively captures complex regulatory dynamics, enabling the identification of temporally significant gene hubs, which are critical for understanding developmental processes.

**Limitations**  
The authors acknowledge that their work is still in progress, which implies potential limitations in the robustness and generalizability of their findings. They do not discuss the scalability of their approach to larger datasets or the computational resources required for training the TGNNs. Additionally, the reliance on specific datasets may limit the applicability of their results to other biological contexts. The absence of detailed hyperparameter tuning and model architecture specifics also raises questions about reproducibility.

**Why it matters**  
This research has significant implications for the field of single-cell biology and the modeling of dynamic biological systems. By demonstrating the efficacy of temporal graph learning, the authors provide a compelling argument for moving beyond static representations in biological modeling. Their findings suggest that integrating temporal dynamics into gene regulatory networks can yield richer insights into cellular differentiation and disease progression, potentially guiding future research and therapeutic strategies. This work lays the groundwork for further exploration of temporal graph-based methodologies in various biological contexts.

Authors: Manuel Dileo, Andrea Sottoriva  
Source: arXiv:2605.28659  
URL: [https://arxiv.org/abs/2605.28659v1](https://arxiv.org/abs/2605.28659v1)
