---
title: "Chain-of-Procedure: Hierarchical Visual-Language Reasoning for Procedural QA"
date: 2026-05-14 15:03:36 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.14928v1"
arxiv_id: "2605.14928"
authors: ["Guanhua Chen", "Yutong Yao", "Shenghe Sun", "Ci-Jun Gao", "Shudong Liu", "Lidia S. Chao"]
slug: chain-of-procedure-hierarchical-visual-language-reasoning-fo
summary_word_count: 409
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in capability within visual-language models (VLMs) for visual procedure question answering (VP-QA), a task that has not been thoroughly explored in the literature. The authors highlight that existing VLMs struggle with two primary issues: (1) inadequate cross-modal retrieval of structured procedural information based on visual inputs, and (2) a misalignment between the granularity of image sequences and the textual decomposition of procedural steps. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose a novel hierarchical reasoning framework called Chain-of-Procedure (CoP). This framework consists of three main components: 
1. **Instruction Retrieval**: CoP first retrieves relevant procedural instructions by analyzing visual cues from the input images.
2. **Step Refinement**: It then refines the retrieved instructions through semantic decomposition, ensuring that the steps align with the visual context.
3. **Next-Step Generation**: Finally, CoP generates the next procedural step based on the refined instructions. The architecture leverages existing VLMs as a backbone, although specific details regarding the model architecture, loss functions, and training compute are not disclosed in the abstract.

**Results**  
CoP was evaluated across six different VLMs, demonstrating significant improvements in performance on the newly introduced ProcedureVQA benchmark. The framework achieved up to a 13% absolute improvement over standard baselines, although specific baseline models and metrics used for comparison are not detailed in the abstract. This performance enhancement indicates that CoP effectively addresses the identified limitations in current VLMs for VP-QA tasks.

**Limitations**  
The authors acknowledge that their approach may still face challenges in generalizing across diverse procedural contexts and varying image qualities. They do not discuss potential issues related to the scalability of the framework or the computational efficiency of the hierarchical reasoning process. Additionally, the reliance on existing VLMs may limit the framework's performance if those models are not optimized for VP-QA tasks.

**Why it matters**  
The introduction of the ProcedureVQA benchmark and the CoP framework has significant implications for future research in visual-language reasoning. By systematically addressing the limitations of current VLMs in procedural contexts, this work paves the way for more effective applications in domains such as robotics, automated assistance, and interactive learning systems. The findings could inspire further advancements in multimodal learning and reasoning, particularly in tasks that require a nuanced understanding of both visual and textual information.

Authors: Guanhua Chen, Yutong Yao, Shenghe Sun, Ci-Jun Gao, Shudong Liu, Lidia S. Chao, Feng Wan, Derek F. Wong  
Source: arXiv:2605.14928  
URL: [https://arxiv.org/abs/2605.14928v1](https://arxiv.org/abs/2605.14928v1)
