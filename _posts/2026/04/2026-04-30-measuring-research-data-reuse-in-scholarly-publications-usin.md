---
title: "Measuring research data reuse in scholarly publications using generative artificial intelligence: Open Science Indicator development and preliminary results"
date: 2026-04-30 16:07:43 +0000
category: research
subcategory: other
company: "PLOS"
secondary_companies: ["DataSeer"]
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.28061v1"
arxiv_id: "2604.28061"
authors: ["Lauren Cadwallader", "Iain Hrynaszkiewicz", "parth sarin", "Tim Vines"]
slug: measuring-research-data-reuse-in-scholarly-publications-usin
summary_word_count: 455
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in quantifying the downstream effects of open science practices, specifically focusing on the reuse of research data in scholarly publications. While existing metascience studies have monitored the prevalence of open science, there is a lack of robust indicators that measure the actual impact of data sharing and reuse. The authors propose a novel approach using generative artificial intelligence to develop an Open Science Indicator that can assess data reuse at scale.

**Method**  
The core technical contribution of this work is the development of a large language model (LLM)-based indicator designed to quantify research data reuse in scholarly publications. The authors leverage generative AI techniques to analyze text from academic papers, extracting instances of data reuse. The methodology involves training the LLM on a diverse corpus of scholarly articles, enabling it to identify and quantify references to reused datasets. The training compute specifics are not disclosed, but the approach emphasizes scalability and efficiency in measuring data reuse compared to traditional bibliometric methods.

**Results**  
The authors report a data reuse rate of 43%, which significantly surpasses the rates typically identified through established bibliometric techniques. This finding suggests that previous assessments may have underestimated the extent of data reuse in the academic literature. The results indicate that the LLM-based approach can effectively capture and quantify data reuse, providing a more comprehensive understanding of the impact of open science practices.

**Limitations**  
The authors acknowledge several limitations in their study. First, the reliance on LLMs may introduce biases based on the training data, potentially affecting the accuracy of data reuse detection. Additionally, the study does not account for the context in which data is reused, which could lead to misinterpretations of the reuse rate. The authors also note that their findings are preliminary and require further validation across different domains and datasets. An obvious limitation not flagged by the authors is the potential for overfitting in the LLM due to the specific nature of the training corpus, which may not generalize well to all fields of research.

**Why it matters**  
This work has significant implications for the field of metascience and the broader open science movement. By providing a scalable and effective method for measuring data reuse, the authors contribute to a more nuanced understanding of the benefits of open science practices. The findings could inform policy decisions regarding data sharing and encourage researchers to adopt more open practices, ultimately enhancing the reproducibility and transparency of scientific research. Furthermore, the development of the Open Science Indicator could pave the way for future studies that explore the relationship between data reuse and research outcomes, fostering a culture of data sharing in academia.

Authors: Lauren Cadwallader, Iain Hrynaszkiewicz, parth sarin, Tim Vines  
Source: arXiv:2604.28061  
URL: [https://arxiv.org/abs/2604.28061v1](https://arxiv.org/abs/2604.28061v1)
