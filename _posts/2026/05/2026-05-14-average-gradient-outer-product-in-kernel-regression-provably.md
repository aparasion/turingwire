---
title: "Average Gradient Outer Product in kernel regression provably recovers the central subspace for multi-index models"
date: 2026-05-14 17:05:30 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.15082v1"
arxiv_id: "2605.15082"
authors: ["Libin Zhu", "Damek Davis", "Dmitriy Drusvyatskiy", "Maryam Fazel"]
slug: average-gradient-outer-product-in-kernel-regression-provably
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in understanding how kernel methods can recover low-dimensional structures in high-dimensional data, specifically in the context of multi-index polynomial models. The authors focus on the challenge of recovering a central subspace from limited data, which is particularly relevant when the number of samples is insufficient for accurate prediction. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of the Average Gradient Outer Product (AGOP) as a method for subspace recovery in kernel ridge regression (KRR). The authors propose fitting a KRR model to the data and then computing the AGOP from the fitted predictor. The theoretical framework shows that under certain assumptions, the top $r$-dimensional eigenspace derived from AGOP can recover the central subspace of the target function $f^*(x) = h(Ux)$, where $U \in \mathbb{R}^{r \times d}$ and $r \ll d$. The paper establishes that while $n \asymp d^{p^*}$ samples are necessary for accurate prediction when the polynomial degree is $p^*$, subspace recovery can occur with significantly fewer samples, specifically $n \asymp d^{p + \delta}$ for any $\delta \in (0,1)$, if a low-degree component of $f^*$ captures all relevant directions.

**Results**  
The authors demonstrate that AGOP effectively recovers the central subspace even when the prediction error remains substantial. They provide theoretical guarantees that the eigenspace of AGOP aligns with the true central subspace, thus separating the tasks of prediction and representation. The results indicate that the sample complexity for subspace recovery is significantly lower than that required for accurate prediction, highlighting the efficiency of the proposed method. However, specific numerical results or comparisons against established baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that their results rely on certain assumptions, such as the structure of the target function and the properties of the data distribution. They do not address potential limitations related to the robustness of AGOP in the presence of noise or outliers, nor do they explore the scalability of the method in extremely high-dimensional settings. Additionally, the lack of empirical validation in the form of experiments or real-world datasets is a notable omission.

**Why it matters**  
This work has significant implications for the field of machine learning, particularly in scenarios where data is scarce but low-dimensional structures are present. By demonstrating that subspace recovery can be achieved with fewer samples than traditionally required for accurate predictions, the findings could lead to more efficient algorithms in high-dimensional settings. This separation of prediction and representation may also enhance the understanding of iterative kernel methods, such as Recursive Feature Machines (RFM), and their practical sample efficiency. The insights gained from this research could inform future work on kernel methods and dimensionality reduction techniques.

Authors: Libin Zhu, Damek Davis, Dmitriy Drusvyatskiy, Maryam Fazel  
Source: arXiv:2605.15082  
URL: https://arxiv.org/abs/2605.15082v1
