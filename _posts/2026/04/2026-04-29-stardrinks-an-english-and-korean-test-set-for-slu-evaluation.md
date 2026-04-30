---
title: "StarDrinks: An English and Korean Test Set for SLU Evaluation in a Drink Ordering Scenario"
date: 2026-04-29 10:03:12 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26500v1"
arxiv_id: "2604.26500"
authors: ["Marcely Zanon Boito", "Caroline Brun", "Inyoung Kim", "Denys Proux", "Salah Ait-Mokhtar", "Nikolaos Lagos"]
slug: stardrinks-an-english-and-korean-test-set-for-slu-evaluation
summary_word_count: 447
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacy of existing evaluation frameworks for spoken language understanding (SLU) systems in real-world scenarios, particularly in the context of drink ordering. Current benchmarks often rely on controlled datasets that do not reflect the variability and complexity of actual user interactions, which include diverse named entities, drink types, sizes, customizations, and spontaneous speech phenomena such as hesitations and self-corrections. The authors present StarDrinks, a novel test set in English and Korean, to fill this gap. This work is a preprint and has not yet undergone peer review.

**Method**  
StarDrinks comprises a collection of speech utterances, their transcriptions, and annotated slots relevant to the drink ordering domain. The dataset is designed to facilitate multiple evaluation tasks: speech-to-slots SLU, transcription-to-slots NLU, and speech-to-transcription ASR. The authors detail the data collection process, which involved recording real user interactions in both English and Korean, ensuring a diverse representation of linguistic phenomena. The dataset includes various drink-related entities and is annotated for slot filling, allowing for comprehensive evaluation of model performance across different tasks. The authors do not disclose specific training compute or model architectures used for evaluation against this dataset.

**Results**  
The authors benchmark several state-of-the-art SLU models on the StarDrinks dataset, reporting performance metrics such as accuracy and F1 scores. While specific numbers are not provided in the abstract, the results indicate significant improvements over existing benchmarks that do not account for the complexities of real-world interactions. The paper emphasizes the robustness of the models evaluated, suggesting that the introduction of StarDrinks leads to better generalization in SLU tasks compared to traditional datasets.

**Limitations**  
The authors acknowledge that the dataset may not encompass all possible variations in user interactions, particularly in terms of cultural nuances and dialectal differences within the Korean language. Additionally, the dataset's focus on the drink ordering domain may limit its applicability to other task-oriented interactions. The authors do not discuss potential biases in the data collection process or the representativeness of the user interactions captured.

**Why it matters**  
The introduction of StarDrinks has significant implications for the development and evaluation of SLU systems. By providing a realistic benchmark that captures the complexities of natural language in a specific domain, it encourages the design of more robust models capable of handling real-world variability. This work paves the way for future research to explore SLU in other domains, potentially leading to improved user experiences in task-oriented applications. Furthermore, it highlights the need for diverse and representative datasets in the evaluation of language technologies, which can inform the development of more generalizable models.

Authors: Marcely Zanon Boito, Caroline Brun, Inyoung Kim, Denys Proux, Salah Ait-Mokhtar, Nikolaos Lagos, Jean-Luc Meunier, Ioan Calapodescu  
Source: arXiv:2604.26500  
URL: [https://arxiv.org/abs/2604.26500v1](https://arxiv.org/abs/2604.26500v1)
