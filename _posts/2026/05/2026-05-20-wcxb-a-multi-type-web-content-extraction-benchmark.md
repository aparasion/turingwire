---
title: "WCXB: A Multi-Type Web Content Extraction Benchmark"
date: 2026-05-20 12:28:12 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21097v1"
arxiv_id: "2605.21097"
authors: ["Murrough Foley"]
slug: wcxb-a-multi-type-web-content-extraction-benchmark
summary_word_count: 427
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing benchmarks for web content extraction, which are often small (100-800 pages), limited to specific content types (primarily news articles), or outdated (from over a decade ago). The authors present the Web Content Extraction Benchmark (WCXB), a comprehensive dataset designed to facilitate the evaluation of extraction systems across a diverse range of web page types. This work is a preprint and has not yet undergone peer review.

**Method**  
The WCXB dataset comprises 2,008 web pages sourced from 1,613 distinct domains, categorized into seven types: articles, forums, products, collections, listings, documentation, and service pages. The dataset is split into a development set of 1,497 pages and a test set of 511 pages, ensuring matched distributions of page types. Ground truth annotations were generated through a rigorous five-stage pipeline that includes LLM-assisted drafting, automated verification, a four-pass review by frontier models, quality verification scripts, and final human review. The authors evaluate 13 extraction systems—11 heuristic and 2 neural—using this dataset to benchmark performance across the various page types.

**Results**  
The evaluation reveals that while the top-performing systems achieve an F1 score of 0.93 on article pages, there is significant performance degradation on structured page types, with F1 scores ranging from 0.41 to 0.84. This stark contrast highlights the limitations of existing benchmarks that focus solely on articles, as they fail to capture the complexities of diverse web content. The results indicate that current extraction systems are not adequately equipped to handle the variability present in non-article page types.

**Limitations**  
The authors acknowledge that the dataset, while comprehensive, may not encompass all possible web page types and structures, potentially limiting its applicability to certain domains. Additionally, the reliance on human review in the annotation process may introduce subjective biases. The paper does not address the computational resources required for training the evaluated systems or the potential impact of domain-specific variations in web content on extraction performance.

**Why it matters**  
The introduction of the WCXB benchmark is significant for advancing the field of web content extraction, as it provides a more representative evaluation framework that includes a variety of page types. This can lead to the development of more robust extraction systems capable of handling diverse web content, which is crucial for applications in search indexing, retrieval-augmented generation, and NLP dataset construction. By revealing the blind spots of existing benchmarks, this work encourages further research into improving extraction techniques for structured and non-standard web pages, ultimately enhancing the performance of large language models and other downstream applications.

Authors: Murrough Foley  
Source: arXiv:2605.21097  
URL: https://arxiv.org/abs/2605.21097v1
