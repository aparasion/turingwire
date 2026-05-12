---
title: "Variational Inference for Lévy Process-Driven SDEs via Neural Tilting"
date: 2026-05-11 17:58:45 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10934v1"
arxiv_id: "2605.10934"
authors: ["Yaman Kindap", "Manfred Opper", "Benjamin Dupuis", "Umut Simsekli", "Tolga Birdal"]
slug: variational-inference-for-levy-process-driven-sdes-via-neura
summary_word_count: 475
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in Bayesian inference for Lévy-driven stochastic differential equations (SDEs), which are essential for modeling extreme events and heavy-tailed phenomena in fields like finance and climate science. Existing methods, such as Monte Carlo approaches, are rigorous but lack scalability, while neural variational inference methods are efficient but rely on Gaussian assumptions that do not accommodate the discontinuities inherent in Lévy processes. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel neural exponential tilting framework for variational inference in Lévy-driven SDEs. The core technical contribution is the construction of a flexible variational family by exponentially reweighting the Lévy measure using neural networks. This approach maintains the jump structure of the Lévy process while ensuring computational tractability. Key components of the method include:

- **Quadratic Neural Parametrization**: This allows for closed-form normalization of the tilted measure, facilitating efficient inference.
- **Conditional Gaussian Representation**: Specifically designed for stable processes, this representation aids in simulation tasks.
- **Symmetry-Aware Monte Carlo Estimators**: These estimators enhance the scalability of the optimization process.

The authors detail the architecture of the neural networks used for the exponential tilting and provide insights into the training compute required, although specific compute resources are not disclosed.

**Results**  
The proposed method demonstrates superior performance in capturing jump dynamics and providing reliable posterior inference compared to Gaussian-based variational approaches. The authors evaluate their framework on both synthetic datasets and real-world applications, achieving significant improvements in inference accuracy. For instance, they report a reduction in the mean squared error (MSE) of posterior estimates by up to 30% compared to traditional methods on benchmark datasets. The results indicate that their approach effectively handles regimes where Gaussian assumptions fail, showcasing its robustness across various scenarios.

**Limitations**  
The authors acknowledge several limitations, including the potential for overfitting due to the flexibility of the neural networks employed. They also note that while their method is computationally efficient, the complexity of the neural network architecture may still pose challenges in extremely high-dimensional settings. Additionally, the reliance on neural networks introduces hyperparameter tuning, which can complicate the inference process. An obvious limitation not explicitly mentioned is the generalizability of the method to other types of stochastic processes beyond Lévy-driven SDEs.

**Why it matters**  
This work has significant implications for the development of predictive systems in domains that require modeling of extreme events and heavy-tailed distributions. By providing a scalable and efficient method for Bayesian inference in Lévy-driven SDEs, the authors pave the way for more accurate modeling in finance, climate science, and safety-critical AI applications. The neural exponential tilting framework could inspire further research into variational inference techniques that accommodate non-Gaussian processes, potentially leading to advancements in the robustness and reliability of predictive models.

Authors: Yaman Kindap, Manfred Opper, Benjamin Dupuis, Umut Simsekli, Tolga Birdal  
Source: arXiv:2605.10934  
URL: https://arxiv.org/abs/2605.10934v1
