---
title: "Memorisation, convergence and generalisation in generative models"
date: 2026-05-20 17:00:37 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.21402v1"
arxiv_id: "2605.21402"
authors: ["Antoine Maillard", "Sebastian Goldt"]
slug: memorisation-convergence-and-generalisation-in-generative-mo
summary_word_count: 468
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the transition from memorization to generalization in generative models, specifically in the context of diffusion models. Previous work by Kadkhodaie et al. (ICLR '24) demonstrated that diffusion models trained on disjoint subsets of a dataset converge to similar densities with sufficient data. However, the precise conditions under which this convergence occurs and its implications for learning the underlying data distribution remain unclear. This paper aims to analytically characterize these transitions, providing insights into the necessary data requirements for convergence and the nature of generalization in linear generative models.

**Method**  
The authors develop an analytical framework to study linear generative models, focusing on the relationship between the number of training samples and the model's ability to generalize. They establish that models exhibit memorization behavior at low sample loads, while convergence to the true data distribution occurs when the number of samples is proportional to the input dimension. The study introduces two distinct objectives in the learning process: (1) matching the bulk of the data distribution and (2) recovering the principal latent factors. The authors utilize convolutional denoisers and datasets with power-law spectra to validate their findings, demonstrating that convergence is independent of the recovery of latent factors, which occurs in a sharp transition.

**Results**  
The paper presents a clear delineation between memorization and convergence, showing that convergence is achieved when the number of training samples is linear in the input dimension. The authors report that in their experiments, models trained with sufficient data exhibit convergence to the true data distribution, while those with insufficient data primarily memorize the training set. The results indicate that generalization can be decomposed into two objectives, with convergence only capturing the first objective related to the bulk data distribution. The findings are supported by empirical results from convolutional denoisers and the datasets analyzed by Kadkhodaie et al., reinforcing the theoretical claims.

**Limitations**  
The authors acknowledge that their analysis is limited to linear generative models and may not generalize to more complex architectures. Additionally, the study primarily focuses on the transition between memorization and convergence without exploring the implications of these findings on model interpretability or robustness. The impact of noise and other factors on the memorization-generalization trade-off is also not extensively addressed, which could be relevant in practical applications.

**Why it matters**  
This work has significant implications for the design and training of generative models, particularly in understanding the conditions under which these models can generalize effectively. By clarifying the distinction between memorization and convergence, the findings can inform future research on model architectures and training strategies that prioritize generalization. The decomposition of generalization into distinct objectives may lead to more targeted approaches in generative modeling, enhancing the ability to recover meaningful latent structures in complex datasets.

Authors: Antoine Maillard, Sebastian Goldt  
Source: arXiv:2605.21402  
URL: https://arxiv.org/abs/2605.21402v1
