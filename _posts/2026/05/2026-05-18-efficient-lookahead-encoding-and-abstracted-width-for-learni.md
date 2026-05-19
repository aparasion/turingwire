---
title: "Efficient Lookahead Encoding and Abstracted Width for Learning General Policies in Classical Planning"
date: 2026-05-18 17:15:23 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18674v1"
arxiv_id: "2605.18674"
authors: ["Michael Aichm\u00fcller", "Simon St\u00e5hlberg", "Martin Funkquist", "Hector Geffner"]
slug: efficient-lookahead-encoding-and-abstracted-width-for-learni
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing approaches in generalized planning, particularly focusing on the inefficiencies of Iterated Width (IW) policies in classical planning domains. While recent Graph Neural Network (GNN) methods have achieved high performance, they still suffer from scalability issues due to the individual evaluation of transitions in IW policies. The authors highlight that IW(1) policies, although linear in complexity with respect to the number of atoms, become computationally prohibitive when dealing with large instances, such as those in the International Planning Competition (IPC) 2023 benchmark. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose two key innovations to enhance the efficiency of IW policies. First, they introduce a holistic encoding of the search tree that allows for the joint representation of IW(1)-reachable states based solely on their relational differences to the current state. This enables Relational GNNs (R-GNNs) to evaluate all transitions in a single forward pass, significantly reducing computational overhead. Second, they define Abstracted IW(1), which employs relational abstraction during novelty checks. Instead of testing fully instantiated atoms, this method abstracts each atom by retaining only one argument and replacing others with their types. An atom is considered novel if any of its abstracted forms is novel, effectively shifting the novelty search from atoms to objects while maintaining the integrity of subgoal structures.

**Results**  
The proposed methods were evaluated on the IPC 2023 benchmark and across various planning domains, demonstrating state-of-the-art performance. The authors report significant improvements over previous approaches, including the classical planner LAMA. Specific performance metrics indicate that their policies achieve a notable increase in efficiency and scalability, although exact numerical results and effect sizes are not detailed in the abstract.

**Limitations**  
The authors acknowledge that while their approach improves scalability and efficiency, it may still face challenges in extremely large or complex planning domains that exceed the relational abstraction capabilities. Additionally, the reliance on R-GNNs may introduce limitations related to the expressiveness of the learned policies, particularly in domains that require nuanced reasoning beyond the relational framework. The paper does not discuss potential impacts of noise or uncertainty in the planning environment, which could affect the robustness of the proposed methods.

**Why it matters**  
This work has significant implications for the field of automated planning, particularly in enhancing the scalability of learning-based approaches. By addressing the computational inefficiencies of IW policies, the proposed methods could facilitate the application of generalized planning in more complex real-world scenarios. The advancements in relational abstraction and holistic encoding may inspire further research into efficient policy learning and planning algorithms, potentially leading to breakthroughs in domains that require high-level reasoning and decision-making.

Authors: Michael Aichmüller, Simon Ståhlberg, Martin Funkquist, Hector Geffner  
Source: arXiv:2605.18674  
URL: [https://arxiv.org/abs/2605.18674v1](https://arxiv.org/abs/2605.18674v1)
