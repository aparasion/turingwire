---
title: "GraphLit: Learning Text-Enriched Dynamic Character Network Representations for Literary Study"
date: 2026-05-27 15:48:13 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.28643v1"
arxiv_id: "2605.28643"
authors: ["Gaspard Michel", "Elena V. Epure", "Romain Hennequin", "Christophe Cerisara", "Mirella Lapata"]
slug: graphlit-learning-text-enriched-dynamic-character-network-re
summary_word_count: 472
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the representation of literary texts by integrating character interactions with their textual contexts, which is often overlooked in existing methods. Prior approaches primarily focus on character interactions as static graphs or sequences of graphs, failing to capture the dynamic nature of character relationships within the narrative context. The authors propose a novel framework, GraphLit, to fill this gap by leveraging Dynamic Heterogeneous Character Networks (DHCNs). This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of Dynamic Heterogeneous Character Networks (DHCNs), which are constructed from literary texts to represent characters and their interactions in a temporally localized manner. The authors extract approximately 20,000 DHCNs from Project Gutenberg, allowing for a rich representation of character dynamics over time. The GraphLit framework employs a masked graph autoencoder objective for self-supervised learning, enabling the model to learn comprehensive literary representations. The architecture details, including the specific layers and hyperparameters, are not disclosed, but the training process involves leveraging the extracted DHCNs to optimize the representation learning. The self-supervised approach allows the model to learn from the structure and context of the graphs without requiring labeled data.

**Results**  
GraphLit demonstrates significant improvements across a diverse set of 12 character-related tasks when compared to both text-only and graph-only baselines. Notably, the model excels in tasks that necessitate contextual understanding, showcasing its ability to leverage the textual context alongside character interactions. The authors report effect sizes that indicate substantial performance gains, although specific numerical results and comparisons to named baselines are not detailed in the abstract. The applicability of DHCNs and GraphLit is further validated through literary analysis, particularly in exploring the relationship between narrative non-linearity and dynamic social features.

**Limitations**  
The authors acknowledge several limitations, including the reliance on Project Gutenberg texts, which may not represent the full diversity of literary styles and genres. Additionally, the model's performance on tasks requiring deep semantic understanding beyond character interactions is not fully explored. The lack of detailed architecture specifications and training compute resources may hinder reproducibility. Furthermore, the self-supervised nature of the learning process may introduce biases based on the structure of the input data.

**Why it matters**  
The introduction of DHCNs and the GraphLit framework has significant implications for literary studies and natural language processing. By effectively integrating character interactions with their textual contexts, this work opens new avenues for analyzing narrative structures and character dynamics in literature. The findings could influence future research in both computational literary analysis and the development of more sophisticated models for understanding complex narrative forms. The ability to study narrative non-linearity in conjunction with social dynamics also suggests potential interdisciplinary applications, bridging literary theory and machine learning.

Authors: Gaspard Michel, Elena V. Epure, Romain Hennequin, Christophe Cerisara, Mirella Lapata  
Source: arXiv:2605.28643  
URL: https://arxiv.org/abs/2605.28643v1
