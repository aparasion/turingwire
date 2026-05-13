---
title: "Stories in Space: In-Context Learning Trajectories in Conceptual Belief Space"
date: 2026-05-12 17:09:41 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12412v1"
arxiv_id: "2605.12412"
authors: ["Eric Bigelow", "Rapha\u00ebl Sarfati", "Daniel Wurgaft", "Owen Lewis", "Thomas McGrath", "Jack Merullo"]
slug: stories-in-space-in-context-learning-trajectories-in-concept
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the latent hypothesis space utilized by Large Language Models (LLMs) during in-context learning. While LLMs exhibit dynamic behavior updates akin to Bayesian inference, the underlying structure of the belief space guiding these updates remains poorly characterized. The authors propose a novel framework that conceptualizes this space as a low-dimensional geometric manifold, thereby providing a structured interpretation of belief dynamics in LLMs.

**Method**  
The authors introduce a framework that models in-context learning as trajectories through a conceptual belief space. They employ a combination of behavioral and representational analyses to investigate these trajectories, particularly in the context of story understanding. The study utilizes linear probes to decode the internal representations of LLMs, allowing for the prediction of model behavior based on the geometry of the belief space. The authors also conduct interventions on these representations to assess their causal impact on belief trajectories. The specific architecture of the LLMs used is not disclosed, nor is the training compute, but the focus is on the geometric properties of the belief space rather than the models themselves.

**Results**  
The findings indicate that belief updates in LLMs can be effectively described as trajectories on low-dimensional, structured manifolds. The authors demonstrate that this geometric structure is consistently reflected in both the behavioral outputs of the models and their internal representations. Notably, the interventions on representations yield predictable changes in belief trajectories, affirming the hypothesis that the geometry of the conceptual space influences model behavior. While specific quantitative results (e.g., effect sizes or performance metrics) are not detailed in the abstract, the implications of the findings suggest a robust correlation between the geometric structure and the dynamics of belief updates.

**Limitations**  
The authors acknowledge that their framework is primarily exploratory and may not capture all aspects of belief dynamics in LLMs. They do not address potential limitations related to the generalizability of their findings across different LLM architectures or tasks beyond story understanding. Additionally, the reliance on linear probes may oversimplify the complexity of the internal representations, potentially overlooking non-linear relationships within the belief space.

**Why it matters**  
This work has significant implications for the understanding of in-context learning in LLMs, providing a geometric perspective that grounds Bayesian interpretations in structured conceptual representations. By elucidating the nature of belief trajectories, this research could inform the design of more interpretable and robust LLMs, enhancing their applicability in tasks requiring dynamic belief updates. Furthermore, the insights gained from this study may pave the way for future research exploring the intersection of geometry and learning dynamics in neural networks, potentially leading to advancements in model interpretability and performance.

Authors: Eric Bigelow, Raphaël Sarfati, Daniel Wurgaft, Owen Lewis, Thomas McGrath, Jack Merullo, Atticus Geiger, Ekdeep Singh Lubana  
Source: arXiv:2605.12412  
URL: [https://arxiv.org/abs/2605.12412v1](https://arxiv.org/abs/2605.12412v1)
