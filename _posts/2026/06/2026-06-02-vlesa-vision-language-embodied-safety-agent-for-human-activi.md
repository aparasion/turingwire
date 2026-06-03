---
title: "VLESA: Vision-Language Embodied Safety Agent for Human Activity Monitoring"
date: 2026-06-02 17:42:17 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.03954v1"
arxiv_id: "2606.03954"
authors: ["Hanjiang Hu", "Yiyuan Pan", "Jiaxing Li", "Xusheng Luo", "Alexander Robey", "Na Li"]
slug: vlesa-vision-language-embodied-safety-agent-for-human-activi
summary_word_count: 385
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper presents VLESA, a framework for real-time safety monitoring of human activities using egocentric video and goal-conditioned safety assessments."
---

**Problem**  
The paper addresses the critical gap in ensuring safety during human-robot interactions, particularly in physical tasks where actions can have immediate consequences. Existing literature lacks a robust framework that can dynamically assess the safety of actions based on context and intent. The authors introduce VLESA, a Vision-Language Embodied Safety Agent, to monitor human activities in real-time and intervene when dangerous actions are predicted. This work is presented as a preprint and has not undergone peer review.

**Method**  
VLESA employs a novel architecture that integrates egocentric video input with goal-conditioned safety annotations. The framework consists of two main components: a goal-conditioned safety Q-filter and an intent-action prediction agent. The Q-filter is trained using a Generalized Risk-averse Policy Optimization (GRPO) approach, allowing it to evaluate actions based on inferred intent without requiring retraining. The intent-action prediction agent is responsible for jointly inferring human goals and predicting future actions from the video feed. The dataset introduced pairs egocentric frames with safety annotations conditioned on specific goals, facilitating the training of the Q-filter.

**Results**  
On the ASIMOV-2.0 benchmark, VLESA demonstrates superior performance in intervention accuracy, achieving a notable improvement over baseline models. Specifically, it surpasses existing methods by accurately predicting interventions at the exact ground-truth frame. The GRPO-trained Q-filter enhances action safety by over 41 percentage points compared to baseline approaches, showcasing the effectiveness of goal-conditioned constrained decoding in real-time safety assessments.

**Limitations**  
The authors acknowledge several limitations, including the reliance on high-quality egocentric video data, which may not always be available in real-world scenarios. Additionally, the framework's performance may be influenced by the diversity of activities and contexts present in the training dataset. The authors do not address potential challenges related to the scalability of the model in more complex environments or the computational overhead associated with real-time processing.

**Why it matters**  
The implications of VLESA are significant for the development of safe human-robot collaboration systems, particularly in environments where physical interactions are prevalent. By providing a mechanism for real-time safety monitoring and intervention, this framework can enhance the reliability of AI systems in critical applications such as healthcare, manufacturing, and autonomous driving. The introduction of a goal-conditioned safety assessment paradigm could pave the way for future research in intent-aware safety systems, as discussed in related works on safety in AI, such as those available on [arXiv](https://arxiv.org/abs/2606.03954v1).
