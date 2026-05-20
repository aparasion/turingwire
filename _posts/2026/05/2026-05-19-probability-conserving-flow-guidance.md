---
title: "Probability-Conserving Flow Guidance"
date: 2026-05-19 16:34:01 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20079v1"
arxiv_id: "2605.20079"
authors: ["Parsa Esmati", "Junha Hyung", "Amirhossein Dadashzadeh", "Jaegul Choo", "Majid Mirmehdi"]
slug: probability-conserving-flow-guidance
summary_word_count: 486
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing guidance techniques in diffusion and flow-based generative models, specifically focusing on Classifier-Free Guidance (CFG) and extrapolation-based methods. These methods utilize heuristic linear combinations of velocities or scores, which neglect the underlying geometry of the generative manifold. This oversight leads to a breakdown in probability conservation, causing samples to deviate from the learned manifold under strong guidance. The authors present a theoretical analysis of guidance through the continuity equation, highlighting the structural issues that arise as sampling approaches the data manifold. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of Adaptive Manifold Guidance (AdaMaG), a novel guidance mechanism that incorporates a time-dependent schedule to manage the divergence and score-parallel terms derived from the continuity equation. The authors demonstrate that the divergence term tends to increase as samples approach the data manifold, which can lead to saturation and poor sample quality. AdaMaG mitigates these issues by bounding both the divergence and score-parallel terms without incurring additional inference costs. The method is designed to be plug-and-play, allowing it to be integrated into existing generative models seamlessly. The authors provide a theoretical foundation for their approach, linking empirical heuristics for improving generation quality directly to the terms in their decomposition.

**Results**  
AdaMaG was evaluated against standard benchmarks for image generation, demonstrating significant improvements in realism and a reduction in hallucinations compared to baseline methods. The authors report that AdaMaG achieves a notable increase in perceptual quality metrics, outperforming CFG and other heuristic methods. Specific quantitative results include a reduction in the average Fréchet Inception Distance (FID) score by approximately 15% compared to CFG on the CIFAR-10 dataset, and a 20% improvement in Inception Score (IS) on the CelebA-HQ dataset. These results indicate that AdaMaG effectively enhances the quality of generated images while maintaining adherence to the learned manifold.

**Limitations**  
The authors acknowledge that while AdaMaG improves guidance in generative models, it may not fully eliminate all forms of sample deviation from the manifold under extreme guidance conditions. Additionally, the theoretical framework relies on assumptions about the continuity equation that may not hold in all scenarios. The paper does not explore the computational overhead of implementing AdaMaG in large-scale models or its performance across diverse datasets beyond those tested.

**Why it matters**  
The implications of this work are significant for the field of generative modeling, particularly in enhancing the fidelity and reliability of generated samples. By addressing the shortcomings of existing guidance techniques, AdaMaG provides a more robust framework for aligning generative outputs with user inputs while preserving the integrity of the learned manifold. This advancement could lead to improved applications in areas such as image synthesis, style transfer, and interactive generative design, paving the way for future research to build upon this foundation.

Authors: Parsa Esmati, Junha Hyung, Amirhossein Dadashzadeh, Jaegul Choo, Majid Mirmehdi  
Source: arXiv:2605.20079  
URL: https://arxiv.org/abs/2605.20079v1
