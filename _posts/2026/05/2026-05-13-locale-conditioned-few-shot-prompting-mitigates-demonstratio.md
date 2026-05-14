---
title: "Locale-Conditioned Few-Shot Prompting Mitigates Demonstration Regurgitation in On-Device PII Substitution with Small Language Models"
date: 2026-05-13 13:47:11 +0000
category: research
subcategory: efficiency_inference
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13538v1"
arxiv_id: "2605.13538"
authors: ["Anuj Sadani", "Deepak Kumar"]
slug: locale-conditioned-few-shot-prompting-mitigates-demonstratio
summary_word_count: 494
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of Personally Identifiable Information (PII) redaction, which typically involves replacing sensitive entities with placeholder tokens, thereby diminishing the utility of the text for downstream tasks such as retrieval and Named Entity Recognition (NER). The authors identify a gap in existing methods that fail to provide consistent, type-preserving substitutes for PII while maintaining the integrity of the text for further processing. The paper specifically tackles the issue of demonstration regurgitation in small language models (SLMs) when tasked with generating contextual surrogates for PII.

**Method**  
The proposed solution is a fully on-device pipeline that integrates three components: a 1.5 billion parameter mixture-of-experts token classifier (openai/privacy-filter) for detecting PII spans, a 1-bit Bonsai-1.7B SLM for generating contextual surrogates, and a rule-based generator (faker) for handling patterned fields. A critical technical contribution is the introduction of locale-conditioned rotating few-shot demonstrations, which utilize a character-range heuristic to select a locale-pure pool and an MD5 hash to sample three demonstrations per input. This approach mitigates the issue of verbatim regurgitation observed with naive fixed three-shot demonstrations. The authors report that with this method, all 482 unique calls to the Bonsai-1.7B SLM succeed without echoing previous outputs, although some residual copying from a limited same-locale demonstration pool remains.

**Results**  
The authors evaluate their method on a multilingual corpus of 2000 documents, where the hybrid perplexity (PPL) of the proposed approach outperforms the faker baseline across all six locales under a multilingual evaluator (XGLM-564M). Specifically, the length preservation metric is best-of-three in four out of six locales. In downstream NER tasks, the performance metrics reveal stark contrasts: the naive redact method yields an F1 score of 0.000, while faker achieves 0.656, and the original text scores 0.960. In a matched subset of 160/40 documents, faker (F1=0.506) outperforms the hybrid method (F1=0.346) with statistical significance (p < 0.001). The authors interpret this as an honest negative finding, indicating that while SLM surrogates produce more natural text, they result in a less varied training distribution, which is detrimental to downstream NER performance.

**Limitations**  
The authors acknowledge that the SLM still exhibits a tendency to copy from a small same-locale demonstration pool, indicating a residual narrowness in the generated outputs. They also note that while their method improves upon previous approaches, the trade-off between naturalness and variety in the training distribution remains a critical concern. Additionally, the reliance on locale-conditioned demonstrations may limit generalizability across diverse datasets.

**Why it matters**  
This work has significant implications for the development of on-device privacy-preserving systems that require effective PII redaction without sacrificing downstream utility. By addressing the limitations of existing methods and introducing a novel prompting strategy, the authors pave the way for more robust applications in sensitive data handling, particularly in multilingual contexts. The findings underscore the importance of balancing naturalness and diversity in training data for enhancing NER performance, which could influence future research directions in language model training and evaluation.

Authors: Anuj Sadani, Deepak Kumar  
Source: arXiv:2605.13538  
URL: https://arxiv.org/abs/2605.13538v1
