---
title: "ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop"
date: 2026-05-18 17:59:02 +0000
category: research
subcategory: evaluation_benchmarks
company: "Oracle"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18746v1"
arxiv_id: "2605.18746"
authors: ["Yining Hong", "Jiageng Liu", "Han Yin", "Manling Li", "Leonidas Guibas", "Li Fei-Fei"]
slug: esi-bench-towards-embodied-spatial-intelligence-that-closes-
summary_word_count: 470
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding embodied spatial intelligence, specifically the perception-action loop where agents actively explore their environment rather than passively observing it. The authors highlight that existing models often assume oracle observations, which limits their applicability in real-world scenarios where agents must make decisions based on incomplete or occluded information. The work introduces ESI-BENCH, a comprehensive benchmark designed to evaluate agents' capabilities in actively acquiring task-relevant evidence across various spatial tasks. This is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the ESI-BENCH benchmark, which encompasses 10 task categories and 29 subcategories built on the OmniGibson platform, inspired by Spelke's core knowledge systems. The benchmark requires agents to utilize a combination of perception, locomotion, and manipulation skills, and to strategically sequence these abilities to gather evidence. The authors conduct extensive experiments using state-of-the-art multi-modal large language models (MLLMs) to evaluate the performance of agents in both active exploration and passive observation scenarios. The training involves simulating environments where agents must make decisions based on their actions and the resulting observations, emphasizing the importance of action choices in the perception-action loop.

**Results**  
The results demonstrate that agents employing active exploration strategies significantly outperform those relying on passive observation. Specifically, agents using active exploration discovered emergent spatial strategies without explicit instructions, achieving a performance improvement of approximately 30% over passive counterparts on various tasks. In contrast, random multi-view approaches, which consume more images, often introduced noise rather than useful information, leading to degraded performance. The authors also note that failures primarily arise from "action blindness," where poor action choices result in suboptimal observations, causing cascading errors. Furthermore, explicit 3D grounding improved reasoning on depth-sensitive tasks, but an imperfect 3D representation was found to be more detrimental than 2D baselines, distorting spatial relations.

**Limitations**  
The authors acknowledge several limitations, including the metacognitive gap where models exhibit high confidence in their decisions despite evidence quality, contrasting with human behavior that seeks falsifying viewpoints and revises beliefs under contradiction. This suggests that improvements in perception or embodied interaction alone are insufficient to bridge this gap. Additionally, the benchmark may not encompass all aspects of spatial intelligence, and the reliance on simulated environments may limit generalizability to real-world applications.

**Why it matters**  
The implications of this work are significant for advancing the field of embodied AI. By establishing a benchmark that emphasizes active exploration and the perception-action loop, the authors provide a framework for evaluating and improving agent performance in complex environments. This research encourages the development of models that can better mimic human-like reasoning and decision-making processes, ultimately leading to more robust and adaptable AI systems capable of navigating real-world challenges.

Authors: Yining Hong, Jiageng Liu, Han Yin, Manling Li, Leonidas Guibas, Li Fei-Fei, Jiajun Wu, Yejin Choi  
Source: arXiv:2605.18746  
URL: https://arxiv.org/abs/2605.18746v1
