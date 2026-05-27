---
title: "Normal Guidance is what Attention Needs"
date: 2026-05-26 17:17:58 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.27306v1"
arxiv_id: "2605.27306"
authors: ["Ethan Harvey", "Dennis Johan Loevlie", "Michael C. Hughes"]
slug: normal-guidance-is-what-attention-needs
summary_word_count: 446
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of training classifiers for 3D medical images using a single binary label for the entire volume, rather than individual labels for each 2D slice. This weakly supervised setting is prevalent in medical imaging, where obtaining slice-level annotations is often impractical. The authors highlight that existing attention-based multiple instance learning (MIL) methods, which are designed to leverage attention scores for slice-level predictions, have been outperformed by a simple center-focused baseline that disregards image content. This gap in capability necessitates a more effective approach to improve slice-level classification accuracy in 3D medical imaging.

**Method**  
The authors introduce a novel regularization technique called Normal Guidance, which encourages the attention distribution learned by MIL methods to conform to a bell-shaped curve. This approach is integrated into attention-based and transformer-based MIL architectures. The training process involves three medical imaging datasets, comprising over 4 million 2D slices, where Normal Guidance is applied to enhance the attention mechanism. The authors do not disclose specific details regarding the loss functions or training compute used, but they emphasize the importance of the proposed regularization in improving slice-level localization.

**Results**  
The implementation of Normal Guidance leads to significant improvements in slice-level classification across three medical imaging datasets. The proposed method outperforms existing state-of-the-art MIL techniques, achieving higher accuracy in slice-level localization tasks while maintaining competitive performance in whole-scan classification. The authors report that their approach surpasses the center-focused baseline and other attention-based methods, although specific numerical results and effect sizes are not detailed in the abstract. The benchmarks used for evaluation include 3D brain scans, thoracic CT scans, and abdominal CT scans.

**Limitations**  
The authors acknowledge that their work is limited to the datasets used in the study, which may not generalize to all types of medical imaging tasks. They do not address potential overfitting issues that could arise from the large number of slices in the training data. Additionally, the reliance on a single binary label for the entire volume may not capture the complexity of certain medical conditions, potentially limiting the applicability of the proposed method in more nuanced clinical scenarios.

**Why it matters**  
The introduction of Normal Guidance has significant implications for the field of medical imaging, particularly in weakly supervised learning contexts. By enhancing the performance of attention-based models, this work paves the way for more accurate slice-level predictions, which are crucial for clinical decision-making. The findings suggest that regularization techniques can play a vital role in improving the interpretability and effectiveness of deep learning models in medical applications, potentially influencing future research directions in both attention mechanisms and weakly supervised learning paradigms.

Authors: Ethan Harvey, Dennis Johan Loevlie, Michael C. Hughes  
Source: arXiv:2605.27306  
URL: [https://arxiv.org/abs/2605.27306v1](https://arxiv.org/abs/2605.27306v1)
