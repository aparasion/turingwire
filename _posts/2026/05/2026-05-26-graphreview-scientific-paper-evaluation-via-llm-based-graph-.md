---
title: "GraphReview: Scientific Paper Evaluation via LLM-Based Graph Message Passing"
date: 2026-05-26 15:58:49 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.27204v1"
arxiv_id: "2605.27204"
authors: ["Pujun Zheng", "Wanying Ren", "Jiacheng Yao", "Guoxiu He", "Star X. Zhao"]
slug: graphreview-scientific-paper-evaluation-via-llm-based-graph-
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in existing literature regarding the evaluation of scientific papers using Large Language Models (LLMs). Current LLM-based methods typically assess manuscripts in isolation, failing to integrate contextual relationships with contemporaneous and prior research. The authors propose a unified framework that leverages a graph-based approach to propagate review evidence across a semantic paper graph, which is not adequately covered in prior works. This is a preprint and has not yet undergone peer review.

**Method**  
The core contribution of this work is the GraphReview framework, which employs a graph-based architecture to model the evaluation of scientific papers. The framework constructs a semantic graph where nodes represent individual papers and edges denote relationships based on review signals. LLMs are utilized to estimate node-level quality priors and generate edge-level comparative evidence through pairwise comparisons of papers. The integration of Personalized PageRank allows for the aggregation of review signals to facilitate quality ranking, decision prediction, and review generation. To enhance the quality of the graph evidence, the authors introduce reward-induced maximum likelihood objectives for training the LLM backbones, optimizing the model for better performance in generating review outputs.

**Results**  
GraphReview demonstrates significant performance improvements over the strongest baseline methods. The framework achieves an average increase of 29.7% across decision and ranking metrics. Specifically, it reports a 23.7% improvement in accuracy and a 57.6% enhancement in Spearman's ρ correlation coefficient. These results indicate that GraphReview not only excels in ranking and decision-making tasks but also produces higher-quality review texts. The model shows robustness and generalization capabilities across different time periods and conference venues, suggesting its versatility in various contexts.

**Limitations**  
The authors acknowledge several limitations, including the potential biases inherent in the training data used for the LLMs, which may affect the quality of the generated reviews. Additionally, the reliance on graph structures may introduce complexity in terms of computational efficiency and scalability, particularly for large datasets. The paper does not address the interpretability of the model's decisions, which is a critical aspect in scientific evaluations. Furthermore, the framework's performance in niche or emerging research areas remains untested.

**Why it matters**  
The implications of GraphReview are significant for the field of scientific paper evaluation. By providing a unified mechanism for integrating contextual relationships among papers, this framework enhances the quality and relevance of reviews, potentially leading to more informed decision-making in the peer review process. The ability to generalize across different time periods and venues suggests that GraphReview could be a valuable tool for academic publishers and researchers alike, facilitating a more nuanced understanding of the scientific landscape. This work opens avenues for further research into graph-based methodologies in natural language processing and the evaluation of academic contributions.

Authors: Pujun Zheng, Wanying Ren, Jiacheng Yao, Guoxiu He, Star X. Zhao  
Source: arXiv cs.CL  
URL: https://arxiv.org/abs/2605.27204v1  
arXiv ID: 2605.27204
