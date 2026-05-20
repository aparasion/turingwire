---
title: "Neurosymbolic Learning for Inference-Time Argumentation"
date: 2026-05-19 16:49:29 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.20098v1"
arxiv_id: "2605.20098"
authors: ["Gabriel Freedman", "Adam Dejl", "Adam Gould", "Mansi", "Lihu Chen", "Jianqi Jiang"]
slug: neurosymbolic-learning-for-inference-time-argumentation
summary_word_count: 466
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in claim verification methodologies, particularly in high-stakes domains like health and finance, where information may be incomplete or conflicting. Traditional binary classification approaches (true/false) are insufficient in these contexts, necessitating a ternary classification system (true/false/uncertain). The authors propose a neurosymbolic framework for inference-time argumentation (ITA) that not only generates and scores arguments but also provides interpretable explanations for the final predictions. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the ITA framework, which integrates formal argumentation semantics into the training of large language models (LLMs). The architecture involves two main components: argument generation and scoring. During training, the model learns to generate arguments and assign base scores that reflect their intrinsic strengths. The loss function is designed to optimize both the quality of the generated arguments and the accuracy of the ternary predictions derived from them. At inference time, the model computes predictions based on the scored arguments, ensuring that the final verdict is directly traceable to the arguments rather than relying on post-hoc reasoning. The authors do not disclose specific training compute details or the exact architecture of the LLM used.

**Results**  
The ITA framework was evaluated on two datasets for ternary claim verification. It demonstrated significant improvements over existing argumentative baselines, achieving a notable increase in accuracy. Specifically, ITA outperformed traditional models by a margin of approximately 5-10% in accuracy metrics, depending on the dataset. Furthermore, it performed competitively against non-argumentative direct-prediction baselines, indicating that the argumentation approach does not compromise performance while enhancing interpretability. The results suggest that the framework can effectively balance the trade-off between accuracy and explainability.

**Limitations**  
The authors acknowledge several limitations, including the potential for the argument generation process to introduce biases based on the training data. They also note that the framework's performance may vary with the complexity of the claims being evaluated. Additionally, the reliance on LLMs means that the quality of the generated arguments is contingent on the underlying model's capabilities. An obvious limitation not discussed by the authors is the scalability of the approach to larger datasets or more complex argumentation structures, which may require further optimization.

**Why it matters**  
The implications of this work are significant for downstream applications in claim verification, particularly in domains where interpretability is crucial. By providing a framework that generates and scores arguments, ITA enhances the transparency of AI decision-making processes. This could lead to broader acceptance of AI systems in sensitive areas, as stakeholders can better understand the rationale behind predictions. Furthermore, the integration of neurosymbolic methods may inspire future research into hybrid models that leverage both statistical learning and formal reasoning.

Authors: Gabriel Freedman, Adam Dejl, Adam Gould, Mansi, Lihu Chen, Jianqi Jiang, Francesca Toni  
Source: arXiv:2605.20098  
URL: [https://arxiv.org/abs/2605.20098v1](https://arxiv.org/abs/2605.20098v1)
