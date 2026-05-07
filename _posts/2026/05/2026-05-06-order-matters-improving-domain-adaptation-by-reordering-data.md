---
title: "Order Matters: Improving Domain Adaptation by Reordering Data"
date: 2026-05-06 16:20:24 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.05084v1"
arxiv_id: "2605.05084"
authors: ["Andrea Napoli", "Paul White"]
slug: order-matters-improving-domain-adaptation-by-reordering-data
summary_word_count: 406
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of domain shift in machine learning, particularly in the context of unsupervised domain adaptation (UDA). The authors highlight that existing methods for minimizing domain discrepancy often suffer from high variance in stochastic settings, which undermines their theoretical advantages. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a novel technique called Optimal Reordering of Data for Error-Reduced Estimation of Discrepancy (ORDERED). This method focuses on optimizing the order in which training data is sampled to reduce the stochastic estimation error of domain discrepancy metrics. Specifically, the paper examines two domain discrepancy losses: correlation alignment (CORAL) and maximum mean discrepancy (MMD). The authors derive the stochastic estimation error as a function of the data sampling order and propose a practical optimization algorithm to determine the optimal order. The implementation details, including the architecture and training compute, are not explicitly disclosed, but the method is designed to be integrated into existing UDA frameworks.

**Results**  
The authors report significant improvements in target domain accuracy on two benchmark datasets for domain shift image classification. Specifically, ORDERED achieves a reduction in variance of discrepancy estimates compared to baseline methods, leading to improved performance metrics. While exact numerical results are not provided in the abstract, the authors claim that their method outperforms standard UDA techniques, indicating a substantial effect size in the context of domain adaptation tasks.

**Limitations**  
The authors acknowledge that their approach may be sensitive to the choice of the initial data ordering and that the optimization process could introduce additional computational overhead. They do not discuss the scalability of the method to larger datasets or more complex domain shifts, which could limit its applicability in real-world scenarios. Additionally, the reliance on specific discrepancy measures (CORAL and MMD) may restrict the generalizability of the findings to other loss functions.

**Why it matters**  
This work has significant implications for the field of domain adaptation, particularly in enhancing the robustness of UDA methods against domain shift. By providing a systematic approach to data ordering, ORDERED could lead to more reliable and efficient training processes in various applications, such as computer vision and natural language processing. The reduction in variance of discrepancy estimates may also facilitate the development of more effective algorithms that can better generalize across domains, ultimately improving the deployment of machine learning models in real-world settings.

Authors: Andrea Napoli, Paul White  
Source: arXiv:2605.05084  
URL: https://arxiv.org/abs/2605.05084v1
