---
title: "Probing Embodied LLMs: When Higher Observation Fidelity Hurts Problem Solving"
date: 2026-05-19 16:27:00 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.20072v1"
arxiv_id: "2605.20072"
authors: ["Oussama Zenkri", "Oliver Brock"]
slug: probing-embodied-llms-when-higher-observation-fidelity-hurts
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how varying observation fidelity impacts the problem-solving capabilities of embodied Large Language Models (LLMs) in robotic systems. While LLMs are increasingly integrated into robotics, their opaque decision-making processes complicate the interpretation of their performance in closed-loop tasks. The authors investigate the relationship between the fidelity of sensory input (RGB, RGB-D, and ground-truth symbolic observations) and the resultant behavior of LLM agents in a physical robotic setup, specifically using the Lockbox task, which features hidden interdependencies.

**Method**  
The authors employ an empirical methodology to assess the performance of LLM agents under different observation conditions. The Lockbox task serves as the experimental framework, where agents are evaluated based on their ability to solve a sequential mechanical puzzle. The study contrasts three types of observations: raw RGB images, RGB-D data, and ground-truth symbolic representations. In addition, the authors conduct controlled simulations where they introduce noise by randomly flipping perceived action outcomes. This manipulation allows them to explore the effects of moderate noise on performance, identifying an optimal flip probability of 40% that yields a 2.85-fold increase in success rates compared to a noise-free baseline. The analysis also examines the reduction in repetitive action loops as a contributing factor to improved performance.

**Results**  
The findings reveal a counterintuitive trend: agents perform best with raw RGB input, achieving higher success rates than with higher fidelity observations. Specifically, the introduction of noise in simulations leads to a peak performance improvement at a 40% flip probability, resulting in a 2.85-fold increase in success rates over the baseline. This suggests that the interaction between perceptual errors and reasoning failures plays a critical role in the agents' problem-solving capabilities, challenging the assumption that higher observation fidelity directly correlates with better performance.

**Limitations**  
The authors acknowledge that their findings may not generalize across all types of tasks or environments, as the Lockbox task is specifically designed with hidden interdependencies that may not be present in other scenarios. Additionally, the reliance on simulated noise may not fully capture the complexities of real-world sensory noise. The study also does not explore the long-term implications of varying observation fidelity on learning and adaptation in LLMs, which could be a significant factor in dynamic environments.

**Why it matters**  
This research has important implications for the design and evaluation of embodied LLMs in robotics. It challenges the prevailing notion that higher observation fidelity is inherently beneficial for problem-solving, suggesting instead that a certain level of perceptual noise may enhance performance by promoting more effective exploration and reducing repetitive behaviors. This insight could inform future work on the integration of LLMs in robotic systems, particularly in optimizing sensory input modalities and understanding the cognitive processes underlying decision-making in complex tasks.

Authors: Oussama Zenkri, Oliver Brock  
Source: arXiv:2605.20072  
URL: https://arxiv.org/abs/2605.20072v1
