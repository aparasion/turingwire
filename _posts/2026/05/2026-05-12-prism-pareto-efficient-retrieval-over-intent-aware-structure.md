---
title: "PRISM: Pareto-Efficient Retrieval over Intent-Aware Structured Memory for Long-Horizon Agents"
date: 2026-05-12 15:28:30 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.12260v1"
arxiv_id: "2605.12260"
authors: ["Jingyi Peng", "Zhongwei Wan", "Weiting Liu", "Qiuzhuang Sun"]
slug: prism-pareto-efficient-retrieval-over-intent-aware-structure
summary_word_count: 459
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing memory management techniques for long-horizon language agents, particularly in the context of conversation history accumulation. Current methods either expand context windows without optimizing retrieval, incur high token costs through fact extraction, or utilize heuristic graph traversal that compromises both accuracy and efficiency. The authors propose PRISM, a novel framework that operates on the premise of treating long-horizon memory as a joint retrieval-and-compression problem over a graph-structured memory. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
PRISM introduces a training-free retrieval framework that integrates four key inference-time components:  
1. **Hierarchical Bundle Search**: This component navigates through typed relation paths to identify relevant information efficiently.  
2. **Query-Sensitive Edge Costing**: It aligns the traversal of the graph with the detected intent of the query, optimizing the retrieval process based on user intent.  
3. **Evidence Compression**: This step compresses the retrieved candidate bundle into a compact context suitable for answering, thereby reducing the context size while maintaining relevance.  
4. **Adaptive Intent Routing**: This mechanism routes the majority of queries through zero-LLM (Large Language Model) tiers, minimizing computational overhead.  

The retrieval process is formulated as a min-cost selection problem over typed path templates, which is then paired with a compression step on the LLM side. This approach allows PRISM to efficiently surface relevant evidence while adhering to strict context budget constraints, without necessitating any fine-tuning or alterations to the upstream ingestion pipeline.

**Results**  
Experiments conducted on the LoCoMo benchmark demonstrate that PRISM significantly outperforms all same-protocol baselines in terms of LLM-judge accuracy. Specifically, PRISM achieves a marked improvement in accuracy while operating under an order-of-magnitude smaller context budget. This performance indicates that PRISM occupies a previously unexploited area of the accuracy-context-cost trade-off, showcasing a superior balance between answer quality and retrieval efficiency.

**Limitations**  
The authors acknowledge that PRISM's performance is contingent on the quality of the underlying graph-structured memory and the effectiveness of the query intent detection mechanism. Additionally, the framework's reliance on a zero-LLM tier for most queries may limit its applicability in scenarios requiring more complex reasoning or nuanced understanding. The paper does not address potential scalability issues when applied to larger datasets or more complex conversational contexts.

**Why it matters**  
The implications of PRISM are significant for the development of long-horizon language agents, particularly in applications requiring efficient memory management and high accuracy in response generation. By providing a framework that balances retrieval efficiency with answer quality, PRISM opens avenues for future research in memory-augmented language models and could influence the design of more sophisticated conversational agents. This work may also inspire further exploration into graph-based memory architectures and their integration with LLMs.

Authors: Jingyi Peng, Zhongwei Wan, Weiting Liu, Qiuzhuang Sun  
Source: arXiv:2605.12260  
URL: [https://arxiv.org/abs/2605.12260v1](https://arxiv.org/abs/2605.12260v1)
