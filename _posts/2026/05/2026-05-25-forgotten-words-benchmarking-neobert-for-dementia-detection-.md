---
title: "Forgotten Words: Benchmarking NeoBERT for Dementia Detection in Low-Resource Conversational Filipino and English Speech"
date: 2026-05-25 16:26:15 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.26007v1"
arxiv_id: "2605.26007"
authors: ["Rez Samantha Z. Floresca", "Edric Castel C. Hao", "Hannah Grachiella Bu\u00f1ales", "Chelsea Dominique E. Temprosa", "Georgianna Z. Reyes", "Kervin Gabriel L. Chua"]
slug: forgotten-words-benchmarking-neobert-for-dementia-detection-
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in NLP capabilities for dementia detection in low-resource languages, specifically Filipino, which has not been previously explored in the context of spontaneous speech. The authors highlight the predominance of English-centric models in existing literature and the lack of tools for effective cognitive screening in bilingual contexts, particularly in the Philippines where code-switching between Filipino and English is common. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors introduce a systematic evaluation of the NeoBERT architecture for dementia detection, utilizing a parallel bilingual dataset comprising 4,000 DementiaBank-derived transcripts. The dataset includes manually translated Filipino transcripts to maintain discourse-level markers indicative of cognitive decline. The study evaluates five model families: TF-IDF + Logistic Regression, BERT, NeoBERT, XLM-R, and RoBERTa-Tagalog, across three settings: monolingual, zero-shot cross-lingual, and bilingual fine-tuning. The key technical contribution is the demonstration that bilingual fine-tuning significantly mitigates cross-lingual performance degradation, achieving robust results across all transformer models.

**Results**  
The findings reveal that English-trained BERT exhibits a substantial drop in performance when applied to Filipino, achieving a Macro-F1 score of 0.455. In contrast, bilingual fine-tuning leads to a remarkable improvement, with Macro-F1 scores ranging from 0.969 to 0.973 across the evaluated transformer models. This indicates that the performance of multilingual clinical NLP systems is more influenced by linguistic coverage during training than by the scale or architecture of the models themselves. The results suggest that effective dementia detection can be achieved in low-resource languages through appropriate training strategies.

**Limitations**  
The authors acknowledge that their study is limited by the size and scope of the dataset, which, while substantial, may not encompass the full linguistic diversity of Filipino speech. Additionally, the reliance on manually translated transcripts may introduce biases or inaccuracies in discourse-level markers. The paper does not address potential overfitting in the bilingual fine-tuning process or the generalizability of the findings to other low-resource languages or dialects.

**Why it matters**  
This research has significant implications for the development of NLP tools in clinical settings, particularly in multilingual and low-resource contexts. By demonstrating the effectiveness of bilingual fine-tuning, the study paves the way for future work in cognitive screening and dementia detection across diverse linguistic backgrounds. It highlights the necessity of incorporating linguistic diversity in training datasets to enhance the robustness of NLP models, ultimately contributing to more inclusive healthcare solutions.

Authors: Rez Samantha Z. Floresca, Edric Castel C. Hao, Hannah Grachiella Buñales, Chelsea Dominique E. Temprosa, Georgianna Z. Reyes, Kervin Gabriel L. Chua  
Source: arXiv cs.CL  
URL: [https://arxiv.org/abs/2605.26007v1](https://arxiv.org/abs/2605.26007v1)  
arXiv ID: 2605.26007
