---
title: "GHGbench: A Unified Multi-Entity, Multi-Task Benchmark for Carbon Emission Prediction"
date: 2026-05-13 16:20:49 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13743v1"
arxiv_id: "2605.13743"
authors: ["Yifan Duan", "Siyuan Zheng", "Lihuan Li", "Chao Xue", "Flora Salim"]
slug: ghgbench-a-unified-multi-entity-multi-task-benchmark-for-car
summary_word_count: 450
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the fragmentation in existing datasets and benchmarks for entity-level carbon emission prediction, which limits the ability to conduct comprehensive evaluations across different contexts. The authors introduce GHGbench, a unified benchmark that consolidates data for both company- and building-level greenhouse gas emissions. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
GHGbench comprises two tracks: the company track and the building track. The company track includes over 32,000 company-year records from more than 12,000 firms, featuring Scope 1+2 and Scope 3 emissions disclosures alongside financial and sectoral signals. The building track harmonizes 491,591 building-year records from 13 open sources into a unified schema, covering 26 metropolitan areas (10 in the U.S., 15 in Australia, and 1 in Singapore). This track incorporates climate covariates and multimodal remote-sensing embeddings. The benchmark defines canonical splits for primary tasks, including in-distribution and cross-region/city transfer, as well as supplementary tasks like temporal hold-out and short-horizon forecasting. Baselines evaluated include gradient-boosted trees, a tabular foundation model, multi-layer perceptrons (MLP), FT-Transformer, and multimodal fusion, with a panel of large language models (LLMs) as auxiliary. All models were assessed using multi-seed paired-bootstrap tests.

**Results**  
The authors report three significant findings: (i) building emissions prediction is structurally more challenging than that of company emissions; (ii) the gap between in-distribution and out-of-distribution performance is substantially larger than any within-model performance differences across both tracks. Notably, the tabular foundation model achieves a statistically significant improvement over tuned trees on a multi-city building emissions task; (iii) multimodal remote-sensing embeddings enhance performance precisely in scenarios where tabular generalization fails. The paper also identifies catastrophic city transfer and the sector-factor lookup ceiling as systematic failure modes in the current methodologies.

**Limitations**  
The authors acknowledge that GHGbench exposes certain limitations, such as the catastrophic city transfer issue and the sector-factor lookup ceiling, which may hinder generalization across different contexts. However, they do not discuss potential biases in the dataset or the implications of using multimodal embeddings, which could introduce complexity in model interpretability. Additionally, the reliance on specific geographic regions may limit the generalizability of findings to other areas.

**Why it matters**  
GHGbench provides a critical resource for researchers and practitioners in the field of carbon emission prediction, offering a standardized framework for evaluating models across diverse contexts. By addressing the fragmentation in existing datasets, this benchmark facilitates more robust comparisons and encourages the development of advanced predictive models. The findings regarding the challenges of building emissions and the effectiveness of multimodal embeddings have implications for future research, particularly in enhancing model generalization and addressing systematic biases in carbon emission predictions.

Authors: Yifan Duan, Siyuan Zheng, Lihuan Li, Chao Xue, Flora Salim  
Source: arXiv:2605.13743  
URL: [https://arxiv.org/abs/2605.13743v1](https://arxiv.org/abs/2605.13743v1)
