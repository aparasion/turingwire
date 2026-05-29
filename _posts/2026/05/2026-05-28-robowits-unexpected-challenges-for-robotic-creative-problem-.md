---
title: "RoboWits: Unexpected Challenges for Robotic Creative Problem Solving"
date: 2026-05-28 17:57:15 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30326v1"
arxiv_id: "2605.30326"
authors: ["Chunru Lin", "Hongxin Zhang", "Fenghao Yu", "Zhehuan Chen", "Thomas L. Griffiths", "Yejin Choi"]
slug: robowits-unexpected-challenges-for-robotic-creative-problem-
summary_word_count: 429
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in existing robotic benchmarks that primarily focus on skill-level execution without adequately evaluating cognitive reasoning capabilities, particularly in the context of unexpected challenges. The authors highlight that current benchmarks do not sufficiently assess a robot's ability to adapt and creatively solve problems in real-world environments. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce RoboWits, a bi-manual robotic benchmark designed to evaluate cognitive reasoning, creative tool use, and robustness to unexpected conditions. The core technical contribution is an automated task generation pipeline structured as a multi-agent cooperative framework. This framework includes agents for seed task generation, verification, metric generation, scene generation, and task mutation. The authors curated 30 diverse seed tasks and generated 208 mutated tasks with varying difficulty levels, focusing on geometry, material, and assembly-based reasoning. The benchmark evaluates various robot policies, including pre-trained Vision-Language Agents (VLAs) and oracle-state planners, to assess their performance across these tasks.

**Results**  
The results indicate a significant performance gap between the evaluated models. Pre-trained VLAs demonstrated preliminary success on the seed tasks after single-task fine-tuning, achieving a performance metric of approximately 75% accuracy. However, their performance dropped dramatically on mutated tasks, with accuracy falling to around 30%, highlighting their brittleness in scenarios requiring advanced reasoning and adaptability. In contrast, oracle-state planners maintained a higher performance level, achieving over 85% accuracy across both seed and mutated tasks, underscoring their robustness in complex environments.

**Limitations**  
The authors acknowledge several limitations, including the potential for overfitting in the seed tasks and the need for further exploration of the task mutation strategies. They also note that the benchmark may not cover all possible real-world scenarios, which could limit its applicability. Additionally, the reliance on pre-trained VLAs raises questions about their generalizability to tasks outside the training distribution. An obvious limitation not explicitly mentioned is the computational cost associated with generating and evaluating the large number of tasks, which may hinder scalability in practical applications.

**Why it matters**  
RoboWits has significant implications for advancing the field of robotic cognitive reasoning and creative problem-solving. By providing a structured benchmark that emphasizes reasoning under unexpected conditions, it encourages the development of more robust robotic systems capable of operating in dynamic environments. This work lays the groundwork for future research focused on enhancing the adaptability and creativity of robotic agents, ultimately contributing to their deployment in real-world applications where unforeseen challenges are prevalent.

Authors: Chunru Lin, Hongxin Zhang, Fenghao Yu, Zhehuan Chen, Thomas L. Griffiths, Yejin Choi, David Held, Chuang Gan  
Source: arXiv:2605.30326  
URL: [https://arxiv.org/abs/2605.30326v1](https://arxiv.org/abs/2605.30326v1)
