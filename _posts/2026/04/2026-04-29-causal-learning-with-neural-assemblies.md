---
title: "Causal Learning with Neural Assemblies"
date: 2026-04-29 17:34:33 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26919v1"
arxiv_id: "2604.26919"
authors: ["Evangelia Kopadi", "Dimitris Kalles"]
slug: causal-learning-with-neural-assemblies
summary_word_count: 415
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the ability of Neural Assemblies—groups of neurons that co-activate and strengthen through local plasticity—to learn and internalize causal directionality between variables. While neural assemblies have been established as effective computational substrates for various tasks, their capacity to discern causal relationships has not been previously demonstrated. This work aims to bridge this gap by providing a mechanism that allows for the learning of directed causal influences.

**Method**  
The authors introduce a novel mechanism called DIRECT (DIRectional Edge Coupling/Training), which facilitates the co-activation of source and target neural assemblies through an adaptive gain schedule. This method leverages the inherent operations of neural assemblies, including projection, local plasticity control, and sparse winner selection, to achieve directional learning without relying on backpropagation. The training process emphasizes local plasticity, which enhances the interpretability of causal claims by making them auditable at the mechanism level. The authors validate their approach using a dual-readout strategy that includes: (i) synaptic-strength asymmetry, which measures the weight differences between forward and reverse connections, and (ii) functional propagation overlap, which assesses the reliability of directional signal flow.

**Results**  
The framework demonstrates perfect structural recovery in a supervised setting with known structures across multiple domains. The authors report significant improvements in causal inference capabilities compared to traditional backpropagation-based methods, although specific baseline models and quantitative metrics are not detailed in the abstract. The results indicate that the proposed method effectively captures causal directionality, as evidenced by the emergent synaptic asymmetries and reliable signal propagation.

**Limitations**  
The authors acknowledge that their approach is primarily validated in controlled environments with known structures, which may limit its generalizability to more complex, real-world scenarios. Additionally, the reliance on local plasticity may restrict the learning capacity compared to global optimization techniques. The paper does not address potential scalability issues or the computational overhead associated with the adaptive gain scheduling in larger networks.

**Why it matters**  
This work has significant implications for the fields of causal inference and explainable AI. By establishing neural assemblies as a biologically plausible framework for learning causal relationships, the authors provide a pathway for integrating neuroscience-inspired models into formal causal reasoning frameworks. The "explainable by design" aspect of the proposed method enhances the interpretability of neural networks, making it easier to trace causal claims back to specific neural activities and synaptic configurations. This could lead to advancements in areas such as decision-making systems, where understanding causal influences is critical.

Authors: Evangelia Kopadi, Dimitris Kalles  
Source: arXiv:2604.26919  
URL: https://arxiv.org/abs/2604.26919v1
