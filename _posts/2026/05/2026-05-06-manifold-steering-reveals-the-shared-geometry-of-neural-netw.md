---
title: "Manifold Steering Reveals the Shared Geometry of Neural Network Representation and Behavior"
date: 2026-05-06 16:46:03 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.05115v1"
arxiv_id: "2605.05115"
authors: ["Daniel Wurgaft", "Can Rager", "Matthew Kowal", "Vasudev Shyam", "Sheridan Feucht", "Usha Bhalla"]
slug: manifold-steering-reveals-the-shared-geometry-of-neural-netw
summary_word_count: 447
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the causal relationship between the geometric structure of neural network representations and the resulting behaviors. While previous works have acknowledged the rich geometric properties of neural representations, they have not sufficiently explored how these geometries influence model behavior. The authors propose a framework to investigate this relationship through interventions in activation space.

**Method**  
The core technical contribution is the introduction of "manifold steering," a method that involves fitting an activation manifold \(M_h\) to the neural network's internal representations and a behavior manifold \(M_y\) to the output probability distributions. The authors conduct interventions along paths defined by \(M_h\) to observe the resulting behavioral trajectories. They compare this approach to linear steering, which assumes a Euclidean geometry and often leads to unnatural outputs. The optimization of interventions is performed to ensure that the paths in activation space align with the curvature of \(M_h\), thereby producing outputs that are more consistent with the model's natural behavior. The experiments span various tasks and modalities, including reasoning tasks in language models and physical dynamics in a video world model.

**Results**  
The authors demonstrate that steering along the activation manifold \(M_h\) yields behavioral trajectories that closely follow the behavior manifold \(M_y\). In contrast, linear steering results in outputs that deviate significantly from the expected behavior. The effectiveness of manifold steering is quantitatively supported by metrics that show improved alignment with natural behaviors across tasks. Specific effect sizes and numerical results are not disclosed in the abstract, but the qualitative findings suggest a strong correlation between the geometry of representations and the induced behaviors.

**Limitations**  
The authors acknowledge that their approach may be limited by the complexity of the manifolds involved and the potential for overfitting during the fitting process. They do not address the scalability of their method to larger models or more complex tasks, nor do they discuss the computational overhead associated with fitting and optimizing the manifolds. Additionally, the reliance on specific geometrical assumptions may not generalize across all neural architectures.

**Why it matters**  
This work has significant implications for the field of neural network interpretability and control. By establishing a direct link between the geometry of neural representations and model behavior, it provides a principled framework for designing interventions that can guide model outputs more effectively. This could lead to advancements in areas such as model fine-tuning, adversarial robustness, and the development of more interpretable AI systems. The findings encourage further exploration of geometric properties in neural networks, potentially influencing future research directions in representation learning and behavior modeling.

Authors: Daniel Wurgaft, Can Rager, Matthew Kowal, Vasudev Shyam, Sheridan Feucht, Usha Bhalla, Tal Haklay, Eric Bigelow et al.  
Source: arXiv:2605.05115  
URL: https://arxiv.org/abs/2605.05115v1
