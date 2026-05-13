---
title: "Overview of the MedHopQA track at BioCreative IX: track description, participation and evaluation of systems for multi-hop medical question answering"
date: 2026-05-12 15:59:28 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.12313v1"
arxiv_id: "2605.12313"
authors: ["Rezarta Islamaj", "Joey Chan", "Robert Leaman", "Jongmyung Jung", "Hyeongsoon Hwang", "Quoc-An Nguyen"]
slug: overview-of-the-medhopqa-track-at-biocreative-ix-track-descr
summary_word_count: 481
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in multi-hop question answering (QA) within the biomedical domain, specifically focusing on the integration of information across multiple sources to answer complex queries. The authors present the BioCreative IX MedHopQA shared task, which is a preprint and unreviewed work, aimed at benchmarking large language models (LLMs) on this challenging task. The need for effective multi-hop reasoning is underscored by the complexity of biomedical information, particularly concerning rare diseases, which necessitates a robust evaluation framework.

**Method**  
The core technical contribution is the development of a novel dataset comprising 1,000 multi-hop QA pairs that require two-hop reasoning through information extracted from distinct Wikipedia pages. The dataset emphasizes questions related to diseases, genes, and chemicals. The evaluation of participating systems was conducted using two metrics: surface string comparison and conceptual accuracy, quantified by the MedCPT score. The challenge attracted 48 submissions from 13 teams, showcasing a variety of approaches. Notably, the use of retrieval-augmented generation (RAG) and retrieval-based strategies emerged as critical for achieving high performance. The top-performing system utilized these techniques effectively, demonstrating the importance of integrating retrieval mechanisms in multi-hop reasoning tasks.

**Results**  
The results indicate a significant performance gap between baseline LLMs and enhanced systems. The leading submission achieved an F1 score of 89.30% and an exact match (EM) score of 87.30% on the MedCPT metric. In contrast, the zero-shot baseline models recorded F1 and EM scores of 67.40% and 60.20%, respectively. This highlights an effect size of approximately 21.90% in F1 score and 27.10% in EM score, demonstrating the efficacy of advanced methodologies over baseline approaches. The findings also suggest that concept-level evaluation provides a more nuanced assessment of answers, particularly when correct responses vary in surface form.

**Limitations**  
The authors acknowledge several limitations, including the potential biases in the dataset due to its reliance on Wikipedia as a source, which may not encompass all relevant biomedical knowledge. Additionally, the challenge's focus on two-hop reasoning may not fully represent the complexities of real-world biomedical queries that could require more extensive reasoning. The authors also note that while retrieval-based strategies were effective, the generalizability of these methods to other domains or more complex multi-hop scenarios remains to be explored.

**Why it matters**  
The implications of this work are significant for downstream research in biomedical information retrieval and QA systems. By providing a publicly available dataset and a structured evaluation framework, the MedHopQA challenge fosters further advancements in multi-hop reasoning capabilities of LLMs. The emphasis on retrieval-augmented techniques may influence future model architectures and training paradigms, encouraging the integration of external knowledge sources to enhance performance in complex reasoning tasks. This work sets a foundation for subsequent studies aimed at improving the accuracy and reliability of AI systems in the biomedical field.

Authors: Rezarta Islamaj, Joey Chan, Robert Leaman, Jongmyung Jung, Hyeongsoon Hwang, Quoc-An Nguyen, Hoang-Quynh Le, Harikrishnan Gurushankar Saisudha et al.  
Source: arXiv:2605.12313  
URL: https://arxiv.org/abs/2605.12313v1
