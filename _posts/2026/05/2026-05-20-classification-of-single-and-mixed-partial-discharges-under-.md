---
title: "Classification of Single and Mixed Partial Discharges under Switching Voltage Using an AWA-CNN Framework"
date: 2026-05-20 16:16:51 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.21352v1"
arxiv_id: "2605.21352"
authors: ["Md Rafid Kaysar Shagor", "Zannatul Ferdousy Mouri", "Farhina Haque", "Anindya Bijoy Das"]
slug: classification-of-single-and-mixed-partial-discharges-under-
summary_word_count: 453
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in capability for classifying partial discharges (PD) under switching-voltage excitation, which is increasingly relevant due to the proliferation of fast-switching power electronics. Traditional methods struggle with the complexities introduced by rapid voltage transitions, which concentrate PD activity and complicate analysis. The authors propose a novel approach to enhance source-oriented PD analysis, which has not been adequately explored in existing literature.

**Method**  
The core technical contribution is the Amplitude-Width-Area (AWA) pattern representation for PD analysis. This method characterizes time-domain PD pulses by three features: pulse amplitude, width, and area. The AWA patterns are constructed such that amplitude and area define the coordinate axes, while pulse width is encoded through color intensity. This visual representation allows for the differentiation of six PD source conditions: corona, internal, surface, corona+internal, corona+surface, and internal+surface. The authors employ two CNN architectures—InceptionV3 and ResNet-18—alongside a Random Forest baseline to evaluate classification performance. The training and testing datasets are not explicitly detailed, but the CNN models are trained to optimize classification accuracy on the generated AWA patterns.

**Results**  
The proposed AWA-CNN framework achieves a testing accuracy exceeding 96% for PD source classification, significantly outperforming the Random Forest baseline, which achieves only 73.33% accuracy. The results indicate that the AWA patterns exhibit distinct source-dependent distributions, facilitating effective multi-class classification under the challenging conditions of switching-voltage excitation. The effect size of the improvement is substantial, demonstrating the efficacy of the AWA representation in enhancing classification performance.

**Limitations**  
The authors acknowledge that the study is limited by the scope of the PD source conditions considered, as only six specific types are analyzed. Additionally, the dataset used for training and testing is not described in detail, which raises questions about the generalizability of the findings. The reliance on CNN architectures may also introduce concerns regarding interpretability and the potential for overfitting, particularly if the dataset is not sufficiently large or diverse. Furthermore, the performance metrics are not accompanied by confidence intervals or statistical significance tests, which could provide deeper insights into the robustness of the results.

**Why it matters**  
This work has significant implications for the field of electrical engineering and power electronics, particularly in the context of predictive maintenance and fault diagnosis. The AWA-CNN framework offers a novel approach to PD analysis that could enhance the reliability of power systems by enabling more accurate detection and classification of PD sources. This advancement could lead to improved monitoring techniques and ultimately contribute to the development of smarter, more resilient power electronic systems. The findings may also inspire further research into visual pattern representations and their applications in other domains of electrical engineering.

Authors: Md Rafid Kaysar Shagor, Zannatul Ferdousy Mouri, Farhina Haque, Anindya Bijoy Das  
Source: arXiv:2605.21352  
URL: [https://arxiv.org/abs/2605.21352v1](https://arxiv.org/abs/2605.21352v1)
