---
title: "Transfer Learning using 66 Diseases for Disease Forecasting Applications"
date: 2026-05-26 16:45:21 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.27269v1"
arxiv_id: "2605.27269"
authors: ["Lauren J Beesley", "Alexander C Murph", "Dave Osthus", "Lauren A Castro"]
slug: transfer-learning-using-66-diseases-for-disease-forecasting-
summary_word_count: 407
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing disease forecasting models that typically rely on a single data stream, which can lead to brittleness in predictions, especially when historical data is limited or noisy. The authors identify a gap in the literature regarding the integration of multiple data streams across various diseases for improved forecasting accuracy. They propose a novel approach that leverages transfer learning across 66 infectious diseases to enhance forecasting capabilities for 20 different disease data streams.

**Method**  
The authors employ a transfer learning framework that utilizes a diverse dataset encompassing 66 infectious diseases. They investigate the impact of incorporating multiple data streams on forecasting performance, utilizing various machine learning models. The specific architectures and training compute details are not disclosed in the abstract, but the study emphasizes the importance of data quality when integrating different streams. The authors compile a publicly available database to facilitate further research in infectious disease forecasting, which serves as a significant resource for the community.

**Results**  
The study reports that incorporating additional data streams improves forecasting performance in 84.9% of the time series and model structures evaluated. This finding suggests a robust advantage in using transfer learning across diseases, although the authors caution that the quality of the added data is critical; poorly matched data can lead to degraded performance. The results indicate a substantial effect size, although specific numerical improvements over baseline models are not detailed in the abstract.

**Limitations**  
The authors acknowledge that while their approach generally enhances forecasting accuracy, the effectiveness is contingent on the similarity of the added data streams to the target disease. They do not specify the exact models used or the computational resources required for training, which could limit reproducibility. Additionally, the study does not address potential overfitting issues that may arise from using diverse datasets, nor does it explore the implications of data sparsity in certain diseases.

**Why it matters**  
This work has significant implications for the field of infectious disease forecasting, as it provides a framework for leveraging transfer learning to improve model robustness and accuracy. By demonstrating that data from multiple diseases can enhance forecasting performance, the study encourages the integration of diverse datasets in future research. The publicly available database created by the authors serves as a valuable resource for researchers, potentially accelerating advancements in disease prediction methodologies and public health responses.

Authors: Lauren J Beesley, Alexander C Murph, Dave Osthus, Lauren A Castro  
Source: arXiv:2605.27269  
URL: [https://arxiv.org/abs/2605.27269v1](https://arxiv.org/abs/2605.27269v1)
