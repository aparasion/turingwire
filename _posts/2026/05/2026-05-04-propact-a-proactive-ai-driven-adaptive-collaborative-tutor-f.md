---
title: "ProPACT: A Proactive AI-Driven Adaptive Collaborative Tutor for Pair Programming"
date: 2026-05-04 15:12:49 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.02703v1"
arxiv_id: "2605.02703"
authors: ["Anahita Golrang", "Kshitij Sharma", "olga viberg"]
slug: propact-a-proactive-ai-driven-adaptive-collaborative-tutor-f
summary_word_count: 435
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in adaptive learning systems that primarily focus on individual learners rather than collaborative dynamics in pair programming. Existing systems are largely reactive, failing to proactively support the coordination of attention and cognitive effort between partners. The authors present ProPACT, a proactive AI-driven adaptive collaborative tutor designed to enhance the collaborative learning experience by treating the collaboration itself as the primary object of instruction. This work is a preprint and has not yet undergone peer review.

**Method**  
ProPACT employs a multimodal dyadic learner model that integrates three key components: Joint Visual Attention (JVA), Joint Mental Effort (JME), and individual mental effort metrics. The model utilizes an XGBoost-based forecasting mechanism to predict suboptimal collaboration states up to 30 seconds in advance. This predictive capability informs a hierarchical adaptive policy that provides minimally intrusive scaffolding tailored to the dyad's current collaboration state. The system dynamically adjusts support levels, fading assistance during productive collaboration while offering timely interventions when suboptimal states are detected. The training data and compute resources used for model development are not disclosed in the paper.

**Results**  
In a within-subject study involving 26 pair-programming dyads, ProPACT demonstrated significant improvements across several metrics compared to baseline conditions. Specifically, proactive feedback led to a 25% increase in debugging success rates, a 30% enhancement in task efficiency, and a 40% rise in feedback uptake. Additionally, post-intervention assessments indicated gains in JVA and JME, with effect sizes suggesting that the proactive approach substantially outperformed traditional reactive methods. These results underscore the effectiveness of forecast-driven adaptivity in real-time collaborative learning environments.

**Limitations**  
The authors acknowledge several limitations, including the small sample size of 26 dyads, which may affect the generalizability of the findings. The study's context is also limited to pair programming, and the results may not directly translate to other collaborative learning scenarios. Furthermore, the reliance on XGBoost for forecasting may introduce biases inherent to the model, and the lack of detailed information on training data and compute resources limits reproducibility. The authors do not address potential challenges in scaling the system or integrating it into existing educational frameworks.

**Why it matters**  
The introduction of ProPACT has significant implications for the design of collaborative learning systems. By shifting the focus from individual performance to the dynamics of collaboration, this work opens avenues for developing more effective educational technologies that enhance peer interactions. The proactive nature of the tutor could lead to improved learning outcomes in various collaborative settings, potentially influencing future research on adaptive learning systems and their application in real-time educational contexts.

Authors: Anahita Golrang, Kshitij Sharma, Olga Viberg  
Source: arXiv:2605.02703  
URL: https://arxiv.org/abs/2605.02703v1
