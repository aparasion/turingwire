---
title: "Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction"
date: 2026-05-18 17:52:14 +0000
category: research
subcategory: agents_robotics
company: "ARM"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.18729v1"
arxiv_id: "2605.18729"
authors: ["Nga Teng Chan", "Yi Zhang", "Yechi Liu", "Renwen Cui", "Fanhu Zeng", "Zeyuan Ding"]
slug: robo-cortex-a-self-evolving-embodied-agent-via-dual-grain-co
summary_word_count: 438
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of navigation in unseen environments for embodied agents, specifically targeting the issue of "experiential amnesia." Existing trajectory-driven and reactive policies often fail to generalize strategies from past interactions, leading to suboptimal performance in novel contexts. The authors propose Robo-Cortex, a self-evolving framework designed to autonomously induce navigation heuristics and refine cognitive strategies through a continuous reflection-adaptation loop. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Robo-Cortex introduces two key components: the Autonomous Knowledge Induction (AKI) mechanism and a Dual-Grain Cognitive Memory system. The AKI distills multimodal trajectories into a structured Navigation Heuristic Library, facilitating knowledge generalization. The Dual-Grain Cognitive Memory consists of a Short-term Reflective Memory (SRM) for real-time local progress analysis and a Long-term Principle Memory (LPM) that abstracts past trajectories into reusable guiding and cautionary principles. The architecture employs a multimodal Imagine-then-Verify loop, where a world model simulates potential outcomes, and a Vision-Language Model (VLM)-based evaluator validates action plans. The training process and compute resources utilized for the model are not disclosed in the paper.

**Results**  
Robo-Cortex was evaluated on three benchmarks: IGNav, AR, and AEQA. The results indicate that Robo-Cortex outperforms strong baselines, achieving a maximum improvement of +4.16% in Success Rate (SPL) over the strongest prior method. Additionally, under heuristic transfer to unseen environments, Robo-Cortex demonstrated an impressive gain of up to +15.30% SPL. Preliminary real-world robotic experiments corroborate the effectiveness of the proposed framework in physical settings, although specific metrics from these experiments are not detailed.

**Limitations**  
The authors acknowledge that the framework's performance may be contingent on the quality and diversity of the training data used for the AKI mechanism. They also note that while the system shows promise in simulated environments, further validation in more complex real-world scenarios is necessary. An obvious limitation not discussed by the authors is the potential computational overhead introduced by the dual-memory architecture and the Imagine-then-Verify loop, which may affect real-time decision-making capabilities in resource-constrained environments.

**Why it matters**  
The implications of Robo-Cortex extend to various applications in robotics and autonomous systems, particularly in enhancing the adaptability and generalization capabilities of embodied agents in dynamic and unpredictable environments. By enabling robots to autonomously evolve their navigation strategies, this work paves the way for more resilient and intelligent systems capable of operating in real-world scenarios without extensive retraining or manual intervention. The framework's approach to integrating cognitive memory with navigation heuristics could inspire future research in autonomous learning and decision-making.

Authors: Nga Teng Chan, Yi Zhang, Yechi Liu, Renwen Cui, Fanhu Zeng, Zeyuan Ding, Xiancong Ren, Zhang Zhang et al.  
Source: arXiv:2605.18729  
URL: [https://arxiv.org/abs/2605.18729v1](https://arxiv.org/abs/2605.18729v1)
