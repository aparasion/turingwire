---
title: "Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora"
date: 2026-05-21 16:02:15 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.22660v1"
arxiv_id: "2605.22660"
authors: ["Maciej Skorski"]
slug: moral-semantics-survive-machine-translation-cross-lingual-ev
summary_word_count: 460
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of translating moral language across languages, particularly in the context of automated moral values classification, which predominantly relies on English-language corpora. The authors highlight the difficulty of faithfully translating idiomatic expressions, slang, and culturally specific references, which can introduce artifacts that obscure the underlying moral semantics. The study specifically investigates whether large language model (LLM)-based translation can effectively bridge this gap, using Polish as a case study.

**Method**  
The authors employ a comprehensive four-method validation pipeline to assess the efficacy of LLM-based translations in preserving moral semantics. The methods include:  
1. **LaBSE Cross-Lingual Embedding Similarity**: This method evaluates the semantic similarity of translated texts using embeddings from the LaBSE model.
2. **Centered Kernel Alignment (CKA)**: CKA is used to measure the alignment of representations between the original and translated texts, providing insights into how well moral cues are preserved.
3. **LLM-as-Judge Evaluation**: This involves using an LLM to assess the moral alignment of the translated texts against the original.
4. **Deep Learning Classifier Parity Tests**: A classifier is trained on the original English data and tested on the translated Polish data to evaluate performance consistency.

The dataset comprises approximately 50,000 morally-annotated social media posts across diverse topics. The authors report mean cosine similarity scores of 0.86 and AUC gaps of 0.01–0.02, indicating that fine-tuning language models further enhances the preservation of moral semantics in translations.

**Results**  
The study demonstrates that LLM-based translations can effectively maintain moral cues, achieving a mean cosine similarity of 0.86 when comparing original and translated texts. The AUC gaps of 0.01–0.02 suggest that the performance of classifiers trained on English data remains robust when applied to Polish translations, particularly after fine-tuning. These results indicate that machine translation can serve as a viable method for moral values research in under-resourced languages, with implications for broader applications in related Slavic languages.

**Limitations**  
The authors acknowledge several limitations, including the challenges posed by slang, vulgarity, and culturally-loaded expressions that may not translate well. They also note that their findings are based on a single language pair (English-Polish), which may limit generalizability to other languages with different linguistic structures or cultural contexts. Additionally, the reliance on LLMs for translation raises concerns about potential biases inherent in the models used.

**Why it matters**  
This research has significant implications for the field of moral values classification, particularly in expanding the accessibility of such research to languages that lack extensive annotated corpora. By demonstrating that machine translation can effectively preserve moral semantics, the study opens avenues for cross-lingual moral psychology research and the development of multilingual moral classifiers. This work could facilitate a more inclusive understanding of moral values across diverse cultures, ultimately enriching the field of computational social science.

Authors: Maciej Skorski  
Source: arXiv:2605.22660  
URL: https://arxiv.org/abs/2605.22660v1
