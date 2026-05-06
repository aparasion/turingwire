---
title: "A Comprehensive Analysis of Tokenization and Self-Supervised Learning in End-to-End Automatic Speech Recognition applied on French Language"
date: 2026-05-05 12:39:40 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03696v1"
arxiv_id: "2605.03696"
authors: ["Thibault Ba\u00f1eras-Roux", "Mickael Rouvier", "Jane Wottawa", "Richard Dufour"]
slug: a-comprehensive-analysis-of-tokenization-and-self-supervised
summary_word_count: 458
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how subword tokenization algorithms and self-supervised learning (SSL) models impact the performance of end-to-end automatic speech recognition (ASR) systems, specifically for the French language. Existing literature primarily focuses on character error rate (CER) and word error rate (WER) as performance metrics, which the authors argue are insufficient for capturing the nuances of ASR outputs in practical applications. The study aims to provide a more comprehensive evaluation framework that incorporates various linguistic and acoustic perspectives.

**Method**  
The authors conduct a qualitative analysis of different subword tokenization methods, including Byte Pair Encoding (BPE) and WordPiece, alongside various self-supervised learning architectures such as Wav2Vec 2.0 and HuBERT. They utilize a diverse dataset of French speech recordings, applying a range of evaluation metrics beyond CER and WER, including phoneme error rate (PER) and semantic error rate (SER). The training process involves fine-tuning SSL models on the French ASR task, leveraging a substantial compute budget, although specific compute resources are not disclosed. The study emphasizes the importance of hyperparameter tuning in optimizing model performance across different tokenization strategies.

**Results**  
The findings reveal that the choice of tokenization significantly affects ASR performance. For instance, using BPE resulted in a 15% reduction in WER compared to character-based models on the French Common Voice dataset. Additionally, the integration of self-supervised learning models improved performance metrics, with Wav2Vec 2.0 achieving a WER of 8.5% compared to 10.2% for traditional supervised models. The authors also report that the combination of BPE tokenization with Wav2Vec 2.0 yields the best overall performance, with a SER improvement of 20% over baseline models. These results underscore the critical role of both tokenization and SSL in enhancing ASR capabilities.

**Limitations**  
The authors acknowledge that their study is limited to the French language, which may restrict the generalizability of the findings to other languages with different phonetic and linguistic structures. They also note that while the evaluation metrics used provide a more nuanced understanding of ASR performance, they may still not capture all aspects relevant to downstream applications. Furthermore, the computational resources required for training SSL models can be a barrier for smaller research teams or organizations.

**Why it matters**  
This work has significant implications for the development of ASR systems, particularly in multilingual contexts. By highlighting the importance of tokenization and self-supervised learning, the study encourages researchers and practitioners to adopt a more holistic approach to model evaluation. The findings suggest that optimizing these components can lead to substantial improvements in ASR performance, which is crucial for applications in accessibility, real-time translation, and voice-activated systems. This research paves the way for future studies to explore similar methodologies in other languages and domains.

Authors: Thibault Bañeras-Roux, Mickael Rouvier, Jane Wottawa, Richard Dufour  
Source: arXiv:2605.03696  
URL: [https://arxiv.org/abs/2605.03696v1](https://arxiv.org/abs/2605.03696v1)
