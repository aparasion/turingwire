---
title: "Star-Fusion: A Multi-modal Transformer Architecture for Discrete Celestial Orientation via Spherical Topology"
date: 2026-04-29 12:01:41 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26582v1"
arxiv_id: "2604.26582"
authors: ["May Hammad", "Menatallh Hammad"]
slug: star-fusion-a-multi-modal-transformer-architecture-for-discr
summary_word_count: 409
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional "Lost-in-Space" (LIS) algorithms for celestial attitude determination, which are hindered by high computational overhead and sensitivity to sensor noise. The authors highlight that existing deep learning approaches often fail to account for the non-Euclidean topology of the celestial sphere and the periodic boundary conditions associated with Right Ascension (RA) and Declination (Dec). This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Star-Fusion, a multi-modal transformer architecture that reformulates the problem of orientation estimation as a discrete topological classification task. The architecture employs spherical K-Means clustering to segment the celestial sphere into K topologically consistent regions, effectively addressing coordinate wrapping artifacts. Star-Fusion utilizes a tripartite fusion strategy comprising: 
1. A SwinV2-Tiny transformer backbone for photometric feature extraction, which captures high-level visual features from input images.
2. A convolutional heatmap branch that provides spatial grounding by generating heatmaps for potential celestial object locations.
3. A coordinate-based Multi-Layer Perceptron (MLP) that anchors the geometric representation of celestial orientations. 
The model is trained on a synthetic dataset derived from Hipparcos data, although specific training compute details are not disclosed.

**Results**  
Star-Fusion achieves a Top-1 accuracy of 93.4% and a Top-3 accuracy of 97.8% on the synthetic Hipparcos-derived dataset. These results are benchmarked against traditional LIS algorithms, demonstrating a significant improvement in accuracy. Additionally, the model maintains an inference latency of 18.4 ms on commercial off-the-shelf (COTS) hardware, indicating its suitability for real-time applications in autonomous spacecraft navigation.

**Limitations**  
The authors acknowledge that the reliance on a synthetic dataset may limit the generalizability of the results to real-world scenarios, where sensor noise and environmental factors could introduce additional complexities. They do not address potential overfitting to the synthetic data or the scalability of the model to larger datasets. Furthermore, the computational efficiency, while promising, has not been validated across diverse hardware configurations or under varying operational conditions.

**Why it matters**  
The development of Star-Fusion has significant implications for the field of autonomous spacecraft navigation, particularly in enhancing the reliability and efficiency of celestial attitude determination. By addressing the challenges posed by non-Euclidean geometries and periodic boundary conditions, this work paves the way for more robust deep learning applications in space exploration. The architecture's real-time capabilities make it a strong candidate for integration into next-generation satellite constellations, potentially improving navigation accuracy and reducing the computational burden on onboard systems.

Authors: May Hammad, Menatallh Hammad  
Source: arXiv:2604.26582  
URL: [https://arxiv.org/abs/2604.26582v1](https://arxiv.org/abs/2604.26582v1)
