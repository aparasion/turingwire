---
title: "What Matters in Practical Learned Image Compression"
date: 2026-05-06 17:17:51 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.05148v1"
arxiv_id: "2605.05148"
authors: ["Kedar Tatwawadi", "Parisa Rahimzadeh", "Zhanghao Sun", "Zhiqi Chen", "Ziyun Yang", "Sanjay Nair"]
slug: what-matters-in-practical-learned-image-compression
summary_word_count: 398
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding the development of a perceptual yet practical learned image codec. While traditional codecs have been optimized for compression efficiency, they often fail to align with human visual perception. The authors note that despite the advancements in learned codecs, a codec that balances perceptual quality with practical runtime performance has not been proposed. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors conduct a comprehensive analysis of key modeling choices that influence the design of a learned image codec optimized for both perceptual quality and runtime efficiency. They introduce several novel techniques and perform performance-aware neural architecture search across millions of backbone configurations. This search aims to identify models that meet specific on-device runtime constraints while maximizing compression performance as measured by perceptual metrics. The resulting codec integrates these optimizations to achieve a superior tradeoff between encoding speed and perceptual quality.

**Results**  
The proposed codec demonstrates significant performance improvements over established baselines. In subjective user studies, it achieves 2.3-3x bitrate savings compared to AV1, AV2, VVC, ECM, and JPEG-AI. Additionally, it offers 20-40% bitrate savings against the best existing learned codec alternatives. The codec operates efficiently on an iPhone 17 Pro Max, encoding 12MP images in as fast as 230ms and decoding them in 150ms, outperforming many leading ML-based codecs that run on NVIDIA V100 GPUs.

**Limitations**  
The authors acknowledge that their study is limited to specific configurations and may not generalize across all potential use cases. They do not address the potential impact of varying image content on codec performance, nor do they explore the implications of hardware variability beyond the iPhone 17 Pro Max. Additionally, the subjective nature of perceptual quality assessments may introduce variability that is not fully captured in their results.

**Why it matters**  
This work has significant implications for the field of image compression, particularly in applications where both perceptual quality and runtime efficiency are critical, such as mobile devices and real-time streaming. By bridging the gap between learned codecs and human visual perception, this research paves the way for future developments in perceptually optimized compression algorithms. It also sets a benchmark for subsequent studies aiming to enhance the performance of learned codecs in practical scenarios.

Authors: Kedar Tatwawadi, Parisa Rahimzadeh, Zhanghao Sun, Zhiqi Chen, Ziyun Yang, Sanjay Nair, Divija Hasteer, Oren Rippel  
Source: arXiv:2605.05148  
URL: [https://arxiv.org/abs/2605.05148v1](https://arxiv.org/abs/2605.05148v1)
