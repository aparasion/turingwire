---
title: "ExDBSCAN: Explaining DBSCAN with Counterfactual Reasoning -- Additional Material"
date: 2026-05-28 16:57:00 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30225v1"
arxiv_id: "2605.30225"
authors: ["Pernille Matthews", "Lena Krieger", "Tommaso Amico", "Artur Zimek", "Thomas Seidl", "Ira Assent"]
slug: exdbscan-explaining-dbscan-with-counterfactual-reasoning-add
summary_word_count: 447
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the interpretability gap in clustering, specifically for the DBSCAN algorithm, which lacks mechanisms to explain cluster assignments. Existing explainability methods are primarily designed for supervised learning and do not extend to unsupervised techniques like DBSCAN. The authors highlight the challenge of understanding why specific points are classified as inliers or outliers and whether these classifications are stable under minor perturbations in the data. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose ExDBSCAN, a post-hoc explanation method that generates counterfactual explanations for DBSCAN cluster assignments. The core technical contribution lies in its use of a density-connected weighted graph to produce multiple counterfactuals. The method employs a physics-inspired model that balances two forces: it repels counterfactual candidates from one another to ensure diversity and attracts them toward the instance being explained to maintain proximity. The theoretical framework guarantees the validity of the generated counterfactuals. The implementation details, including the specific architecture of the density-connected graph and the optimization techniques used to balance the forces, are not disclosed in the abstract.

**Results**  
ExDBSCAN was empirically evaluated on 30 tabular datasets, demonstrating superior performance compared to four baseline methods. The results indicate that ExDBSCAN achieves perfect validity in its counterfactual explanations while also retrieving diverse and proximal counterfactuals. Although specific numerical results and effect sizes are not provided in the abstract, the authors claim that ExDBSCAN outperforms all baselines across the evaluated datasets, suggesting a significant improvement in the interpretability of DBSCAN clustering results.

**Limitations**  
The authors acknowledge that ExDBSCAN is a post-hoc method, which means it does not alter the underlying DBSCAN algorithm but rather provides explanations after clustering has occurred. This could limit its applicability in real-time systems where immediate interpretability is required. Additionally, the method's reliance on a density-connected graph may introduce computational overhead, particularly for large datasets. The paper does not discuss the scalability of ExDBSCAN or its performance in high-dimensional spaces, which are common challenges in clustering tasks.

**Why it matters**  
The introduction of ExDBSCAN has significant implications for the field of unsupervised learning, particularly in enhancing the interpretability of clustering algorithms. By providing actionable counterfactual explanations, this method can facilitate better understanding and trust in clustering outcomes, which is crucial for applications in sensitive domains such as healthcare and finance. Furthermore, the theoretical guarantees of validity may encourage the adoption of ExDBSCAN in practical scenarios where explainability is paramount. This work lays the groundwork for future research into explainable clustering methods and could inspire the development of similar techniques for other unsupervised learning algorithms.

Authors: Pernille Matthews, Lena Krieger, Tommaso Amico, Artur Zimek, Thomas Seidl, Ira Assent  
Source: arXiv:2605.30225  
URL: https://arxiv.org/abs/2605.30225v1
