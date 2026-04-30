---
title: "MoRFI: Monotonic Sparse Autoencoder Feature Identification"
date: 2026-04-29 16:32:57 +0000
category: research
subcategory: alignment_safety
company: "Meta"
secondary_companies: ["Mistral"]
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.26866v1"
arxiv_id: "2604.26866"
authors: ["Dimitris Dimakopoulos", "Shay B. Cohen", "Ioannis Konstas"]
slug: morfi-monotonic-sparse-autoencoder-feature-identification
summary_word_count: 451
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the mechanisms behind hallucinations in large language models (LLMs) during post-training, particularly in the context of closed-book question answering (QA). While it is known that supervised fine-tuning (SFT) can exacerbate hallucinations, the specific latent factors contributing to this phenomenon remain poorly characterized. The authors aim to elucidate these factors by conducting controlled experiments on various LLMs.

**Method**  
The authors conduct a controlled fine-tuning experiment on three LLMs: Llama 3.1 (8B parameters), Gemma 2 (9B parameters), and Mistral 7B v03. They fine-tune these models on seven distinct QA datasets, systematically varying the percentage of new knowledge introduced and the number of training epochs. To analyze the impact of this fine-tuning on model behavior, they employ pre-trained sparse autoencoders (SAEs) to examine the residual stream activations across different checkpoints. The core technical contribution is the Monotonic Relationship Feature Identification (MoRFI) method, which identifies features in the SAE that respond monotonically to the controlled fine-tuning data mixtures. This approach allows the authors to capture causally relevant latent directions that contribute to hallucinations.

**Results**  
The experiments reveal that incrementally introducing new knowledge significantly increases the incidence of hallucinations, with a more pronounced effect observed with extended training epochs. The authors quantify this effect by measuring performance on the test sets of the QA datasets, demonstrating that the models' ability to retrieve stored knowledge deteriorates as exposure to unknown facts increases. The MoRFI method successfully identifies latent directions that correlate with this degradation, providing a reliable mechanism for discovering the underlying causes of hallucinations across different models.

**Limitations**  
The authors acknowledge several limitations, including the potential overfitting to the specific datasets used for fine-tuning and the limited generalizability of their findings to other tasks beyond closed-book QA. Additionally, the reliance on sparse autoencoders may introduce biases based on the architecture and training of the SAEs themselves. The study does not explore the long-term implications of these findings on model deployment in real-world applications, nor does it address the scalability of the MoRFI method to larger or more diverse datasets.

**Why it matters**  
This work has significant implications for the development of more robust LLMs, particularly in mitigating hallucinations during post-training. By identifying the latent factors that contribute to these issues, researchers can better design fine-tuning protocols that minimize the introduction of erroneous information. The MoRFI method provides a novel analytical framework that can be applied to other models and tasks, potentially leading to improved understanding and control over model behavior in various contexts. This research paves the way for future investigations into the causal mechanisms of knowledge retrieval and the design of more reliable AI systems.

Authors: Dimitris Dimakopoulos, Shay B. Cohen, Ioannis Konstas  
Source: arXiv:2604.26866  
URL: [https://arxiv.org/abs/2604.26866v1](https://arxiv.org/abs/2604.26866v1)
