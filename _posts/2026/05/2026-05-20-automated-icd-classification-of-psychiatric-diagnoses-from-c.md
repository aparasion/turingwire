---
title: "Automated ICD Classification of Psychiatric Diagnoses: From Classical NLP to Large Language Models"
date: 2026-05-20 13:26:05 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21154v1"
arxiv_id: "2605.21154"
authors: ["Fernando Ortega", "Ra\u00fal Lara-Cabrera", "Jorge Due\u00f1as-Ler\u00edn", "Alejandro de la Torre-Luque", "Merc\u00e9 Salvador Robert", "Enrique Baca-Garc\u00eda"]
slug: automated-icd-classification-of-psychiatric-diagnoses-from-c
summary_word_count: 398
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in automated classification of psychiatric diagnoses using Natural Language Processing (NLP) techniques, specifically focusing on the mapping of free-text clinical descriptions to the International Classification of Diseases (ICD). The authors highlight the administrative burden faced by mental health professionals due to manual coding processes and the inadequacy of existing methods to handle the complexity and ambiguity inherent in psychiatric language. 

**Method**  
The study employs a specialized dataset comprising 145,513 Spanish psychiatric descriptions. It evaluates various text representation paradigms, including classical frequency-based models such as Bag-of-Words (BoW) and Term Frequency-Inverse Document Frequency (TF-IDF), alongside advanced transformer-based models like e5_large, BioLORD, and Llama-3-8B. The authors fine-tune the e5_large model end-to-end, optimizing it for the specific clinical nomenclature associated with psychiatric diagnoses. The training process and compute resources are not explicitly disclosed, but the focus on LLMs indicates a significant computational investment typical of such models.

**Results**  
The e5_large model achieved the highest performance with a micro F1 score of 0.866, outperforming traditional methods and other evaluated LLMs. The results demonstrate that transformer-based embeddings effectively capture implicit semantic cues and the nuanced medical terminology necessary for accurate classification. The study provides a clear performance benchmark against classical NLP methods, illustrating the substantial improvements in classification accuracy when utilizing state-of-the-art LLMs.

**Limitations**  
The authors acknowledge several limitations, including the potential biases in the dataset, which may affect generalizability to other languages or cultural contexts. They also note the challenge of "long-tail" label distributions, where certain diagnoses may be underrepresented, complicating model training. Additionally, the reliance on fine-tuning LLMs may require significant computational resources, which could limit accessibility for smaller institutions. The study does not address the interpretability of the model's decisions, which is critical in clinical settings.

**Why it matters**  
This research has significant implications for the automation of psychiatric diagnosis coding, potentially reducing the administrative burden on mental health professionals and improving the accuracy of diagnostic classification. By demonstrating the effectiveness of LLMs in this domain, the study paves the way for further exploration of NLP applications in healthcare, particularly in areas where language complexity and ambiguity are prevalent. The findings encourage future work on adapting LLMs to other medical specialties and highlight the importance of addressing dataset biases and interpretability in clinical AI applications.

Authors: Fernando Ortega, Raúl Lara-Cabrera, Jorge Dueñas-Lerín, Alejandro de la Torre-Luque, Mercé Salvador Robert, Enrique Baca-García  
Source: arXiv:2605.21154  
URL: https://arxiv.org/abs/2605.21154v1
