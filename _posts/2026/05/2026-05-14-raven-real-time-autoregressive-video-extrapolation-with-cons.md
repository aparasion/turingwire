---
title: "RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO"
date: 2026-05-14 17:59:30 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.15190v1"
arxiv_id: "2605.15190"
authors: ["Yanzuo Lu", "Ronglai Zuo", "Jiankang Deng"]
slug: raven-real-time-autoregressive-video-extrapolation-with-cons
summary_word_count: 425
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing causal autoregressive video diffusion models in generating high-quality video extrapolations over extended time horizons. Specifically, it identifies a gap in the alignment between the training distributions encountered during model training and the distributions present during inference, which negatively impacts the quality of long-term video generation. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce the Real-time Autoregressive Video Extrapolation Network (RAVEN), which employs a novel training-time test framework. This framework reorganizes the self-rollout process into an interleaved sequence of clean historical endpoints and noisy denoising states, thereby aligning the training attention mechanism with the inference-time extrapolation process. This approach allows for downstream chunk losses to effectively supervise the history representations critical for future predictions. Additionally, the paper proposes Consistency-model Group Relative Policy Optimization (CM-GRPO), which reformulates the consistency sampling step as a conditional Gaussian transition. This method applies online Reinforcement Learning (RL) directly to the transition kernel, circumventing the Euler-Maruyama auxiliary process used in previous flow-model RL approaches. The architecture and training compute specifics are not disclosed, but the focus on real-time streaming generation is emphasized.

**Results**  
RAVEN demonstrates superior performance compared to recent causal video distillation baselines across multiple evaluation metrics, including quality, semantic coherence, and dynamic range. The authors report significant improvements in extrapolation accuracy, although specific numerical results and effect sizes are not detailed in the abstract. The combination of RAVEN with CM-GRPO yields additional performance enhancements, indicating that the proposed methods effectively address the identified gaps in video generation quality.

**Limitations**  
The authors acknowledge that the reliance on interleaved sequences may introduce complexity in the training process, potentially affecting scalability. They do not discuss the computational overhead associated with the proposed RL framework or the generalizability of the model to diverse video content types. Additionally, the lack of extensive ablation studies limits the understanding of the individual contributions of RAVEN and CM-GRPO to the overall performance improvements.

**Why it matters**  
The introduction of RAVEN and CM-GRPO has significant implications for the field of video generation, particularly in applications requiring real-time performance, such as video streaming and interactive media. By addressing the alignment between training and inference distributions, this work paves the way for more robust and high-fidelity video extrapolation methods. The advancements in autoregressive modeling and reinforcement learning techniques could inspire further research into hybrid approaches that leverage the strengths of both paradigms, potentially leading to breakthroughs in generative modeling across various domains.

Authors: Yanzuo Lu, Ronglai Zuo, Jiankang Deng  
Source: arXiv:2605.15190  
URL: [https://arxiv.org/abs/2605.15190v1](https://arxiv.org/abs/2605.15190v1)
