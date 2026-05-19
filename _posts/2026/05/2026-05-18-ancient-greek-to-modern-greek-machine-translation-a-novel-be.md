---
title: "Ancient Greek to Modern Greek Machine Translation: A Novel Benchmark and Fine-Tuning Experiments on LLMs and NMT Models"
date: 2026-05-18 14:56:44 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18504v1"
arxiv_id: "2605.18504"
authors: ["Spyridon Mavromatis", "Sokratis Sofianopoulos", "Prokopis Prokopidis", "Maria Giagkou"]
slug: ancient-greek-to-modern-greek-machine-translation-a-novel-be
summary_word_count: 409
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of resources and benchmarks for Machine Translation (MT) from Ancient Greek (AG) to Modern Greek (MG), a low-resource language pair. The authors introduce the AG-MG Parallel Corpus, which contains 132,481 sentence-aligned pairs derived from various literary, historical, and biblical texts. This work is presented as a preprint and has not yet undergone peer review, highlighting the need for further validation in the community.

**Method**  
The authors propose a novel corpus creation pipeline that integrates web-scraped data with a multi-stage sentence-level alignment and refinement process. The alignment utilizes VecAlign with LaBSE embeddings, which are fine-tuned on a manually-aligned AG-MG subset. Following this, an LLM-based error correction phase is conducted using Gemini 2.5 Flash to enhance alignment quality. The paper benchmarks several fine-tuning strategies across Neural Machine Translation (NMT) models, specifically NLLB and M2M100, as well as a Greek LLM, Llama-Krikri-8B. The fine-tuning strategies include full-parameter tuning and QLoRA adaptation, which are evaluated for their effectiveness in improving translation performance.

**Results**  
The experiments demonstrate that fine-tuning significantly enhances model performance, with improvements of up to +10.3 BLEU points over base models. The Llama-Krikri-8B model, when fully fine-tuned, achieves the highest BLEU score of 13.16. In contrast, the QLoRA-adapted M2M100-1.2B model exhibits the largest relative gains, showcasing competitive results in the context of the new benchmark. These results indicate that the proposed methods and dataset can substantially advance the state of AG-MG translation.

**Limitations**  
The authors acknowledge that the AG-MG Parallel Corpus, while extensive, is still limited by the inherent challenges of low-resource languages, including potential biases in the source texts and the representativeness of the dataset. Additionally, the reliance on web-scraped data may introduce noise or misalignments that could affect translation quality. The paper does not address the scalability of the proposed methods to other low-resource language pairs or the generalizability of the findings beyond the specific models tested.

**Why it matters**  
This work significantly contributes to the field of Greek Natural Language Processing (NLP) by providing a foundational dataset and benchmarking framework for AG-MG translation. The introduction of the AG-MG Parallel Corpus and the evaluation of modern MT models on this task can catalyze further research in low-resource language translation, potentially inspiring similar efforts for other underrepresented languages. The findings underscore the importance of fine-tuning strategies in enhancing model performance, which could inform future work in multilingual and low-resource MT systems.

Authors: Spyridon Mavromatis, Sokratis Sofianopoulos, Prokopis Prokopidis, Maria Giagkou  
Source: arXiv:2605.18504  
URL: [https://arxiv.org/abs/2605.18504v1](https://arxiv.org/abs/2605.18504v1)
