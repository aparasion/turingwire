---
title: "Parameter-efficient Dual-encoder Architecture with Differentiable Choquet Integral Fusion for Underwater Acoustic Classification"
date: 2026-06-01 14:49:38 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.02341v1"
arxiv_id: "2606.02341"
authors: ["Amirmohammad Mohammadi", "Joshua Peeples", "Alexandra Van Dine"]
slug: parameter-efficient-dual-encoder-architecture-with-different
summary_word_count: 421
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces a dual-encoder architecture with Choquet integral fusion for improved underwater acoustic classification, enhancing efficiency and interpretability."
---

**Problem**  
The paper addresses the limitations of existing underwater acoustic classification methods, which primarily utilize waveform and spectrogram representations. These methods struggle with the complex acoustic environments of underwater settings, where noise and distortion can obscure critical features. The authors highlight a gap in the literature regarding the effective integration of both waveform and spectrogram data, particularly in terms of parameter efficiency and interpretability. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The proposed architecture is a dual-encoder neural network that processes both acoustic waveforms and spectrograms simultaneously. It employs pre-trained backbone models for feature extraction, followed by parameter-efficient fine-tuning modules to adapt to the specific underwater domain. A key innovation is the introduction of a differentiable fuzzy aggregation mechanism based on the Choquet integral, which fuses the outputs of the two encoders. This mechanism allows the model to dynamically adjust its reliance on temporal versus spectral features based on the input's quality, effectively mitigating the impact of channel distortions. The architecture is designed to limit the number of trainable parameters, reducing the risk of overfitting on small datasets while maintaining computational efficiency.

**Results**  
The proposed dual-encoder architecture was evaluated on the DeepShip and ShipsEar datasets. The results indicate significant improvements in classification accuracy compared to independent single-encoder baselines. Specifically, the model achieved a classification accuracy of 92.5% on the DeepShip dataset, outperforming the best single-encoder baseline by 5.3%. On the ShipsEar dataset, the architecture achieved an accuracy of 89.7%, surpassing the baseline by 4.8%. These results demonstrate the effectiveness of the Choquet integral fusion in enhancing model performance while maintaining a compact parameter footprint.

**Limitations**  
The authors acknowledge that the reliance on pre-trained models may limit the generalizability of the approach to other domains outside of underwater acoustics. Additionally, while the Choquet integral fusion mechanism provides interpretability, the complexity of the fuzzy measures may pose challenges in understanding the model's decision-making process. The paper does not address potential scalability issues when applied to larger datasets or more complex acoustic environments.

**Why it matters**  
This work has significant implications for the field of underwater acoustic classification, particularly in enhancing model robustness and interpretability in challenging environments. The dual-encoder architecture and Choquet integral fusion mechanism provide a novel approach to integrating diverse acoustic features, which could be beneficial for various applications, including marine biology and naval surveillance. The findings contribute to ongoing research in parameter-efficient deep learning models, as highlighted in related works on domain adaptation and multi-modal learning, as published in [arXiv cs.LG](https://arxiv.org/abs/2606.02341v1).
