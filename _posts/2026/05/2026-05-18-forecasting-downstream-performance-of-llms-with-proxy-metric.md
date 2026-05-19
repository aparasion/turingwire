---
title: "Forecasting Downstream Performance of LLMs With Proxy Metrics"
date: 2026-05-18 16:17:15 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18607v1"
arxiv_id: "2605.18607"
authors: ["Arkil Patel", "Siva Reddy", "Marius Mosbach", "Dzmitry Bahdanau"]
slug: forecasting-downstream-performance-of-llms-with-proxy-metric
summary_word_count: 429
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in reliable performance forecasting for language models (LMs) during the model development lifecycle. Traditional metrics, such as cross-entropy loss, are poorly aligned with downstream performance, while direct evaluation on downstream tasks is computationally expensive and often yields sparse data, particularly in early training stages. The authors aim to provide a more effective method for model selection and evaluation by proposing proxy metrics derived from token-level statistics.

**Method**  
The authors introduce a framework for constructing proxy metrics that aggregate token-level statistics from a candidate model's next token distribution, specifically focusing on expert-written solutions. The proposed metrics include entropy, top-k accuracy, and expert token rank. The evaluation is conducted across three distinct settings: (1) cross-family model selection, (2) pretraining data selection, and (3) training-time forecasting. The authors report that their proxy metrics outperform traditional loss-based and compute-based baselines, achieving a mean Spearman Rho of 0.81 for model selection compared to 0.36 for cross-entropy loss. For pretraining data selection, the proxy metrics rank 25 candidate corpora with approximately $10{,}000\times$ less compute than direct evaluation. In training-time forecasting, the metrics extrapolate downstream accuracy across an $18\times$ compute horizon, reducing error by roughly 50% compared to existing methods.

**Results**  
The proposed proxy metrics demonstrate significant improvements over traditional methods across the three evaluated settings:  
1. **Cross-family model selection**: Mean Spearman Rho = 0.81 (baseline: 0.36 for cross-entropy loss).  
2. **Pretraining data selection**: Achieves ranking of 25 candidate corpora with $10{,}000\times$ less compute than direct evaluation.  
3. **Training-time forecasting**: Extrapolates downstream accuracy with 50% less error compared to existing alternatives over an $18\times$ compute horizon.  
These results indicate that the proposed metrics provide a more reliable and efficient means of assessing model capabilities.

**Limitations**  
The authors acknowledge that their approach relies on the availability of expert-written solutions, which may not be feasible for all tasks or domains. Additionally, while the proxy metrics show promise, they have not been validated across a wide range of architectures or tasks beyond those tested in the paper. The generalizability of the findings to other model families or languages remains an open question.

**Why it matters**  
This work has significant implications for the model development lifecycle in natural language processing (NLP). By providing a more efficient and reliable means of forecasting model performance, the proposed proxy metrics can facilitate better decision-making regarding architecture selection, pretraining data curation, and training strategies. This could lead to faster iterations and improved outcomes in the development of LMs, ultimately enhancing the capabilities of NLP systems.

Authors: Arkil Patel, Siva Reddy, Marius Mosbach, Dzmitry Bahdanau  
Source: arXiv:2605.18607  
URL: [https://arxiv.org/abs/2605.18607v1](https://arxiv.org/abs/2605.18607v1)
