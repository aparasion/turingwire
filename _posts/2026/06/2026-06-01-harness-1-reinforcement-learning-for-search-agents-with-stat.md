---
title: "Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses"
date: 2026-06-01 15:21:41 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02373v1"
arxiv_id: "2606.02373"
authors: ["Pengcheng Jiang", "Zhiyi Shi", "Kelly Hong", "Xueqiang Xu", "Jiashuo Sun", "Jimeng Sun"]
slug: harness-1-reinforcement-learning-for-search-agents-with-stat
summary_word_count: 424
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces Harness-1, a 20B parameter search agent that utilizes a state-externalizing harness to improve retrieval performance in reinforcement learning."
---

**Problem**  
The paper addresses the limitations of traditional reinforcement learning (RL) frameworks for search agents, which often require the policy to manage both semantic search decisions and bookkeeping tasks. This dual responsibility can hinder performance, as the environment is better suited to maintain state information. The authors propose a novel approach, Harness-1, to alleviate this issue by externalizing state management, allowing the policy to focus solely on decision-making. This work is a preprint and has not yet undergone peer review.

**Method**  
Harness-1 is a 20 billion parameter search agent designed to operate within a stateful search harness. The architecture separates the responsibilities of the RL policy and the environment: the harness manages working memory, which includes a candidate pool, an importance-tagged curated set, compact evidence links, verification records, and budget-aware context rendering. The RL policy is tasked with semantic decisions such as what to search, which documents to retain or discard, what to verify, and when to terminate the search. The training process leverages reinforcement learning techniques, although specific details regarding the loss function and training compute are not disclosed in the paper.

**Results**  
Harness-1 demonstrates significant improvements in retrieval performance across eight benchmarks, including web search, finance, patents, and multi-hop question answering (QA). It achieves an average curated recall of 0.730, surpassing the next strongest open search subagent by 11.4 points. Notably, Harness-1 remains competitive with larger frontier-model searchers, indicating its efficiency and effectiveness. The model's performance is particularly robust on held-out transfer benchmarks, suggesting that the explicit management of search state through reinforcement learning enhances generalization capabilities beyond the training domains.

**Limitations**  
The authors acknowledge that while Harness-1 shows promising results, the reliance on a stateful harness may introduce complexity in deployment and scalability. Additionally, the paper does not provide extensive details on the computational resources required for training or the specific configurations of the benchmarks used. There is also no discussion on the potential limitations of the harness design itself, such as its adaptability to different search contexts or its performance in real-world applications.

**Why it matters**  
The introduction of Harness-1 represents a significant advancement in the design of search agents, particularly in how they manage state and decision-making processes. By externalizing state management, the framework allows for more efficient and effective retrieval strategies, which could have broad implications for various applications in information retrieval and natural language processing. This work lays the groundwork for future research into state management in RL environments, as highlighted in related literature on search agent optimization and reinforcement learning methodologies, as published in [arXiv cs.CL](https://arxiv.org/abs/2606.02373v1).
