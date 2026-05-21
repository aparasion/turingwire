---
title: "Findings of the Fifth Shared Task on Multilingual Coreference Resolution: Expanding Datasets for Long-Range Entities"
date: 2026-05-20 16:35:09 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21369v1"
arxiv_id: "2605.21369"
authors: ["Michal Nov\u00e1k", "Miloslav Konop\u00edk", "Anna Nedoluzhko", "Martin Popel", "Ond\u0159ej Pra\u017e\u00e1k", "Jakub Sido"]
slug: findings-of-the-fifth-shared-task-on-multilingual-coreferenc
summary_word_count: 438
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations in multilingual coreference resolution (MCR) systems, particularly in handling long-range entities—coreferential chains that span significant distances across sentences. The fifth iteration of the Shared Task on MCR, held at the CODI-CRAC 2026 workshop, expands the existing literature by introducing five new datasets and two additional languages, thereby enhancing the linguistic diversity and complexity of the task. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution involves the organization of a competitive task that requires participants to develop systems for mention identification and identity-based coreference clustering. The task utilizes version 1.4 of CorefUD, a harmonized multilingual dataset comprising 27 datasets across 19 languages. Ten systems participated, including four based on large language models (LLMs): three fine-tuned models and one few-shot model. The evaluation metrics and methodologies for assessing coreference resolution performance are not explicitly detailed in the abstract, but the focus on long-range entities suggests a need for robust contextual understanding and memory mechanisms in the models employed.

**Results**  
While specific performance metrics are not disclosed in the abstract, the paper indicates that traditional systems maintained a performance lead over LLM-based approaches. However, LLMs exhibited significant potential, hinting at their capability to challenge established methodologies in future iterations of the task. The results suggest that the integration of long-range entity handling in MCR is an area where LLMs could improve, although exact effect sizes and comparisons to baseline models are not provided.

**Limitations**  
The authors acknowledge the challenge of evaluating long-range coreference resolution, which may not be fully captured by existing metrics. They also note that while LLMs show promise, their performance is still behind traditional systems, indicating a gap in their ability to generalize across diverse linguistic contexts. An additional limitation not explicitly mentioned is the potential overfitting of LLMs to the training datasets, which could hinder their performance on unseen data or in real-world applications.

**Why it matters**  
This work has significant implications for the development of multilingual natural language processing systems, particularly in enhancing the understanding of coreference resolution in complex linguistic scenarios. The introduction of new datasets and the focus on long-range entities could pave the way for more sophisticated models that better capture the nuances of human language. As LLMs continue to evolve, their integration into coreference resolution tasks may lead to breakthroughs that improve the accuracy and applicability of multilingual systems in various downstream applications, such as machine translation, information extraction, and conversational agents.

Authors: Michal Novák, Miloslav Konopík, Anna Nedoluzhko, Martin Popel, Ondřej Pražák, Jakub Sido, Milan Straka, Zdeněk Žabokrtský et al.  
Source: arXiv:2605.21369  
URL: [https://arxiv.org/abs/2605.21369v1](https://arxiv.org/abs/2605.21369v1)
