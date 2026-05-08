---
title: "SoftSAE: Dynamic Top-K Selection for Adaptive Sparse Autoencoders"
date: 2026-05-07 17:28:40 +0000
category: research
subcategory: interpretability
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06610v1"
arxiv_id: "2605.06610"
authors: ["Jakub St\u0119pie\u0144", "Marcin Mazur", "Jacek Tabor", "Przemys\u0142aw Spurek"]
slug: softsae-dynamic-top-k-selection-for-adaptive-sparse-autoenco
summary_word_count: 405
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the capability of Sparse Autoencoders (SAEs) to adaptively select the number of active features based on the complexity of input data. Traditional Top-K SAEs enforce a fixed sparsity level (K) across all inputs, which fails to account for the varying intrinsic dimensionality of real-world data. This limitation can lead to suboptimal feature selection, where simple inputs may be over-represented and complex inputs under-represented. The authors present SoftSAE, a preprint work, to overcome this limitation by introducing a dynamic selection mechanism for sparsity.

**Method**  
The core technical contribution of this work is the SoftSAE architecture, which incorporates a differentiable Soft Top-K operator. This operator enables the model to learn an input-dependent sparsity level (k), allowing for a variable number of active features tailored to the complexity of each input. The training process involves standard backpropagation, leveraging the differentiability of the Soft Top-K operator to optimize the selection of features dynamically. The authors do not disclose specific training compute or dataset details, but they emphasize the model's ability to adjust the number of active features in response to the input's characteristics.

**Results**  
Experimental evaluations demonstrate that SoftSAE outperforms traditional Top-K SAEs on several benchmarks, although specific baseline models are not named in the summary. The results indicate that SoftSAE effectively identifies meaningful features while also selecting an appropriate number of features for each concept. The authors report significant improvements in representation quality, although exact effect sizes and quantitative metrics are not provided in the abstract.

**Limitations**  
The authors acknowledge that while SoftSAE improves feature selection, it may still be sensitive to the choice of hyperparameters related to the Soft Top-K operator. Additionally, the paper does not address potential computational overhead introduced by the dynamic selection mechanism, which could impact scalability in large datasets. Other limitations include the lack of extensive empirical validation across diverse datasets and the absence of a comparison with other adaptive sparsity techniques.

**Why it matters**  
The implications of this work are significant for mechanistic interpretability in machine learning, particularly in the context of Large Language Models (LLMs) and Vision Transformers (ViTs). By enabling adaptive feature selection, SoftSAE enhances the interpretability of neural network representations, allowing for more accurate translations of model computations into human-understandable concepts. This advancement could facilitate better understanding and debugging of complex models, ultimately contributing to more robust AI systems.

Authors: Jakub Stępień, Marcin Mazur, Jacek Tabor, Przemysław Spurek  
Source: arXiv:2605.06610  
URL: [https://arxiv.org/abs/2605.06610v1](https://arxiv.org/abs/2605.06610v1)
