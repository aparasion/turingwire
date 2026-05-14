---
title: "(How) Do Large Language Models Understand High-Level Message Sequence Charts?"
date: 2026-05-13 16:50:51 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13773v1"
arxiv_id: "2605.13773"
authors: ["Mohammad Reza Mousavi"]
slug: how-do-large-language-models-understand-high-level-message-s
summary_word_count: 415
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the understanding of how Large Language Models (LLMs) interpret the semantics of High-Level Message Sequence Charts (HMSCs), which are formal visual models used in software architecture. While LLMs are increasingly utilized in automating software development tasks, their capability to handle the formal semantics of architectural specifications remains underexplored. This study specifically investigates whether LLMs can accurately perform semantic tasks related to HMSCs, which are foundational to Sequence Diagrams in the Unified Modeling Language (UML).

**Method**  
The authors evaluate three LLMs—Gemini-3, GPT-5.4, and Qwen-3.6—across 129 semantic tasks that encompass a range of complexities. These tasks include querying basic semantic constructs (events and their ordering), performing semantic-preserving abstractions and compositions, and calculating traces and trace-equivalent labeled transition systems (LTSs). The evaluation framework is designed to assess the models' understanding of HMSCs' formal semantics, with a focus on accuracy in various semantic concepts. The training compute and specific architectural details of the LLMs are not disclosed in the paper.

**Results**  
The findings reveal that the LLMs exhibit a modest overall accuracy of approximately 52% in understanding the semantics of HMSCs. Performance varies significantly across different semantic tasks: the models achieve around 88% accuracy in basic semantic constructs but drop to about 36% for tasks involving abstraction and composition, and 42% for traces and LTSs. Notably, all three models demonstrate particular difficulty with concepts such as co-regions and explicit causal dependencies, failing to utilize these in semantic-preserving transformations.

**Limitations**  
The authors acknowledge that the overall accuracy of 52% indicates a limited understanding of HMSCs by the LLMs. They specifically highlight the models' struggles with higher-order semantic reasoning tasks, which could impact their utility in practical applications. Additionally, the study does not explore the potential influence of model size or training data diversity on performance, nor does it consider the implications of these limitations for real-world software engineering tasks.

**Why it matters**  
This research has significant implications for the deployment of LLMs in software development, particularly in tasks requiring a deep understanding of formal specifications. The modest performance on semantic reasoning tasks suggests that while LLMs can assist in automating certain aspects of software design, their limitations in understanding formal semantics may lead to inaccuracies in generated artifacts. This work encourages further investigation into enhancing LLM capabilities in formal reasoning and suggests that future models may need to incorporate more robust mechanisms for understanding complex semantic structures to be effectively utilized in architectural design.

Authors: Mohammad Reza Mousavi  
Source: arXiv:2605.13773  
URL: [https://arxiv.org/abs/2605.13773v1](https://arxiv.org/abs/2605.13773v1)
