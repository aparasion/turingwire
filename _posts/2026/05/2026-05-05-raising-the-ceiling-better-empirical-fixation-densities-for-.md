---
title: "Raising the Ceiling: Better Empirical Fixation Densities for Saliency Benchmarking"
date: 2026-05-05 15:45:00 +0000
category: research
subcategory: evaluation_benchmarks
company: "ServiceNow"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03885v1"
arxiv_id: "2605.03885"
authors: ["Susmit Agrawal", "Jannis Hollman", "Matthias K\u00fcmmerer"]
slug: raising-the-ceiling-better-empirical-fixation-densities-for-
summary_word_count: 407
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacy of existing empirical fixation density estimation methods in saliency benchmarking, specifically the reliance on fixed-bandwidth isotropic Gaussian Kernel Density Estimation (KDE). The authors argue that this method has not evolved for decades, leading to potential inaccuracies in benchmark conclusions, leaderboard rankings, and analyses of human visual behavior. As the field transitions towards sample-level evaluations, such as failure case analysis and per-image model comparisons, the need for reliable per-image density estimates becomes increasingly critical.

**Method**  
The authors propose a novel mixture model that integrates an adaptive-bandwidth KDE based on Abramson's method, along with center bias and uniform components, to enhance the estimation of empirical fixation densities. This model is designed to capture various spatial and semantic types of interobserver consistency. The parameters of the model are optimized for each image using leave-one-subject-out cross-validation, allowing for a more tailored approach to density estimation. The methodology aims to improve the accuracy of fixation density estimates, which are crucial for evaluating saliency models.

**Results**  
The proposed method demonstrates significant improvements in interobserver consistency estimates across multiple benchmarks. The authors report median per-image gains of 5-15% in log-likelihood and up to 2 percentage points in Area Under the Curve (AUC) compared to the standard fixed-bandwidth KDE. For images that are most relevant to failure case analysis, improvements exceed 25%. These results indicate that the new method not only enhances the quality of fixation density estimates but also provides a more reliable basis for evaluating saliency models.

**Limitations**  
The authors acknowledge that their method, while an improvement, may still be sensitive to the quality and quantity of eye-tracking data used for training. Additionally, the reliance on leave-one-subject-out cross-validation may introduce variability depending on the specific dataset employed. They do not address potential computational overhead associated with the adaptive bandwidth selection process, which could limit scalability in large datasets.

**Why it matters**  
This work has significant implications for the field of saliency modeling and benchmarking. By establishing a more robust framework for empirical fixation density estimation, the authors provide a pathway for more accurate evaluations of saliency models, particularly in identifying failure cases. The findings suggest that empirical fixation densities should be viewed as dynamic estimates that can evolve with methodological advancements, thereby encouraging further research into improved saliency detection techniques. This could lead to enhanced model performance and a deeper understanding of human visual attention mechanisms.

Authors: Susmit Agrawal, Jannis Hollman, Matthias Kümmerer  
Source: arXiv:2605.03885  
URL: [https://arxiv.org/abs/2605.03885v1](https://arxiv.org/abs/2605.03885v1)
