---
title: "LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation"
date: 2026-06-01 17:50:49 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2606.02553v1"
arxiv_id: "2606.02553"
authors: ["Qixin Hu", "Shuai Yang", "Wei Huang", "Song Han", "Yukang Chen"]
slug: longlive-rag-a-general-retrieval-augmented-framework-for-lon
summary_word_count: 433
classification_confidence: 0.70
source_truncated: false
layout: post
description: "LongLive-RAG introduces a retrieval-augmented framework for autoregressive long video generation, mitigating error accumulation and identity drift."
---

**Problem**  
Existing autoregressive (AR) video generation methods struggle with long-horizon synthesis due to accumulated errors and identity drift, particularly when employing sliding-window attention. This approach creates an irreversible trajectory where errors compound, leading to degraded outputs. The authors identify a gap in the literature regarding the effective use of historical latent representations in long video generation, proposing a novel framework that leverages retrieval mechanisms to enhance the generation process. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose LongLive-RAG, a retrieval-augmented generation framework that treats previously generated latents as a dynamic, searchable history. At each generation step, LongLive-RAG employs a query embedding to retrieve relevant historical latents, allowing the model to condition on non-local context rather than being limited to a recent sliding window. A key technical contribution is the introduction of the Window Temporal Delta Loss, which minimizes redundant local similarities and promotes the capture of significant temporal changes in the embeddings. This retrieval mechanism incurs minimal overhead compared to the generation process, enhancing the model's ability to maintain coherence over longer video sequences. The framework is compatible with various AR backbones, although specific architectures and training compute details are not disclosed.

**Results**  
LongLive-RAG demonstrates significant improvements in long video quality across multiple AR backbones and varying generation lengths. The framework achieves the best average rank on the VBench-Long benchmark, outperforming existing methods that rely solely on sliding-window attention. While specific quantitative results are not detailed in the abstract, the authors emphasize the qualitative enhancements in video coherence and reduced identity drift, indicating a substantial effect size compared to baseline models.

**Limitations**  
The authors acknowledge that while LongLive-RAG effectively reduces error accumulation, it may still be susceptible to limitations inherent in the AR generation paradigm, such as potential biases in the retrieved latents. Additionally, the reliance on historical latents may introduce challenges in scenarios where the initial conditions are suboptimal. The paper does not address the computational complexity of the retrieval process in detail, which could impact scalability for very long video sequences.

**Why it matters**  
The introduction of LongLive-RAG represents a significant advancement in the field of long video generation, particularly by framing the problem as a retrieval-augmented task. This approach not only mitigates common pitfalls associated with traditional AR methods but also opens avenues for further research into content-addressable memory systems in generative models. The implications of this work extend to various applications in video synthesis, storytelling, and interactive media, as it enhances the potential for coherent long-form content generation. For further details, see the full paper available on [arXiv](https://arxiv.org/abs/2606.02553v1).
