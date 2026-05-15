---
title: "From Scenes to Elements: Multi-Granularity Evidence Retrieval for Verifiable Multimodal RAG"
date: 2026-05-14 16:20:02 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.15019v1"
arxiv_id: "2605.15019"
authors: ["Guanhua Chen", "Chuyue Huang", "Yutong Yao", "Shudong Liu", "Xueqing Song", "Lidia S. Chao"]
slug: from-scenes-to-elements-multi-granularity-evidence-retrieval
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing Multimodal Retrieval-Augmented Generation (RAG) systems, which typically retrieve evidence at coarse granularities, such as entire images or scenes. This approach leads to a mismatch with fine-grained user queries, resulting in unverifiable failures. The authors introduce GranuVistaVQA, a multimodal benchmark that features real-world landmarks with element-level annotations across multiple viewpoints, highlighting the challenge of partial observations where individual images contain only subsets of entities. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is GranuRAG, a multi-granularity framework that treats visual elements as first-class retrieval units. The framework operates in three stages: 
1. **Element-level Detection and Classification**: This stage identifies and classifies individual visual elements within images.
2. **Multi-Granularity Cross-Modal Alignment**: This stage aligns the detected elements with textual queries, facilitating evidence retrieval at varying granularities.
3. **Attribution-Constrained Generation**: This final stage generates responses while ensuring that the retrieved evidence is accurately attributed to the corresponding elements, enhancing transparency in the generation process.

The authors do not disclose specific details regarding the architecture, loss functions, or training compute used in their experiments.

**Results**  
GranuRAG demonstrates significant performance improvements over six strong baselines on the GranuVistaVQA benchmark. The system achieves up to a 29.2% improvement in retrieval accuracy, indicating a substantial enhancement in handling fine-grained queries compared to existing methods. The results underscore the effectiveness of element-level retrieval in addressing the challenges posed by multimodal queries.

**Limitations**  
The authors acknowledge that their approach may still struggle with highly complex scenes where element-level detection could be ambiguous or incomplete. Additionally, the reliance on element-level annotations may limit the applicability of GranuVistaVQA to scenarios where such detailed annotations are not available. The paper does not discuss potential computational overhead introduced by the multi-granularity framework, which could impact scalability in real-world applications.

**Why it matters**  
This work has significant implications for the development of more robust multimodal systems capable of handling fine-grained user queries. By enabling transparent error diagnosis through element-level retrieval, GranuRAG paves the way for improved verifiability in RAG systems. The introduction of the GranuVistaVQA benchmark also provides a valuable resource for future research, encouraging the exploration of fine-grained multimodal retrieval tasks. This could lead to advancements in applications such as visual question answering, interactive AI systems, and enhanced user experience in multimodal interfaces.

Authors: Guanhua Chen, Chuyue Huang, Yutong Yao, Shudong Liu, Xueqing Song, Lidia S. Chao, Derek F. Wong  
Source: arXiv:2605.15019  
URL: https://arxiv.org/abs/2605.15019v1
