---
title: "Vector RAG vs LLM-Compiled Wiki: A Preregistered Comparison on a Small Multi-Domain Research"
date: 2026-05-18 14:41:16 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18490v1"
arxiv_id: "2605.18490"
authors: ["Theodore O. Cochran"]
slug: vector-rag-vs-llm-compiled-wiki-a-preregistered-comparison-o
summary_word_count: 433
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the comparative effectiveness of two methodologies for enhancing large language model (LLM) performance on question-answering tasks over a small multi-domain research corpus. Specifically, it contrasts a Vector Retrieval-Augmented Generation (RAG) system with an LLM-compiled markdown wiki, focusing on their capabilities in evidence organization, citation support, and operational cost.

**Method**  
The study employs a controlled experimental design where both systems were tasked with answering the same 13 questions derived from 24 research papers. The Vector RAG system utilizes a single-round retrieval mechanism to fetch relevant information, while the LLM-compiled wiki organizes findings in a markdown format. The evaluation involved blinded scoring by LLM judges, focusing on metrics such as groundedness and claim-level citation support. The authors also introduced a decomposition-based variant of RAG to assess its performance in cross-paper synthesis while minimizing LLM token usage. The training compute specifics were not disclosed, but the analysis emphasizes the cost-effectiveness of query token usage in RAG compared to the wiki.

**Results**  
The results indicate that the LLM-compiled wiki outperformed the Vector RAG system in connecting findings across papers, achieving a higher score in overall organization. However, after adjusting for judge biases, the advantage diminished. RAG met the preregistered criteria for single-fact lookup questions, demonstrating its efficiency in this context. Notably, the wiki incurred a significantly higher query token cost, undermining its expected operational efficiency. The decomposition-based RAG variant managed to recover much of the wiki's advantage in cross-paper synthesis while maintaining a lower token cost, although it did not match the wiki's performance in claim-by-claim citation support.

**Limitations**  
The authors acknowledge that their findings are limited by the small size of the research corpus and the specific nature of the questions posed. They also note that the performance metrics may vary with different types of queries or larger datasets. An additional limitation is the potential bias in LLM judges, which could affect the scoring of the answers. The study does not explore the scalability of either system beyond the tested corpus or the implications of varying LLM architectures on performance.

**Why it matters**  
This research has significant implications for the development of systems aimed at synthesizing research findings. It highlights that grounded research synthesis is multifaceted, with no single architecture excelling across all dimensions of evidence organization, citation support, and operational cost. The findings suggest that future work should focus on optimizing these systems for specific tasks rather than seeking a one-size-fits-all solution. This nuanced understanding can guide the design of more effective LLM applications in academic and research settings.

Authors: Theodore O. Cochran  
Source: arXiv:2605.18490  
URL: https://arxiv.org/abs/2605.18490v1
