---
title: "A Comparative Analysis of Machine Learning and Deep Learning Models for Tweet Sentiment Classification: A Case Study on the Sentiment140 Dataset"
date: 2026-05-06 13:21:07 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.04888v1"
arxiv_id: "2605.04888"
authors: ["Vita Anggraini", "Cintya Bella", "Bastian", "Luluk Muthoharoh", "Ardika Satria", "Martin C. T. Manullang"]
slug: a-comparative-analysis-of-machine-learning-and-deep-learning
summary_word_count: 483
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the comparative performance of traditional machine learning models versus deep learning architectures for sentiment classification in social media text. Specifically, it investigates the efficacy of Logistic Regression with TF-IDF features against a Bidirectional Long Short-Term Memory (BiLSTM) model on the Sentiment140 dataset, which is a well-known benchmark for sentiment analysis. The study is particularly relevant given the increasing volume of unstructured sentiment data generated on platforms like Twitter, necessitating effective automated analysis methods.

**Method**  
The authors employed a Logistic Regression model utilizing TF-IDF (Term Frequency-Inverse Document Frequency) for feature extraction, which is a standard approach in traditional machine learning for text classification. In contrast, the deep learning component is based on a BiLSTM architecture, which captures contextual information from both directions in the text sequence. The dataset used consists of a 10,000-tweet subset from the Sentiment140 dataset, which includes labeled sentiments. The models were trained and evaluated on this subset, with the Logistic Regression model serving as a baseline. The training compute details were not disclosed, but the models were integrated into a web application using Streamlit and deployed on Hugging Face Spaces for public access.

**Results**  
The results indicate that the Logistic Regression model achieved an accuracy of 73.5%, outperforming the BiLSTM model, which achieved an accuracy of 69.17%. The authors noted that the BiLSTM exhibited mild overfitting, suggesting that the complexity of the model may not be justified given the dataset size. These results highlight a significant effect size favoring the traditional model over the deep learning approach in this specific context, challenging the assumption that more complex models always yield better performance in sentiment classification tasks.

**Limitations**  
The authors acknowledge that the study is limited by the size of the dataset subset used (10,000 tweets), which may not fully represent the diversity of sentiment expressions on Twitter. Additionally, the mild overfitting observed in the BiLSTM model raises concerns about its generalizability to larger datasets. The paper does not explore other deep learning architectures or hyperparameter tuning, which could potentially improve the performance of the BiLSTM. Furthermore, the integration into a web application, while useful for accessibility, does not provide insights into the model's performance in real-time scenarios or on larger datasets.

**Why it matters**  
This work has significant implications for the field of sentiment analysis, particularly in contexts where computational resources are limited or where rapid deployment is necessary. The findings suggest that traditional machine learning methods, when combined with effective feature extraction techniques, can outperform more complex deep learning models for specific tasks, such as sentiment classification of informal text. This could influence future research directions, encouraging a reevaluation of the necessity of deep learning for similar applications and promoting the exploration of hybrid approaches that leverage the strengths of both paradigms.

Authors: Vita Anggraini, Cintya Bella, Bastian, Luluk Muthoharoh, Ardika Satria, Martin C. T. Manullang  
Source: arXiv cs.CL  
URL: https://arxiv.org/abs/2605.04888v1
