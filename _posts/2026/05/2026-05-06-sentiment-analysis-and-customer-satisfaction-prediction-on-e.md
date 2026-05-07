---
title: "Sentiment Analysis and Customer Satisfaction Prediction on E-Commerce Platforms Based on YouTube Comments Using the XGBoost Algorithm"
date: 2026-05-06 13:20:58 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.04887v1"
arxiv_id: "2605.04887"
authors: ["Ridho Benedictus Togi Manik", "Muhammad Aqil Ramadhan", "Ihsan Maulana Yusuf", "Luluk Muthoharoh", "Ardika Satria", "Martin Clinton Tosima Manullang"]
slug: sentiment-analysis-and-customer-satisfaction-prediction-on-e
summary_word_count: 462
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in sentiment analysis and customer satisfaction prediction specifically within the context of e-commerce platforms, utilizing YouTube comments as a data source. The authors highlight the challenge posed by the unstructured and multi-contextual nature of comments on video-centric social networks, which complicates traditional sentiment tracking methods. The study aims to develop a robust predictive model that can effectively analyze this data type, which has been underexplored in existing literature.

**Method**  
The core technical contribution of this work is the application of the Extreme Gradient Boosting (XGBoost) algorithm for sentiment analysis, enhanced by Term Frequency-Inverse Document Frequency (TF-IDF) vectorization for feature extraction. The authors preprocess a secondary dataset of YouTube comments from e-commerce review videos, transforming raw text into normalized numerical features suitable for machine learning. The model is optimized using the PyCaret framework, which automates hyperparameter tuning and model selection. The training compute details are not disclosed, but the methodology emphasizes the importance of feature engineering and model optimization in achieving high classification performance.

**Results**  
The experimental results indicate that the XGBoost model, when optimized through PyCaret, outperforms baseline models in terms of classification accuracy and robustness. While specific headline numbers are not provided in the abstract, the authors claim superior performance metrics compared to standard benchmarks in sentiment analysis. Additionally, the study reveals that socio-political terminologies significantly influence the polarity of customer satisfaction, suggesting a nuanced understanding of sentiment in e-commerce discourse. The results underscore the model's ability to capture complex sentiment dynamics that traditional methods may overlook.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a secondary dataset, which may not fully represent the broader e-commerce landscape. They also note potential biases in the YouTube comments, as the dataset may be skewed towards specific demographics or sentiments. Furthermore, the study does not explore the temporal dynamics of sentiment, which could provide insights into how customer satisfaction evolves over time. An additional limitation is the lack of comparative analysis with other advanced models, such as deep learning architectures, which could provide a more comprehensive evaluation of the proposed method's effectiveness.

**Why it matters**  
This research has significant implications for downstream work in sentiment analysis and customer satisfaction prediction, particularly in the context of e-commerce. By leveraging YouTube comments, the study opens new avenues for understanding consumer sentiment in a rapidly evolving digital landscape. The findings regarding the influence of socio-political language on customer satisfaction could inform marketing strategies and content creation for e-commerce platforms. Moreover, the methodological advancements in using XGBoost and TF-IDF vectorization may serve as a foundation for future studies aiming to analyze unstructured text data in various domains.

Authors: Ridho Benedictus Togi Manik, Muhammad Aqil Ramadhan, Ihsan Maulana Yusuf, Luluk Muthoharoh, Ardika Satria, Martin Clinton Tosima Manullang  
Source: arXiv:2605.04887  
URL: [https://arxiv.org/abs/2605.04887v1](https://arxiv.org/abs/2605.04887v1)
