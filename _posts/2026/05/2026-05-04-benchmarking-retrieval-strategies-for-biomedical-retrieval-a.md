---
title: "Benchmarking Retrieval Strategies for Biomedical Retrieval-Augmented Generation: A Controlled Empirical Study"
date: 2026-05-04 12:21:46 +0000
category: research
subcategory: evaluation_benchmarks
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02520v1"
arxiv_id: "2605.02520"
authors: ["Devi Prasad Bal", "Subhashree Puhan"]
slug: benchmarking-retrieval-strategies-for-biomedical-retrieval-a
summary_word_count: 428
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of systematic empirical evaluations of retrieval strategies in the context of Retrieval-Augmented Generation (RAG) for biomedical applications. While RAG has been established as a method for grounding large language model (LLM) outputs in external knowledge, the effectiveness of various retrieval strategies in high-stakes domains like biomedicine has not been rigorously assessed. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors conduct a controlled empirical study comparing five retrieval strategies: Dense Vector Search, Hybrid BM25 + Dense retrieval, Cross-Encoder Reranking, Multi-Query Expansion, and Maximal Marginal Relevance (MMR). All strategies utilize a fixed generation model (GPT-4o-mini) and a common vector store (ChromaDB), with OpenAI's text-embedding-3-small embeddings for consistency. The evaluation is based on 250 question-answer pairs from a preprocessed subset of the BioASQ benchmark (rag-mini-bioasq). Four DeepEval metrics are employed: contextual precision, contextual recall, faithfulness, and answer relevancy, with results reported alongside 95% confidence intervals. A no-context ablation serves as a baseline to demonstrate the impact of retrieval.

**Results**  
Cross-Encoder Reranking achieves the highest composite score of 0.827 and the best contextual precision at 0.852, indicating that enhanced query-document interaction leads to significant retrieval improvements. The Dense baseline follows closely with a composite score of 0.822, only 0.005 points lower than the top strategy. Multi-Query Expansion, while designed to enhance recall, results in the lowest contextual precision of 0.671, suggesting that excessive query diversification can introduce noise. MMR, which aims for diversity, compromises answer relevancy. All RAG configurations significantly outperform the no-context ablation in terms of answer relevancy, with scores ranging from 0.658 to 0.701 compared to 0.287 for the ablation, underscoring the practical benefits of retrieval in this context.

**Limitations**  
The authors acknowledge that their study is limited to a specific biomedical question-answering dataset and may not generalize across other domains or datasets. Additionally, the reliance on a single generation model (GPT-4o-mini) may restrict the applicability of findings to other LLMs. The evaluation metrics, while comprehensive, may not capture all nuances of retrieval effectiveness in real-world applications.

**Why it matters**  
This work provides critical insights into the effectiveness of various retrieval strategies in RAG systems, particularly in the biomedical domain where accuracy is paramount. The findings can inform the design of more effective retrieval mechanisms in LLMs, potentially leading to improved performance in question-answering tasks. By making the full pipeline, hyperparameters, and evaluation code publicly available, the authors facilitate further research and development in this area, encouraging the exploration of retrieval strategies in other high-stakes applications.

Authors: Devi Prasad Bal, Subhashree Puhan  
Source: arXiv:2605.02520  
URL: [https://arxiv.org/abs/2605.02520v1](https://arxiv.org/abs/2605.02520v1)
