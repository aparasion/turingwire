---
title: "Quantum Feature Selection with Higher-Order Binary Optimization on Trapped-Ion Hardware"
date: 2026-04-29 16:01:39 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.26834v1"
arxiv_id: "2604.26834"
authors: ["Carlos Flores-Garrig\u00f3s", "Anton Simen", "Qi Zhang", "Enrique Solano", "Narendra N. Hegade", "Sayonee Ray"]
slug: quantum-feature-selection-with-higher-order-binary-optimizat
summary_word_count: 460
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional feature selection methods in machine learning, particularly those based on Quadratic Unconstrained Binary Optimization (QUBO). The authors propose a novel quantum feature-selection framework that utilizes a higher-order unconstrained binary optimization (HUBO) formulation, which incorporates multivariate dependencies through one-, two-, and three-body interaction terms. This approach aims to capture complex statistical relationships among features that standard QUBO methods overlook. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the HUBO model that integrates higher-order interactions derived from mutual information measures into the feature selection process. The objective function is designed to account for feature relevance, pairwise redundancy, and higher-order statistical structures. To mitigate the risk of trivial solutions where all features are selected, the authors introduce structured linear penalties that promote sparsity while retaining informative variables. The optimization of the HUBO instances is performed using digitized counterdiabatic quantum optimization on IonQ Forte, a trapped-ion quantum processor. The performance of this quantum approach is compared against noiseless quantum simulations and two classical baselines: SelectKBest based on mutual information and Principal Component Analysis (PCA).

**Results**  
The proposed quantum feature-selection framework was evaluated on two benchmark datasets: the Gallstone dataset and the Spambase dataset. The results indicate that the quantum method achieves competitive classification performance compared to the classical baselines. Specifically, the quantum approach not only produces compact and informative feature subsets but also demonstrates good qualitative agreement between hardware executions and noiseless simulations. The authors report that the quantum method effectively captures higher-order dependencies, which enhances the predictive performance of the selected feature subsets.

**Limitations**  
The authors acknowledge several limitations, including the reliance on specific quantum hardware (IonQ Forte), which may not be widely accessible. Additionally, the scalability of the HUBO approach to larger datasets and its performance under noisy conditions are not fully explored. The paper does not address the computational overhead associated with the digitized counterdiabatic optimization process, which may limit practical applications. Furthermore, the comparison with classical methods is limited to only two baselines, which may not represent the full spectrum of feature selection techniques available.

**Why it matters**  
This work has significant implications for the intersection of quantum computing and machine learning, particularly in the realm of feature selection. By demonstrating the feasibility of implementing higher-order feature-selection Hamiltonians on current trapped-ion processors, the authors pave the way for future research that could leverage quantum optimization techniques to enhance machine learning preprocessing tasks. The ability to capture complex feature interactions may lead to improved model performance and insights in various applications, from bioinformatics to natural language processing.

Authors: Carlos Flores-Garrigós, Anton Simen, Qi Zhang, Enrique Solano, Narendra N. Hegade, Sayonee Ray, Claudio Girotto, Jason Iaconis et al.  
Source: arXiv:2604.26834  
URL: https://arxiv.org/abs/2604.26834v1
