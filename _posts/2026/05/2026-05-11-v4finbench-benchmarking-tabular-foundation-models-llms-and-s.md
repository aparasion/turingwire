---
title: "V4FinBench: Benchmarking Tabular Foundation Models, LLMs, and Standard Methods on Corporate Bankruptcy Prediction"
date: 2026-05-11 17:38:17 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10896v1"
arxiv_id: "2605.10896"
authors: ["Marcin Kostrzewa", "Sebastian Tomczak", "Roman Furman", "Anna Poberezhna", "Micha\u0142 Furga\u0142a", "Oleksii Furman"]
slug: v4finbench-benchmarking-tabular-foundation-models-llms-and-s
summary_word_count: 465
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of comprehensive benchmarks for corporate bankruptcy prediction, particularly in the context of severe class imbalance and multi-horizon forecasting. Existing datasets are limited in size and scope, with most public datasets containing between 6,000 and 80,000 observations, while larger datasets are often behind paywalls. The authors present V4FinBench, a new benchmark comprising over one million company-year records from the Visegràd Group economies (2006-2021), which is designed to facilitate the evaluation of various predictive models in a more realistic financial context. This work is a preprint and has not yet undergone peer review.

**Method**  
V4FinBench includes 131 financial and non-financial features and supports six prediction horizons, with a composite distress criterion that captures solvency, profitability, and liquidity deterioration. The dataset is characterized by a class imbalance with positive rates ranging from 0.19% to 0.36%. The authors evaluate several models, including standard tabular baselines, a finetuned TabPFN, and a QLoRA-finetuned Llama-3-8B. The finetuning of TabPFN incorporates imbalance-aware techniques, allowing it to match or exceed the performance of gradient boosting models at longer time horizons. The evaluation metrics used include F1-score and ROC-AUC.

**Results**  
The results indicate that the imbalance-aware finetuned TabPFN outperforms gradient boosting on both F1-score and ROC-AUC at longer prediction horizons. Specifically, TabPFN achieves superior performance compared to gradient boosting, particularly in the context of longer-term predictions. In contrast, the Llama-3-8B model consistently underperforms gradient boosting across all horizons, with a notable decline in performance as the prediction horizon extends. Additionally, in an external evaluation using the American Bankruptcy Dataset, the V4FinBench-finetuned TabPFN checkpoint demonstrates improved performance over the vanilla TabPFN, indicating that the finetuning process captures transferable financial distress structures rather than merely V4-specific patterns.

**Limitations**  
The authors acknowledge that while V4FinBench provides a substantial dataset for benchmarking, it is still limited to the Visegràd Group economies, which may not generalize to other regions or economic contexts. Furthermore, the reliance on historical data from 2006-2021 may not account for recent economic shifts or crises. The performance of Llama-3-8B raises questions about the applicability of large language models in tabular data contexts, suggesting a need for further exploration of their capabilities in financial prediction tasks.

**Why it matters**  
The introduction of V4FinBench is significant for advancing research in corporate bankruptcy prediction, as it provides a large-scale, publicly available dataset that can facilitate the development and evaluation of various predictive models under realistic conditions. This benchmark can help bridge the gap between traditional tabular methods and emerging foundation models, fostering innovation in financial forecasting techniques. The findings also highlight the importance of model adaptation and the potential for transfer learning in financial applications, paving the way for future research in this domain.

Authors: Marcin Kostrzewa, Sebastian Tomczak, Roman Furman, Anna Poberezhna, Michał Furgała, Oleksii Furman, Maciej Zięba  
Source: arXiv:2605.10896  
URL: https://arxiv.org/abs/2605.10896v1
