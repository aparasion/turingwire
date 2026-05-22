---
title: "MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems"
date: 2026-05-21 17:48:33 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22794v1"
arxiv_id: "2605.22794"
authors: ["Qianshu Cai", "Yonggang Zhang", "Xianzhang Jia", "Wei Xue", "Jun Song", "Xinmei Tian"]
slug: moss-self-evolution-through-source-level-rewriting-in-autono
summary_word_count: 479
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of current autonomous agent systems, which remain static post-deployment and do not learn from user interactions. Existing self-evolving agents are restricted to modifying text-mutable artifacts, such as skill files and prompt configurations, leaving the underlying codebase unaltered. This results in persistent structural failures that cannot be addressed through text-based adaptations. The authors propose a novel approach to self-evolution that operates at the source code level, which is a more comprehensive and effective medium for adaptation. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is MOSS, a self-evolving system that performs source-level rewriting on autonomous agent architectures. MOSS operates through a deterministic multi-stage pipeline, where each evolution is driven by an automatically curated batch of production-failure evidence. The system delegates code modifications to an external coding-agent CLI, while maintaining control over the stage ordering and decision-making processes. Candidate code modifications are validated by replaying the failure evidence against the modified code in ephemeral trial workers. Successful candidates are then promoted to production through a user-consent-gated in-place container swap, with health probes ensuring rollback capabilities in case of failure. The architecture emphasizes deterministic outcomes and resilience against long-context drift, enhancing the agent's ability to adapt without human intervention.

**Results**  
MOSS was evaluated on the OpenClaw benchmark, achieving a significant improvement in performance. The mean grader score for a four-task evaluation increased from 0.25 to 0.61 in a single evolution cycle, demonstrating a substantial enhancement in the agent's capabilities. This performance was achieved without any human intervention, showcasing the effectiveness of the self-evolution mechanism compared to traditional methods that rely on manual updates.

**Limitations**  
The authors acknowledge several limitations, including the dependency on the quality of the curated failure evidence, which may affect the efficacy of the self-evolution process. Additionally, the reliance on external coding-agent CLI for modifications introduces potential points of failure and may limit the scope of adaptations. The system's performance in diverse operational environments and its scalability to more complex agent architectures remain untested. Furthermore, the implications of user consent in the promotion process could introduce delays or biases in the evolution cycle.

**Why it matters**  
The implications of MOSS are significant for the field of autonomous agents, as it introduces a paradigm shift in how these systems can evolve post-deployment. By enabling source-level adaptations, MOSS addresses a critical gap in the ability of agents to learn from real-world interactions and failures. This capability could lead to more robust and resilient autonomous systems that can self-correct and improve over time, reducing the need for human intervention and accelerating the deployment of intelligent agents in dynamic environments. The work sets a foundation for future research into self-evolving systems and their applications across various domains.

Authors: Qianshu Cai, Yonggang Zhang, Xianzhang Jia, Wei Xue, Jun Song, Xinmei Tian, Yike Guo  
Source: arXiv:2605.22794  
URL: [https://arxiv.org/abs/2605.22794v1](https://arxiv.org/abs/2605.22794v1)
