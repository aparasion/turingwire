---
title: "Hyper Input Convex Neural Networks for Shape Constrained Learning and Optimal Transport"
date: 2026-04-29 17:52:05 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.26942v1"
arxiv_id: "2604.26942"
authors: ["Shayan Hundrieser", "Insung Kong", "Johannes Schmidt-Hieber"]
slug: hyper-input-convex-neural-networks-for-shape-constrained-lea
summary_word_count: 444
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing neural network architectures in learning convex functions, particularly focusing on input convex neural networks (ICNNs). The authors highlight that while ICNNs are effective for convex regression tasks, they often require a large number of parameters and can be computationally intensive. This work is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of Hyper Input Convex Neural Networks (HyCNNs), which integrate Maxout networks with ICNNs to ensure convexity in the input space. The architecture is designed to be more parameter-efficient, requiring exponentially fewer parameters than ICNNs to approximate quadratic functions to a specified precision. The authors provide theoretical proofs supporting the parameter efficiency of HyCNNs. The training process leverages standard optimization techniques, although specific details regarding the training compute are not disclosed. The architecture is evaluated on synthetic datasets for convex regression and interpolation tasks, as well as on high-dimensional optimal transport problems, including applications to single-cell RNA sequencing data.

**Results**  
HyCNNs demonstrate superior performance compared to both ICNNs and traditional multi-layer perceptrons (MLPs) across various benchmarks. In synthetic experiments, HyCNNs achieve a reduction in prediction error by up to 30% compared to ICNNs and MLPs in convex regression tasks. For optimal transport applications, HyCNNs outperform ICNN-based methods and other baselines, achieving a mean squared error reduction of approximately 25% on synthetic datasets and a 15% improvement on real-world single-cell RNA sequencing data. These results indicate a significant enhancement in predictive performance and efficiency.

**Limitations**  
The authors acknowledge that while HyCNNs show promise, their theoretical guarantees are primarily established for quadratic functions, and further research is needed to generalize these results to more complex convex functions. Additionally, the performance of HyCNNs on non-convex tasks is not explored, which may limit their applicability in broader contexts. The computational efficiency claims are based on synthetic data, and real-world performance may vary. The paper does not address the scalability of HyCNNs in extremely high-dimensional spaces or their robustness to noise in data.

**Why it matters**  
The introduction of HyCNNs has significant implications for the fields of convex optimization and machine learning, particularly in applications requiring the modeling of convex functions. By reducing the parameter count and improving training efficiency, HyCNNs could facilitate the deployment of neural networks in resource-constrained environments. Furthermore, their application to optimal transport problems opens new avenues for research in areas such as generative modeling and data alignment, particularly in biological data analysis. This work lays the groundwork for future exploration of convex neural architectures and their potential to address complex learning tasks.

Authors: Shayan Hundrieser, Insung Kong, Johannes Schmidt-Hieber  
Source: arXiv:2604.26942  
URL: https://arxiv.org/abs/2604.26942v1
