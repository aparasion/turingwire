---
title: "MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation"
date: 2026-05-26 17:59:19 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27366v1"
arxiv_id: "2605.27366"
authors: ["Huawei Lin", "Peng Li", "Jie Song", "Fuxin Jiang", "Tieying Zhang"]
slug: muse-autoskill-self-evolving-agents-via-skill-creation-memor
summary_word_count: 422
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing skill creation methodologies in large language model (LLM) agents, which typically treat skills as isolated and static entities. This approach restricts the reusability, reliability, and long-term enhancement of skills. The authors propose the MUSE-Autoskill framework, which allows for the continuous evolution of skills through a unified lifecycle encompassing creation, memory, management, evaluation, and refinement. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The MUSE-Autoskill framework introduces a skill-centric architecture that enables agents to autonomously create, store, and refine skills. Key components include:
- **Skill Creation**: Skills are generated on demand based on task requirements.
- **Skill Memory**: A novel memory system accumulates experience for each skill, facilitating effective reuse and adaptation across tasks.
- **Skill Management**: Skills are organized and selected efficiently, allowing agents to choose the most relevant skills for a given task.
- **Skill Evaluation**: Skills undergo unit testing and receive runtime feedback, which informs their continuous refinement.

The authors do not disclose specific details regarding the training compute or the exact architecture used in their experiments, focusing instead on the lifecycle management of skills.

**Results**  
The authors conducted experiments on the SkillsBench benchmark, demonstrating that lifecycle-managed skills significantly enhance task success rates, efficiency, and skill reuse. While specific numerical results are not provided in the abstract, the paper claims that the MUSE-Autoskill framework outperforms traditional skill management approaches, indicating a marked improvement in cross-agent skill transfer. The results suggest that treating skills as long-lived, experience-aware, and testable assets leads to better overall performance in task-solving capabilities.

**Limitations**  
The authors acknowledge that their framework is still in the early stages of development and may require further validation across a broader range of tasks and environments. They do not address potential scalability issues related to the memory management of skills or the computational overhead introduced by continuous skill evaluation and refinement. Additionally, the reliance on unit tests for skill evaluation may not capture all aspects of skill performance in dynamic environments.

**Why it matters**  
The MUSE-Autoskill framework has significant implications for the development of more adaptive and efficient LLM agents. By enabling agents to evolve their skills continuously, this approach could lead to more robust performance in complex, real-world applications. The emphasis on skill lifecycle management may inspire future research into dynamic skill adaptation and the integration of memory systems in AI agents, potentially influencing the design of next-generation autonomous systems.

Authors: Huawei Lin, Peng Li, Jie Song, Fuxin Jiang, Tieying Zhang  
Source: arXiv:2605.27366  
URL: [https://arxiv.org/abs/2605.27366v1](https://arxiv.org/abs/2605.27366v1)
