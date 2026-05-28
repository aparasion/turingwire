---
title: "Improving Evaluation of Recombination-based Cartesian Genetic Programming"
date: 2026-05-27 11:54:14 +0000
category: research
subcategory: evaluation_benchmarks
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.28353v1"
arxiv_id: "2605.28353"
authors: ["Duy Long Tran", "Anja Jankovic", "Marie Anastacio", "Holger Hoos", "Roman Kalkreuth"]
slug: improving-evaluation-of-recombination-based-cartesian-geneti
summary_word_count: 443
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the underutilization of recombination-based genetic operators in Cartesian Genetic Programming (CGP), which has predominantly relied on mutation as the primary mechanism for evolutionary search. Despite recent advancements in CGP, the literature has largely overlooked the potential benefits of recombination techniques, primarily due to perceived performance limitations. This study is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The authors investigate two specific recombination-based operators: subgraph crossover and discrete phenotypic recombination. They utilize the SRBench benchmarking platform for symbolic regression to evaluate these operators. The implementations are integrated within the TinyverseGP framework, allowing for systematic experimentation. The authors conduct hyperparameter optimization for both recombination operators, focusing on tuning parameters that influence the performance of CGP. The optimization process is critical, as it aims to enhance the efficacy of the recombination methods, which have historically been deemed inferior to mutation-based approaches.

**Results**  
The study reports significant performance improvements when employing hyperparameter optimization for the recombination-based operators. Specifically, the authors demonstrate that the optimized subgraph crossover and discrete phenotypic recombination outperform traditional mutation-based CGP on the SRBench benchmark. While exact numerical results are not provided in the abstract, the authors claim that these improvements are substantial enough to warrant further investigation into recombination methods in CGP. The results suggest that the performance gap between mutation and recombination can be narrowed through careful tuning of hyperparameters.

**Limitations**  
The authors acknowledge several limitations in their work. Firstly, the study is confined to the SRBench platform, which may not fully represent the diversity of problems encountered in real-world applications of CGP. Additionally, the hyperparameter optimization process may introduce biases that could affect the generalizability of the results. The paper does not explore the scalability of the recombination operators across larger or more complex datasets, nor does it compare the computational costs associated with the different genetic operators. Furthermore, the long-term evolutionary dynamics of these operators remain unexplored, which could impact their effectiveness in sustained evolutionary runs.

**Why it matters**  
This research has significant implications for the field of evolutionary computation, particularly in the context of CGP. By demonstrating that hyperparameter optimization can enhance the performance of recombination-based operators, the authors open avenues for future research that could lead to more robust and efficient evolutionary algorithms. The findings challenge the prevailing notion that mutation is the superior operator in CGP, suggesting that a more balanced approach incorporating recombination could yield better results. This work encourages further exploration of hybrid strategies in genetic programming, potentially leading to advancements in symbolic regression and other optimization tasks.

Authors: Duy Long Tran, Anja Jankovic, Marie Anastacio, Holger Hoos, Roman Kalkreuth  
Source: arXiv:2605.28353  
URL: [https://arxiv.org/abs/2605.28353v1](https://arxiv.org/abs/2605.28353v1)
