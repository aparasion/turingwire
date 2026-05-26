---
title: "Retrieval-Augmented Detection of Potentially Abusive Clauses in Chilean Terms of Service"
date: 2026-05-25 16:38:10 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26019v1"
arxiv_id: "2605.26019"
authors: ["Christoffer Loeffler", "Tom\u00e1s Rey Pizarro", "Daniel Ignacio Miranda V\u00e1squez", "Andrea Mart\u00ednez Freile"]
slug: retrieval-augmented-detection-of-potentially-abusive-clauses
summary_word_count: 465
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in automated detection of potentially abusive clauses in online Terms of Service (ToS) specific to Chilean consumer law. The challenge lies in the legal complexity of identifying clauses that may violate mandatory consumer protections, as some clauses are overtly illegal while others require nuanced interpretation based on standards like good faith and contractual imbalance. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose a retrieval-augmented generation (RAG) framework that integrates several components for the detection and classification of abusive clauses. The architecture employs a hybrid dense-sparse retrieval mechanism to efficiently identify relevant clauses from the Chilean Abusive Terms of Service Extended corpus, which consists of 100 contracts and 10,029 annotated clauses across 24 categories. The framework utilizes prompt augmentation to enhance the performance of medium-sized open-weight language models. The training process involves fine-tuning these models on the annotated dataset, leveraging both local execution capabilities and a refined legal annotation scheme to improve the accuracy of clause classification. The computational efficiency is emphasized, allowing local models to achieve performance levels comparable to larger cloud-based systems while minimizing token usage.

**Results**  
The experimental results demonstrate that the retrieval-augmented prompting approach significantly outperforms traditional baselines and even some commercial models. Specifically, the RAG framework achieves a notable increase in classification accuracy, with effect sizes indicating improvements of up to 15% over standard fine-tuned encoders on the annotated dataset. The authors report that their method allows local models to approach the performance of larger models while reducing computational costs, making it a viable option for practical applications in consumer contract review.

**Limitations**  
The authors acknowledge several limitations, including the potential biases in the annotated dataset and the reliance on the quality of the legal annotations. They also note that the framework's performance may vary with different legal contexts outside of Chile, limiting its generalizability. Additionally, the local execution model may not capture the full range of contextual nuances present in more extensive cloud-based systems. The authors do not discuss the implications of model interpretability or the potential for adversarial examples in legal text classification.

**Why it matters**  
This work has significant implications for the automation of legal text analysis, particularly in consumer protection contexts. By providing a robust framework for detecting abusive clauses, it enhances the ability of consumers and legal practitioners to identify and challenge unfair contractual terms. The introduction of the Chilean Abusive Terms of Service Extended corpus also contributes to the field by offering a valuable resource for future research in legal NLP. Furthermore, the findings may inspire similar approaches in other jurisdictions, promoting the development of AI-assisted tools for consumer rights advocacy.

Authors: Christoffer Loeffler, Tomás Rey Pizarro, Daniel Ignacio Miranda Vásquez, Andrea Martínez Freile  
Source: arXiv:2605.26019  
URL: [https://arxiv.org/abs/2605.26019v1](https://arxiv.org/abs/2605.26019v1)
