---
title: "An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration"
date: 2026-05-05 17:10:25 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.03989v1"
arxiv_id: "2605.03989"
authors: ["Dutao Zhang", "Tian Liao"]
slug: an-agent-oriented-pluggable-experience-rag-skill-for-experie
summary_word_count: 406
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitation of existing retrieval-augmented generation (RAG) systems, which typically rely on a single, fixed retrieval pipeline across diverse tasks such as factoid question answering, multi-hop reasoning, and scientific verification. The authors argue that these tasks exhibit distinct retrieval preferences that are not adequately served by a monolithic approach. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Experience-RAG Skill, an agent-oriented pluggable retrieval orchestration layer that operates between the agent and a pool of retrievers. This skill is designed to analyze the current context or scene, consult an experience memory, and select the most suitable retrieval strategy dynamically. The architecture allows for flexible retrieval strategy selection, which is encapsulated as a reusable skill rather than being hard-coded into the agent's workflow. The authors do not disclose specific details about the training compute or the exact architecture of the experience memory, but they emphasize the modularity and adaptability of their approach.

**Results**  
The Experience-RAG Skill achieves an overall normalized Discounted Cumulative Gain (nDCG@10) of 0.8924 across multiple benchmarks, including BeIR/nq, BeIR/hotpotqa, and BeIR/scifact. This performance surpasses that of fixed single-retriever baselines, demonstrating a significant improvement in retrieval effectiveness. Additionally, the proposed method remains competitive with Adaptive-RAG-style routing, indicating that the dynamic selection of retrieval strategies can yield performance on par with more complex adaptive systems.

**Limitations**  
The authors acknowledge that their approach is contingent on the quality and diversity of the retriever pool, which may limit generalizability across different domains. They also note that the experience memory's effectiveness is dependent on the richness of the contextual information it can leverage. An obvious limitation not explicitly mentioned is the potential computational overhead introduced by the dynamic retrieval strategy selection, which may affect real-time performance in latency-sensitive applications.

**Why it matters**  
The implications of this work are significant for the development of more sophisticated retrieval-augmented systems. By framing retrieval strategy selection as a pluggable skill, the authors propose a modular approach that can enhance the adaptability and efficiency of RAG systems across various tasks. This could lead to improved performance in applications requiring nuanced retrieval capabilities, such as conversational agents, automated scientific research tools, and complex question-answering systems. The findings suggest a shift towards more flexible architectures in AI systems, promoting the idea that retrieval strategies should be contextually driven rather than static.

Authors: Dutao Zhang, Tian Liao  
Source: arXiv:2605.03989  
URL: [https://arxiv.org/abs/2605.03989v1](https://arxiv.org/abs/2605.03989v1)
