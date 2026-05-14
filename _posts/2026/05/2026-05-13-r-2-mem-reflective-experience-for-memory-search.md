---
title: "R^2-Mem: Reflective Experience for Memory Search"
date: 2026-05-13 13:09:36 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13486v1"
arxiv_id: "2605.13486"
authors: ["Xinyuan Wang", "Wenyu Mao", "Junkang Wu", "Xiang Wang", "Xiangnan He"]
slug: r-2-mem-reflective-experience-for-memory-search
summary_word_count: 407
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing deep search agents in memory systems, which often replicate past errors due to their inability to learn from both high- and low-quality search trajectories. The authors propose R^2-Mem, a reflective experience framework designed to enhance the learning process of memory search systems. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
R^2-Mem introduces a two-stage framework comprising an offline and an online component. In the offline stage, a Rubric-guided Evaluator assesses historical search trajectories, scoring the quality of each step. This evaluation informs a self-Reflection Learner that distills abstract experiences from the evaluated trajectories. The online inference phase utilizes the retrieved experiences to inform future search actions, thereby mitigating the likelihood of repeating past mistakes. The architecture does not rely on reinforcement learning (RL), making it a low-cost alternative for enhancing the performance of large language model (LLM) agents. The authors do not disclose specific details regarding the training compute or dataset used.

**Results**  
R^2-Mem demonstrates significant improvements over strong baselines across various benchmarks. The framework achieves an increase in F1 scores by up to 22.6%, indicating enhanced effectiveness in memory search tasks. Additionally, it reduces token consumption by 12.9% and search iterations by 20.2%, showcasing improved efficiency. These results suggest that R^2-Mem not only enhances the quality of search outcomes but also optimizes resource utilization.

**Limitations**  
The authors acknowledge that the framework's reliance on historical trajectories may limit its applicability in dynamic environments where past experiences may not be relevant. Additionally, the evaluation metrics focus primarily on F1 scores, token consumption, and search iterations, which may not capture all dimensions of performance in diverse applications. The paper does not address potential scalability issues or the impact of varying the rubric used for evaluation on the overall performance of the system.

**Why it matters**  
The implications of R^2-Mem are significant for the development of self-improving LLM agents, particularly in applications requiring efficient memory retrieval and decision-making. By providing a framework that allows agents to learn from past experiences without the overhead of reinforcement learning, R^2-Mem paves the way for more robust and adaptable AI systems. This work could influence future research on memory systems and the integration of reflective learning mechanisms in AI, potentially leading to advancements in areas such as conversational agents, information retrieval, and autonomous decision-making.

Authors: Xinyuan Wang, Wenyu Mao, Junkang Wu, Xiang Wang, Xiangnan He  
Source: arXiv:2605.13486  
URL: [https://arxiv.org/abs/2605.13486v1](https://arxiv.org/abs/2605.13486v1)
