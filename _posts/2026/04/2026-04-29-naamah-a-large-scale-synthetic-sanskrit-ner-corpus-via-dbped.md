---
title: "Naamah: A Large Scale Synthetic Sanskrit NER Corpus via DBpedia Seeding and LLM Generation"
date: 2026-04-29 09:12:57 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26456v1"
arxiv_id: "2604.26456"
authors: ["Akhil Rajeev P", "Annarao Kulkarni"]
slug: naamah-a-large-scale-synthetic-sanskrit-ner-corpus-via-dbped
summary_word_count: 420
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the critical gap in annotated resources for Named Entity Recognition (NER) in classical Sanskrit literature, which hampers digitization efforts. The authors highlight the limitations of existing methodologies that leverage generic Large Language Models (LLMs) for data augmentation, noting their susceptibility to errors and insufficient reasoning capabilities for classical grammar. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors introduce Naamah, a synthetic NER dataset comprising 102,942 sentences, generated through a novel methodology that integrates entity extraction from DBpedia with a 24 billion parameter hybrid reasoning model. This model is designed to produce grammatically coherent and syntactically diverse training data. The dataset serves as a benchmark for evaluating two transformer architectures: the large multilingual XLM-RoBERTa and the more parameter-efficient IndicBERTv2. The training process and specific loss functions are not detailed in the abstract, but the focus on leveraging a hybrid reasoning model suggests an emphasis on enhancing contextual understanding in the generated data.

**Results**  
The authors benchmark the performance of XLM-RoBERTa and IndicBERTv2 on the Naamah dataset, reporting significant improvements in NER accuracy compared to baseline models. While specific numerical results are not provided in the abstract, the implication is that the proposed dataset and methodologies yield superior performance metrics, likely surpassing existing benchmarks in Sanskrit NER tasks. The effectiveness of the dataset is underscored by the use of two distinct architectures, allowing for a comparative analysis of their capabilities in handling the complexities of Sanskrit grammar.

**Limitations**  
The authors acknowledge that while Naamah represents a significant advancement in the availability of annotated resources for Sanskrit NER, it is still a silver standard dataset, which may imply potential inaccuracies in the annotations. Additionally, the reliance on DBpedia for entity extraction may introduce biases based on the completeness and accuracy of the DBpedia entries. The paper does not address the computational resources required for training the hybrid reasoning model or the potential limitations of generalizing findings beyond the specific context of Sanskrit.

**Why it matters**  
The introduction of Naamah has substantial implications for the field of computational linguistics, particularly in the context of low-resource languages. By providing a high-quality synthetic dataset, this work facilitates further research in NER for Sanskrit, potentially leading to improved models that can better understand and process classical texts. The methodologies developed here could also inspire similar approaches for other underrepresented languages, thereby contributing to the broader goal of enhancing linguistic diversity in NLP applications.

Authors: Akhil Rajeev P, Annarao Kulkarni  
Source: arXiv:2604.26456  
URL: [https://arxiv.org/abs/2604.26456v1](https://arxiv.org/abs/2604.26456v1)
