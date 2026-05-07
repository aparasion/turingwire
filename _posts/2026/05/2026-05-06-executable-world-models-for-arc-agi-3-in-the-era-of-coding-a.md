---
title: "Executable World Models for ARC-AGI-3 in the Era of Coding Agents"
date: 2026-05-06 17:12:36 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.05138v1"
arxiv_id: "2605.05138"
authors: ["Sergey Rodionov"]
slug: executable-world-models-for-arc-agi-3-in-the-era-of-coding-a
summary_word_count: 414
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the development of coding-agent systems for the ARC-AGI-3 benchmark, specifically focusing on the use of executable world models. The authors present a preprint work that explores how agents can leverage a world model that is both executable and verifiable, without relying on hand-coded game-specific logic. This approach aims to enhance the generalizability of agents across various tasks within the ARC-AGI-3 framework.

**Method**  
The core technical contribution is the design of a coding-agent system that maintains an executable Python world model. The architecture includes a scripted controller, predefined interfaces for the world model, verifier programs, and a plan executor. The agent refactors its world model towards simpler abstractions, akin to a Minimum Description Length (MDL) principle, to promote simplicity bias. The training process involves evaluating the model against previous observations and planning actions based on the model before execution. The system was tested on 25 public ARC-AGI-3 games, with each playthrough initiated by a fresh agent instance, ensuring no access to prior playthrough data.

**Results**  
The agent fully solved 7 out of the 25 games, demonstrating a Relative Human Action Efficiency (RHAE) greater than 75% on 6 games. The mean per-game RHAE across all games was reported at 32.58%. These results indicate a significant performance level, especially considering the absence of game-specific code, which positions this system as a general baseline for future ARC-AGI-3 agents. The authors note that performance on the private validation set has yet to be evaluated, which may further inform the robustness of the approach.

**Limitations**  
The authors acknowledge that the current evaluation is limited to public games, and the performance on the private validation set remains untested. Additionally, the reliance on a scripted controller and predefined interfaces may restrict the adaptability of the agent in more complex or dynamic environments. The study also does not address the scalability of the approach to more intricate tasks or the potential computational overhead associated with the verification and refactoring processes.

**Why it matters**  
This work has significant implications for the development of generalizable AI agents capable of operating across diverse tasks without extensive customization. By demonstrating the feasibility of verifier-driven executable world models, the authors provide a foundation for future research into more sophisticated coding agents. This approach could lead to advancements in autonomous agents that can learn and adapt in real-time, enhancing their applicability in real-world scenarios and contributing to the broader field of artificial general intelligence (AGI).

Authors: Sergey Rodionov  
Source: arXiv:2605.05138  
URL: [https://arxiv.org/abs/2605.05138v1](https://arxiv.org/abs/2605.05138v1)
