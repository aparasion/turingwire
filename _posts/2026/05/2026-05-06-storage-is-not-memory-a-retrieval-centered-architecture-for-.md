---
title: "Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall"
date: 2026-05-06 13:27:41 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.04897v1"
arxiv_id: "2605.04897"
authors: ["Joshua Adler", "Guy Zehavi"]
slug: storage-is-not-memory-a-retrieval-centered-architecture-for-
summary_word_count: 443
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of traditional agent memory architectures that rely on extraction at ingestion, which leads to the loss of potentially relevant information before a query is made. The authors argue that this approach is inadequate for effective recall in multi-session conversational contexts, where the ability to retrieve verbatim events is crucial. The paper proposes a novel architecture, True Memory, that aims to enhance retrieval capabilities by preserving all events in their original form, thereby enabling more accurate responses to user queries.

**Method**  
The core technical contribution is the True Memory architecture, which consists of six layers designed to facilitate a multi-stage retrieval pipeline. This architecture operates directly on events stored in a single SQLite file, eliminating the need for external databases, vector indices, graph stores, or GPU resources. The system is optimized for commodity CPUs, making it accessible for widespread deployment. The authors detail the training process and the specific configurations tested, including a 56-configuration ablation study that evaluates variations within the top-performing setups. The architecture is evaluated using a matched gpt-4.1-mini answer model, ensuring consistency in performance assessment across different benchmarks.

**Results**  
True Memory Pro achieves notable performance metrics across several benchmarks. On the LoCoMo dataset, which consists of 1,540 questions from 10 multi-session conversations, it reaches an accuracy of 93.0% (3-run mean), significantly outperforming Mem0 (61.4%), Supermemory (65.4%), Zep (approximately 71%), and EverMemOS (94.5%). In the LongMemEval benchmark, True Memory Pro scores 87.8% (3-run mean) on 500 questions. Additionally, on the BEAM-1M dataset, which includes 700 questions at the 1-million-token scale, it achieves 76.6% (3-run mean), surpassing the previous best result of 73.9% from Hindsight. The ablation study indicates a 1.3-percentage-point performance variation within the top configurations, highlighting the sensitivity of the architecture to specific design choices.

**Limitations**  
The authors acknowledge that the architecture's reliance on a single SQLite file may limit scalability and performance in high-demand scenarios. They do not address potential issues related to the computational efficiency of the retrieval process, particularly as the volume of stored events increases. Additionally, the paper does not explore the impact of varying the underlying language model beyond the matched gpt-4.1-mini, which may affect generalizability across different NLP tasks.

**Why it matters**  
The implications of this work are significant for the development of more effective conversational agents and memory systems. By shifting the focus from storage to retrieval, True Memory offers a framework that could enhance the accuracy and relevance of responses in multi-session interactions. This approach may inform future research on memory architectures, particularly in contexts where preserving the integrity of information is critical for user engagement and satisfaction.

Authors: Joshua Adler, Guy Zehavi  
Source: arXiv:2605.04897  
URL: [https://arxiv.org/abs/2605.04897v1](https://arxiv.org/abs/2605.04897v1)
