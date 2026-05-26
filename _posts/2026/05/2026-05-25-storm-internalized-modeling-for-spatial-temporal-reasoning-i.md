---
title: "STORM: Internalized Modeling for Spatial-Temporal Reasoning in Video-Language Models"
date: 2026-05-25 16:33:00 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.26014v1"
arxiv_id: "2605.26014"
authors: ["Yiming Liang", "Yixiao Chen", "Yiyang Zhou", "Yixuan Wang", "Shoubin Yu", "Andong Deng"]
slug: storm-internalized-modeling-for-spatial-temporal-reasoning-i
summary_word_count: 432
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing large vision-language models (LVLMs) in handling video reasoning tasks that require tracking motion, temporal order, and evolving visual states across frames. Current methodologies often rely on externalizing reasoning through mechanisms such as textual chain-of-thought (CoT), keyframe selection, and external tool usage, which introduce latency and complexity during inference. The authors propose STORMS (Spatial-Temporal reasoning via internalized Modeling) as a solution to internalize reasoning processes, thereby reducing reliance on these external methods. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
STORMS introduces a two-stage framework for internalized reasoning in LVLMs. In Stage I, the model aligns latent tokens with thought-video representations derived from generated videos, effectively grounding latent states in dynamic visual evidence. This alignment allows the model to capture spatial-temporal relationships without explicit textual annotations. In Stage II, the model is trained with answer-only supervision, which encourages the internalization of reasoning processes without the need for step-by-step guidance. Notably, during inference, STORMS performs a bounded latent rollout, eliminating the need for video regeneration, frame reinsertion, or external visual tools. The training process leverages generated thought videos solely for supervision, streamlining the inference pipeline.

**Results**  
STORMS demonstrates significant improvements in video reasoning accuracy across multiple benchmarks, including VideoMME, MVBench, TempCompass, and MMVU. The paper reports that STORMS achieves a notable reduction in inference overhead compared to traditional methods that utilize external tools or video generation. While specific numerical results are not detailed in the abstract, the authors emphasize that the improvements are substantial, indicating a clear advantage over named baselines.

**Limitations**  
The authors acknowledge that the reliance on generated thought videos during training may limit the model's generalizability to real-world scenarios where such videos are not available. Additionally, the internalization of reasoning processes may not fully capture complex reasoning tasks that require explicit step-by-step annotations. The paper does not address potential issues related to the scalability of the model or its performance on diverse video datasets outside the evaluated benchmarks.

**Why it matters**  
The implications of STORMS are significant for the field of video-language models, as it proposes a novel approach to internalizing reasoning processes that can enhance both efficiency and accuracy. By reducing inference-time latency and engineering complexity, STORMS paves the way for more streamlined applications in video reasoning tasks. This work could inspire further research into internalized reasoning frameworks, potentially leading to advancements in other domains that require complex temporal and spatial reasoning.

Authors: Yiming Liang, Yixiao Chen, Yiyang Zhou, Yixuan Wang, Shoubin Yu, Andong Deng, Fuxiao Liu, Qin Zhang et al.  
Source: arXiv:2605.26014  
URL: [https://arxiv.org/abs/2605.26014v1](https://arxiv.org/abs/2605.26014v1)
