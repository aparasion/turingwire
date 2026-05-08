---
title: "COVID-19 Infodemic. Understanding content features in detecting fake news using a machine learning approach"
date: 2026-05-07 15:36:17 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.06435v1"
arxiv_id: "2605.06435"
authors: ["Balakrishnan Vimala", "Hii Lee Zing", "Laporte Eric"]
slug: covid-19-infodemic-understanding-content-features-in-detecti
summary_word_count: 471
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the use of content features—specifically textual and linguistic attributes—in the detection of fake news. Despite empirical evidence suggesting that these features can effectively differentiate between real and fake news, their application in machine learning models has been underexplored. The study focuses on enhancing fake news detection capabilities during the COVID-19 pandemic, a period marked by a significant infodemic.

**Method**  
The authors conducted a series of experiments utilizing a newly compiled dataset from the COVID-19 pandemic. They explored various content features, including word bigrams and part-of-speech (POS) distributions, to assess their impact on fake news detection. The study employed several traditional machine learning algorithms: Decision Tree, K-Nearest Neighbor (KNN), Logistic Regression, Support Vector Machine (SVM), and Random Forest. The Random Forest model demonstrated the highest performance across all experimental setups. The authors also analyzed the individual contributions of textual and linguistic features, finding that while both improved detection rates when used separately, their combination did not yield significant enhancements. The study emphasizes the comparative effectiveness of bigrams versus POS tags in the context of fake news detection.

**Results**  
The Random Forest model achieved the best performance metrics, although specific numerical results (e.g., accuracy, F1-score) are not disclosed in the abstract. The SVM model followed closely in performance. The study indicates that both textual and linguistic features contribute positively to the detection of fake news, but the lack of improvement when combined suggests potential limitations in feature interaction. The authors provide a qualitative analysis of the differences in effectiveness between bigrams and POS tags, although quantitative comparisons are not detailed.

**Limitations**  
The authors acknowledge that the combination of textual and linguistic features did not lead to significant improvements in detection accuracy, which may indicate limitations in the feature set or model architecture. Additionally, the study does not explore deep learning approaches, which could potentially outperform traditional methods given the complexity of language. The dataset is also limited to content generated during the COVID-19 pandemic, which may not generalize to other contexts or types of misinformation. Furthermore, the absence of a comprehensive evaluation against state-of-the-art deep learning models leaves a gap in understanding the relative performance of their approach.

**Why it matters**  
This research underscores the importance of content features in the realm of fake news detection, particularly in times of crisis when misinformation can have severe consequences. By demonstrating that traditional machine learning methods can effectively utilize these features, the study opens avenues for further exploration into hybrid models that may incorporate both traditional and deep learning techniques. The findings may inform future research on feature selection and model design in the context of misinformation detection, potentially leading to more robust systems capable of addressing the challenges posed by the infodemic.

Authors: Balakrishnan Vimala, Hii Lee Zing, Laporte Eric  
Source: arXiv:2605.06435  
URL: https://arxiv.org/abs/2605.06435v1
