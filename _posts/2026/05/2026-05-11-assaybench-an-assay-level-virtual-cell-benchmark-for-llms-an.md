---
title: "AssayBench: An Assay-Level Virtual Cell Benchmark for LLMs and Agents"
date: 2026-05-11 17:27:16 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10876v1"
arxiv_id: "2605.10876"
authors: ["Edward De Brouwer", "Carl Edwards", "Alexander Wu", "Jenna Collier", "Graham Heimberg", "Xiner Li"]
slug: assaybench-an-assay-level-virtual-cell-benchmark-for-llms-an
summary_word_count: 435
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of a standardized benchmark for in silico phenotypic screening, a critical task in drug discovery that involves predicting cellular responses to perturbations. Existing benchmarks primarily focus on molecular readouts, which do not directly correlate with the phenotypic endpoints essential for real-world applications. The authors present AssayBench, a novel assay-level benchmark designed to evaluate the performance of large language models (LLMs) and agentic systems in predicting phenotypic outcomes from diverse biological data. This work is a preprint and has not yet undergone peer review.

**Method**  
AssayBench is constructed from 1,920 publicly available CRISPR screens, encompassing five broad classes of cellular phenotypes. The core technical contribution is the formulation of the screen prediction task as a gene rank prediction problem for each assay. The authors introduce the adjusted normalized Discounted Cumulative Gain (nDCG) as a continuous evaluation metric, which allows for performance comparison across heterogeneous assays. The evaluation includes various existing methods, with a focus on zero-shot generalist LLMs, biology-specific LLMs, and trainable baselines. The authors also explore optimization techniques such as fine-tuning, ensembling, and prompt optimization to enhance model performance.

**Results**  
The evaluation reveals that current methods are significantly below the empirically estimated performance ceilings for phenotypic screen prediction. Notably, zero-shot generalist LLMs outperform both biology-specific LLMs and trainable baselines across the benchmark. The introduction of optimization techniques yields further improvements in performance, although specific numerical results and effect sizes are not disclosed in the abstract. The findings suggest that there is substantial room for advancement in the predictive capabilities of models in this domain.

**Limitations**  
The authors acknowledge that the benchmark is based on publicly available CRISPR screens, which may not encompass the full diversity of biological contexts encountered in real-world applications. Additionally, the performance of models may vary significantly based on the specific phenotypic classes and the quality of the input data. The paper does not address potential biases in the datasets used or the generalizability of the results across different biological systems.

**Why it matters**  
AssayBench represents a significant step toward establishing a practical testbed for evaluating progress in in silico phenotypic screening and virtual cell models. By providing a standardized framework, it enables researchers to benchmark their models against a common set of tasks, facilitating the comparison of methodologies and driving advancements in predictive modeling for drug discovery. The implications extend to enhancing the efficiency of biological discovery processes, potentially leading to faster identification of therapeutic targets and improved drug development pipelines.

Authors: Edward De Brouwer, Carl Edwards, Alexander Wu, Jenna Collier, Graham Heimberg, Xiner Li, Meena Subramaniam, Ehsan Hajiramezanali et al.  
Source: arXiv:2605.10876  
URL: https://arxiv.org/abs/2605.10876v1
