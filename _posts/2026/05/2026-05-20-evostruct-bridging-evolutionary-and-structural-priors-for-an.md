---
title: "EvoStruct: Bridging Evolutionary and Structural Priors for Antibody CDR Design via Protein Language Model Adaptation"
date: 2026-05-20 17:59:16 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.21485v1"
arxiv_id: "2605.21485"
authors: ["Mansoor Ahmed", "Sujin Lee", "Umar Khayaz", "Murray Patterson"]
slug: evostruct-bridging-evolutionary-and-structural-priors-for-an
summary_word_count: 416
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing equivariant graph neural network (GNN) methods in antibody complementarity-determining region (CDR) design, specifically the issue of vocabulary collapse. Current GNN approaches tend to over-predict certain amino acids, such as tyrosine and glycine, while neglecting functionally significant residues. The authors identify that this failure stems from GNN encoders learning amino acid distributions from limited structural data, which leads to the omission of evolutionary substitution patterns present in evolutionary databases.

**Method**  
The authors propose EvoStruct, a novel framework that integrates a frozen protein language model (PLM) with 3D structural information from an E(3)-equivariant GNN through a cross-attention adapter. This architecture is designed to specifically address the vocabulary collapse issue in CDR design. EvoStruct employs a progressive unfreezing strategy for the PLM, allowing it to adaptively learn from the structural context while maintaining the evolutionary information. Additionally, the method incorporates R-Drop consistency regularization to enhance robustness during training. The training compute details are not disclosed, but the architecture leverages existing PLM capabilities alongside GNN structural representations.

**Results**  
EvoStruct demonstrates significant improvements on the CHIMERA-Bench dataset, achieving a 16% increase in sequence recovery and a 43% reduction in perplexity compared to the best-performing GNN baselines. Furthermore, it recovers 2.3 times greater amino acid diversity and exhibits the highest binding-pair correlation with ground truth data among various antibody design methods. These results indicate a substantial advancement in both the accuracy and diversity of CDR designs, showcasing EvoStruct's effectiveness in overcoming the limitations of prior approaches.

**Limitations**  
The authors acknowledge that while EvoStruct improves upon existing methods, it may still be constrained by the quality and comprehensiveness of the structural data used for training. Additionally, the reliance on a frozen PLM could limit the adaptability of the model to novel sequences not represented in the training data. The paper does not discuss potential scalability issues or the computational overhead introduced by the cross-attention mechanism, which could impact deployment in resource-constrained environments.

**Why it matters**  
The implications of this work are significant for the field of antibody design and protein engineering. By effectively bridging evolutionary and structural priors, EvoStruct not only enhances the accuracy of CDR design but also promotes greater diversity in amino acid selection, which is crucial for developing therapeutically relevant antibodies. This approach could pave the way for more sophisticated models that integrate multiple sources of biological knowledge, potentially leading to breakthroughs in protein design and synthetic biology applications.

Authors: Mansoor Ahmed, Sujin Lee, Umar Khayaz, Murray Patterson  
Source: arXiv:2605.21485  
URL: https://arxiv.org/abs/2605.21485v1
