---
title: "BeLink: Biomedical Entity Linking Meets Generative Re-Ranking"
date: 2026-05-21 13:52:55 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.22501v1"
arxiv_id: "2605.22501"
authors: ["Darya Shlyk", "Stefano Montanelli", "Lawrence Hunter"]
slug: belink-biomedical-entity-linking-meets-generative-re-ranking
summary_word_count: 405
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in Biomedical Entity Linking (BEL) using large language models (LLMs), particularly in terms of computational resources and deployment challenges in real-world applications. The authors highlight that existing BEL methods struggle with scalability and speed, which limits their practical utility. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce BeLink, a modular end-to-end BEL system that incorporates a novel generative re-ranking approach. The core technical contribution is the application of instruction-tuning to open-source generative models specifically at the re-ranking stage of the BEL pipeline. This set-wise instruction-tuning formulation allows for efficient candidate selection from a pool of potential entity links. The training process leverages a diverse set of biomedical texts to fine-tune the generative model, although specific details regarding the dataset size and training compute are not disclosed. The architecture is designed to optimize both accuracy and inference speed, making it suitable for practical deployment.

**Results**  
BeLink demonstrates substantial improvements in linking accuracy across multiple BEL benchmarks. The reported accuracy gains range from 3% to 24% compared to state-of-the-art methods, with specific performance metrics not detailed in the abstract. Additionally, the authors claim a reduction in inference time, although exact figures are not provided. The benchmarks used for evaluation include standard datasets in the biomedical domain, which are critical for assessing the efficacy of BEL systems.

**Limitations**  
The authors acknowledge that while their approach significantly enhances accuracy and efficiency, it may still be limited by the inherent biases present in the training data used for instruction-tuning. They do not address potential issues related to the generalizability of their model across diverse biomedical domains or the scalability of their approach to larger datasets. Furthermore, the reliance on generative models may introduce variability in performance based on the specific model architecture chosen.

**Why it matters**  
The implications of this work are significant for the field of biomedical informatics, particularly in enhancing the accuracy and efficiency of entity linking systems. By integrating generative re-ranking into the BEL pipeline, BeLink provides a promising avenue for improving the deployment of LLMs in real-world biomedical applications. This could facilitate better information retrieval, knowledge extraction, and ultimately, more effective decision-making in healthcare and research settings. The modular design of BeLink also suggests potential for future enhancements and adaptations, paving the way for further innovations in BEL methodologies.

Authors: Darya Shlyk, Stefano Montanelli, Lawrence Hunter  
Source: arXiv:2605.22501  
URL: [https://arxiv.org/abs/2605.22501v1](https://arxiv.org/abs/2605.22501v1)
