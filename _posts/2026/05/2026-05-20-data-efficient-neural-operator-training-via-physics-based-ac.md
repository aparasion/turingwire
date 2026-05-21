---
title: "Data-Efficient Neural Operator Training via Physics-Based Active Learning"
date: 2026-05-20 16:13:53 +0000
category: research
subcategory: training_methods
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21348v1"
arxiv_id: "2605.21348"
authors: ["Alicja Polanska", "Lorenzo Zanisi", "Vignesh Gopakumar", "Stanislas Pamela"]
slug: data-efficient-neural-operator-training-via-physics-based-ac
summary_word_count: 445
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the significant gap in the data efficiency of neural operators when solving partial differential equations (PDEs). While neural operators can drastically reduce computational costs associated with traditional numerical methods, their training typically requires large datasets, which can be prohibitive. The authors propose a solution through active learning, specifically a physics-informed approach that selectively acquires the most informative training samples, thereby reducing the data requirements for effective training.

**Method**  
The core technical contribution is the introduction of a novel physics-based active learning algorithm that utilizes the residuals of PDEs to inform data selection. This method operates iteratively, where the model identifies and acquires samples that are expected to yield the highest information gain regarding its understanding of the underlying physics. The authors validate their approach through numerical experiments on two benchmark problems: the 1D Burgers equation and the 2D compressible Navier-Stokes equations. The architecture of the neural operator is not explicitly detailed, but the training process incorporates the physics-based acquisition strategy, which injects an inductive bias into the model. The authors do not disclose specific training compute metrics, focusing instead on the qualitative improvements in data efficiency.

**Results**  
The results demonstrate that the physics-based acquisition method consistently outperforms random sampling strategies in terms of data efficiency. In the experiments conducted, the proposed method achieves performance metrics that match the state-of-the-art benchmarks for both the 1D Burgers equation and the 2D compressible Navier-Stokes equations. While specific numerical results are not provided in the summary, the authors emphasize that their approach leads to a significant reduction in the amount of training data required to achieve comparable performance, thus highlighting the effectiveness of the physics-informed strategy.

**Limitations**  
The authors acknowledge that their method may be limited by the complexity of the PDEs being solved and the assumptions inherent in the physics-informed framework. They do not address potential scalability issues when applying this method to higher-dimensional problems or more complex physical systems. Additionally, the reliance on the quality of the initial model and the selection of the acquisition function could impact the overall performance, which is not explored in depth.

**Why it matters**  
This work has significant implications for the field of scientific machine learning, particularly in applications where data acquisition is expensive or time-consuming. By improving data efficiency through a physics-informed active learning approach, the authors provide a pathway for more effective training of neural operators, potentially enabling their application to a broader range of complex PDEs. This could lead to advancements in simulations across various scientific domains, including fluid dynamics, materials science, and beyond, where understanding the underlying physics is crucial.

Authors: Alicja Polanska, Lorenzo Zanisi, Vignesh Gopakumar, Stanislas Pamela  
Source: arXiv:2605.21348  
URL: https://arxiv.org/abs/2605.21348v1
