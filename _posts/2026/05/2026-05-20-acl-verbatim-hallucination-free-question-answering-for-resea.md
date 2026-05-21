---
title: "ACL-Verbatim: hallucination-free question answering for research"
date: 2026-05-20 12:30:29 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21102v1"
arxiv_id: "2605.21102"
authors: ["G\u00e1bor Recski", "Szilveszter T\u00f3th", "Nadia Verdha", "Istv\u00e1n Boros", "\u00c1d\u00e1m Kov\u00e1cs"]
slug: acl-verbatim-hallucination-free-question-answering-for-resea
summary_word_count: 415
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the prevalent issue of hallucinations in Large Language Models (LLMs) when applied to academic research, particularly in the context of question answering. The authors highlight the gap in reliable methods for extracting accurate information from trusted sources, specifically within the ACL Anthology. The work is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The authors introduce the extractive question answering system VerbatimRAG, which is designed to map user queries directly to verbatim text spans in research papers. A key contribution is the creation of a novel ground truth dataset that facilitates the mapping of user queries to relevant text spans. This dataset is constructed through human annotation by NLP researchers, utilizing synthetic user queries generated via a custom pipeline based on the ScIRGen methodology. The authors evaluate various extractive models on this benchmark, with a focus on a 150M-parameter ModernBERT token classifier. This classifier is trained using silver supervision derived from the aforementioned pipeline, optimizing for the task of extractive question answering.

**Results**  
The ModernBERT token classifier achieves a word-level F1 score of 53.6, outperforming the strongest evaluated LLM extractor, which scores 48.7. This performance is assessed on the newly created benchmark, demonstrating a significant improvement in extractive question answering capabilities for academic research. The results indicate that the proposed method effectively reduces hallucinations by providing direct access to verified text spans, thus enhancing the reliability of information retrieval from research papers.

**Limitations**  
The authors acknowledge several limitations, including the reliance on synthetic queries, which may not fully capture the diversity of real-world user inquiries. Additionally, the performance of the ModernBERT model may be constrained by the size of the training dataset and the specific domain of the ACL Anthology, potentially limiting generalizability to other fields. The paper does not address the computational resources required for training the models or the scalability of the VerbatimRAG system in broader applications.

**Why it matters**  
This work has significant implications for the development of AI-assisted research tools, particularly in enhancing the accuracy and reliability of information retrieval from academic literature. By mitigating hallucinations in LLMs, the proposed system can improve the efficiency of researchers in accessing high-quality information, thereby fostering more reliable academic discourse. The introduction of a dedicated benchmark for extractive question answering in research papers also sets a precedent for future studies, encouraging further exploration of extractive methods in various domains.

Authors: Gábor Recski, Szilveszter Tóth, Nadia Verdha, István Boros, Ádám Kovács  
Source: arXiv:2605.21102  
URL: https://arxiv.org/abs/2605.21102v1
