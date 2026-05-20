---
title: "KoRe: Compact Knowledge Representations for Large Language Models"
date: 2026-05-19 17:53:29 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.20170v1"
arxiv_id: "2605.20170"
authors: ["Davide Cavicchini", "Fausto Giunchiglia", "Jacopo Staiano"]
slug: kore-compact-knowledge-representations-for-large-language-mo
summary_word_count: 423
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of knowledge representation in Large Language Models (LLMs), which encode world knowledge within their parameters, leading to issues such as opacity, difficulty in debugging, and susceptibility to hallucinations. The authors highlight that while Knowledge Graphs (KGs) offer human-readable and easily editable representations of knowledge, existing integration methods necessitate extensive retraining or fine-tuning of LLMs. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose KoRe, a novel methodology that encodes 1-hop sub-graphs from KGs into compact discrete knowledge tokens. These tokens are then injected into the backbone of an LLM, allowing for efficient knowledge integration without the need for extensive retraining. The architecture details are not explicitly disclosed, but the approach leverages the existing LLM framework to enhance its knowledge representation capabilities. The training compute requirements are not specified, but the authors emphasize the efficiency of their method in terms of token usage, achieving a reduction of up to 10x compared to traditional methods.

**Results**  
KoRe was evaluated on three established benchmarks, although specific names of these benchmarks are not provided in the abstract. The results indicate that the proposed method achieves competitive performance relative to baseline models that do not utilize the compact discrete KG representations. The authors report a significant reduction in token usage, achieving up to a 10x decrease, which suggests improved efficiency in knowledge representation without sacrificing performance. However, exact performance metrics (e.g., accuracy, F1 scores) against specific baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that their approach may still be limited by the inherent constraints of the LLM architecture and the quality of the underlying Knowledge Graphs. They do not discuss potential challenges related to the scalability of the method or the generalizability of the results across different domains or types of knowledge. Additionally, the reliance on 1-hop sub-graphs may restrict the depth of knowledge representation, potentially limiting the model's reasoning capabilities in more complex scenarios.

**Why it matters**  
The implications of KoRe are significant for the integration of structured knowledge into LLMs, as it offers a method to enhance knowledge representation while minimizing retraining costs. This could lead to more robust and interpretable AI systems capable of better reasoning and reduced hallucination rates. The approach may pave the way for future research on hybrid models that combine the strengths of LLMs and KGs, potentially influencing applications in knowledge-intensive tasks such as question answering, information retrieval, and conversational agents.

Authors: Davide Cavicchini, Fausto Giunchiglia, Jacopo Staiano  
Source: arXiv:2605.20170  
URL: [https://arxiv.org/abs/2605.20170v1](https://arxiv.org/abs/2605.20170v1)
