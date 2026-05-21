---
title: "Velocityformer: Broken-Symmetry-Matched Equivariant Graph Transformers for Cosmological Velocity Reconstruction"
date: 2026-05-20 17:59:05 +0000
category: research
subcategory: theory
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.21483v1"
arxiv_id: "2605.21483"
authors: ["Tilman Tr\u00f6ster", "David Mirkovic", "Veronika Oehl", "Arne Thomsen"]
slug: velocityformer-broken-symmetry-matched-equivariant-graph-tra
summary_word_count: 454
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of accurately reconstructing galaxy velocities from spectroscopic surveys to measure the kinematic Sunyaev-Zel'dovich (kSZ) effect, which is crucial for understanding the large-scale distribution of baryonic matter in cosmology. The existing methods struggle with the broken symmetry in observational data due to the preferred line-of-sight direction, which affects the signal-to-noise ratio (SNR) of kSZ measurements. The authors identify a gap in the literature regarding the application of equivariant models that can effectively handle this broken symmetry while maintaining high data efficiency.

**Method**  
The core technical contribution is the Velocityformer, an equivariant graph transformer architecture specifically designed to align with the broken symmetry of the observational data. The architecture incorporates inductive biases that reflect the underlying physics of the problem, particularly focusing on translational and rotational equivariance. The model is trained using a combination of low-fidelity simulations and high-fidelity simulated galaxy catalogues, leveraging only 4 low-fidelity simulations to achieve high accuracy. The training process emphasizes conditioning on the physics-based long-wavelength solution, enhancing data efficiency and generalization capabilities across various input geometries, cosmological parameters, and galaxy samples.

**Results**  
Velocityformer demonstrates a significant improvement in the correlation coefficient \( r \) between reconstructed and true velocities, achieving a 35% increase over the standard linear theory baseline. It consistently outperforms machine learning baselines across all tested data volumes. Specifically, on high-fidelity simulated galaxy catalogues, Velocityformer achieves a 30% improvement in \( r \) compared to the physical baseline, which translates directly to a similar gain in SNR for observational data. These results indicate that the model not only enhances reconstruction accuracy but also provides robust performance across diverse conditions.

**Limitations**  
The authors acknowledge that the model's performance is contingent on the quality of the low-fidelity simulations used for training. Additionally, while the model generalizes well, its performance on real observational data remains to be fully validated. The paper does not address potential limitations related to the scalability of the model to larger datasets or the computational costs associated with training on high-fidelity simulations. Furthermore, the reliance on specific simulation parameters may limit the model's applicability to other cosmological scenarios.

**Why it matters**  
The development of Velocityformer has significant implications for cosmological research, particularly in enhancing the precision of kSZ measurements, which are vital for understanding the distribution of baryonic matter. By effectively addressing the broken symmetry in observational data, this work paves the way for more accurate cosmological inferences and could influence future methodologies in velocity reconstruction. The model's data efficiency and generalization capabilities also suggest potential applications in other areas of astrophysics and beyond, where equivariant models can be leveraged to improve performance in the presence of complex symmetries.

Authors: Tilman Tröster, David Mirkovic, Veronika Oehl, Arne Thomsen  
Source: arXiv:2605.21483  
URL: https://arxiv.org/abs/2605.21483v1
