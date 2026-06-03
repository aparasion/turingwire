---
title: "Correcting Neural Operator Spectral Bias via Diffusion Posterior Sampling with Sparse Observations"
date: 2026-06-02 17:26:15 +0000
category: research
subcategory: other
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.03936v1"
arxiv_id: "2606.03936"
authors: ["Niccol\u00f2 Perrone", "Fanny Lehmann", "Stefania Fresca", "Filippo Gatti"]
slug: correcting-neural-operator-spectral-bias-via-diffusion-poste
summary_word_count: 430
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces FreqNO-DPS, a method that mitigates spectral bias in neural operator surrogates using diffusion posterior sampling with sparse observations."
---

**Problem**  
Neural operator surrogates (NO) are effective for approximating solutions to partial differential equations (PDEs) but exhibit spectral bias, particularly in high-frequency content, which limits their applicability in scenarios requiring fine-scale resolution. This paper addresses the gap in the literature regarding the correction of spectral bias in NOs, particularly when only sparse sensor measurements are available. The authors propose a novel approach to integrate these sparse observations into the NO framework, enhancing the fidelity of predictions without relying on extensive numerical simulations. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors introduce FreqNO-DPS, which combines an unconditional score-based diffusion prior trained on high-fidelity simulations with diffusion posterior sampling (DPS) conditioned on sparse observations. The method employs a frozen neural operator to guide the sampling process. A key innovation is the development of a closed-form, spectrally shaped guidance score that adjusts the surrogate's predictions based on frequency-dependent accuracy, eliminating the need for denoiser backpropagation. The framework requires only paired surrogate/reference data and leverages the approximate spectral diagonality of the residuals, which can be verified for new surrogates using a coherence diagnostic provided by the authors.

**Results**  
FreqNO-DPS was evaluated on 3D elastic wavefield predictions with sensor coverage at 5% and 2%. The method achieved near-zero spectral bias across all frequency bands, significantly outperforming both the original surrogate and sensor-only DPS approaches, which exhibited systematic high-frequency attenuation. The isotropic guidance baseline improved pointwise accuracy but failed to mitigate the spectral bias effectively, underscoring the necessity of frequency-dependent calibration. The results indicate a substantial improvement in the fidelity of NO predictions when integrating sparse observations through the proposed framework.

**Limitations**  
The authors acknowledge that the method's performance is contingent on the quality of the paired surrogate/reference data. Additionally, while the framework is designed to be broadly applicable, it may require adjustments for specific PDE problems that do not conform to the assumptions of approximate spectral diagonality. The reliance on high-fidelity simulations for training the diffusion prior may also limit the method's scalability in scenarios where such data is scarce.

**Why it matters**  
The proposed FreqNO-DPS framework represents a significant advancement in the field of neural operators by effectively addressing spectral bias, which is critical for applications requiring high-resolution predictions from sparse data. This work opens avenues for further research into the integration of machine learning techniques with traditional numerical methods, potentially enhancing the reliability of surrogate models in various scientific and engineering domains. The implications of this research are substantial, as it provides a robust methodology for improving the accuracy of NOs, as published in [arXiv](https://arxiv.org/abs/2606.03936v1).
