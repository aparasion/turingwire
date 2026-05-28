---
title: "Can Large Language Models Handle Discourse Particles? A Case Study of Colloquial Malay"
date: 2026-05-27 17:42:52 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.28782v1"
arxiv_id: "2605.28782"
authors: ["Mariah Al Giptiah Binte Yusoff", "Jakin Tan", "Bocheng Chen", "Guangliang Liu", "Xi Chen"]
slug: can-large-language-models-handle-discourse-particles-a-case-
summary_word_count: 440
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the understanding of large language models (LLMs) regarding their handling of discourse particles, particularly in colloquial Malay. While discourse particles are essential for conveying emotions and intentions in human communication, existing literature predominantly focuses on high-resource languages like English, leaving a void in the analysis of LLMs' capabilities in low-resource languages. The authors aim to fill this gap by proposing a systematic evaluation framework for LLMs in the context of Malay.

**Method**  
The authors introduce \textsc{MalayPrag}, a benchmark specifically designed to evaluate LLMs' performance in processing discourse particles in colloquial Malay. This benchmark is underpinned by five linguistically grounded attributes that categorize the pragmatic functions of discourse particles. The study involves prompting ten off-the-shelf LLMs to perform three distinct prediction tasks related to these discourse particles. The tasks are designed to assess the models' ability to connect discourse particles with their intended pragmatic meanings. The training compute and specific architectures of the LLMs are not disclosed, but the focus is on evaluating existing models rather than training new ones.

**Results**  
The experimental results indicate that current LLMs struggle significantly with accurately associating discourse particles with their pragmatic functions in Malay. The introduction of the five attributes from the \textsc{MalayPrag} benchmark markedly enhances the models' performance, suggesting that structured scaffolding is crucial for improving pragmatic competence. While specific numerical results are not provided in the abstract, the authors emphasize the substantial challenges faced by the models, implying a notable effect size in the performance improvement when using the proposed attributes.

**Limitations**  
The authors acknowledge that their study is limited to colloquial Malay and may not generalize to other languages or dialects. Additionally, the reliance on off-the-shelf LLMs means that the findings may not reflect the capabilities of models specifically fine-tuned for Malay discourse. The study does not explore the underlying reasons for the models' shortcomings, nor does it provide a comprehensive analysis of the linguistic diversity within Malay itself. Furthermore, the benchmark's effectiveness in other Southeast Asian languages remains untested.

**Why it matters**  
This work has significant implications for the development of LLMs in low-resource languages, particularly in enhancing their pragmatic understanding. By establishing a benchmark and a framework for discourse particles, the study paves the way for future research aimed at improving LLMs' performance in understanding nuanced human communication. The findings highlight the necessity for structured approaches in training models to handle pragmatic aspects of language, which could inform the design of more sophisticated LLMs capable of engaging in human-like discourse across diverse languages.

Authors: Mariah Al Giptiah Binte Yusoff, Jakin Tan, Bocheng Chen, Guangliang Liu, Xi Chen  
Source: arXiv:2605.28782  
URL: [https://arxiv.org/abs/2605.28782v1](https://arxiv.org/abs/2605.28782v1)
