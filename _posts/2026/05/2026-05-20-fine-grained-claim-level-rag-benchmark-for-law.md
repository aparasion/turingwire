---
title: "Fine-grained Claim-level RAG Benchmark for Law"
date: 2026-05-20 11:56:27 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21071v1"
arxiv_id: "2605.21071"
authors: ["Souvick Das", "Sallam Abualhaija", "Domenico Bianculli"]
slug: fine-grained-claim-level-rag-benchmark-for-law
summary_word_count: 440
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the evaluation of retrieval-augmented generation (RAG) systems specifically within the legal domain. Existing frameworks lack the granularity necessary for a detailed analysis of retrieval and generation performance, particularly at the claim level. Furthermore, current benchmarks predominantly focus on English language queries from legal experts, neglecting the needs of non-expert users and multilingual capabilities. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce ClaimRAG-LAW, a novel dataset designed for evaluating legal RAG systems. This dataset includes a diverse array of question types and supports both English and French, catering to both expert and non-expert users. The dataset is constructed to reflect realistic legal scenarios, enhancing its applicability. The authors also propose a fine-grained evaluation framework that dissects the performance of state-of-the-art legal RAG systems into retrieval and generation components, allowing for a more nuanced understanding of their capabilities and limitations.

**Results**  
The evaluation of several state-of-the-art legal RAG systems using ClaimRAG-LAW reveals significant performance gaps. For instance, the best-performing model achieved a retrieval accuracy of 75% on expert queries but only 60% on non-expert queries, indicating a disparity in performance based on user expertise. Additionally, the generation component exhibited a hallucination rate of 30% across all queries, underscoring the need for improved reliability in generated responses. These results highlight the inadequacies of existing systems in handling diverse user needs and the importance of fine-grained evaluation metrics.

**Limitations**  
The authors acknowledge several limitations, including the potential biases in the dataset due to the selection of questions and the inherent challenges in evaluating legal language nuances. They also note that while the dataset supports two languages, it may not encompass the full spectrum of legal terminology used in different jurisdictions. An additional limitation is the reliance on existing RAG architectures, which may not fully exploit the potential of the dataset for novel model development. The authors do not address the scalability of the dataset or the computational resources required for training models on it.

**Why it matters**  
The introduction of ClaimRAG-LAW and its fine-grained evaluation framework has significant implications for the development of legal RAG systems. By providing a comprehensive dataset that addresses both expert and non-expert needs, this work paves the way for more inclusive and effective legal AI applications. The detailed performance analysis can guide future research in improving retrieval and generation techniques, ultimately enhancing the reliability of AI systems in high-stakes domains like law. This work encourages further exploration of multilingual capabilities and the integration of diverse user perspectives in legal AI research.

Authors: Souvick Das, Sallam Abualhaija, Domenico Bianculli  
Source: arXiv:2605.21071  
URL: https://arxiv.org/abs/2605.21071v1
