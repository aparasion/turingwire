---
title: "Continuous Diffusion Scales Competitively with Discrete Diffusion for Language"
date: 2026-05-18 15:15:24 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18530v1"
arxiv_id: "2605.18530"
authors: ["Zhihan Yang", "Wei Guo", "Shuibai Zhang", "Subham Sekhar Sahoo", "Yongxin Chen", "Arash Vahdat"]
slug: continuous-diffusion-scales-competitively-with-discrete-diff
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the perceived scalability limitations of continuous diffusion language models (DLMs) compared to discrete DLMs. While diffusion models have gained traction in language modeling, continuous diffusion has been considered less competitive in terms of scalability and performance. The authors aim to challenge this notion by presenting a new architecture that aligns continuous diffusion with the advancements seen in discrete models.

**Method**  
The core technical contribution is the development of RePlaid, an enhanced version of the Plaid model, which integrates architectural elements from modern discrete DLMs. RePlaid employs a likelihood-based training approach, optimizing the noise schedule to minimize the variance of the Evidence Lower Bound (ELBO). This optimization leads to a linear cross-entropy loss over time, facilitating a more uniform distribution of denoising difficulty across the training process. The authors also emphasize the importance of embedding optimization via likelihood, which results in structured geometries that enhance likelihood gains. The training compute requirements are not explicitly disclosed, but the authors claim a compute gap of only 20× compared to autoregressive models.

**Results**  
RePlaid achieves a new state-of-the-art perplexity (PPL) of 22.1 on the OpenWebText benchmark among continuous DLMs, outperforming previous models such as Duo and MDLM, particularly in the over-trained regime. The results indicate that RePlaid not only uses fewer parameters than Duo but also demonstrates superior generation quality. The authors provide quantitative comparisons, highlighting that RePlaid's performance is competitive with discrete DLMs, thereby validating the scalability of continuous diffusion models.

**Limitations**  
The authors acknowledge that while RePlaid shows promising results, it is still a preprint and has not undergone peer review. They do not discuss potential limitations related to the generalizability of their findings across different datasets or tasks, nor do they address the computational efficiency of training RePlaid compared to other state-of-the-art models. Additionally, the implications of the model's architecture on interpretability and robustness are not explored.

**Why it matters**  
This work has significant implications for the future of language modeling, particularly in the context of continuous diffusion approaches. By demonstrating that continuous DLMs can achieve competitive performance with discrete models, the authors open avenues for further research into likelihood-based training methods and their applications in various NLP tasks. The insights regarding noise schedule optimization and embedding structures could inform the design of future models, potentially leading to more efficient and effective language generation systems.

Authors: Zhihan Yang, Wei Guo, Shuibai Zhang, Subham Sekhar Sahoo, Yongxin Chen, Arash Vahdat, Morteza Mardani, John Thickstun  
Source: arXiv:2605.18530  
URL: [https://arxiv.org/abs/2605.18530v1](https://arxiv.org/abs/2605.18530v1)
