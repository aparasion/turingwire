---
title: "GRASP: Plan-Guided Graph Retrieval with Adaptive Fusion and Reranking on Semi-Structured Knowledge Bases"
date: 2026-05-28 17:07:32 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30237v1"
arxiv_id: "2605.30237"
authors: ["Yicheng Tao", "Yiqun Wang", "Xiangchen Song", "Xin Luo", "Kai Liu", "Jie Liu"]
slug: grasp-plan-guided-graph-retrieval-with-adaptive-fusion-and-r
summary_word_count: 417
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing hybrid retrieval systems for semi-structured knowledge bases (SKBs), which typically either utilize graph structures solely for query expansion, employ a global weighting scheme for textual and structural data, or depend on fine-tuned graph-traversal generators. The authors identify a gap in the capability of these systems to effectively integrate plan-based graph retrieval with dense retrieval methods and reranking strategies. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose GRASP, a novel three-stage retrieval framework designed for SKBs. The architecture consists of:  
1. **Plan-based Graph Retrieval**: This stage utilizes a structured plan to guide the retrieval process, leveraging the inherent relationships within the graph.
2. **Plan-conditioned Fusion**: In this stage, a dense retriever is employed to fuse the results from the graph-based retrieval with textual data, allowing for a more nuanced integration of information.
3. **Fine-tuned Reranking**: The final stage involves a reranking mechanism that refines the candidate results based on learned representations, enhancing the relevance of the retrieved documents.

The authors do not disclose specific details regarding the training compute or the datasets used, but they emphasize the robustness of the framework through ablation and sensitivity analyses.

**Results**  
GRASP demonstrates significant improvements over existing baselines across all metrics on the three STaRK benchmarks. Notably, the average Hit@1 metric increases from 62.0 to 73.9, indicating a substantial enhancement in retrieval accuracy. The paper provides detailed comparisons against named baselines, showcasing GRASP's effectiveness in retrieving relevant documents from SKBs.

**Limitations**  
The authors acknowledge that while GRASP improves retrieval performance, it may still be sensitive to the quality of the underlying knowledge graph and the initial query formulation. Additionally, the framework's reliance on a dense retriever may introduce computational overhead, which could limit its scalability in large-scale applications. The paper does not address potential biases in the knowledge graph or the implications of using a plan-based approach in diverse domains.

**Why it matters**  
The implications of GRASP are significant for downstream applications that rely on SKBs, such as product search, academic paper retrieval, and precision medicine. By effectively integrating plan-based retrieval with dense retrieval and reranking, GRASP sets a new benchmark for hybrid retrieval systems, potentially leading to more accurate and contextually relevant search results. This work opens avenues for further research into adaptive retrieval strategies and the optimization of knowledge graph utilization in various AI applications.

Authors: Yicheng Tao, Yiqun Wang, Xiangchen Song, Xin Luo, Kai Liu, Jie Liu  
Source: arXiv:2605.30237  
URL: [https://arxiv.org/abs/2605.30237v1](https://arxiv.org/abs/2605.30237v1)
