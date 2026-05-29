---
title: "Faithful Embeddings of Irregular and Asynchronous Data for Online Log-NCDEs"
date: 2026-05-28 16:46:11 +0000
category: research
subcategory: theory
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30213v1"
arxiv_id: "2605.30213"
authors: ["Benjamin Walker", "Alexandre Bloch", "Lingyi Yang", "Sam Morley", "Terry Lyons"]
slug: faithful-embeddings-of-irregular-and-asynchronous-data-for-o
summary_word_count: 424
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of embedding irregular and asynchronous data into continuous-time models, specifically focusing on Neural Controlled Differential Equations (NCDEs). Traditional methods rely on interpolation or imputation to reconstruct continuous observation paths, which can introduce sensitivity to the reconstruction method chosen. The authors argue that this reconstruction step is unnecessary and propose a new embedding approach that maintains the integrity of the data without requiring such transformations. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a continuous and injective embedding for Log-NCDEs, leveraging the concept of compact-set universality. Their method records observations as increments and composes these increments over arbitrary query intervals to directly form log-signatures. This approach allows for the generation of interval-level summaries of the data without the need for prior interpolation of the observed variables. The architecture is built upon the rectilinear control path for NCDEs, ensuring that the embedding is both efficient and robust. The training compute requirements are not explicitly disclosed, but the method is designed for online computation, suggesting a focus on efficiency in real-time applications.

**Results**  
The authors validate their approach through experiments on both synthetic controlled dynamics and real-world time-series datasets. They report that their embedding method achieves high accuracy and efficiency, demonstrating robustness to irregular, asynchronous, and sparse observations. While specific numerical results and effect sizes are not detailed in the abstract, the authors claim that their method outperforms traditional interpolation-based approaches, indicating a significant improvement in handling irregular data.

**Limitations**  
The authors acknowledge that their method relies on certain mild conditions for the transfer of compact-set universality from the model input space to the data space. They do not discuss potential limitations related to the scalability of their approach to very large datasets or the computational overhead associated with real-time applications. Additionally, the performance on highly noisy data or extreme sparsity scenarios is not explicitly evaluated, which could be a concern for practical applications.

**Why it matters**  
This work has significant implications for the modeling of irregular and asynchronous data in various domains, including finance, healthcare, and IoT applications. By eliminating the need for interpolation, the proposed embedding method enhances the efficiency and accuracy of continuous-time models, potentially leading to better predictive performance in real-time systems. The findings could inspire further research into alternative embedding techniques and their applications in other continuous-time frameworks, paving the way for more robust models in the face of irregular data.

Authors: Benjamin Walker, Alexandre Bloch, Lingyi Yang, Sam Morley, Terry Lyons  
Source: arXiv:2605.30213  
URL: https://arxiv.org/abs/2605.30213v1
