---
title: "Linearizing Vision Transformer with Test-Time Training"
date: 2026-05-04 16:16:26 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.02772v1"
arxiv_id: "2605.02772"
authors: ["Yining Li", "Dongchen Han", "Zeyu Liu", "Hanyi Wang", "Yulin Wang", "Gao Huang"]
slug: linearizing-vision-transformer-with-test-time-training
summary_word_count: 395
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of effectively transferring weights from pretrained Softmax attention models to linear-complexity attention mechanisms, specifically in the context of Vision Transformers (ViTs). The authors highlight that while linear attention mechanisms can mitigate the quadratic complexity of Softmax attention, training these models from scratch is computationally expensive. The fundamental representational gap between the two attention types complicates the weight transfer process. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach that leverages Test-Time Training (TTT) to facilitate the transition from Softmax to linear attention. They introduce a two-layer dynamic formulation of TTT that aligns structurally with Softmax attention, allowing for the direct inheritance of pretrained weights. To address representational discrepancies, they implement key instance normalization and a lightweight locality enhancement module, which aim to improve key shift-invariance and locality properties. The model, termed SD3.5-T$^5$, is based on the Stable Diffusion 3.5 architecture and is fine-tuned for just one hour on 4×H20 GPUs.

**Results**  
The SD3.5-T$^5$ model achieves competitive performance in text-to-image generation, matching the quality of a fine-tuned Softmax attention model. Specifically, it demonstrates a 1.32× and 1.47× acceleration in inference speed at 1K and 2K resolutions, respectively. These results indicate that the proposed method not only preserves the quality of the output but also significantly enhances computational efficiency, which is critical for real-time applications.

**Limitations**  
The authors acknowledge that their approach may not generalize across all types of tasks or datasets, as it is specifically tailored for the Stable Diffusion architecture. Additionally, the reliance on TTT may introduce additional complexity during deployment, as it requires a specific training regime. The paper does not address potential limitations related to the scalability of the method to larger models or different architectures beyond ViTs.

**Why it matters**  
This work has significant implications for the deployment of linear attention mechanisms in practical applications, particularly in scenarios where computational resources are limited. By demonstrating that effective weight transfer is possible through architectural and representational alignment, the authors pave the way for more efficient models that can leverage existing pretrained weights. This could lead to broader adoption of linear attention mechanisms in various domains, including computer vision and natural language processing, where efficiency and performance are paramount.

Authors: Yining Li, Dongchen Han, Zeyu Liu, Hanyi Wang, Yulin Wang, Gao Huang  
Source: arXiv:2605.02772  
URL: [https://arxiv.org/abs/2605.02772v1](https://arxiv.org/abs/2605.02772v1)
