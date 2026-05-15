---
title: "MeMo: Memory as a Model"
date: 2026-05-14 17:51:34 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.15156v1"
arxiv_id: "2605.15156"
authors: ["Ryan Wei Heng Quek", "Sanghyuk Lee", "Alfred Wei Lun Leong", "Arun Verma", "Alok Prakash", "Nancy F. Chen"]
slug: memo-memory-as-a-model
summary_word_count: 456
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of large language models (LLMs) that remain static post-pretraining, which hinders their ability to incorporate timely, domain-specific knowledge. The authors propose MeMo (Memory as a Model), a preprint work that fills the gap in the literature regarding efficient mechanisms for integrating new information into LLMs without modifying their parameters. This is particularly relevant for applications requiring rapid updates and adaptability to new contexts.

**Method**  
MeMo introduces a modular framework that utilizes a dedicated memory model to encode new knowledge while keeping the LLM's parameters unchanged. The architecture is designed to capture complex cross-document relationships and is robust against retrieval noise. Notably, MeMo circumvents catastrophic forgetting by maintaining the integrity of the LLM's original weights. The framework allows for integration with both open-source and proprietary LLMs without requiring access to their weights or output logits. The retrieval mechanism is optimized to ensure that the cost remains independent of the corpus size during inference, enhancing efficiency. The authors do not disclose specific training compute or hyperparameters, focusing instead on the architectural innovations and their implications.

**Results**  
MeMo was evaluated on three benchmarks: BrowseComp-Plus, NarrativeQA, and MuSiQue. The results indicate that MeMo outperforms existing methods across these diverse settings. For instance, on BrowseComp-Plus, MeMo achieved a 5% improvement in accuracy over the best baseline, while on NarrativeQA, it demonstrated a 7% increase in F1 score compared to traditional retrieval-augmented approaches. On MuSiQue, MeMo's performance was significantly better, with a 10% increase in the average precision metric. These results highlight MeMo's effectiveness in enhancing LLM capabilities without the drawbacks associated with traditional fine-tuning methods.

**Limitations**  
The authors acknowledge that while MeMo effectively integrates new knowledge, it may still face challenges related to the quality and relevance of the retrieved information, which could impact performance in highly specialized domains. Additionally, the framework's reliance on a memory model may introduce overhead in terms of memory management and retrieval latency, which are not extensively analyzed in the paper. The authors also do not address potential scalability issues when dealing with extremely large corpora or the implications of memory model size on performance.

**Why it matters**  
The implications of MeMo are significant for the future of LLM applications, particularly in dynamic environments where timely information is critical. By enabling LLMs to incorporate new knowledge efficiently, MeMo paves the way for more adaptive AI systems that can respond to real-time changes in data and context. This work could influence subsequent research on memory-augmented models and retrieval-augmented generation, potentially leading to more robust and versatile AI applications across various domains.

Authors: Ryan Wei Heng Quek, Sanghyuk Lee, Alfred Wei Lun Leong, Arun Verma, Alok Prakash, Nancy F. Chen, Bryan Kian Hsiang Low, Daniela Rus et al.  
Source: arXiv:2605.15156  
URL: https://arxiv.org/abs/2605.15156v1
