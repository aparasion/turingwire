---
title: "Interpretable Computer Vision for Defect Detection in X-ray Tomography of Aerospace SiC/SiC Composites"
date: 2026-05-19 17:46:49 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20159v1"
arxiv_id: "2605.20159"
authors: ["Antonio Pe\u00f1a Corredor", "Julien Lesseur", "Romain Nunez", "Paul Rivalland", "Thomas Philippe"]
slug: interpretable-computer-vision-for-defect-detection-in-x-ray-
summary_word_count: 421
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in interpretability and traceability in the automated defect detection of aerospace SiC/SiC composites using X-ray computed tomography (XCT). Current methodologies rely heavily on expert visual assessments, which lack systematic traceability for accept/reject decisions. The authors aim to enhance the transparency of deep learning models, specifically convolutional networks, to meet the stringent requirements of industrial inspection practices.

**Method**  
The core technical contribution is the p-ResNet-50 architecture, an extension of the standard ResNet-50 that incorporates a prototype layer. This layer is designed to align six learned prototypes with expert-defined semantic categories: healthy matrix, matrix-air interfaces, pores, line-like defects, and mixed morphologies. The architecture employs two novel regularization terms—anchor-based and medoid-based—to tether prototypes to expert-selected patches, mitigating the issue of prototype collapse commonly seen in prototype networks. The model is trained on a dataset comprising approximately 12,000 patches extracted from four defect-rich SiC/SiC laboratory specimens. Latent-space analysis is performed using UMAP to visualize semantically coherent sub-domains and identify regions of uncertainty in the model's predictions.

**Results**  
The p-ResNet-50 achieves competitive performance compared to a black-box ResNet-50 baseline, with an accuracy of 0.957 versus 0.959 and a ROC-AUC of 0.994 compared to 0.993. While there is a slight reduction in sensitivity, the model demonstrates higher precision and specificity. The framework not only provides defect mapping but also offers explicit evidence patches for each classification, enhancing the interpretability of the model's decisions. The ability to flag uncertainty regions further aids inspectors in understanding the model's reliability.

**Limitations**  
The authors acknowledge that while the p-ResNet-50 improves interpretability, it may still be susceptible to misclassifications, particularly in complex defect scenarios. Additionally, the reliance on expert-defined categories may limit the model's adaptability to novel defect types not represented in the training data. The study does not address the scalability of the approach to larger datasets or real-time inspection scenarios, which could be a significant consideration in industrial applications.

**Why it matters**  
This work has significant implications for the integration of machine learning in industrial defect detection workflows, particularly in aerospace applications where safety and reliability are paramount. By embedding domain-expert knowledge into prototype networks, the proposed methodology not only enhances the interpretability of deep learning models but also establishes a framework that can be adapted to other XCT inspection scenarios requiring traceable and auditable decision-making processes. This could lead to broader adoption of automated systems in critical inspection tasks, ultimately improving efficiency and safety in aerospace manufacturing.

Authors: Antonio Peña Corredor, Julien Lesseur, Romain Nunez, Paul Rivalland, Thomas Philippe  
Source: arXiv:2605.20159  
URL: [https://arxiv.org/abs/2605.20159v1](https://arxiv.org/abs/2605.20159v1)
