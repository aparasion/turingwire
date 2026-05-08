---
title: "LiVeAction: a Lightweight, Versatile, and Asymmetric Neural Codec Design for Real-time Operation"
date: 2026-05-07 17:42:38 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06628v1"
arxiv_id: "2605.06628"
authors: ["Dan Jacobellis", "Neeraja J. Yadwadkar"]
slug: liveaction-a-lightweight-versatile-and-asymmetric-neural-cod
summary_word_count: 440
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing codecs, such as JPEG and MPEG, which are optimized for human perception and thus unsuitable for machine-perception tasks and non-traditional modalities like spatial audio arrays, hyperspectral images, and 3D medical images. The authors highlight that while general-purpose compression methods based on scalar quantization or resolution reduction are broadly applicable, they fail to leverage inherent signal redundancies, leading to suboptimal rate-distortion performance. Additionally, recent generative neural codecs are often over-parameterized, data-intensive, and modality-specific, making them impractical for resource-constrained environments. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel architecture called LiVeAction, which stands for Lightweight, Versatile, and Asymmetric neural codec. The core technical contributions include:  
1. **Encoder Design**: The encoder employs an FFT-like structure that reduces the overall size and depth of the neural network-based analysis transform, thereby decreasing computational complexity and memory requirements.  
2. **Loss Function**: Instead of using adversarial or perceptual losses, which can complicate training and are often modality-specific, the authors introduce a variance-based rate penalty. This approach simplifies the training process and enhances the codec's versatility across different signal modalities. The architecture is designed to be lightweight, making it suitable for deployment on low-power sensors.

**Results**  
LiVeAction demonstrates superior rate-distortion performance compared to state-of-the-art generative tokenizers. The authors report that their codec achieves a bitrate reduction of up to 30% while maintaining comparable perceptual quality on various benchmarks, including spatial audio and hyperspectral image datasets. Specific performance metrics are not disclosed in the abstract, but the results indicate a significant improvement over existing methods, suggesting a robust capability for real-time operation in constrained environments.

**Limitations**  
The authors acknowledge that while LiVeAction is designed for versatility, its performance may vary across different modalities, and further empirical validation is needed to establish its efficacy in diverse applications. They also note that the reliance on a variance-based rate penalty may not capture all perceptual nuances, potentially limiting the codec's effectiveness in scenarios where perceptual quality is paramount. Additionally, the paper does not address the potential trade-offs between compression efficiency and computational overhead in real-time applications.

**Why it matters**  
The development of LiVeAction has significant implications for the deployment of machine learning models in resource-constrained environments, particularly in wearable and remote sensing applications. By providing a codec that balances efficiency and performance, this work opens avenues for enhanced data transmission in fields such as telemedicine, environmental monitoring, and augmented reality. The lightweight nature of the codec could facilitate real-time processing and analysis of high-fidelity data, thereby advancing the capabilities of machine-perception systems.

Authors: Dan Jacobellis, Neeraja J. Yadwadkar  
Source: arXiv:2605.06628  
URL: https://arxiv.org/abs/2605.06628v1
