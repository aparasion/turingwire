---
title: "PersonalAI 2.0: Enhancing knowledge graph traversal/retrieval with planning mechanism for Personalized LLM Agents"
date: 2026-05-13 13:06:30 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13481v1"
arxiv_id: "2605.13481"
authors: ["Mikhail Menschikov", "Matvey Iskornev", "Alexander Kharitonov", "Alina Bogdanova", "Mikhail Belkin", "Ekaterina Lisitsyna"]
slug: personalai-2-0-enhancing-knowledge-graph-traversal-retrieval
summary_word_count: 462
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper presents PersonalAI 2.0 (PAI-2), a preprint framework aimed at addressing the limitations of existing Graph Retrieval-Augmented Generation (GraphRAG) methods in enhancing large language model (LLM) systems through external knowledge graphs (KG). The authors identify a gap in the capability of current systems to perform adaptive and iterative information retrieval, which is crucial for improving the factual correctness of generated responses. The work is particularly relevant for personalized AI applications that require robust knowledge representation and reasoning.

**Method**  
PAI-2 introduces a dynamic, multistage query processing pipeline that enhances the interaction between LLMs and KGs. The architecture employs a planning mechanism that facilitates adaptive information search, utilizing extracted entities, matched graph vertices, and generated clue-queries. The framework integrates various graph traversal algorithms, such as BeamSearch and WaterCircles, to optimize the retrieval process. The training compute specifics are not disclosed, but the evaluation leverages LLMs in the 7-14 billion parameter range. The authors also implement an LLM-as-a-Judge mechanism to assess the quality of generated answers, which plays a critical role in the iterative refinement of the retrieval process.

**Results**  
PAI-2 demonstrates significant improvements over baseline methods, including LightRAG, RAPTOR, and HippoRAG 2, across six benchmarks: Natural Questions, TriviaQA, HotpotQA, 2WikiMultihopQA, MuSiQue, and DiaASQ. The framework achieves an average gain of 4% in factual correctness as measured by LLM-as-a-Judge across four benchmarks, indicating a reduction in hallucination rates and an increase in precision. Notably, the use of graph traversal algorithms yields an average improvement of 6% over standard flatten retrievers. Furthermore, the search plan enhancement mechanism contributes an 18% boost in performance when enabled. An ablation study reveals that PAI-2 achieves a state-of-the-art (SOTA) information-retention score of 89% on the MINE-1 benchmark.

**Limitations**  
The authors acknowledge that while PAI-2 shows promising results, it is still a preprint and has not undergone peer review. They do not discuss potential scalability issues or the computational overhead introduced by the multistage query processing pipeline. Additionally, the reliance on LLMs in the 7-14 billion parameter range may limit accessibility for smaller-scale applications. The generalizability of the results across diverse domains and languages is also not addressed.

**Why it matters**  
The implications of PAI-2 are significant for the development of next-generation personalized AI systems. By enhancing the integration of KGs with LLMs, the framework paves the way for more context-aware and scalable AI applications. The ability to reduce hallucination rates and improve factual correctness is critical for applications in domains such as customer support, education, and content generation, where accuracy is paramount. PAI-2's architecture and methodologies could serve as a foundational model for future research in personalized AI, particularly in the context of knowledge-driven applications.

Authors: Mikhail Menschikov, Matvey Iskornev, Alexander Kharitonov, Alina Bogdanova, Mikhail Belkin, Ekaterina Lisitsyna, Artyom Sosedka, Victoria Dochkina et al.  
Source: arXiv:2605.13481  
URL: https://arxiv.org/abs/2605.13481v1
