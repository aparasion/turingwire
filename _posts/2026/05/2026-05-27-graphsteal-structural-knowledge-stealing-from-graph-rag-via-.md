---
title: "GraphSteal: Structural Knowledge Stealing from Graph RAG via Traversal Reconstruction"
date: 2026-05-27 15:50:14 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.28645v1"
arxiv_id: "2605.28645"
authors: ["Jinze Gu", "Qinghua Mao", "Xi Lin", "Jun Wu"]
slug: graphsteal-structural-knowledge-stealing-from-graph-rag-via-
summary_word_count: 421
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the security of Retrieval-Augmented Generation (RAG) systems that utilize knowledge graphs, specifically focusing on the privacy vulnerabilities introduced by these structured data sources. The authors highlight that while Graph RAG enhances language models (LLMs) by integrating structured knowledge, it simultaneously exposes a new attack vector where adversaries can exploit the system to reconstruct hidden knowledge graphs. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel structure-oriented reconstruction framework designed to extract and reconstruct knowledge graphs from Graph RAG systems. The framework employs two primary search strategies: 

1. **Depth-Wise Heuristic Search**: This method focuses on extracting fine-grained node attributes by recursively expanding evidence centered around specific entities. It aims to gather detailed information about individual nodes in the graph.

2. **Breadth-Wise Diffusion Search**: This approach infers the overall graph topology by propagating information across neighborhoods defined by relational connections. It seeks to reconstruct the structural relationships between entities in the graph.

The authors conduct experiments on both generic and healthcare-related scenarios, demonstrating the effectiveness of their framework in recovering substantial portions of the original knowledge graph.

**Results**  
The proposed method achieves a remarkable recovery rate, successfully reconstructing over 90% of the original knowledge graph from various Graph RAG systems. The experiments reveal that the method can accurately identify sensitive entities, relations, and structural dependencies, showcasing high fidelity in the reconstruction process. The authors compare their results against existing guardrails, which provide limited defense against the proposed attack, underscoring the effectiveness of their approach.

**Limitations**  
The authors acknowledge that their framework primarily focuses on the structural aspects of knowledge graphs and may not account for all potential adversarial strategies. They also note that the effectiveness of their method may vary depending on the specific characteristics of the knowledge graph and the RAG system in use. Additionally, the paper does not explore the computational overhead associated with the reconstruction process, which could impact real-world applicability. 

**Why it matters**  
This research has significant implications for the security of Graph RAG systems, highlighting the urgent need for enhanced privacy measures in the design of these architectures. The findings suggest that existing defenses are insufficient to protect against structural knowledge stealing, prompting a reevaluation of how sensitive information is managed within knowledge graphs. This work opens avenues for future research focused on developing robust privacy-preserving techniques in the context of structured knowledge retrieval and generation.

Authors: Jinze Gu, Qinghua Mao, Xi Lin, Jun Wu  
Source: arXiv:2605.28645  
URL: [https://arxiv.org/abs/2605.28645v1](https://arxiv.org/abs/2605.28645v1)
