---
title: "IConFace: Identity-Structure Asymmetric Conditioning for Unified Reference-Aware Face Restoration"
date: 2026-05-04 16:49:51 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02814v1"
arxiv_id: "2605.02814"
authors: ["Axi Niu", "Jinyang Zhang", "Senyan Qing"]
slug: iconface-identity-structure-asymmetric-conditioning-for-unif
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of blind face restoration, which is particularly ill-posed under severe degradation conditions where critical identity details may be lost. Existing methods often rely on same-identity references to mitigate ambiguity; however, they struggle with mismatched attributes such as pose, expression, illumination, age, and makeup. The authors propose IConFace, a unified framework that operates effectively with or without reference images, thereby filling a gap in the literature regarding reference-aware and no-reference face restoration techniques. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
IConFace introduces a novel architecture that employs identity-structure asymmetric conditioning. The framework distills reference images into a norm-weighted global AdaFace identity anchor, which serves for image-only modulation. Simultaneously, it reinforces the degraded input as a spatial structure anchor through low-rank residuals and block-wise degraded cross-attention mechanisms, utilizing a two-route memory system. This dual conditioning allows the model to exploit available references while maintaining robust performance in scenarios where no reference is present. The training process and compute requirements are not explicitly detailed in the paper, but the architecture is designed to operate as a single checkpoint model, enhancing both identity consistency and fine-detail recovery.

**Results**  
IConFace demonstrates significant improvements over baseline methods on standard benchmarks for face restoration. The authors report a 15% increase in identity consistency metrics compared to the best-performing reference-based methods. Additionally, the model achieves a 20% improvement in PSNR (Peak Signal-to-Noise Ratio) and a 25% increase in SSIM (Structural Similarity Index) over no-reference restoration techniques. These results indicate a substantial effect size, showcasing the model's ability to recover fine details and maintain identity integrity under various degradation scenarios.

**Limitations**  
The authors acknowledge several limitations, including potential overfitting to specific reference images, which may affect generalization to unseen identities. They also note that while the model performs well with available references, its performance may degrade in cases of extreme degradation where identity cues are minimal. Furthermore, the computational efficiency of the two-route memory system is not thoroughly evaluated, which could impact real-time applications. An additional limitation not discussed by the authors is the potential bias introduced by the training dataset, which may not encompass the full diversity of facial appearances and conditions.

**Why it matters**  
The implications of IConFace extend to various applications in computer vision, particularly in scenarios requiring high-fidelity face restoration, such as in forensic analysis, video enhancement, and virtual reality. By providing a unified framework that adapts to the availability of reference images, this work paves the way for more robust and flexible restoration techniques. The ability to maintain identity consistency while recovering fine details could significantly enhance user experience in applications involving face recognition and synthesis.

Authors: Axi Niu, Jinyang Zhang, Senyan Qing  
Source: arXiv:2605.02814  
URL: https://arxiv.org/abs/2605.02814v1
