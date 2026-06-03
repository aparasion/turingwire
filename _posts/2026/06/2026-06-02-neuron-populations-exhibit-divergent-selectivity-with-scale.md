---
title: "Neuron Populations Exhibit Divergent Selectivity with Scale"
date: 2026-06-02 17:59:52 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.03990v1"
arxiv_id: "2606.03990"
authors: ["Amil Dravid", "Yasaman Bahri", "Alexei A. Efros", "Yossi Gandelsman"]
slug: neuron-populations-exhibit-divergent-selectivity-with-scale
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper explores how neuron populations in neural networks evolve with scale, revealing a sublinear growth pattern and increased selectivity in Rosetta Neurons."
---

**Problem**  
This work addresses the gap in understanding how neuron populations within neural networks scale, particularly focusing on the behavior of Rosetta Neurons across different model sizes. Previous studies have primarily examined macroscopic metrics like loss, leaving a lack of insight into neuron-level dynamics as model size increases. The authors aim to extend scaling laws to encompass neuron selectivity and specialization, providing a more granular view of neural network behavior. This is a preprint and has not yet undergone peer review.

**Method**  
The authors analyze Rosetta Neurons, a class of neurons identified in prior research (Dravid et al., 2023), across language models with up to 30 billion parameters and vision models with up to 5 billion parameters. They employ an analytical model that balances feature utility against neuron capacity to explain observed phenomena. The study reveals that the population of Rosetta Neurons grows according to a sublinear power law, indicating that while the absolute number of these neurons increases, they occupy a diminishing fraction of the total neuron count. The authors also introduce the Neuron Polarization Effect, where Rosetta Neurons become more selective and monosemantic as model size increases, diverging from a larger, less selective non-Rosetta population.

**Results**  
The findings indicate that Rosetta Neurons exhibit a sublinear growth pattern, with their proportion of the total neuron count decreasing as model size increases. Specifically, the study quantifies that the selectivity of Rosetta Neurons increases significantly, with a marked distinction from non-Rosetta neurons. The targeted data-filtering case study demonstrates that Rosetta Neurons become more domain-specialized with scale, suggesting a systematic change in neuron universality and specialization. The results provide a quantitative framework for understanding neuron behavior in large-scale models, although specific numerical results and effect sizes are not detailed in the abstract.

**Limitations**  
The authors acknowledge that their analysis is limited to specific model architectures and sizes, which may not generalize across all neural network types. Additionally, the study does not explore the implications of these findings on downstream tasks or the potential for transfer learning. The analytical model, while insightful, may oversimplify the complexities of neuron interactions and their contributions to overall model performance.

**Why it matters**  
This research has significant implications for the design and interpretation of large-scale neural networks. By elucidating the scaling behavior of neuron populations, it provides a framework for understanding how model size influences neuron selectivity and specialization, which can inform future architectural choices and training strategies. The findings suggest that as models scale, the interpretability of neuron functions may improve, potentially leading to more effective and efficient training paradigms. This work contributes to the ongoing discourse on scaling laws in deep learning, as published in [arXiv](https://arxiv.org/abs/2606.03990v1).
