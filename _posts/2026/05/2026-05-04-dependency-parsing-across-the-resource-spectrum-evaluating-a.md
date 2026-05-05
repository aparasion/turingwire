---
title: "Dependency Parsing Across the Resource Spectrum: Evaluating Architectures on High and Low-Resource Languages"
date: 2026-05-04 13:55:32 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02608v1"
arxiv_id: "2605.02608"
authors: ["Kevin Guan", "Happy Buzaaba", "Christiane Fellbaum"]
slug: dependency-parsing-across-the-resource-spectrum-evaluating-a
summary_word_count: 439
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the performance of transformer-based models versus simpler architectures for dependency parsing in low-resource languages, particularly focusing on under-resourced African languages. While transformers have dominated high-resource language tasks, their efficacy in low-resource settings remains inadequately explored, creating uncertainty in their applicability for syntactic tool development in these contexts.

**Method**  
The authors evaluate four dependency parsing architectures: Biaffine LSTM, Stack-Pointer Network, AfroXLMR-large, and RemBERT. The evaluation spans ten typologically diverse languages, emphasizing low-resource African languages. The study employs a comparative analysis of parsing performance across varying amounts of training data, specifically examining the crossover point where transformer models begin to outperform simpler architectures. The Biaffine LSTM serves as the baseline, while the performance of transformers is assessed in relation to corpus size and morphological complexity, quantified using the Mean Type-Token Ratio (MATTR). The training compute details are not disclosed, but the architectures are implemented in a standard framework for dependency parsing tasks.

**Results**  
The Biaffine LSTM consistently outperforms the transformer models (AfroXLMR-large and RemBERT) in low-resource scenarios, with significant performance gains observed in parsing accuracy metrics. As training data increases, the performance of transformers improves, eventually surpassing the Biaffine LSTM. The crossover point occurs within a resource range typical of treebanks for under-resourced languages, indicating that the Biaffine LSTM is more effective until a certain threshold of annotated data is reached. The study quantifies the effect of morphological complexity, revealing it as a significant predictor of the transformers' relative disadvantage, even after controlling for corpus size.

**Limitations**  
The authors acknowledge that their findings are limited to the specific architectures and languages evaluated, which may not generalize across all low-resource languages or parsing tasks. Additionally, the study does not explore the impact of different training regimes or hyperparameter tuning on model performance. The reliance on MATTR as a measure of morphological complexity may also oversimplify the linguistic diversity present in the evaluated languages. Furthermore, the computational resources and specific training configurations used for each model are not detailed, which could affect reproducibility.

**Why it matters**  
This work has significant implications for the development of syntactic tools in low-resource settings. By demonstrating that simpler architectures like the Biaffine LSTM can outperform more complex transformer models in low-resource scenarios, the study suggests a strategic approach for researchers and practitioners. It highlights the importance of considering resource availability and morphological characteristics when selecting models for dependency parsing tasks. The findings advocate for a phased approach to model deployment, where simpler models are prioritized until sufficient annotated data is available to leverage the strengths of transformer architectures.

Authors: Kevin Guan, Happy Buzaaba, Christiane Fellbaum  
Source: arXiv:2605.02608  
URL: [https://arxiv.org/abs/2605.02608v1](https://arxiv.org/abs/2605.02608v1)
