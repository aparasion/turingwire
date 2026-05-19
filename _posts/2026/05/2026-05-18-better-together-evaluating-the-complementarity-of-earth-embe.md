---
title: "Better Together: Evaluating the Complementarity of Earth Embedding Models"
date: 2026-05-18 17:10:13 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.18667v1"
arxiv_id: "2605.18667"
authors: ["Thijs L van der Plas", "Jacob JW Bakermans", "Vishal Nedungadi", "Gabriel\u0117 Tij\u016bnaityt\u0117", "Marc Ru\u00dfwurm", "Ioannis N Athanasiadis"]
slug: better-together-evaluating-the-complementarity-of-earth-embe
summary_word_count: 467
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the evaluation of Earth embedding models, which are designed to convert Earth observation data into spatially relevant embeddings. Traditionally, these models have been assessed in isolation, focusing on their individual performance on downstream tasks. This approach neglects the potential benefits of fusing multiple embeddings, which could yield richer, more informative representations. The authors propose a framework to evaluate the complementarity of these embeddings, emphasizing the performance improvements achievable through their integration.

**Method**  
The authors introduce an embedding complementarity index that quantifies the performance gain from fusing multiple Earth embeddings compared to the best-performing single model. They evaluate four distinct Earth embedding models: AlphaEarth, Tessera, GeoCLIP, and SatCLIP. The evaluation is conducted across six downstream tasks, including land cover classification and regression. The models are assessed in isolation, in all possible pairs, and in a joint configuration. The training compute details are not disclosed, but the methodology emphasizes the systematic exploration of embedding combinations to identify optimal fusions. The complementarity index serves as a versatile metric applicable to any embedding and task, facilitating a comprehensive analysis of model interactions.

**Results**  
The results indicate that fused embeddings outperform the best single model in four out of six evaluated tasks, demonstrating the underappreciated capabilities of Earth embeddings when considered in isolation. Specifically, the authors report that the complementarity effect is both task- and location-dependent, suggesting that the benefits of fusion vary based on the specific characteristics of the tasks and the spatial context. For the land cover regression task, the authors observe that the degree of complementarity is influenced by the spatial scale of the land cover classes, indicating a nuanced relationship between embedding fusion and task requirements.

**Limitations**  
The authors acknowledge that their findings are contingent on the specific models and tasks evaluated, which may limit the generalizability of the results. They do not address potential computational overhead associated with fusing multiple embeddings, which could impact real-time applications. Additionally, the study does not explore the implications of embedding quality or the potential for overfitting when combining models, which could skew performance metrics. The absence of a comprehensive analysis of the computational efficiency of the proposed methods is another notable limitation.

**Why it matters**  
This work has significant implications for the future of Earth observation modeling. By reframing the evaluation of Earth embeddings to focus on their complementarity, the authors suggest that the most substantial advancements in performance may arise from strategic combinations of models rather than the development of superior individual embeddings. This perspective encourages researchers to explore multi-embedding strategies, potentially leading to more robust and effective applications in various domains, including environmental monitoring, urban planning, and disaster response.

Authors: Thijs L van der Plas, Jacob JW Bakermans, Vishal Nedungadi, Gabrielė Tijūnaitytė, Marc Rußwurm, Ioannis N Athanasiadis  
Source: arXiv:2605.18667  
URL: https://arxiv.org/abs/2605.18667v1
