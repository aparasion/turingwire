---
title: "GaitProtector: Impersonation-Driven Gait De-Identification via Training-Free Diffusion Latent Optimization"
date: 2026-05-12 17:27:56 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.12431v1"
arxiv_id: "2605.12431"
authors: ["Huiran Duan", "Qian Zhou", "Zhongliang Guo", "Junhao Dong", "Yuqi Li", "Guoying Zhao"]
slug: gaitprotector-impersonation-driven-gait-de-identification-vi
summary_word_count: 422
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
Conventional gait de-identification methods struggle with a trade-off between effective identity suppression and the introduction of spatiotemporal distortions, which can hinder downstream applications sensitive to structural integrity. This paper presents GaitProtector, addressing this gap by proposing a novel framework that integrates impersonation-driven techniques for gait de-identification. Notably, this work is a preprint and has not undergone peer review.

**Method**  
GaitProtector introduces a dual-component approach: (i) obfuscation, which repels the gait from the source identity, and (ii) impersonation, which attracts it toward a target identity. The target identity acts as a semantic anchor, guiding the optimization process towards structurally plausible gait patterns while leveraging a pretrained diffusion model. The method employs a training-free diffusion latent optimization pipeline, where input silhouette sequences are inverted into the latent space of a pretrained 3D video diffusion model. The optimization of latent codes is performed iteratively using a differentiable adversarial objective, allowing for the synthesis of protected gaits without the need for retraining a generator for each dataset.

**Results**  
GaitProtector was evaluated on the CASIA-B dataset, achieving a 56.7% impersonation success rate in a black-box gait recognition scenario. The method significantly reduced Rank-1 identification accuracy from 89.6% to 15.0%, indicating effective identity obfuscation. Additionally, the framework maintained favorable visual and temporal quality in the generated gaits. When assessed for downstream utility on the Scoliosis1K dataset, the diagnostic accuracy decreased from 91.4% to 74.2%, demonstrating that the method preserves essential gait characteristics while providing privacy protection.

**Limitations**  
The authors acknowledge that while GaitProtector effectively reduces identification accuracy, the impersonation success rate may still pose risks in certain contexts. Additionally, the reliance on a pretrained diffusion model may limit adaptability to diverse gait datasets with varying characteristics. The paper does not address potential computational overhead associated with the iterative optimization process, nor does it explore the implications of using different target identities on the obfuscation quality.

**Why it matters**  
GaitProtector represents a significant advancement in gait de-identification by leveraging pretrained 3D diffusion priors in a training-free manner, which could streamline the implementation of privacy-preserving technologies in real-world applications. The framework's ability to balance identity protection with the preservation of structural integrity opens avenues for further research in privacy-aware machine learning, particularly in sensitive domains such as healthcare and surveillance. This work sets a precedent for future studies to explore the integration of generative models in privacy protection tasks, potentially influencing the design of more robust and efficient de-identification methods.

Authors: Huiran Duan, Qian Zhou, Zhongliang Guo, Junhao Dong, Yuqi Li, Guoying Zhao, Yingli Tian  
Source: arXiv:2605.12431  
URL: https://arxiv.org/abs/2605.12431v1
