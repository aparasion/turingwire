---
title: "Don't Forget Your Embeddings: Robust Knowledge Erasure via Precise Editing of Embeddings"
date: 2026-06-02 14:15:25 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.03695v1"
arxiv_id: "2606.03695"
authors: ["Clara Haya Suslik", "Or Shafran", "Mor Geva"]
slug: don-t-forget-your-embeddings-robust-knowledge-erasure-via-pr
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces EMBER, a module for precise erasure of knowledge in language models by targeting token embeddings, enhancing robustness against relearning."
---

**Problem**  
The paper addresses the critical gap in the ability to effectively erase specific knowledge from language models, which is essential for safety and compliance in real-world applications. Existing methods primarily focus on updating model parameters for persistent knowledge removal but often fail to prevent the recovery of erased knowledge through adversarial prompting or relearning. This work is particularly relevant as it is a preprint and has not undergone peer review, indicating that the findings should be interpreted with caution.

**Method**  
The authors propose EMBedding ERasure (EMBER), a novel plug-and-play module that utilizes Sparse Matrix Factorization to facilitate precise erasure of concept-related features directly from token embeddings. EMBER operates by identifying and modifying the embedding vectors associated with specific concepts, thereby enhancing the efficacy of existing erasure methods. The module is designed to be integrated with current language models without requiring extensive retraining. The authors conducted comprehensive evaluations using two large language models: Gemma-2-2B-it and Llama-3.1-8B-Instruct, assessing the performance of EMBER across various task formats.

**Results**  
The integration of EMBER significantly improved the erasure efficacy and specificity compared to baseline methods. Notably, the authors report a reduction in regained accuracy by up to 50% when using EMBER, limiting it to 35% on the Llama model, in contrast to 70%-76% for prior methods. This indicates a substantial enhancement in robustness against relearning. Additionally, the coherence loss associated with using EMBER was minimal and localized, affecting only a small subset of concept-exclusive tokens, which suggests that the overall integrity of the model's performance is largely preserved.

**Limitations**  
The authors acknowledge that while EMBER improves erasure efficacy, it may not completely eliminate the risk of knowledge recovery in all scenarios. The localized coherence cost, while minimal, could still impact specific tasks that rely heavily on the affected tokens. Furthermore, the evaluation is limited to the two models tested, and the generalizability of EMBER to other architectures or tasks remains to be established. The authors also do not address potential computational overhead introduced by the Sparse Matrix Factorization process.

**Why it matters**  
The findings of this paper have significant implications for the development of safer and more compliant AI systems, particularly in contexts where knowledge management is critical. By demonstrating that precise embedding-level interventions can enhance the robustness of knowledge erasure, this work paves the way for future research into more effective methods for managing the knowledge retention and erasure capabilities of language models. This is particularly relevant as the deployment of AI systems continues to expand in sensitive applications. The work is available on [arXiv](https://arxiv.org/abs/2606.03695v1) and contributes to the ongoing discourse on ethical AI and model safety.
