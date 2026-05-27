---
title: "Formalization of Malagasy conjugation"
date: 2026-05-26 15:19:59 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.27161v1"
arxiv_id: "2605.27161"
authors: ["Joro Ny Aina Ranaivoarison", "Eric Laporte", "Baholisoa Simone Ralalaoherivony"]
slug: formalization-of-malagasy-conjugation
summary_word_count: 391
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of computational resources for Malagasy verb morphology, specifically the absence of a comprehensive morphological analyzer for simple verbs in the Malagasy language. The authors present a preprint work that formalizes the conjugation patterns of Malagasy verbs, filling a significant gap in the computational linguistics literature related to under-resourced languages.

**Method**  
The authors utilize the Unitex platform to construct a dictionary-based morphological analyzer. The core technical contribution involves the creation of an electronic dictionary specifically for Malagasy simple verbs, encoded with morphological features. The morphological variations of verb stems and their combinations with inflectional affixes are formalized using finite-state transducers (FSTs), represented as editable graphs. A total of 78 transducers are designed to generate a comprehensive dictionary of allomorphs for verb stems, while an additional 271 transducers are employed by the morphological analyzer to recognize stems and affixes in conjugated verbs. The design emphasizes readability and extensibility, allowing linguists to update and expand the resources as needed.

**Results**  
The paper does not provide quantitative performance metrics or comparisons against established baselines, as it primarily focuses on the construction of the morphological analyzer rather than empirical evaluations. However, the authors claim that the system is capable of accurately generating and recognizing a wide range of verb forms, which suggests a robust implementation of the morphological rules encoded in the transducers.

**Limitations**  
The authors acknowledge that the work is primarily focused on simple verbs and does not address more complex verb forms or other parts of speech. Additionally, the performance of the morphological analyzer has not been empirically validated against existing tools or benchmarks, which limits the assessment of its effectiveness. The reliance on the Unitex platform may also restrict the accessibility of the tool to users unfamiliar with this specific software.

**Why it matters**  
This work has significant implications for the field of computational linguistics, particularly for the development of resources for under-researched languages like Malagasy. By providing a structured approach to morphological analysis, it lays the groundwork for future linguistic research and applications, such as natural language processing tasks, machine translation, and language preservation efforts. The emphasis on readability and extensibility of the transducers also encourages collaboration among linguists, potentially leading to richer linguistic resources and more comprehensive analyses of Malagasy morphology.

Authors: Joro Ny Aina Ranaivoarison, Eric Laporte, Baholisoa Simone Ralalaoherivony  
Source: arXiv:2605.27161  
URL: https://arxiv.org/abs/2605.27161v1
