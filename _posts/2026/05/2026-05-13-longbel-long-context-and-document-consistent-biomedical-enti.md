---
title: "LongBEL: Long-Context and Document-Consistent Biomedical Entity Linking"
date: 2026-05-13 12:47:21 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13451v1"
arxiv_id: "2605.13451"
authors: ["Adam Remaki", "Xavier Tannier", "Christel G\u00e9rardin"]
slug: longbel-long-context-and-document-consistent-biomedical-enti
summary_word_count: 432
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing biomedical entity linking systems that typically operate at the sentence level, linking mentions independently without considering the broader document context. This approach can lead to inconsistencies, particularly when the same entity is referenced multiple times in different forms within a document. The authors propose LongBEL, a document-level generative framework that leverages full-document context and a memory of previous predictions to enhance linking accuracy. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
LongBEL employs a generative architecture that integrates full-document context with a memory mechanism to maintain consistency across entity predictions. The model is trained using cross-validated predictions instead of relying solely on gold labels, which mitigates the training-inference mismatch and reduces cascading errors. The authors utilize a combination of local, global, and memory-based variants to optimize performance. The training process involves five biomedical benchmarks in English, French, and Spanish, although specific details regarding the architecture, loss functions, and training compute are not disclosed in the abstract.

**Results**  
LongBEL demonstrates significant improvements over traditional sentence-level generative baselines across five biomedical benchmarks. The model achieves the most substantial gains in scenarios where concepts frequently recur within documents, indicating its effectiveness in enhancing document-level consistency. While specific numerical results are not provided in the abstract, the authors emphasize that the ensemble of local, global, and memory-based variants yields the best performance across all evaluated benchmarks. The results suggest that LongBEL primarily enhances the accuracy of linking recurring concepts rather than isolated mentions.

**Limitations**  
The authors acknowledge that their approach may still struggle with highly ambiguous mentions that do not recur within the document. Additionally, the reliance on cross-validated predictions may introduce its own set of biases, particularly if the validation set does not adequately represent the diversity of the data. The paper does not discuss the computational efficiency of the model or its scalability to larger datasets, which are critical considerations for real-world applications.

**Why it matters**  
The introduction of LongBEL has significant implications for biomedical text processing, particularly in improving the accuracy and consistency of entity linking in documents where entities are mentioned multiple times. By addressing the limitations of existing systems, this work paves the way for more robust applications in biomedical informatics, such as knowledge extraction, information retrieval, and clinical decision support systems. The focus on document-level context could inspire further research into generative models that leverage memory mechanisms for other NLP tasks, potentially leading to advancements in how contextual information is utilized across various domains.

Authors: Adam Remaki, Xavier Tannier, Christel Gérardin  
Source: arXiv:2605.13451  
URL: https://arxiv.org/abs/2605.13451v1
