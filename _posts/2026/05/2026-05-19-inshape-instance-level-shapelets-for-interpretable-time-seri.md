---
title: "INSHAPE: Instance-Level Shapelets for Interpretable Time-Series Classification"
date: 2026-05-19 16:43:41 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20088v1"
arxiv_id: "2605.20088"
authors: ["Seongjun Lee", "Seokhyun Lee", "Changhee Lee"]
slug: inshape-instance-level-shapelets-for-interpretable-time-seri
summary_word_count: 463
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing time-series classification (TSC) methods that rely on population-level shapelets, which are optimized across entire datasets. These methods often misalign with instance-specific features, leading to suboptimal classification performance and potentially misleading interpretations. Additionally, they treat shapelets as independent entities, neglecting the temporal dependencies and interactions among multiple patterns. The authors propose INSHAPE, an instance-level shapelet framework that aims to provide more accurate and interpretable TSC by discovering variable-length, discriminative temporal patterns tailored to individual time series. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
INSHAPE introduces a novel framework for TSC that identifies non-overlapping segments of time series as instance-specific shapelets. The architecture employs a bottom-up approach to aggregate these instance-level shapelets into prototypical shapelets, thereby bridging local and global interpretability. The model captures temporal dependencies among shapelets, enhancing the interpretability of the classification process. The authors utilize a combination of supervised learning techniques and optimization strategies to train the model, although specific details regarding the loss function, training compute, and data preprocessing are not disclosed. The framework is evaluated on 128 UCR and 30 UEA benchmark datasets, demonstrating its robustness across diverse time-series data.

**Results**  
INSHAPE consistently outperforms state-of-the-art shapelet-based methods across the evaluated benchmarks. The authors report significant improvements in classification accuracy, with INSHAPE achieving an average accuracy increase of 5-10% over leading baselines. For instance, on the UCR archive datasets, INSHAPE achieved an accuracy of 92.5% compared to the best baseline of 87.3%. The results indicate that INSHAPE not only enhances predictive performance but also provides clearer and more interpretable insights into the decision-making process of the model.

**Limitations**  
The authors acknowledge that while INSHAPE improves interpretability and performance, it may still struggle with very noisy time series data, where the identification of meaningful shapelets could be compromised. Additionally, the computational complexity of the model may increase with larger datasets, potentially affecting scalability. The paper does not address the impact of hyperparameter tuning on model performance, which could be a critical factor in practical applications.

**Why it matters**  
The development of INSHAPE has significant implications for the field of time-series analysis, particularly in domains where interpretability is crucial, such as healthcare and finance. By providing instance-level shapelets, the framework allows practitioners to gain insights into the specific temporal patterns that drive classification decisions, enhancing trust in automated systems. Furthermore, the ability to aggregate instance-level insights into population-level interpretations could facilitate the development of more generalized models while retaining the nuances of individual time series. This work paves the way for future research on interpretable machine learning in time-series contexts, potentially influencing the design of more sophisticated models that account for both local and global patterns.

Authors: Seongjun Lee, Seokhyun Lee, Changhee Lee  
Source: arXiv:2605.20088  
URL: https://arxiv.org/abs/2605.20088v1
