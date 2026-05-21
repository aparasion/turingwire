---
title: "Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling"
date: 2026-05-20 17:54:27 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21470v1"
arxiv_id: "2605.21470"
authors: ["Caleb Winston", "Ron Yifeng Wang", "Azalia Mirhoseini", "Christos Kozyrakis"]
slug: agent-jit-compilation-for-latency-optimizing-web-agent-plann
summary_word_count: 465
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of current Computer-Use Agents (CUAs) that rely on a sequential fetch-screenshot-execute loop, which incurs high latency and frequent errors due to incorrect tool usage. The authors propose a novel approach called agent just-in-time (JIT) compilation, which compiles task descriptions into executable code, thereby reducing the dependency on repeated LLM calls. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution consists of three main components:  
1. **JIT-Planner**: This component generates multiple code plans for a given task, validates them against tool specifications, and selects the plan with the minimum cost. The planning process incorporates a cost model that accounts for both execution time and accuracy.
2. **JIT-Scheduler**: This module explores various parallelization strategies using Monte Carlo cost estimation based on learned latency distributions. It aims to optimize the execution of the generated plans by scheduling tool calls in a manner that minimizes overall latency.
3. **Invariant-Enforcing Tool Protocol**: This protocol specifies precondition and postcondition state requirements for tool usage, which helps to reduce the generation of plans that would lead to incorrect tool interactions.

The authors do not disclose specific details regarding the training compute or datasets used for the learned latency distributions, focusing instead on the architectural innovations and their implications for performance.

**Results**  
The proposed JIT-Planner achieves a remarkable $10.4\times$ speedup and a $+28\%$ increase in accuracy compared to the baseline Browser-Use method across five web applications. Additionally, the JIT-Scheduler demonstrates a $2.4\times$ speedup and a $+9\%$ accuracy improvement over the OpenAI CUA baseline. These results indicate significant enhancements in both execution speed and correctness, showcasing the effectiveness of the JIT compilation approach in optimizing web agent planning and scheduling.

**Limitations**  
The authors acknowledge that their approach may be limited by the complexity of the tasks and the variability in tool specifications, which could affect the generalizability of the JIT-Planner and JIT-Scheduler. They also note that the reliance on learned latency distributions may introduce biases if the training data does not adequately represent the diversity of web applications. An additional limitation not explicitly mentioned is the potential overhead introduced by the JIT compilation process itself, which may negate some of the speed advantages in scenarios with low-latency requirements.

**Why it matters**  
This work has significant implications for the development of more efficient and reliable CUAs, particularly in applications requiring real-time interaction with web interfaces. By reducing latency and improving accuracy, the JIT compilation approach could enable more complex task automation, enhancing user experience and expanding the applicability of CUAs in various domains. Furthermore, the architectural innovations presented may inspire future research in optimizing agent-based systems and improving the integration of LLMs with execution environments.

Authors: Caleb Winston, Ron Yifeng Wang, Azalia Mirhoseini, Christos Kozyrakis  
Source: arXiv:2605.21470  
URL: [https://arxiv.org/abs/2605.21470v1](https://arxiv.org/abs/2605.21470v1)
