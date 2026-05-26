---
title: "CITYREP: A Unified Benchmark for Urban Representations Across Cities, Tasks, and Modalities"
date: 2026-05-25 17:03:46 +0000
category: research
subcategory: evaluation_benchmarks
company: "Meta"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26036v1"
arxiv_id: "2605.26036"
authors: ["Junyuan Liu", "Xinglei Wang", "Zichao Zeng", "Jiazhuang Feng", "Quan Qin", "Ilya Ilyankou"]
slug: cityrep-a-unified-benchmark-for-urban-representations-across
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations in current urban representation learning evaluations, which typically focus on a narrow set of cities and tasks, often employing random data splits that introduce spatial leakage. This results in inflated performance metrics and weakens the ability to generalize across different urban environments. The authors propose CityRep, a unified benchmark designed to provide a more robust evaluation framework for urban representations across multiple cities, tasks, and data modalities. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
CityRep introduces a comprehensive evaluation framework that consists of three main components:  
1. **Spatial Unit-Agnostic Evaluation Framework**: This framework allows for the integration of heterogeneous urban representations through a standardized alignment module, facilitating comparisons across different representation types.  
2. **Unified Evaluation Protocol**: The authors implement block-based spatial splits to mitigate spatial leakage, ensuring that the evaluation is rigorous and fair. This protocol is crucial for accurately assessing model performance without the confounding effects of data leakage.  
3. **Multi-City, Multi-Task Benchmark Suite**: CityRep encompasses a diverse set of datasets and tasks, covering 8 cities and 8 tasks, including regression, classification, and distribution prediction. The benchmark evaluates 11 representative urban representation models, providing a comprehensive landscape for urban representation learning.

**Results**  
The evaluation results indicate that model performance is highly sensitive to the chosen split protocol. Specifically, the use of random splits led to inflated performance scores and altered model rankings, highlighting the importance of the proposed block-based spatial splits. The authors report substantial variability in performance across different cities and tasks, emphasizing the necessity for generalization-aware evaluation methods. The paper does not provide specific numerical results or effect sizes, but it underscores the critical impact of evaluation methodology on model performance assessment.

**Limitations**  
The authors acknowledge that the benchmark is still in its early stages and may require further refinement as more urban representation models are developed. They also note that while CityRep aims to standardize evaluations, the complexity of urban environments may still pose challenges in achieving truly generalizable representations. Additionally, the reliance on specific cities and tasks may limit the applicability of findings to other urban contexts not included in the benchmark.

**Why it matters**  
CityRep has significant implications for the field of urban representation learning, as it provides a structured and reproducible framework for evaluating models. By addressing the issues of spatial leakage and narrow evaluation scopes, it facilitates fair comparisons and supports the development of urban foundation models that can generalize across diverse urban settings. This benchmark is expected to catalyze further research and innovation in urban representation learning, ultimately contributing to more effective urban planning and management solutions.

Authors: Junyuan Liu, Xinglei Wang, Zichao Zeng, Jiazhuang Feng, Quan Qin, Ilya Ilyankou, Guangsheng Dong, Tao Cheng  
Source: arXiv:2605.26036  
URL: [https://arxiv.org/abs/2605.26036v1](https://arxiv.org/abs/2605.26036v1)
