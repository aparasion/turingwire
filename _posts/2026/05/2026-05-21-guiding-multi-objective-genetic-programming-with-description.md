---
title: "Guiding Multi-Objective Genetic Programming with Description Length Improves Symbolic Regression Solutions"
date: 2026-05-21 12:07:05 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.22374v1"
arxiv_id: "2605.22374"
authors: ["Gabriel Kronberger", "Fabricio Olivetti de Franca", "Deaglan J. Bartlett", "Harry Desmond", "Pedro G. Ferreira"]
slug: guiding-multi-objective-genetic-programming-with-description
summary_word_count: 431
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of traditional heuristics in symbolic regression using genetic programming (GPSR), particularly the issues of overfitting and structural bloat in the presence of noise. Existing model selection criteria like Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) may not effectively balance model complexity and generalization. The authors propose using description length (DL) and fractional Bayes factor (FBF) as principled alternatives to improve the selection of compact expressions that generalize well.

**Method**  
The core technical contribution involves the implementation of DL using a Fisher-information-based parameter encoding. The authors compare DL and FBF against AIC and BIC across various datasets, including both synthetic benchmarks with noise and real-world regression problems. They explore three distinct search/selection strategies:  
1. Multi-objective search optimizing for accuracy and program length, followed by DL/FBF selection.  
2. Multi-objective search using DL directly as an objective.  
3. Single-objective optimization with DL/FBF as the fitness function.  
The study emphasizes the importance of using DL/FBF for post-selection rather than as a direct fitness function, as the latter often leads to premature convergence.

**Results**  
The results demonstrate that the DL/FBF post-selection approach significantly enhances test performance compared to the AIC/BIC baseline across multiple datasets. Specifically, the authors report that using BIC in conjunction with the function complexity penalty from DL/FBF yields comparable results to the DL/FBF post-selection method. However, when DL/FBF is employed directly as a fitness function in single-objective GPSR, it frequently results in overly simplistic models, indicating a trade-off in model complexity and performance.

**Limitations**  
The authors acknowledge that while DL/FBF improves model selection, the direct use of these criteria as fitness functions can lead to premature convergence. They do not address the computational overhead associated with calculating DL and FBF, which may impact scalability in larger datasets or more complex models. Additionally, the study does not explore the integration of these methods with other advanced techniques in genetic programming, such as ensemble methods or hybrid approaches.

**Why it matters**  
This work has significant implications for the field of symbolic regression and genetic programming. By providing a robust framework for model selection that mitigates overfitting and structural bloat, the findings can enhance the reliability of GPSR in practical applications. The proposed methods can serve as a foundation for future research aimed at improving model interpretability and generalization in noisy environments. Furthermore, the insights gained from this study can inform the design of more sophisticated genetic programming algorithms that leverage principled model selection criteria.

Authors: Gabriel Kronberger, Fabricio Olivetti de Franca, Deaglan J. Bartlett, Harry Desmond, Pedro G. Ferreira  
Source: arXiv cs.NE  
URL: [https://arxiv.org/abs/2605.22374v1](https://arxiv.org/abs/2605.22374v1)  
arXiv ID: 2605.22374
