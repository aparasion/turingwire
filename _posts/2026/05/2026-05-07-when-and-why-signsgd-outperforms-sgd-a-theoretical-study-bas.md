---
title: "When and Why SignSGD Outperforms SGD: A Theoretical Study Based on $\ell_1$-norm Lower Bounds"
date: 2026-05-07 17:32:09 +0000
category: research
subcategory: training_methods
company: "MiniMax"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06615v1"
arxiv_id: "2605.06615"
authors: ["Hongyi Tao", "Dingzhi Yu", "Lijun Zhang"]
slug: when-and-why-signsgd-outperforms-sgd-a-theoretical-study-bas
summary_word_count: 432
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the theoretical gap in understanding the conditions under which sign-based optimization algorithms, specifically SignSGD, outperform traditional Stochastic Gradient Descent (SGD). Despite empirical evidence of SignSGD's effectiveness in training large models, existing literature primarily focuses on SGD's minimax optimality under $\ell_2$-norms, which limits the exploration of sign-based methods in standard optimization settings. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a theoretical framework that leverages $\ell_1$-norm stationarity and $\ell_\infty$-smoothness to analyze sign-based optimizers. They introduce a separable noise model that captures the coordinate-wise nature of signed updates, allowing for a more nuanced comparison between SignSGD and SGD. The core technical contributions include deriving matched upper and lower bounds for SignSGD, demonstrating that it can reduce optimization complexity by a factor of $d$ (the problem dimension) under conditions of sparse noise. The authors extend their analysis to the matrix domain, providing an optimal lower bound for the Muon optimizer, thereby showing that the benefits of sign-based methods scale with dimensionality. The theoretical framework is validated through empirical results from pretraining a 124M parameter GPT-2 model, where the convergence rates of SignSGD are shown to align with the derived theoretical predictions.

**Results**  
The paper presents significant findings: under the specified conditions, SignSGD achieves a complexity reduction of $d$ compared to SGD when dealing with sparse noise. The authors demonstrate that this theoretical advantage translates into practical performance, as evidenced by faster convergence rates during the pretraining of the GPT-2 model. While specific numerical results are not detailed in the abstract, the implications suggest a marked improvement in training efficiency relative to SGD, particularly in high-dimensional settings.

**Limitations**  
The authors acknowledge that their theoretical results are contingent upon the assumptions of $\ell_1$-norm stationarity and $\ell_\infty$-smoothness, which may not hold in all practical scenarios. Additionally, the analysis is primarily focused on sparse noise, leaving open questions regarding the performance of SignSGD in more general noise conditions. The paper does not explore the impact of hyperparameter tuning or the effects of different learning rates on the performance of sign-based methods.

**Why it matters**  
This work has significant implications for the optimization landscape in machine learning, particularly for large-scale model training. By providing a theoretical foundation for the advantages of sign-based methods, it encourages further exploration of these algorithms in various contexts, potentially leading to more efficient training protocols. The findings could influence the design of future optimizers and contribute to a deeper understanding of the trade-offs between different optimization strategies in high-dimensional spaces.

Authors: Hongyi Tao, Dingzhi Yu, Lijun Zhang  
Source: arXiv:2605.06615  
URL: [https://arxiv.org/abs/2605.06615v1](https://arxiv.org/abs/2605.06615v1)
