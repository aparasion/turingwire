---
title: "OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory"
date: 2026-04-29 12:49:30 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26622v1"
arxiv_id: "2604.26622"
authors: ["Jinze Li", "Yang Zhang", "Xin Yang", "Jiayi Qu", "Jinfeng Xu", "Shuo Yang"]
slug: ocr-memory-optical-context-retrieval-for-long-horizon-agent-
summary_word_count: 423
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing memory systems in autonomous large language model (LLM) agents, particularly in long-horizon interactive settings. Current systems are constrained by text-context budgets, which make it impractical to store or revisit raw trajectories due to token costs. Summarization methods, while reducing token usage, often lead to information loss and fragmented evidence. The authors propose a novel approach, Optical Context Retrieval Memory (OCR-Memory), to overcome these challenges. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
OCR-Memory introduces a memory framework that utilizes the visual modality to create high-density representations of agent experiences. Historical trajectories are rendered into images, each annotated with unique visual identifiers. The retrieval process employs a "locate-and-transcribe" paradigm, where relevant regions of the image are selected using visual anchors, and the corresponding verbatim text is retrieved. This method minimizes the need for free-form text generation, thereby reducing the risk of hallucination. The architecture leverages visual encoding to enhance memory capacity while maintaining fidelity in evidence recovery. Specific details regarding the training compute and dataset used are not disclosed in the paper.

**Results**  
The authors report significant improvements in performance on long-horizon agent benchmarks when using OCR-Memory compared to traditional memory systems. The results indicate that OCR-Memory can effectively increase memory capacity while preserving the integrity of retrieved information. Although specific numerical results and effect sizes are not detailed in the abstract, the paper claims consistent gains under strict context limits, suggesting a robust advantage over named baselines.

**Limitations**  
The authors acknowledge that OCR-Memory's reliance on visual representations may introduce challenges related to the quality and interpretability of the generated images. Additionally, the method's performance may be contingent on the effectiveness of the visual anchors used for retrieval. The paper does not address potential scalability issues related to the generation and storage of visual representations, nor does it explore the implications of varying visual fidelity on retrieval accuracy.

**Why it matters**  
The introduction of OCR-Memory has significant implications for the development of more efficient memory systems in LLM agents, particularly in applications requiring long-term interaction and experience reuse. By leveraging visual modalities, this framework could pave the way for more sophisticated memory architectures that balance token efficiency with information retention. This work may inspire further research into multimodal memory systems and their applications in complex, interactive environments, potentially enhancing the capabilities of autonomous agents in various domains.

Authors: Jinze Li, Yang Zhang, Xin Yang, Jiayi Qu, Jinfeng Xu, Shuo Yang, Junhua Ding, Edith Cheuk-Han Ngai  
Source: arXiv:2604.26622  
URL: https://arxiv.org/abs/2604.26622v1
