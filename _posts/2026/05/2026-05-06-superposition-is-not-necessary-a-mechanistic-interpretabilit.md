---
title: "Superposition Is Not Necessary: A Mechanistic Interpretability Analysis of Transformer Representations for Time Series Forecasting"
date: 2026-05-06 17:23:27 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.05151v1"
arxiv_id: "2605.05151"
authors: ["Alper Y\u0131ld\u0131r\u0131m"]
slug: superposition-is-not-necessary-a-mechanistic-interpretabilit
summary_word_count: 388
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the representational mechanisms of Transformer architectures in the context of time series forecasting. While Transformers have been successful in NLP, their effectiveness in time series tasks remains underexplored. The paper specifically investigates why simple linear models, such as DLinear, continue to perform competitively against more complex Transformer models, without a mechanistic explanation for this phenomenon.

**Method**  
The authors employ sparse autoencoders (SAEs) to analyze the internal representations of the PatchTST Transformer model. They establish that a single-layer, narrow-dimensional Transformer can achieve forecasting performance comparable to deeper configurations across standard benchmarks. The SAEs are trained on the post-GELU intermediate feedforward network (FFN) activations, with dictionary sizes varying from 0.5x to 4.0x the native dimensionality of the representations. The study focuses on the effects of dictionary expansion on downstream performance and the sensitivity of the representations to targeted causal interventions on dominant latent features.

**Results**  
The findings indicate that expanding the dictionary size yields negligible changes in downstream performance, averaging only 0.214%. Notably, large portions of the overcomplete dictionaries remain inactive, suggesting a sparse representation. The targeted interventions on dominant latent features result in minimal perturbations to the forecasts, indicating that the representations do not rely on strong superposition. Across all evaluated configurations, the authors find no empirical evidence supporting the necessity of superposition for achieving competitive performance on standard forecasting benchmarks.

**Limitations**  
The authors acknowledge that their analysis is limited to the PatchTST architecture and may not generalize to all Transformer variants or other forecasting tasks. Additionally, the study does not explore the implications of these findings on the broader landscape of model interpretability or the potential for other architectures. The reliance on specific benchmarks may also limit the applicability of the results to diverse real-world time series data.

**Why it matters**  
This work has significant implications for the understanding of Transformer models in time series forecasting. By demonstrating that superposition is not a requisite for competitive performance, the study challenges the prevailing notion that complex compositional representations are essential for success in this domain. This insight may encourage further exploration of simpler models and their mechanisms, potentially leading to more efficient forecasting solutions. Additionally, the findings could inform future research on model interpretability and the design of architectures tailored for time series tasks.

Authors: Alper Yıldırım  
Source: arXiv:2605.05151  
URL: [https://arxiv.org/abs/2605.05151v1](https://arxiv.org/abs/2605.05151v1)
