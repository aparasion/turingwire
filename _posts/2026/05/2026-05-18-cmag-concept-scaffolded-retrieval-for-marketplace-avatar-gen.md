---
title: "CMAG: Concept-Scaffolded Retrieval for Marketplace Avatar Generation"
date: 2026-05-18 17:21:43 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.18680v1"
arxiv_id: "2605.18680"
authors: ["Rajeev Goel", "Jason Ding", "Phani Harish Wajjala", "Pavan Turaga", "Tejaswi Gowda", "Krishna C. Garikipati"]
slug: cmag-concept-scaffolded-retrieval-for-marketplace-avatar-gen
summary_word_count: 437
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of text-only retrieval systems in the context of avatar generation for metaverse platforms, where users expect to create avatars from a variety of 3D assets. The authors highlight that existing methods struggle with the ambiguity of natural language, noisy metadata, and the challenges of ensuring stylistic and geometric compatibility among independently retrieved components. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce CMAG (Concept-Scaffolded Retrieval for Marketplace Avatar Generation), a framework that enhances avatar generation through a multi-step process. The core components include:

1. **Concept Scaffold Synthesis**: This module generates an intermediate 3D scaffold that provides spatial and stylistic context, helping to clarify user intent beyond the limitations of text prompts.
2. **View-Aware Part Discovery**: This component employs prompt decomposition and text-grounded segmentation to extract localized visual evidence, ensuring that the retrieved parts align with the user's request.
3. **Prompt-Conditioned Taxonomy Router**: This router enforces category coverage and resolves semantic-to-taxonomic mismatches, ensuring that the retrieved components fit within the defined taxonomy.
4. **Hybrid Category-Wise Retriever**: This retriever combines part-based fusion with a concept-residual fallback mechanism, utilizing feature suppression to enhance retrieval accuracy.
5. **Agentic Vision-Language Model**: This model filters and re-ranks the candidate components across categories, driving an iterative verification loop to ensure that the assembled avatars are both prompt-faithful and topologically consistent.

The authors do not disclose specific training compute or dataset details.

**Results**  
CMAG is evaluated against strong baselines on diverse compositional prompts. The results indicate significant improvements in retrieval robustness and compositional correctness. While specific numerical results are not provided in the abstract, the authors emphasize that CMAG outperforms existing methods, particularly in scenarios characterized by prompt ambiguity, suggesting a substantial effect size in retrieval accuracy and user satisfaction.

**Limitations**  
The authors acknowledge that the framework's reliance on a well-defined taxonomy may limit its applicability in more open-ended scenarios. Additionally, the performance metrics and specific datasets used for evaluation are not detailed, which could hinder reproducibility. The paper does not address potential computational overhead introduced by the multi-step retrieval and verification processes.

**Why it matters**  
The implications of CMAG are significant for the development of more robust avatar generation systems in metaverse environments. By addressing the challenges of text ambiguity and ensuring stylistic and geometric coherence, CMAG paves the way for more intuitive user experiences in creator-driven marketplaces. This work could influence future research in multimodal retrieval systems, particularly in contexts where user intent must be inferred from ambiguous inputs.

Authors: Rajeev Goel, Jason Ding, Phani Harish Wajjala, Pavan Turaga, Tejaswi Gowda, Krishna C. Garikipati  
Source: arXiv:2605.18680  
URL: [https://arxiv.org/abs/2605.18680v1](https://arxiv.org/abs/2605.18680v1)
