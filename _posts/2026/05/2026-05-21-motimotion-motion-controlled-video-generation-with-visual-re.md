---
title: "MotiMotion: Motion-Controlled Video Generation with Visual Reasoning"
date: 2026-05-21 17:59:36 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.22818v1"
arxiv_id: "2605.22818"
authors: ["Lee Hsin-Ying", "Hanwen Jiang", "Yiqun Mei", "Jing Shi", "Ming-Hsuan Yang", "Zhixin Shu"]
slug: motimotion-motion-controlled-video-generation-with-visual-re
summary_word_count: 437
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing motion-controlled image-to-video generation models, which typically adhere strictly to user-defined trajectories that are often sparse, imprecise, and causally incomplete. Such rigid adherence can lead to unnatural or implausible video outputs, as these models frequently overlook secondary causal effects that arise from primary motions. The authors propose MotiMotion, a novel framework that reformulates the motion control task into a reasoning-then-generation paradigm. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
MotiMotion introduces a two-step approach: reasoning followed by generation. The framework employs a training-free vision-language reasoner to refine the image-space coordinates of primary trajectories and to generate plausible secondary motions that enhance the overall coherence of the video. A key innovation is the confidence-aware control scheme, which modulates the strength of guidance based on the confidence level of the input trajectories. This allows the model to closely adhere to high-confidence plans while leveraging its internal generative priors to correct artifacts in low-confidence scenarios. The architecture details, including specific neural network configurations or loss functions, are not disclosed in the abstract.

**Results**  
The authors present a new benchmark, MotiBench, which consists of interaction-centric scenes designed to evaluate the model's performance in generating videos triggered by motion. MotiMotion outperforms existing methods in terms of producing videos with more plausible object behaviors and interactions. The evaluation includes both vision-language model (VLM)-based metrics and a human study, where MotiMotion is preferred over baseline models. While specific quantitative results (e.g., FID scores, accuracy metrics) are not provided in the abstract, the qualitative improvements in interaction realism are emphasized.

**Limitations**  
The authors acknowledge that the reliance on a training-free approach may limit the model's adaptability to diverse scenarios that require extensive training data. Additionally, the confidence-aware control scheme's effectiveness may vary depending on the quality of the input trajectories, which could still lead to suboptimal outputs in cases of highly ambiguous or noisy inputs. The paper does not discuss potential computational costs associated with the reasoning process or the scalability of the proposed framework.

**Why it matters**  
MotiMotion's approach to integrating visual reasoning into motion-controlled video generation represents a significant advancement in the field, particularly in addressing the shortcomings of existing models that fail to account for secondary causal effects. By introducing a systematic evaluation benchmark, MotiBench, the authors provide a valuable resource for future research in motion-based video generation. This work has implications for applications in interactive media, gaming, and virtual reality, where realistic motion and interactions are critical for user engagement.

Authors: Lee Hsin-Ying, Hanwen Jiang, Yiqun Mei, Jing Shi, Ming-Hsuan Yang, Zhixin Shu  
Source: arXiv:2605.22818  
URL: [https://arxiv.org/abs/2605.22818v1](https://arxiv.org/abs/2605.22818v1)
