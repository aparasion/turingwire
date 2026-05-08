---
title: "From 124 Million Tokens to 1,021 Neologisms: A Large-Scale Pipeline for Automatic Neologism Detection"
date: 2026-05-07 15:32:56 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.06426v1"
arxiv_id: "2605.06426"
authors: ["Diego Rossini", "Lonneke van der Plas"]
slug: from-124-million-tokens-to-1021-neologisms-a-large-scale-pip
summary_word_count: 412
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in automated neologism detection within natural language processing (NLP). Existing methods often lack scalability and modularity, limiting their applicability to large corpora. The authors propose a comprehensive pipeline that integrates rule-based filtering with large language model (LLM) classification to systematically identify neologisms in extensive datasets, specifically targeting the nuances of word formation through grammatical and extra-grammatical morphology.

**Method**  
The proposed pipeline is modular and designed for scalability, leveraging a combination of rule-based approaches and LLMs for classification. It operates on a dataset of 527 million English-language Reddit posts from 2005 to 2024, from which 124.6 million unique tokens are extracted. The pipeline employs a four-class classification scheme: neologism, entity, foreign, and none. Each candidate neologism is classified by multiple LLMs, with a majority voting mechanism to determine the final classification. The architecture allows for easy adaptation to different datasets and linguistic contexts. The authors also emphasize the importance of manual verification, which is conducted on the final set of candidates.

**Results**  
The pipeline successfully reduces the initial token set by over 99.99%, yielding 1,021 neologism candidates. Manual annotation of these candidates reveals that 599 (58.7%) are confirmed as genuine lexical innovations. The study highlights significant cross-model disagreement in LLM classifications, indicating the complexity of neologism detection. The results demonstrate the effectiveness of the pipeline in identifying neologisms at scale, although specific performance metrics (e.g., precision, recall) against baseline models are not provided.

**Limitations**  
The authors acknowledge the challenge of operationalizing neologism detection due to the inherent variability in language and the subjective nature of neologism classification. They note that the reliance on LLMs introduces variability in classification outcomes, as evidenced by the cross-model disagreement. Additionally, the manual verification process, while thorough, is limited to a small subset of candidates, which may not fully represent the broader linguistic landscape. The authors do not address potential biases in the Reddit dataset or the implications of using a single social media platform for neologism detection.

**Why it matters**  
This work has significant implications for downstream applications in NLP, particularly in the areas of language evolution, lexicography, and sociolinguistics. By providing a scalable and modular framework for neologism detection, the authors pave the way for further research into lexical innovation and its impact on language models. The availability of the pipeline code and annotated datasets facilitates reproducibility and encourages further exploration of neologism detection methodologies across diverse linguistic corpora.

Authors: Diego Rossini, Lonneke van der Plas  
Source: arXiv:2605.06426  
URL: https://arxiv.org/abs/2605.06426v1
