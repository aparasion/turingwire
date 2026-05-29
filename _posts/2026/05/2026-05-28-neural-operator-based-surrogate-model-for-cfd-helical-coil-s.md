---
title: "Neural Operator-Based Surrogate Model for CFD:Helical Coil Steam Generator in Small Modular Reactor"
date: 2026-05-28 17:33:22 +0000
category: research
subcategory: other
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30277v1"
arxiv_id: "2605.30277"
authors: ["Minseo Lee", "Seongmin Oh", "Chaehyeon Song", "Bumjin Cho", "Shilaj Baral", "Sangam Khanal"]
slug: neural-operator-based-surrogate-model-for-cfd-helical-coil-s
summary_word_count: 461
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the application of neural operator-based surrogate models for computational fluid dynamics (CFD) in the context of small modular reactors (SMRs), specifically for real-time thermal-hydraulic simulations. While AI-based surrogate modeling has been explored to reduce the computational burden of CFD, there has been a lack of studies focusing on transient analysis for SMR-specific geometries, particularly in the helical coil steam generator (HCSG) of the System-integrated Modular Advanced Reactor (SMART).

**Method**  
The authors propose an integrated framework that combines reduced-order modeling (ROM) with neural operators. Two distinct ROM strategies are employed: a multi-layer perceptron (MLP)-based autoencoder (AE) for unstructured mesh data and a convolutional autoencoder (CAE) for structured mesh data. Both strategies are coupled with a deep operator network (DeepONet) to form the latent DeepONet (L-DeepONet). Additionally, the Fourier neural operator (FNO) is utilized for comparative analysis. A multi-scale technique is incorporated into both frameworks to address spectral bias and enhance the prediction of Kármán vortex streets within the HCSG. The L-DeepONet effectively captures instantaneous periodic vortex dynamics in velocity and pressure fields, while the FNO and its multi-scale variant focus on time-averaged mean flow and pressure drop estimates.

**Results**  
The multi-scale L-DeepONet demonstrated superior performance in capturing the transient dynamics of the flow, achieving a significant reduction in prediction error for instantaneous velocity and pressure fields compared to the FNO. The authors report that the L-DeepONet outperformed the FNO in terms of temporal resolution, while the FNO provided reliable estimates for mean flow characteristics. Specific numerical results are not disclosed in the abstract, but the comparative analysis indicates that the choice of architecture should be aligned with the specific objectives of the digital twin application, depending on the CFD data type and required flow resolution.

**Limitations**  
The authors acknowledge that their study is limited to the specific geometry of the HCSG in SMRs and may not generalize to other reactor designs or fluid dynamics scenarios. Additionally, the computational efficiency of the proposed models in real-time applications is not quantitatively assessed. The reliance on specific neural network architectures may also introduce biases based on the training data and the inherent limitations of the surrogate modeling approach.

**Why it matters**  
This work has significant implications for the development of digital twin technologies in nuclear engineering, particularly for enhancing the operational safety and efficiency of SMRs. By providing a framework that links neural operator architectures to specific CFD data types and flow resolution requirements, this research paves the way for more effective real-time simulations in complex thermal-hydraulic systems. The findings could inform future research on surrogate modeling in other engineering domains where high-fidelity simulations are computationally prohibitive.

Authors: Minseo Lee, Seongmin Oh, Chaehyeon Song, Bumjin Cho, Shilaj Baral, Sangam Khanal, Minseop Song, Joongoo Jeon  
Source: arXiv:2605.30277  
URL: https://arxiv.org/abs/2605.30277v1
