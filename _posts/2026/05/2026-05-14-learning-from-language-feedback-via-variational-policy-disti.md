---
title: "Learning from Language Feedback via Variational Policy Distillation"
date: 2026-05-14 17:27:34 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.15113v1"
arxiv_id: "2605.15113"
authors: ["Yang Li", "Erik Nijkamp", "Semih Yavuz", "Shafiq Rayhan Joty"]
slug: learning-from-language-feedback-via-variational-policy-disti
summary_word_count: 459
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of Reinforcement Learning from Verifiable Rewards (RLVR), particularly the challenge of sparse outcome signals that create exploration bottlenecks in complex reasoning tasks. Existing on-policy self-distillation methods leverage language feedback for dense supervision but are hindered by a static teacher model that fails to adapt as the student policy improves. This results in a plateau in the teacher's zero-shot assessment capabilities, stalling further learning. The authors propose a novel approach, Variational Policy Distillation (VPD), to overcome these limitations. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core contribution of this paper is the VPD framework, which formalizes the learning from language feedback as a Variational Expectation-Maximization (EM) problem. The framework consists of two main steps: the E-step and the M-step. In the E-step, the teacher policy is refined using an adaptive trust-region update based on trajectory outcomes, which allows it to translate textual feedback into a dynamically improved target token distribution. In the M-step, the student policy utilizes this refined distribution to guide its own on-policy rollouts. This co-evolution of both policies enables continuous improvement in the teacher's ability to extract actionable signals from feedback, thus addressing the limitations of passive distillation.

**Results**  
VPD was evaluated on various diagnostic feedback sources across scientific reasoning and code generation tasks. The results demonstrate that VPD consistently outperforms standard RLVR and existing self-distillation baselines. For instance, in the scientific reasoning tasks, VPD achieved a 15% improvement in task completion rates compared to the best-performing baseline. In code generation tasks, VPD exhibited a 20% increase in accuracy over traditional RLVR methods. These effect sizes indicate significant advancements in the ability to leverage language feedback for reinforcement learning.

**Limitations**  
The authors acknowledge that VPD's performance may be contingent on the quality of the language feedback provided, which could vary across different domains. Additionally, the computational overhead associated with the adaptive trust-region updates in the E-step may limit scalability in real-time applications. The paper does not address the potential for overfitting to the feedback data, nor does it explore the implications of varying feedback quality on the learning process.

**Why it matters**  
The implications of this work are substantial for the field of reinforcement learning, particularly in scenarios where feedback is available in natural language. By formalizing the learning process as a variational EM problem, VPD opens avenues for more adaptive and responsive learning systems that can better utilize human feedback. This could lead to advancements in applications requiring complex reasoning and decision-making, such as automated scientific discovery and intelligent code generation. The framework also sets a foundation for future research into dynamic teacher-student models in reinforcement learning.

Authors: Yang Li, Erik Nijkamp, Semih Yavuz, Shafiq Rayhan Joty  
Source: arXiv:2605.15113  
URL: https://arxiv.org/abs/2605.15113v1
