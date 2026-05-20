---
title: "CLIF: Concept-Level Influence Functions for Transparent Bottleneck Models"
date: 2026-05-19 13:42:38 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.19848v1"
arxiv_id: "2605.19848"
authors: ["Yike Sun", "Mingkun Xu", "Mu You", "Zhongzhi He", "Henghua Shen", "Zehan Tan"]
slug: clif-concept-level-influence-functions-for-transparent-bottl
summary_word_count: 460
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in interpretability of deep learning models, particularly in high-stakes applications such as medical diagnosis and finance, where understanding model decisions is crucial. The authors propose a novel method to enhance interpretability through the use of influence functions, focusing on both sample-level and concept-level insights. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of Concept-Level Influence Functions (CLIF), which leverage influence functions to assess the impact of training samples and concepts on model predictions. The architecture utilized is based on Concept Bottleneck Models (CBMs), which explicitly model concepts that influence predictions. The authors employ a two-pronged approach: first, they analyze the influence of individual training samples on model outputs, identifying both helpful and harmful samples. Second, they conduct a concept-level analysis to determine which concepts significantly affect predictions. The methodology includes adjusting the labels and weights of influential samples to restore model performance to baseline levels without retraining, thus demonstrating the practical utility of influence functions for data debugging. The experiments are conducted on the CEBaB and Yelp datasets, although specific training compute details are not disclosed.

**Results**  
The results indicate that CLIF effectively identifies impactful training samples, achieving a notable restoration of model performance when adjustments are made. On the CEBaB dataset, the authors report a performance recovery of up to 10% in accuracy after modifying influential samples. For the Yelp dataset, the influence functions successfully pinpointed harmful samples, leading to a similar performance recovery. The concept-level analysis revealed that certain concepts within the CBM framework had a significant effect on predictions, with modifications leading to observable changes in model behavior. These results suggest that CLIF provides a robust mechanism for enhancing interpretability in NLP models.

**Limitations**  
The authors acknowledge that their approach may not generalize across all model architectures and datasets, as it is specifically tailored for CBMs. Additionally, the reliance on influence functions may introduce computational overhead, particularly in large-scale datasets. The paper does not address potential biases in the training data that could affect the influence function outcomes. Furthermore, the practical implications of modifying concepts in real-world applications remain to be fully explored.

**Why it matters**  
The implications of this work are significant for the field of interpretable machine learning. By providing a method to transparently analyze the influence of training samples and concepts, CLIF enhances the ability of practitioners to debug and improve model performance without extensive retraining. This approach could facilitate the deployment of deep learning models in critical domains where interpretability is paramount, ultimately fostering greater trust and reliability in AI systems.

Authors: Yike Sun, Mingkun Xu, Mu You, Zhongzhi He, Henghua Shen, Zehan Tan, Derek F. Wong, Tao Fang  
Source: arXiv:2605.19848  
URL: [https://arxiv.org/abs/2605.19848v1](https://arxiv.org/abs/2605.19848v1)
