---
title: "Colored Noise Diffusion Sampling"
date: 2026-05-28 17:58:13 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.30332v1"
arxiv_id: "2605.30332"
authors: ["Hadar Davidson", "Noam Issachar", "Sagie Benaim"]
slug: colored-noise-diffusion-sampling
summary_word_count: 398
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the existing literature on diffusion models, specifically the inefficiencies in stochastic differential equation (SDE) solvers that fail to leverage the spectral bias inherent in generative trajectories. Traditional SDE solvers inject uniform white noise throughout the sampling process, which does not align with the model's natural tendency to resolve low-frequency structures before high-frequency details. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework for SDE inference that emphasizes frequency-decoupled energy transfer, termed Colored Noise Sampling (CNS). CNS is a training-free stochastic solver that replaces the uniform white noise injection with a dynamic schedule that is both timestep- and frequency-dependent. This approach allows for a more efficient allocation of energy to unresolved frequency bands, effectively steering the generative process toward the true data manifold. The architecture is agnostic, demonstrating compatibility with various models, including SiT, JiT, and FLUX. The authors do not disclose specific training compute requirements, as CNS operates solely at inference time.

**Results**  
CNS demonstrates significant performance improvements over standard ODE and SDE baselines across multiple architectures. On the ImageNet-256 benchmark, CNS achieves unguided Fréchet Inception Distance (FID) reductions: from 8.26 to 6.27 on SiT-XL/2, from 32.39 to 26.69 on JiT-B/16, and from 11.88 to 8.31 on JiT-H/16. Additionally, CNS yields consistent relative FID improvements when combined with Classifier-Free Guidance, showcasing its effectiveness as a plug-and-play solution for enhancing image synthesis quality.

**Limitations**  
The authors acknowledge that while CNS improves sampling efficiency, it may not generalize equally well across all types of data distributions or model architectures. They do not address potential computational overhead introduced by the dynamic scheduling mechanism, nor do they explore the implications of using CNS in real-time applications. Furthermore, the lack of peer review raises questions about the robustness of the findings and the reproducibility of results.

**Why it matters**  
The introduction of CNS has significant implications for the field of generative modeling, particularly in enhancing the efficiency and quality of image synthesis. By aligning the sampling process with the spectral bias of diffusion models, CNS could lead to advancements in various applications, including image generation, video synthesis, and other domains where high-fidelity outputs are critical. This work opens avenues for further exploration of frequency-aware sampling techniques and their integration into existing generative frameworks.

Authors: Hadar Davidson, Noam Issachar, Sagie Benaim  
Source: arXiv:2605.30332  
URL: https://arxiv.org/abs/2605.30332v1
