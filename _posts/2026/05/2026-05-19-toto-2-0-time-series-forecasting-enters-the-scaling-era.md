---
title: "Toto 2.0: Time Series Forecasting Enters the Scaling Era"
date: 2026-05-19 17:08:24 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: critical
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20119v1"
arxiv_id: "2605.20119"
authors: ["Emaad Khwaja", "Chris Lettieri", "Gerald Woo", "Eden Belouadah", "Marc Cenac", "Guillaume Jarry"]
slug: toto-2-0-time-series-forecasting-enters-the-scaling-era
summary_word_count: 443
classification_confidence: 0.90
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the scalability of time series forecasting models, specifically the lack of robust foundation models that can effectively leverage large parameter counts. The authors present Toto 2.0, a family of models that demonstrate significant improvements in forecasting performance as model size increases, from 4 million to 2.5 billion parameters. This work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this work is the Toto 2.0 architecture, which is designed to scale effectively with parameter size. The authors employ a single training recipe across all model sizes, which includes a novel u-muP hyperparameter transfer pipeline that facilitates the transfer of hyperparameters between different model sizes. The training data consists of diverse time series datasets, although specific datasets are not disclosed. The models are trained using a standard loss function for forecasting tasks, likely mean squared error (MSE), but this is not explicitly stated. The training compute is also not detailed, leaving a gap in understanding the resource requirements for scaling.

**Results**  
Toto 2.0 achieves state-of-the-art performance on three key benchmarks: BOOM, GIFT-Eval, and the contamination-resistant TIME benchmark. The authors report significant improvements over existing baselines, although specific numerical results (e.g., RMSE or MAE values) and effect sizes are not provided in the abstract. The benchmarks are well-known in the time series forecasting community, and the results suggest that Toto 2.0 can reliably outperform previous models, particularly in scenarios where larger parameter counts are utilized.

**Limitations**  
The authors acknowledge that while Toto 2.0 demonstrates improved performance, the scalability of the models may lead to increased computational costs and resource requirements, which could limit accessibility for smaller organizations. Additionally, the paper does not discuss the potential overfitting risks associated with larger models, nor does it provide a comprehensive analysis of the model's performance across different types of time series data (e.g., seasonal vs. non-seasonal). The lack of detailed training compute information also limits reproducibility.

**Why it matters**  
The implications of this work are significant for the field of time series forecasting. By establishing that foundation models can scale effectively, the authors pave the way for future research that can explore even larger models and more complex architectures. The release of the Toto 2.0 models under an open license encourages further experimentation and application in various domains, potentially leading to advancements in areas such as finance, supply chain management, and climate modeling. This work also sets a precedent for the development of scalable architectures in other domains of machine learning.

Authors: Emaad Khwaja, Chris Lettieri, Gerald Woo, Eden Belouadah, Marc Cenac, Guillaume Jarry, Enguerrand Paquin, Xunyi Zhao et al.  
Source: arXiv:2605.20119  
URL: https://arxiv.org/abs/2605.20119v1
