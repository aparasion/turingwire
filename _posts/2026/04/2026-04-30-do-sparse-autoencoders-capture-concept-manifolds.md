---
title: "Do Sparse Autoencoders Capture Concept Manifolds?"
date: 2026-04-30 17:08:07 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28119v1"
arxiv_id: "2604.28119"
authors: ["Usha Bhalla", "Thomas Fel", "Can Rager", "Sheridan Feucht", "Tal Haklay", "Daniel Wurgaft"]
slug: do-sparse-autoencoders-capture-concept-manifolds
summary_word_count: 500
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacy of sparse autoencoders (SAEs) in capturing the geometric structure of concepts, which are often organized along low-dimensional manifolds rather than independent linear directions. The authors identify a gap in the literature regarding the theoretical understanding of how SAEs can represent these manifolds and the conditions under which they do so. This work is crucial as it challenges the prevailing assumption that concepts can be effectively represented as isolated linear features, thereby prompting a reevaluation of representation learning methodologies.

**Method**  
The authors propose a theoretical framework that delineates two distinct mechanisms through which SAEs can capture manifolds: global and local representations. In the global approach, a compact group of atoms is allocated such that their linear span encompasses the entire manifold. Conversely, the local approach involves distributing the manifold representation across features that selectively tile specific regions of the underlying geometry. The authors empirically demonstrate that existing SAE architectures often exhibit a fragmented regime termed "dilution," where both global and local representations are mixed, leading to suboptimal recovery of continuous structures. The study emphasizes the need for post-hoc unsupervised discovery methods that focus on coherent groups of atoms rather than isolated directions, thereby enhancing the interpretability of learned representations.

**Results**  
The empirical findings reveal that SAEs struggle to effectively recover continuous manifold structures, with the dilution phenomenon leading to a fragmented representation. While specific quantitative results are not disclosed in the abstract, the authors suggest that the performance of SAEs is significantly hindered when compared to potential methods that could leverage coherent geometric representations. The implications of these findings indicate that current SAE architectures may not be fully utilizing the underlying geometric relationships present in the data, which could lead to less interpretable and less effective feature extraction.

**Limitations**  
The authors acknowledge that their framework does not provide a comprehensive solution to the problem of manifold representation in SAEs, and they highlight the need for further exploration into the conditions under which SAEs can effectively capture manifold structures. Additionally, the empirical validation of their theoretical claims may require more extensive experimentation across diverse datasets and architectures. An obvious limitation not explicitly mentioned is the potential computational overhead associated with implementing the proposed post-hoc discovery methods, which may not be feasible in all practical applications.

**Why it matters**  
This work has significant implications for the field of representation learning, as it advocates for a paradigm shift from viewing individual directions as the primary units of interpretability to considering geometric objects as fundamental components. By elucidating the limitations of current SAE architectures in capturing manifold structures, the authors pave the way for future research that could lead to more robust and interpretable models. This could enhance the applicability of representation learning in various domains, including computer vision and natural language processing, where understanding the underlying geometric relationships is crucial for model performance and interpretability.

Authors: Usha Bhalla, Thomas Fel, Can Rager, Sheridan Feucht, Tal Haklay, Daniel Wurgaft, Siddharth Boppana, Matthew Kowal et al.  
Source: arXiv:2604.28119  
URL: [https://arxiv.org/abs/2604.28119v1](https://arxiv.org/abs/2604.28119v1)
