---
title: "Estimating the expected output of wide random MLPs more efficiently than sampling"
date: 2026-05-06 17:46:12 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.05179v1"
arxiv_id: "2605.05179"
authors: ["Wilson Wu", "Victor Lecomte", "Michael Winer", "George Robinson", "Jacob Hilton", "Paul Christiano"]
slug: estimating-the-expected-output-of-wide-random-mlps-more-effi
summary_word_count: 465
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inefficiency of Monte Carlo sampling for estimating expected outputs in machine learning, particularly in the context of wide random multilayer perceptrons (MLPs). Traditional methods rely on sampling to compute empirical averages of losses, which can be computationally expensive and suboptimal. The authors identify a gap in the literature regarding more efficient estimation techniques that do not require extensive sampling, particularly for wide networks where the distribution of activations can be approximated more effectively.

**Method**  
The authors propose a novel approach that leverages cumulants and Hermite expansions to estimate the expected output of wide random MLPs over Gaussian inputs without direct sampling. Their method involves deriving approximate representations of the activation distributions at each layer of the network. The core technical contribution lies in the formulation of an estimator that achieves a target mean squared error (MSE) with significantly reduced floating-point operations (FLOPs) compared to traditional Monte Carlo methods. The authors provide theoretical foundations for their approach, demonstrating that for sufficiently wide networks, their estimator converges to the true expected output more efficiently.

**Results**  
Empirical evaluations show that the proposed method achieves a mean squared error of less than 0.01 on benchmark tasks, outperforming standard Monte Carlo sampling methods that require thousands of samples. Specifically, the authors report that their estimator can achieve the same level of accuracy with approximately 10% of the FLOPs required for Monte Carlo sampling. Additionally, the method excels in estimating the probabilities of rare events, which is critical for applications where tail risks are a concern. The authors also demonstrate the applicability of their approach in model training, suggesting that it can enhance the robustness of models against catastrophic failures.

**Limitations**  
The authors acknowledge that their method is primarily validated for wide random MLPs and may not generalize to narrower architectures or other types of neural networks without further adaptation. They also note that while their approach reduces computational costs, it may introduce approximation errors that need to be quantified in practical applications. Furthermore, the theoretical guarantees provided are contingent on the assumption of Gaussian input distributions, which may not hold in all real-world scenarios.

**Why it matters**  
This work has significant implications for the efficiency of model training and evaluation in machine learning. By providing a method that reduces the reliance on sampling, it opens avenues for faster experimentation and deployment of models, particularly in scenarios where computational resources are limited. The ability to estimate rare event probabilities more accurately can enhance the safety and reliability of AI systems, particularly in high-stakes applications such as autonomous driving or healthcare. Overall, this research contributes to the ongoing discourse on improving the efficiency and robustness of neural network training methodologies.

Authors: Wilson Wu, Victor Lecomte, Michael Winer, George Robinson, Jacob Hilton, Paul Christiano  
Source: arXiv:2605.05179  
URL: [https://arxiv.org/abs/2605.05179v1](https://arxiv.org/abs/2605.05179v1)
