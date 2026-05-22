---
title: "Live Music Diffusion Models: Efficient Fine-Tuning and Post-Training of Interactive Diffusion Music Generators"
date: 2026-05-21 16:54:07 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22717v1"
arxiv_id: "2605.22717"
authors: ["Zachary Novack", "Stephen Brade", "Haven Kim", "Hugo Flores Garc\u00eda", "Nithya Shikarpur", "Chinmay Talegaonkar"]
slug: live-music-diffusion-models-efficient-fine-tuning-and-post-t
summary_word_count: 436
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing state-of-the-art (SOTA) discrete autoregressive (AR) models for interactive music generation, which require substantial computational resources for both training and inference. The authors highlight the gap in the literature regarding the adaptation of audio diffusion models for real-time applications, particularly in live performance and co-creation scenarios. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Live Music Diffusion Models (LMDMs), which modify the generative diffusion process to enhance computational efficiency for interactive music generation. The key technical contribution is the implementation of block-wise key-value (KV) caching during inference, which allows LMDMs to achieve comparable or superior efficiency to discrete Live Music Models (LMMs). Additionally, the authors propose a novel post-training alignment technique called ARC-Forcing, which mitigates error accumulation without relying on reinforcement learning (RL) or reward models. The training process leverages a dataset of diverse music samples, although specific details regarding the dataset size and training compute are not disclosed.

**Results**  
LMDMs demonstrate significant improvements in inference efficiency compared to traditional discrete AR models. The authors report that LMDMs can operate effectively on consumer-grade hardware, such as a gaming laptop, enabling real-time music generation. In various creative applications, including text-conditioned generation and sketch-based music synthesis, LMDMs outperform baseline models in terms of both latency and output quality. The paper provides quantitative results, although specific numerical metrics and comparisons to named baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that while LMDMs improve efficiency, they may still face challenges in scalability and the complexity of real-time audio processing. The reliance on block-wise KV caching may introduce latency in certain scenarios, particularly in highly dynamic musical contexts. Additionally, the paper does not address potential limitations related to the diversity of the training dataset or the generalizability of the model across different musical genres.

**Why it matters**  
The development of LMDMs has significant implications for the field of interactive music generation, particularly in live performance settings. By enabling real-time music synthesis on consumer hardware, this work democratizes access to advanced generative models for musicians and artists. The ARC-Forcing technique also opens avenues for further research into post-training alignment methods in generative models, potentially influencing future work in both music generation and other domains requiring real-time interaction. The ability to use LMDMs as a "generative delay" in live performances suggests new possibilities for artist-AI collaboration, enhancing the creative process and expanding the toolkit available to musicians.

Authors: Zachary Novack, Stephen Brade, Haven Kim, Hugo Flores García, Nithya Shikarpur, Chinmay Talegaonkar, Suwan Kim, Valerie K. Chen et al.  
Source: arXiv:2605.22717  
URL: [https://arxiv.org/abs/2605.22717v1](https://arxiv.org/abs/2605.22717v1)
