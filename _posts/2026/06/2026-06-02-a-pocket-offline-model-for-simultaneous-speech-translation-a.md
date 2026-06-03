---
title: "A Pocket Offline Model for Simultaneous Speech Translation as CUNI Submission to IWSLT 2026"
date: 2026-06-02 17:37:11 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.03948v1"
arxiv_id: "2606.03948"
authors: ["Aziz Sharipov Ortega", "Dominik Mach\u00e1\u010dek"]
slug: a-pocket-offline-model-for-simultaneous-speech-translation-a
summary_word_count: 400
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper presents a compact offline model for simultaneous speech translation, achieving high quality and low computational requirements across multiple languages."
---

**Problem** — This work addresses the gap in simultaneous speech translation capabilities, particularly for offline models, which are often limited in translation quality and computational efficiency. The authors highlight the need for a model that can perform well in both low- and high-latency scenarios while maintaining a manageable parameter size. This paper is a preprint and has not undergone peer review.

**Method** — The authors implement the Canary model, which utilizes the AlignAtt policy for direct speech-to-text translation. Canary is designed with a parameter count of 1 billion, making it relatively lightweight compared to other state-of-the-art models. The training data includes a diverse set of multilingual datasets, enabling the model to support 25 source languages and 25 target languages. The training process is optimized for both translation quality and computational efficiency, although specific training compute details are not disclosed.

**Results** — The Canary model demonstrates superior translation quality compared to similarly sized baselines in both low-latency and high-latency conditions. In computationally unaware simulations, the model outperforms existing systems, achieving significant improvements in translation accuracy. While exact metrics are not provided in the abstract, the authors claim that their model consistently exceeds the performance of established benchmarks in simultaneous speech translation tasks, specifically for Czech to English and English to German and Italian.

**Limitations** — The authors acknowledge that their model's performance may vary depending on the specific language pairs and the quality of the input audio. They also note that while the model is designed for offline use, it may not fully capture the nuances of real-time translation in dynamic environments. Additionally, the lack of peer review raises questions about the robustness of the findings, and the authors do not discuss potential biases in the training data or the implications of multilingual support on translation accuracy.

**Why it matters** — This research contributes to the field of simultaneous speech translation by providing a model that balances high translation quality with low computational demands, making it suitable for deployment in resource-constrained environments. The multilingual capabilities of the Canary model could facilitate broader accessibility in translation applications, particularly in scenarios where real-time processing is not feasible. The implications of this work extend to various applications in natural language processing and machine translation, as it offers a viable solution for offline translation tasks. This is particularly relevant for future research in multilingual models and their integration into real-world applications, as published in [arXiv](https://arxiv.org/abs/2606.03948v1).
