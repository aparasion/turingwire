---
title: "CommunityFact: A Dynamic, Multilingual, Multi-domain Benchmark for Misinformation Detection in the Wild"
date: 2026-05-28 17:09:19 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.30241v1"
arxiv_id: "2605.30241"
authors: ["Sahajpreet Singh", "Insyirah Mujtahid", "Min-Yen Kan", "Kokil Jaidka"]
slug: communityfact-a-dynamic-multilingual-multi-domain-benchmark-
summary_word_count: 413
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacy of static benchmarks for misinformation detection in dynamic, multilingual, and multi-domain online environments. Existing benchmarks fail to capture the complexities and variability of real-world misinformation, particularly in fast-paced settings. The authors present CommunityFact, a refreshable benchmark designed to evaluate misinformation detection models in a more representative manner. This work is a preprint and has not yet undergone peer review.

**Method**  
CommunityFact comprises 15,992 standalone claims across five languages and two domains, focusing on coverage, granularity, and redistributability. The authors evaluate ten large language models (LLMs) under various inference-time capabilities, including reasoning and web-search functionalities. The evaluation methodology includes assessing the models' performance in closed-input verification scenarios and their ability to leverage web access for improved accuracy. The authors also explore model-specific mechanisms for retrieval expansion and pruning to align LLMs' source-selection policies with those of human raters from Community Notes, a crowdsourced annotation platform.

**Results**  
The findings indicate that closed-input verification remains a significant challenge, with web access providing the most substantial performance improvements. Specifically, web-enabled LLMs demonstrated a marked increase in accuracy when retrieving information from the web, although their source-selection policies often diverged from those preferred by human raters. The authors report that the gap in alignment can be mitigated through tailored retrieval strategies. Additionally, the results reveal considerable performance variation across different language-domain slices and the evidence ecosystems utilized by web-enabled systems. The paper provides quantitative metrics, although specific numerical results are not detailed in the abstract.

**Limitations**  
The authors acknowledge several limitations, including the potential biases in the Community Notes annotations and the variability in model performance across different languages and domains. They also note that the benchmark's refreshability may introduce challenges in maintaining consistency over time. An additional limitation not explicitly mentioned is the reliance on web access, which may not be feasible in all operational contexts, potentially skewing the evaluation of models that cannot utilize real-time web data.

**Why it matters**  
CommunityFact has significant implications for the field of misinformation detection, as it provides a more realistic and dynamic framework for evaluating model performance. By integrating Community Notes as a training signal, the benchmark opens avenues for developing claim-conditioned source suggesters, which could enhance the factual verification process for novel claims. This work encourages further exploration of multilingual and multi-domain approaches in misinformation detection, ultimately contributing to more robust and reliable systems in combating misinformation in real-world scenarios.

Authors: Sahajpreet Singh, Insyirah Mujtahid, Min-Yen Kan, Kokil Jaidka  
Source: arXiv:2605.30241  
URL: [https://arxiv.org/abs/2605.30241v1](https://arxiv.org/abs/2605.30241v1)
