---
title: "Dimensionality-Aware Anomaly Detection in Learned Representations of Self-Supervised Speech Models"
date: 2026-05-04 15:18:15 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.02715v1"
arxiv_id: "2605.02715"
authors: ["Sandra Arcos-Holzinger", "Sarah M. Erfani", "James Bailey", "Sanjeev Khudanpur"]
slug: dimensionality-aware-anomaly-detection-in-learned-representa
summary_word_count: 437
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the robustness of self-supervised speech models (S3Ms) under perturbations, particularly focusing on how local geometric changes in learned representations correlate with performance degradation in automatic speech recognition (ASR). Existing literature primarily examines representation similarity or global dimensionality, which fails to provide insights into the nuanced local geometric transformations that occur due to various types of noise, both benign and adversarial.

**Method**  
The authors introduce GRIDS, a novel framework that employs Local Intrinsic Dimensionality (LID) to analyze layer-wise representations from two prominent S3Ms: WavLM and wav2vec 2.0. The methodology involves calculating LID across different layers of the models to assess how perturbations affect local geometry. The training process and specific datasets are not disclosed, but the framework is designed to evaluate the impact of low and high signal-to-noise ratio (SNR) perturbations on LID. The authors demonstrate that LID increases for low SNR perturbations and diverges at high SNR, where benign noise approaches the clean representation while adversarial inputs maintain elevated LID in early layers. This LID analysis is then leveraged for anomaly detection, achieving area under the receiver operating characteristic (AUROC) scores ranging from 0.78 to 1.00.

**Results**  
The study reports that LID consistently increases with low SNR perturbations, indicating a degradation in local geometric structure. At high SNR, benign noise converges towards the clean representation, while adversarial perturbations retain elevated LID levels, suggesting a distinct response to different types of noise. The correlation between LID elevation and word error rate (WER) increases is highlighted, establishing a direct link between local geometric changes and ASR performance. The anomaly detection capability of layer-wise LID features is validated with AUROC scores between 0.78 and 1.00, outperforming traditional methods in transcript-free monitoring scenarios.

**Limitations**  
The authors acknowledge that their approach is limited to the specific architectures of WavLM and wav2vec 2.0, which may not generalize to other S3Ms. Additionally, the study does not explore the implications of LID changes across diverse datasets or languages, which could affect the robustness of the findings. The reliance on LID as a sole metric for anomaly detection may overlook other critical factors influencing ASR performance.

**Why it matters**  
This work has significant implications for the development of more robust S3Ms, particularly in real-world applications where noise and adversarial attacks are prevalent. By providing a framework for understanding local geometric changes in representations, GRIDS opens avenues for transcript-free monitoring and anomaly detection in ASR systems. This could lead to improved resilience of speech models in practical deployments, enhancing their reliability in diverse acoustic environments.

Authors: Sandra Arcos-Holzinger, Sarah M. Erfani, James Bailey, Sanjeev Khudanpur  
Source: arXiv:2605.02715  
URL: [https://arxiv.org/abs/2605.02715v1](https://arxiv.org/abs/2605.02715v1)
