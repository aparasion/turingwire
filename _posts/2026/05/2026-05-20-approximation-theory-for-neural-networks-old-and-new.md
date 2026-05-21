---
title: "Approximation Theory for Neural Networks: Old and New"
date: 2026-05-20 17:42:34 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21451v1"
arxiv_id: "2605.21451"
authors: ["Soumendu Sundar Mukherjee", "Himasish Talukdar"]
slug: approximation-theory-for-neural-networks-old-and-new
summary_word_count: 457
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding the quantitative aspects of universal approximation theorems for neural networks, particularly focusing on approximation rates, parameter efficiency, and the influence of architectural features such as depth and width. While previous works have established qualitative results, this survey aims to synthesize and clarify the quantitative theory that has emerged over the last four decades. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors conduct a comprehensive review of existing literature on approximation theory as it pertains to neural networks. They discuss classical density results for single-hidden-layer networks and present quantitative bounds that connect approximation error to network size and the smoothness of target functions. The paper emphasizes depth-width trade-offs, illustrating how deeper architectures can achieve better parameter efficiency for specific structured function classes. Additionally, the authors explore Kolmogorov–Arnold Networks (KANs), highlighting their unique architectural properties and approximation-theoretic advantages. The survey does not introduce new architectures or loss functions but synthesizes existing theoretical results to provide a clearer understanding of the implications of network design choices.

**Results**  
The paper summarizes key findings from various studies, indicating that deeper networks can reduce the number of parameters required to achieve a given approximation error compared to shallower networks. For instance, it is noted that certain structured function classes can be approximated with significantly fewer parameters when using deeper architectures. The authors also reference specific quantitative bounds, although exact numerical results and comparisons against named baselines are not provided in the abstract. The implications of these findings suggest that the choice of network depth and width can lead to substantial improvements in approximation efficiency, although specific effect sizes are not detailed.

**Limitations**  
The authors acknowledge that their survey is limited to existing theoretical results and does not present new empirical findings or experimental validations of the discussed theories. Additionally, the focus on specific structured function classes may not generalize to all types of functions encountered in practical applications. The paper also does not address the computational complexity associated with training deeper networks, which could impact their practical deployment.

**Why it matters**  
This survey is significant for researchers and engineers as it consolidates a wealth of theoretical insights into the design and efficiency of neural networks. By elucidating the relationship between network architecture and approximation capabilities, it provides a framework for future research aimed at optimizing neural network designs. The emphasis on depth-width trade-offs and the exploration of KANs may inspire new architectural innovations and guide practitioners in selecting appropriate network configurations for specific tasks. Understanding these theoretical foundations is crucial for advancing the field of deep learning and improving model performance across various applications.

Authors: Soumendu Sundar Mukherjee, Himasish Talukdar  
Source: arXiv:2605.21451  
URL: [https://arxiv.org/abs/2605.21451v1](https://arxiv.org/abs/2605.21451v1)
