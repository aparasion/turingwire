---
title: "Beyond Localization: A Comprehensive Diagnosis of Perspective-Conditioned Spatial Reasoning in MLLMs from Omnidirectional Images"
date: 2026-05-12 17:11:17 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.12413v1"
arxiv_id: "2605.12413"
authors: ["Yuangong Chen", "Wai Keung Wong", "Jiaxing Li", "Ioannis Patras", "Xu Zheng"]
slug: beyond-localization-a-comprehensive-diagnosis-of-perspective
summary_word_count: 463
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of Multimodal Large Language Models (MLLMs) in Perspective-Conditioned Spatial Reasoning (PCSR) when interpreting 360-degree omnidirectional images. Despite advancements in visual perception, MLLMs struggle with spatial reasoning tasks that require viewpoint-dependent inference. The authors introduce a new diagnostic benchmark, PCSR-Bench, to systematically evaluate this capability, filling a gap in the literature regarding the assessment of spatial reasoning in MLLMs under varying perspectives. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose PCSR-Bench, a benchmark comprising 84,373 question-answer pairs derived from 2,600 omnidirectional images across 26 indoor environments. The benchmark encompasses eight tasks that range from foundational perception tasks (e.g., object counting, relative distance, and relative direction) to advanced PCSR tasks, including compositional chains, egocentric rotation, perspective re-anchoring, ego-distortion, and limited-FOV visibility. The evaluation involves 14 representative MLLMs, assessing their performance on these tasks. Additionally, the authors conduct a reinforcement learning (RL)-based diagnostic study on a 7B-parameter model, employing reward shaping to investigate the potential for improving performance on PCSR tasks. The study reveals that reward design, including weight allocation and formulation, significantly influences the model's ability to adapt.

**Results**  
The evaluation of MLLMs on PCSR-Bench reveals a pronounced perception-reasoning gap. For foundational tasks, the models achieve an accuracy of 57.59% on relative direction, but performance deteriorates significantly on advanced tasks: 13.49% on egocentric rotation, 7.13% on egocentric distortion, and a mere 0.64% on open-ended compositional reasoning. The RL-based intervention demonstrates that a matched 7B baseline can be improved from 31.10% to 60.06% accuracy under controlled conditions, indicating that while there is some plasticity in the models' performance, the improvements are task-selective and contingent on the specifics of the reward design.

**Limitations**  
The authors acknowledge that the improvements observed through RL-based reward shaping are not universally applicable across all tasks, highlighting the task-selective nature of the gains. They also note that the evaluation protocol's design can influence outcomes, suggesting that further exploration is needed to generalize findings. Additionally, the reliance on a single model architecture (7B) may limit the applicability of results to other MLLMs with different architectures or parameter counts.

**Why it matters**  
This work underscores the critical bottleneck posed by PCSR in MLLMs, revealing significant gaps in their spatial reasoning capabilities. The introduction of PCSR-Bench provides a valuable tool for future research aimed at enhancing MLLMs' performance in spatial reasoning tasks. The findings suggest that while there is potential for improvement through targeted optimization, the nature of the tasks and the design of reward mechanisms will play crucial roles in shaping model performance. This research paves the way for further investigations into enhancing MLLMs' reasoning capabilities, particularly in dynamic and complex environments.

Authors: Yuangong Chen, Wai Keung Wong, Jiaxing Li, Ioannis Patras, Xu Zheng  
Source: arXiv:2605.12413  
URL: [https://arxiv.org/abs/2605.12413v1](https://arxiv.org/abs/2605.12413v1)
