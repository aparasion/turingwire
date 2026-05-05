---
title: "Universality in Deep Neural Networks: An approach via the Lindeberg exchange principle"
date: 2026-05-04 16:14:26 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.02771v1"
arxiv_id: "2605.02771"
authors: ["Filippo Giovagnini", "Sotirios Kotitsas", "Marco Romito"]
slug: universality-in-deep-neural-networks-an-approach-via-the-lin
summary_word_count: 420
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the behavior of deep neural networks (DNNs) as they approach infinite width, particularly in relation to their convergence to Gaussian processes. Existing literature lacks quantitative bounds on the Wasserstein distance between finite-width networks and their infinite-width Gaussian counterparts. This work aims to provide a theoretical framework that elucidates this relationship, which is crucial for understanding the generalization properties of DNNs.

**Method**  
The authors introduce a novel Lindeberg principle tailored for DNNs, which facilitates the replacement of layer weights with Gaussian random variables. This principle is pivotal in deriving bounds on the $2$-Wasserstein distance, a metric that quantifies the difference between probability distributions. The analysis is conducted under specific regularity conditions on the activation functions, which are not explicitly detailed but are essential for the validity of the results. The paper does not disclose specific training compute or datasets, as the focus is primarily theoretical.

**Results**  
The authors establish that, under the defined conditions, the $2$-Wasserstein distance between a finite-width DNN and its infinite-width Gaussian limit can be bounded quantitatively. While specific numerical results are not provided, the theoretical bounds suggest that as the width of the network increases, the convergence to the Gaussian limit is guaranteed, thus reinforcing the universality of DNNs. The implications of these results are significant, as they provide a rigorous foundation for the behavior of DNNs in the infinite-width regime, which has been a topic of empirical observation in prior studies.

**Limitations**  
The authors acknowledge that their results are contingent upon the regularity assumptions of the activation functions, which may not hold for all commonly used activations. Additionally, the theoretical nature of the work means that practical implications may vary, and the bounds provided may not translate directly to finite-width networks in all scenarios. The paper does not address the computational complexity of applying the Lindeberg principle in practice, nor does it explore the implications of different network architectures beyond fully connected layers.

**Why it matters**  
This work has significant implications for the theoretical understanding of DNNs, particularly in the context of their generalization capabilities and the transition from finite to infinite width. By establishing a quantitative framework for the convergence to Gaussian processes, it opens avenues for further research into the design of neural architectures that leverage these properties. Additionally, the findings may influence the development of new training methodologies and regularization techniques that align with the theoretical underpinnings of DNN behavior in the infinite-width limit.

Authors: Filippo Giovagnini, Sotirios Kotitsas, Marco Romito  
Source: arXiv:2605.02771  
URL: [https://arxiv.org/abs/2605.02771v1](https://arxiv.org/abs/2605.02771v1)
