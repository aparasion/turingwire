---
title: "Paris 2.0: A Decentralized Diffusion Model for Video Generation"
date: 2026-05-25 17:27:22 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.26064v1"
arxiv_id: "2605.26064"
authors: ["Ali Rouzbayani", "Bidhan Roy", "Marcos Villagra", "Zhiying Jiang"]
slug: paris-2-0-a-decentralized-diffusion-model-for-video-generati
summary_word_count: 440
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in decentralized training methodologies for video generation, specifically focusing on the challenge of achieving temporally coherent video outputs. Prior work, notably Paris 1.0, established the feasibility of decentralized training for image generation but did not extend this capability to video. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Paris 2.0 employs a decentralized diffusion model (DDM) architecture, building on the foundational principles of Paris 1.0. The model is pre-trained using a decentralized computation framework, which allows for distributed training across multiple nodes without reliance on a centralized GPU cluster. The training process utilizes a low-resolution text-to-video dataset, optimizing for both video coherence and quality. The authors do not disclose specific architectural details or the exact training compute used, but they emphasize the model's ability to generate videos that maintain temporal consistency. The loss function is implicitly tied to the Frechet Video Distance (FVD) metric, which is used to evaluate the quality of generated videos.

**Results**  
Paris 2.0 demonstrates significant improvements over a baseline monolithic model trained on the same dataset with an equivalent total compute budget. The Frechet Video Distance (FVD) is reduced from 561.04 to 279.01, indicating a ~2.0x enhancement in video quality. Additionally, the model shows improved performance in CLIP text-video similarity and aesthetic scoring, although specific numerical improvements for these metrics are not provided. These results suggest that decentralized training can effectively compete with traditional centralized approaches in video generation tasks.

**Limitations**  
The authors acknowledge that while Paris 2.0 achieves notable improvements in video generation, it is still constrained by the low-resolution training setup, which may limit the applicability of the model to high-resolution video generation tasks. Furthermore, the decentralized training framework may introduce challenges related to synchronization and communication overhead among nodes, which are not explicitly addressed in the paper. The lack of peer review also raises questions about the robustness of the findings and the potential for undisclosed biases or limitations in the experimental setup.

**Why it matters**  
The development of Paris 2.0 has significant implications for the field of video generation, particularly in contexts where centralized computational resources are limited or unavailable. By demonstrating that high-quality video generation can be achieved through decentralized methods, this work opens avenues for more accessible and scalable video generation solutions. It also sets a precedent for future research into decentralized training frameworks, potentially influencing the design of models across various domains in machine learning. The findings could encourage further exploration of decentralized architectures, leading to innovations in both efficiency and model performance.

Authors: Ali Rouzbayani, Bidhan Roy, Marcos Villagra, Zhiying Jiang  
Source: arXiv:2605.26064  
URL: https://arxiv.org/abs/2605.26064v1
