---
title: "Benchmarking Parameter-Efficient Fine-Tuning of Large Language Models for Low-Resource Tajik Text Generation with the Tajik Web Corpus"
date: 2026-05-05 13:28:31 +0000
category: research
subcategory: training_methods
company: "Mistral"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03742v1"
arxiv_id: "2605.03742"
authors: ["Mullosharaf K. Arabov"]
slug: benchmarking-parameter-efficient-fine-tuning-of-large-langua
summary_word_count: 417
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of resources and systematic evaluation for fine-tuning large language models (LLMs) on low-resource languages, specifically Tajik, which is written in Cyrillic script. The authors present the Tajik Web Corpus, the largest open-access corpus for Tajik, comprising 319,298 documents (~1.11 billion characters). This work is a preprint and has not undergone peer review, highlighting the need for further validation in the community.

**Method**  
The core technical contribution involves benchmarking 17 configurations of LLMs, including autoregressive, encoder-decoder, and encoder-only architectures. The fine-tuning strategies evaluated are full fine-tuning, Low-Rank Adaptation (LoRA), and Quantized LoRA (QLoRA) with ranks of 8 and 16. The models were assessed on a subsample of 10,000 documents from the Tajik Web Corpus. Quality metrics included perplexity and cross-entropy loss, while computational efficiency was measured through peak GPU memory usage and training time. The best-performing model was Mistral 7B fine-tuned with QLoRA (r=16), achieving a mean perplexity of 5.03 with a standard deviation of 0.03. 

**Results**  
The results indicate that for smaller models in the GPT-2 family, full fine-tuning outperformed LoRA, yielding a perplexity of 3.48 for GPT-2 Medium compared to LoRA's range of 7.60-8.42. However, full fine-tuning led to catastrophic forgetting of previously learned information. The encoder-only model XLM-RoBERTa exhibited the poorest performance with a perplexity of 59.3. The findings suggest that while increasing the rank from 8 to 16 in QLoRA provided marginal improvements, it also resulted in higher memory consumption without significant gains in performance.

**Limitations**  
The authors acknowledge that the study is limited by the relatively small size of the training subsample (10,000 documents) compared to the full corpus. Additionally, the evaluation metrics focus primarily on perplexity and cross-entropy loss, which may not fully capture the qualitative aspects of generated text. The potential for catastrophic forgetting in full fine-tuning is also a critical limitation that could affect model robustness. The paper does not explore the impact of different training epochs or hyperparameter tuning extensively, which could influence the results.

**Why it matters**  
This work is significant as it lays the groundwork for future research in low-resource language processing, particularly for Tajik. By providing a comprehensive analysis of parameter-efficient fine-tuning (PEFT) strategies, it offers practical recommendations for model selection and fine-tuning approaches that optimize computational resources while maintaining quality. The release of the Tajik Web Corpus also facilitates further exploration and development of NLP applications in Tajik, potentially leading to improved accessibility and representation of the language in digital spaces.

Authors: Mullosharaf K. Arabov  
Source: arXiv:2605.03742  
URL: [https://arxiv.org/abs/2605.03742v1](https://arxiv.org/abs/2605.03742v1)
