---
title: "scTranslation: A Comprehensive Benchmark for Single-Cell Multi-Omics Modality Translation"
date: 2026-06-02 17:00:49 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.03906v1"
arxiv_id: "2606.03906"
authors: ["Jiabei Cheng", "Jingbo Zhou", "Jun Xia", "Changkai Li", "Zhen Lei", "Chang Yu"]
slug: sctranslation-a-comprehensive-benchmark-for-single-cell-mult
summary_word_count: 369
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces scTranslation, a benchmark for evaluating single-cell multi-omics modality translation, addressing gaps in systematic evaluation."
---

**Problem**  
The paper addresses the lack of a systematic benchmark for evaluating computational methods in single-cell multi-omics modality translation. Despite the emergence of various translation models, there is no comprehensive framework that evaluates datasets, metrics, and influencing factors affecting model performance. This gap is critical, especially given the high costs and noise associated with multi-omics experiments, which necessitate robust evaluation methods. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose scTranslation, a benchmark that encompasses diverse datasets for single-cell multi-omics translation tasks. It integrates state-of-the-art models and provides a comprehensive set of evaluation metrics. The benchmark evaluates model performance across various scenarios, including feature selection, feature quality, and few-shot learning settings. The authors conduct a large-scale study of existing translation methods, analyzing their performance under these different conditions. The benchmark is open-sourced, with the code available at https://github.com/Bunnybeibei/scTranslation, facilitating further research and reproducibility.

**Results**  
The study reveals significant insights into the performance of current translation models, although specific numerical results and comparisons against named baselines are not detailed in the abstract. The authors emphasize that factors such as feature selection and quality substantially influence model performance, which has not been systematically studied in prior works. The findings suggest that existing models may not generalize well across different scenarios, highlighting the need for tailored approaches in multi-omics translation tasks.

**Limitations**  
The authors acknowledge that their benchmark may not cover all possible scenarios in single-cell multi-omics translation, and the performance metrics may need further refinement. Additionally, the reliance on existing models may limit the exploration of novel architectures that could outperform current state-of-the-art methods. The study does not provide detailed quantitative results, which could be a limitation for practitioners seeking specific performance metrics.

**Why it matters**  
The introduction of scTranslation is significant for advancing the field of single-cell multi-omics research, as it provides a structured approach to evaluate and compare translation methods. By systematically addressing the influencing factors on model performance, this benchmark opens avenues for future research and development of more effective translation models. The findings and methodologies presented in this work can inform subsequent studies and enhance the understanding of cellular states and regulatory mechanisms, as published in [arXiv](https://arxiv.org/abs/2606.03906v1).
