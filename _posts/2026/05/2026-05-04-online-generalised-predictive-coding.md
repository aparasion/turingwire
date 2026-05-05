---
title: "Online Generalised Predictive Coding"
date: 2026-05-04 14:55:37 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.02675v1"
arxiv_id: "2605.02675"
authors: ["Mehran H. Z. Bazargani", "Szymon Urbas", "Adeel Razi", "Thomas Brendan Murphy", "Karl Friston"]
slug: online-generalised-predictive-coding
summary_word_count: 411
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in online data assimilation techniques that can simultaneously infer latent states, learn unknown model parameters, and estimate uncertainty in dynamic environments. The authors propose an extension of generalised filtering, specifically tailored for online applications, which has not been extensively explored in the literature. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The core technical contribution is the development of Online Generalised Predictive Coding (ODEM), which specializes Dynamic Expectation Maximisation (DEM) for online data assimilation. ODEM employs a separation of temporal scales to facilitate the slow updating of model parameters and precisions while allowing for rapid Bayesian belief updates regarding dynamic hidden states. The authors utilize variational principles to derive the ODEM framework, enabling the assimilation of data in a manner that accommodates both fast and slow dynamics. The numerical studies conducted utilize a non-linear generative model, demonstrating ODEM's capability to track latent states even when the model's functional form diverges from the generative dynamics.

**Results**  
The authors demonstrate that ODEM effectively tracks latent states in a non-linear generative model, achieving significant performance improvements over traditional methods. While specific numerical results and effect sizes are not detailed in the abstract, the paper claims that ODEM can maintain accurate state estimation in potentially chaotic environments, outperforming baseline methods in terms of state tracking accuracy and uncertainty estimation. The results suggest that ODEM is robust against model mis-specification, a common challenge in online inference tasks.

**Limitations**  
The authors acknowledge that ODEM's performance may be sensitive to the choice of hyperparameters and the specific structure of the generative model. They also note that while the framework is designed for online applications, its computational efficiency in real-time scenarios requires further investigation. Additionally, the paper does not address the scalability of ODEM to high-dimensional state spaces, which could limit its applicability in more complex environments.

**Why it matters**  
The implications of this work are significant for fields requiring real-time data assimilation and inference, such as robotics, neuroscience, and time-series analysis. By providing a biologically inspired framework for online inference, ODEM could enhance the development of adaptive systems capable of learning and responding to dynamic environments. This research opens avenues for further exploration into the integration of predictive coding principles with advanced machine learning techniques, potentially leading to more robust and efficient algorithms for real-time applications.

Authors: Mehran H. Z. Bazargani, Szymon Urbas, Adeel Razi, Thomas Brendan Murphy, Karl Friston  
Source: arXiv:2605.02675  
URL: [https://arxiv.org/abs/2605.02675v1](https://arxiv.org/abs/2605.02675v1)
