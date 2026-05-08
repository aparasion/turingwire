---
title: "Invariant Features in Language Models: Geometric Characterization and Model Attribution"
date: 2026-05-07 15:50:31 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.06458v1"
arxiv_id: "2605.06458"
authors: ["Agnibh Dasgupta", "Abdullah Tanvir", "Xin Zhong"]
slug: invariant-features-in-language-models-geometric-characteriza
summary_word_count: 443
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the geometric structure of invariant features in language models, particularly how these models maintain robustness to paraphrasing. While previous research has noted the stability of semantic information in language models, the specific mechanisms and representations that contribute to this invariance remain poorly characterized. The authors aim to elucidate the nature of these invariant features and their implications for model behavior and attribution.

**Method**  
The authors propose a local geometric framework that posits semantically equivalent inputs occupy structured regions in the latent space of language models. They introduce three core contributions:  
1. **Geometric Characterization**: They define invariant latent features geometrically, suggesting that paraphrastic variations occur along nuisance directions while semantic identity is preserved in invariant subspaces.  
2. **Contrastive Subspace Discovery**: A novel method is developed to differentiate between semantic-changing and semantic-preserving variations in the latent space. This involves analyzing the geometry of the latent representations to identify invariant components.  
3. **Zero-shot Model Attribution**: The authors apply their findings to model attribution tasks, demonstrating that invariant representations can effectively capture model-specific geometric patterns, facilitating accurate attribution of outputs to specific model behaviors. The training compute and specific architectures used in their experiments are not disclosed.

**Results**  
Empirical evaluations across various models and layers reveal that invariant structures emerge predominantly in specific depth regions of the models. The authors report that semantic displacements are largely outside the identified nuisance subspace, indicating a clear separation of semantic-preserving and semantic-changing variations. They demonstrate that interventions at the representation level causally influence model outputs, reinforcing the role of invariant components. The results suggest that their geometric framework provides a robust method for understanding the organization of meaning in language models, although specific numerical results and effect sizes are not detailed in the summary.

**Limitations**  
The authors acknowledge that their framework is primarily exploratory and may not capture all aspects of semantic invariance in language models. They do not address potential limitations related to the generalizability of their findings across different model architectures or the scalability of their contrastive subspace discovery method. Additionally, the lack of detailed quantitative results may hinder the assessment of the practical impact of their contributions.

**Why it matters**  
This work has significant implications for the understanding of how language models encode and organize semantic information. By framing semantic invariance as a local geometric property, the authors provide a new perspective that could inform future research on model interpretability and robustness. The insights gained from this study may also enhance the development of more effective model attribution techniques, which are crucial for ensuring accountability in AI systems.

Authors: Agnibh Dasgupta, Abdullah Tanvir, Xin Zhong  
Source: arXiv:2605.06458  
URL: https://arxiv.org/abs/2605.06458v1
