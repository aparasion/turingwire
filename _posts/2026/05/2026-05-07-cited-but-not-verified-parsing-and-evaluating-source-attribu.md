---
title: "Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents"
date: 2026-05-07 17:46:45 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.06635v1"
arxiv_id: "2605.06635"
authors: ["Hailey Onweller", "Elias Lumer", "Austin Huber", "Pia Ramchandani", "Vamse Kumar Subbiah", "Corey Feld"]
slug: cited-but-not-verified-parsing-and-evaluating-source-attribu
summary_word_count: 440
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the capability of large language models (LLMs) to provide verifiable citations in generated reports. Current methodologies either rely on LLMs to self-cite accurately, which can introduce bias, or utilize retrieval-augmented generation (RAG) techniques that fail to validate the accessibility, relevance, or factual consistency of sources. The authors propose a novel framework for evaluating source attribution in LLM-generated content, which is essential for ensuring the reliability of information synthesized by deep research agents.

**Method**  
The authors introduce a reproducible Abstract Syntax Tree (AST) parser that extracts inline citations from LLM-generated Markdown reports. The framework evaluates citations across three dimensions: (1) **Link Works** for URL accessibility, (2) **Relevant Content** for topical alignment, and (3) **Fact Check** for factual accuracy against the source content. The evaluation employs rubric-based LLM-as-a-judge evaluators, which are calibrated through human review, allowing for a systematic assessment of citation quality. The authors benchmark 14 LLMs, both closed-source and open-source, across these dimensions, providing a comprehensive analysis of citation performance.

**Results**  
The findings indicate that the best-performing models maintain link validity at over 94% and relevance at above 80%. However, factual accuracy is significantly lower, ranging from 39% to 77%. Notably, fewer than 50% of open-source models successfully generate cited reports in a one-shot setting. Ablation studies reveal that as the number of retrieval tool calls increases from 2 to 150, Fact Check accuracy declines by approximately 42% on average across two leading models. This suggests that increased retrieval does not correlate with improved citation accuracy, highlighting a critical disconnect between citation quality and factual reliability.

**Limitations**  
The authors acknowledge that their framework is limited to the evaluation of citations in Markdown reports and may not generalize to other formats. Additionally, the reliance on LLMs for evaluating citations introduces potential biases, as the evaluators themselves are models that may inherit the same inaccuracies present in the source material. The study also does not address the implications of citation context or the potential for misinterpretation of sources by LLMs.

**Why it matters**  
This work has significant implications for the development of reliable LLMs in research contexts. By providing a structured evaluation framework, it enables researchers to better understand the limitations of LLM-generated citations and fosters improvements in citation accuracy. The findings underscore the necessity for enhanced verification mechanisms in LLMs, which could lead to more trustworthy outputs in academic and professional settings. This research paves the way for future studies aimed at refining citation practices in AI-generated content, ultimately contributing to the integrity of information dissemination.

Authors: Hailey Onweller, Elias Lumer, Austin Huber, Pia Ramchandani, Vamse Kumar Subbiah, Corey Feld  
Source: arXiv:2605.06635  
URL: [https://arxiv.org/abs/2605.06635v1](https://arxiv.org/abs/2605.06635v1)
