---
title: "Code as Agent Harness"
date: 2026-05-18 17:59:03 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18747v1"
arxiv_id: "2605.18747"
authors: ["Xuying Ning", "Katherine Tieu", "Dongqi Fu", "Tianxin Wei", "Zihao Li", "Yuanchen Bei"]
slug: code-as-agent-harness
summary_word_count: 499
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the emerging role of code in agentic systems, where code transitions from being merely a target output to serving as a foundational substrate for agent reasoning, action, environment modeling, and execution-based verification. The authors present a unified framework termed "code as agent harness," which is not only a conceptual shift but also a practical necessity in the context of large language models (LLMs) that have shown proficiency in code understanding and generation. This work is a preprint and has not yet undergone peer review.

**Method**  
The authors propose a structured approach to the concept of code as an agent harness, organized into three interconnected layers:  
1. **Harness Interface**: This layer focuses on how code facilitates connections between agents and their reasoning, actions, and environment modeling.  
2. **Harness Mechanisms**: This layer delves into the operational aspects of the harness, including planning, memory management, tool utilization for long-horizon execution, and feedback-driven control mechanisms that enhance reliability and adaptability.  
3. **Scaling to Multi-Agent Systems**: The final layer discusses the extension of the harness concept from single-agent to multi-agent systems, emphasizing the role of shared code artifacts in enabling coordination, review, and verification among multiple agents.  

The paper synthesizes existing methods and applications across various domains, such as coding assistants, GUI/OS automation, embodied agents, scientific discovery, and enterprise workflows. The authors also identify open challenges in harness engineering, including the need for evaluation metrics beyond task success, verification under incomplete feedback, and ensuring safety in human oversight scenarios.

**Results**  
While the paper does not present quantitative results or benchmark comparisons typical of empirical studies, it provides a comprehensive survey of existing methodologies and applications that leverage the code as agent harness framework. The authors summarize practical implementations across diverse fields, indicating a broad applicability of the proposed framework, although specific performance metrics against named baselines are not disclosed.

**Limitations**  
The authors acknowledge several limitations, including the need for improved evaluation methods that extend beyond final task success, challenges in verifying agent behavior under incomplete feedback, and the complexities of maintaining a consistent shared state across multiple agents. They also highlight the necessity for human oversight in safety-critical applications, which is crucial for ensuring the reliability of agent actions. However, the paper does not address potential scalability issues related to computational resources or the implications of code quality on agent performance.

**Why it matters**  
This work is significant as it reframes the role of code in AI systems, proposing a unified roadmap for developing executable, verifiable, and stateful AI agents. By centering code as the operational backbone of agentic AI, the paper lays the groundwork for future research in harness engineering, which could lead to more robust and adaptable AI systems capable of complex reasoning and multi-agent collaboration. The outlined challenges also provide a fertile ground for future investigations, potentially influencing the design of next-generation AI frameworks.

Authors: Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei, Jiaru Zou, Mengting Ai et al.  
Source: arXiv:2605.18747  
URL: [https://arxiv.org/abs/2605.18747v1](https://arxiv.org/abs/2605.18747v1)
