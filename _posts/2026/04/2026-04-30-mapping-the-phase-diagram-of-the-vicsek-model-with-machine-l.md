---
title: "Mapping the Phase Diagram of the Vicsek Model with Machine Learning"
date: 2026-04-30 17:52:23 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.28167v1"
arxiv_id: "2604.28167"
authors: ["Grace T. Bai", "Brandon B. Le"]
slug: mapping-the-phase-diagram-of-the-vicsek-model-with-machine-l
summary_word_count: 475
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the phase behavior of the Vicsek model, a well-known model for collective motion in biological systems. While previous studies have explored specific parameter regimes, a comprehensive mapping of the phase diagram across the three-dimensional parameter space defined by density (ρ), noise (η), and speed (v₀) remains underexplored. The authors aim to leverage machine learning techniques to classify and interpolate the phase structure, thereby providing a more complete representation of the phase behavior in this model.

**Method**  
The authors construct a dataset by simulating the Vicsek model across a grid of parameter points in the (η, ρ, v₀) space. For each parameter configuration, they compute long-time dynamical observables, which serve as features for classification. A K-Means clustering algorithm is employed to categorize each point into one of three phases: disorder, order, or coexistence. Subsequently, a neural network classifier is trained on the clustered labels, achieving a classification accuracy of 0.92. The architecture specifics of the neural network are not disclosed, nor is the compute resource used for training. The resulting phase map not only delineates the coexistence region but also extrapolates phase boundaries beyond the sampled simulation points, thus providing a more global perspective on the phase behavior.

**Results**  
The authors report a classification accuracy of 0.92 for the neural network classifier, indicating a robust mapping of the phase behavior. The phase diagram generated reveals a narrow coexistence region between ordered and disordered phases, which was not previously identified in earlier studies. The method successfully extends the inferred phase boundaries, suggesting that the machine learning approach can effectively interpolate phase behavior in regions where direct simulation data is sparse. The results demonstrate a significant improvement over traditional methods that rely solely on simulation data, highlighting the potential of machine learning in this domain.

**Limitations**  
The authors acknowledge that their approach is limited by the quality and density of the simulation data used for training. The reliance on K-Means clustering may also introduce biases based on the choice of the number of clusters, which is not explicitly justified in the paper. Additionally, the neural network architecture and hyperparameters are not detailed, which could affect reproducibility and generalization. The study does not address the scalability of the method to higher-dimensional parameter spaces or other collective motion models, which may limit its applicability.

**Why it matters**  
This work has significant implications for the study of collective motion and phase transitions in complex systems. By providing a systematic framework for mapping phase diagrams using machine learning, it opens avenues for exploring other models of collective behavior beyond the Vicsek model. The methodology can potentially be adapted to other physical systems where phase behavior is influenced by multiple parameters, thus enriching the toolkit available for researchers in statistical physics and related fields.

Authors: Grace T. Bai, Brandon B. Le  
Source: arXiv:2604.28167  
URL: https://arxiv.org/abs/2604.28167v1
