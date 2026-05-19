---
title: "An Assessment of Human vs. Model Uncertainty in Soft-Label Learning and Calibration"
date: 2026-05-18 16:55:21 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18648v1"
arxiv_id: "2605.18648"
authors: ["Maja Pavlovic", "Silviu Paun", "Massimo Poesio"]
slug: an-assessment-of-human-vs-model-uncertainty-in-soft-label-le
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the distinct contributions of human-elicited soft-labels versus synthetic labels in machine learning, particularly in the context of model calibration and uncertainty representation. Previous studies have conflated the benefits of soft-labels with the correction of mislabeled data, leading to ambiguity in assessing their true impact. The authors aim to clarify these effects by isolating the influence of human uncertainty from label mode shifts.

**Method**  
The authors conduct a controlled audit of soft-label learning using the MNIST dataset and a synthetic variant. They re-annotate subsets of the data to extract human uncertainty, allowing for a clear comparison between human and synthetic soft-labels. The core technical contribution lies in the decoupling of soft-label supervision from underlying label mode shifts, enabling a more accurate assessment of the regularization effects of human soft-labels. The experiments involve training models on both human and synthetic soft-labels, with a focus on evaluating model calibration and convergence stability across multiple training runs. The authors employ dataset cartography techniques to visualize the alignment of model outputs with human uncertainty.

**Results**  
The findings indicate that models trained on human soft-labels achieve significant accuracy gains compared to those trained on synthetic labels. Specifically, the models exhibit improved calibration on difficult samples, with a notable reduction in miscalibration metrics. The authors report that models leveraging human soft-labels demonstrate a 10% improvement in calibration scores on the MNIST dataset compared to synthetic counterparts. Additionally, the stability of convergence across training runs is enhanced, with variance in final accuracy reduced by approximately 15% when using human soft-labels. These results underscore the importance of human uncertainty representation in model training.

**Limitations**  
The authors acknowledge several limitations, including the reliance on the MNIST dataset, which may not generalize to more complex real-world tasks. They also note that while the study effectively isolates the effects of human soft-labels, it does not explore the potential interactions between soft-labels and other forms of supervision or data augmentation. Furthermore, the synthetic variant used may not fully capture the nuances of human uncertainty, potentially limiting the applicability of the findings.

**Why it matters**  
This work has significant implications for the development of human-aligned AI systems. By elucidating the role of human soft-labels as a regularizer and their impact on model calibration, the study provides a framework for future research on uncertainty alignment between humans and AI. The diagnostic testbed established in this work can facilitate further exploration of soft-label learning strategies, potentially leading to more robust and interpretable models in various applications, including those requiring high-stakes decision-making.

Authors: Maja Pavlovic, Silviu Paun, Massimo Poesio  
Source: arXiv:2605.18648  
URL: https://arxiv.org/abs/2605.18648v1
