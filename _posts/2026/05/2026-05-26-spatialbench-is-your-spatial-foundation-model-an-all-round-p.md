---
title: "SpatialBench: Is Your Spatial Foundation Model an All-Round Player?"
date: 2026-05-26 17:59:20 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.27367v1"
arxiv_id: "2605.27367"
authors: ["Haosong Peng", "Hao Li", "Jiaqi Chen", "Yuhao Pan", "Runmao Yao", "Yalun Dai"]
slug: spatialbench-is-your-spatial-foundation-model-an-all-round-p
summary_word_count: 472
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in evaluating spatial foundation models (SFMs) across diverse downstream tasks and conditions. While existing models have shown strong performance on specific datasets, their generalization capabilities across varying viewpoints, scene domains, input densities, and hardware constraints remain inadequately assessed. The authors highlight that current evaluations are limited by narrow paradigm coverage and arbitrary sampling methods, which do not provide a comprehensive understanding of model robustness. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce SpatialBench, a benchmark designed to holistically evaluate SFMs across multiple paradigms and domains. SpatialBench encompasses 19 datasets and 546 scenes across five distinct spatial domains, facilitating a rigorous assessment of 41 models across six paradigms. The evaluation is structured around five task suites and incorporates four different input density settings. The benchmark employs deterministic sampling to ensure consistency in evaluations. Additionally, the authors propose a new large-scale dataset, DA-Next-5M, and a baseline model, DA-Next, aimed at enhancing spatial representation learning. The findings indicate that full-context attention mechanisms improve accuracy, while bounded-memory strategies enhance scalability for long sequences.

**Results**  
The evaluation reveals that current SFMs do not qualify as all-round players, with performance metrics indicating significant limitations. The authors provide empirical evidence that strict domain alignment and high data quality are more critical for performance than mere dataset scaling. Specific performance metrics are not disclosed in the abstract, but the results suggest that existing models struggle with generalization across the diverse conditions tested in SpatialBench. The introduction of DA-Next-5M and the DA-Next model serves as a strong baseline, pushing the boundaries of what is achievable in spatial representation tasks.

**Limitations**  
The authors acknowledge that their benchmark, while comprehensive, may still be limited by the specific domains and tasks included. They do not address potential biases in dataset selection or the representativeness of the scenes used. Furthermore, the reliance on deterministic sampling may not capture the variability present in real-world applications. The performance metrics provided are not exhaustive, and the implications of the findings on broader model architectures remain to be explored.

**Why it matters**  
The introduction of SpatialBench is significant for the field of spatial representation learning, as it provides a structured framework for evaluating the generalization capabilities of SFMs. By highlighting the importance of domain alignment and data quality, this work encourages future research to focus on these aspects rather than solely on dataset size. The development of DA-Next-5M and the DA-Next model offers a new avenue for advancing spatial foundation models, potentially leading to more robust applications in real-world scenarios. This benchmark could serve as a reference point for future studies, fostering a deeper understanding of model capabilities and limitations.

Authors: Haosong Peng, Hao Li, Jiaqi Chen, Yuhao Pan, Runmao Yao, Yalun Dai, Fushuo Huo, Fangzhou Hong et al.  
Source: arXiv:2605.27367  
URL: [https://arxiv.org/abs/2605.27367v1](https://arxiv.org/abs/2605.27367v1)
