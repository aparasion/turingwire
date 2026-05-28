---
title: "CLANE: Continual Learning of Actions on Neuromorphic Hardware from Event Cameras"
date: 2026-05-27 12:24:04 +0000
category: research
subcategory: agents_robotics
company: "Intel"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.28387v1"
arxiv_id: "2605.28387"
authors: ["Elvin Hajizada", "Michael Neumeier", "Edward Paxon Frady", "Yulia Sandamirskaya", "Axel von Arnim", "Bing Li"]
slug: clane-continual-learning-of-actions-on-neuromorphic-hardware
summary_word_count: 489
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in continual learning for action recognition using neuromorphic hardware, specifically focusing on the deployment of an end-to-end learning pipeline that operates on event-based data from event cameras. Prior work has not successfully integrated continual learning capabilities with neuromorphic processing for action recognition tasks, particularly in real-world scenarios. The authors present CLANE, a system designed to learn new actions continuously without forgetting previously learned classes, which is crucial for applications in augmented reality (AR), virtual reality (VR), and robotics. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
CLANE employs a spiking 2D Convolutional Neural Network (CNN) for spatiotemporal feature extraction from event camera data. The architecture includes a novel learning head called CLP-SNN (Continual Learning Protocol for Spiking Neural Networks), which is adapted for action clips through two innovative modules: a Temporal Aggregation Layer and a fixed-point Normalization Layer, both tailored for the Intel Loihi 2 neuromorphic chip. The system is designed to operate efficiently on-device, leveraging the asynchronous and sparse nature of event camera outputs. The training process is optimized for low energy consumption and latency, with the authors providing detailed comparisons against a sequential CNN+GRU+CLP baseline running on a conventional edge GPU.

**Results**  
CLANE achieves a notable accuracy of 70.4% on the THU E-ACT-50 dataset, which consists of 50 action classes captured under real-world conditions. This performance is evaluated in a continual learning context, where the model is required to learn new actions while retaining knowledge of previously learned classes. The system demonstrates over 100x energy reduction and 16x lower latency compared to the baseline model, validated through iso-algorithm cross-platform benchmarking across three evaluation levels. These results highlight the effectiveness of CLANE in both performance and efficiency metrics.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a specific neuromorphic hardware platform (Intel Loihi 2), which may restrict generalizability to other hardware. Additionally, the continual learning framework may face challenges in scalability as the number of action classes increases, potentially leading to catastrophic forgetting. The dataset used, while comprehensive, may not encompass all possible real-world action variations, which could affect the model's robustness in diverse environments. The paper does not address the potential impact of noise and occlusion in event camera data on learning performance.

**Why it matters**  
The development of CLANE has significant implications for the fields of AR, VR, and robotics, where real-time, on-device learning is essential for user privacy and system responsiveness. By demonstrating a successful integration of continual learning with neuromorphic hardware, this work paves the way for future research into more efficient and adaptive AI systems capable of operating in dynamic environments. The methodologies and findings could inspire further advancements in neuromorphic computing and event-based learning paradigms, potentially leading to broader applications in autonomous systems and intelligent interfaces.

Authors: Elvin Hajizada, Michael Neumeier, Edward Paxon Frady, Yulia Sandamirskaya, Axel von Arnim, Bing Li, Eyke Hüllermeier  
Source: arXiv:2605.28387  
URL: https://arxiv.org/abs/2605.28387v1
