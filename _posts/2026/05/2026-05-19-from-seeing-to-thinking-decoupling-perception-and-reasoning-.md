---
title: "From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models"
date: 2026-05-19 17:58:40 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.20177v1"
arxiv_id: "2605.20177"
authors: ["Juncheng Wu", "Hardy Chen", "Haoqin Tu", "Xianfeng Tang", "Freda Shi", "Hui Liu"]
slug: from-seeing-to-thinking-decoupling-perception-and-reasoning-
summary_word_count: 447
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a critical gap in the performance of vision-language models (VLMs), specifically the insufficient visual perception capabilities that hinder their effectiveness in visual tasks. While existing literature emphasizes the importance of reasoning in VLMs, the authors argue that the lack of robust visual perception is a more significant limiting factor. The study systematically investigates the interplay between perception and reasoning in VLM post-training, proposing a novel approach to enhance visual perception through decoupled training stages.

**Method**  
The authors introduce a staged training methodology that separates the training of visual perception, visual reasoning, and textual reasoning into distinct phases. This approach utilizes specialized training data tailored for each capability. Key technical contributions include:

1. **Targeted Optimization**: Visual perception is optimized using specialized datasets, which are crucial for effective learning.
2. **Reinforcement Learning (RL)**: The authors demonstrate that visual perception is more effectively learned through RL techniques compared to traditional supervised fine-tuning (SFT) based on captions.
3. **Curriculum Learning**: The proposed staged training represents a new dimension of curriculum learning, orthogonal to traditional difficulty-based curricula, allowing for the combination of both strategies to yield enhanced performance.

The training compute details are not explicitly disclosed, but the methodology emphasizes the importance of structured training phases.

**Results**  
The proposed staged training approach leads to significant performance improvements across multiple VLMs. Notable results include:

- A 1.5% increase in reasoning accuracy.
- A reduction of 20.8% in reasoning trace length, indicating that improved visual perception allows for more efficient reasoning processes.
- Performance gains on specific benchmarks: +5.2% on WeMath and +3.7% on RealWorldQA compared to baseline models.

These results demonstrate that the decoupling of perception and reasoning not only enhances individual capabilities but also leads to superior overall model performance.

**Limitations**  
The authors acknowledge that their approach may require extensive specialized datasets for effective training, which could limit generalizability. Additionally, the reliance on RL for visual perception learning may introduce complexity in training dynamics. The paper does not address potential scalability issues when applying this methodology to larger, more complex VLMs or the computational costs associated with staged training.

**Why it matters**  
This work has significant implications for the development of more effective VLMs by highlighting the necessity of robust visual perception as a foundation for reasoning capabilities. The introduction of a staged training approach provides a framework for future research to explore the interplay between different cognitive capabilities in VLMs. By establishing a new curriculum dimension, this study encourages further investigation into optimizing training strategies for improved model performance across various visual reasoning tasks.

Authors: Juncheng Wu, Hardy Chen, Haoqin Tu, Xianfeng Tang, Freda Shi, Hui Liu, Hanqing Lu, Cihang Xie et al.  
Source: arXiv:2605.20177  
URL: [https://arxiv.org/abs/2605.20177v1](https://arxiv.org/abs/2605.20177v1)
