---
title: "Bias Leaves a Gradient Trail: Label-Free Bias Identification via Gradient Probes on Concept Decompositions"
date: 2026-05-27 17:39:10 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.28780v1"
arxiv_id: "2605.28780"
authors: ["Thomas Vitry", "Kieran Edgeworth", "Stefan Wermter", "Jae Hee Lee"]
slug: bias-leaves-a-gradient-trail-label-free-bias-identification-
summary_word_count: 484
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in bias identification methodologies for vision classifiers, particularly focusing on the limitations of existing techniques that rely on curated datasets, spurious-attribute labels, or retraining. These methods can be impractical for deployed models or when the specific biases are unknown. The authors propose a novel, label-free approach for post-hoc bias identification in frozen vision models, which is particularly relevant given the increasing deployment of AI systems in real-world applications where biases can lead to significant ethical and performance issues. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a method that leverages non-negative matrix factorization (NMF) on intermediate activations of a vision model to extract interpretable concept vectors from patches of inputs predicted as a target class. The core technical contribution is the development of a bias estimator that ranks candidate concepts based on their interaction with backpropagated gradients from misclassified examples. Specifically, concepts that are activated during the correction of false negatives are identified as potential bias indicators, while those activated during false positives are suppressed. The method operates solely on standard class labels from a held-out audit dataset, making it applicable to a wide range of scenarios without requiring additional data or model retraining.

**Results**  
The proposed method was evaluated on three benchmarks: Colored MNIST, Waterbirds, and CelebA. On Colored MNIST and Waterbirds, the method successfully identified concepts aligned with known spurious cues. Notably, suppressing the top-ranked bias concepts during inference led to significant improvements in worst-group accuracy: up to 17.9 percentage points on Waterbirds and 10.4 percentage points on CelebA. These results demonstrate the effectiveness of the method in enhancing model robustness against spurious correlations without necessitating retraining or parameter updates.

**Limitations**  
The authors acknowledge that their approach may not generalize to all types of biases, particularly those that are more complex or less interpretable. Additionally, the reliance on backpropagated gradients may introduce noise in the bias estimation process, especially in models with intricate architectures. The method's performance is contingent on the quality of the audit dataset, and the authors do not explore the implications of varying dataset sizes or distributions on the bias identification process. Furthermore, the method's applicability to other domains beyond vision tasks remains untested.

**Why it matters**  
This work has significant implications for the field of machine learning, particularly in the context of deploying AI systems in sensitive applications. By providing a label-free, interpretable method for bias identification, the authors enable practitioners to audit and mitigate biases in frozen models without the need for extensive retraining or additional data collection. This approach not only enhances the interpretability of model decisions but also contributes to the development of more equitable AI systems. The findings encourage further exploration of gradient-based techniques for bias analysis across various domains and model architectures.

Authors: Thomas Vitry, Kieran Edgeworth, Stefan Wermter, Jae Hee Lee  
Source: arXiv cs.CV  
URL: [https://arxiv.org/abs/2605.28780v1](https://arxiv.org/abs/2605.28780v1)
