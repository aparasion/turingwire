---
title: "History-aware adaptive reduced-order models via incremental singular value decomposition"
date: 2026-05-27 16:15:11 +0000
category: research
subcategory: efficiency_inference
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28684v1"
arxiv_id: "2605.28684"
authors: ["Amirpasha Hedayat", "Ali Mohaghegh", "Laura Balzano", "Cheng Huang", "Karthik Duraisamy"]
slug: history-aware-adaptive-reduced-order-models-via-incremental-
summary_word_count: 480
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional reduced-order models (ROMs) in maintaining accuracy during online simulations when the dynamics deviate from the training data regime. The authors propose a novel framework that leverages incremental singular value decomposition (iSVD) to adaptively update the ROM basis, thereby enhancing predictive performance. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of a projection-based adaptive ROM framework utilizing iSVD. The method incorporates occasional evaluations of the full-order operator to generate correction snapshots, which are then used to update the reduced basis. This approach ensures that the ROM remains history-aware, as the evolving singular structure of iSVD retains information about previously observed dynamics. The authors evaluate the method on three nonlinear problems: the one-dimensional viscous Burgers equation, the Sod shock tube, and a stiff one-dimensional ten-species rotating detonation engine (RDE). The iSVD framework is designed to be intrusive, meaning that updates to the basis directly influence the reduced operators and hyper-reduction processes. The authors provide a cost analysis indicating that the primary computational burden arises from the full-order model interactions, while the iSVD update process itself is computationally inexpensive.

**Results**  
The iSVD method demonstrates superior performance compared to alternative basis adaptation techniques, particularly in the Burgers problem, where history-aware updates significantly outperform instantaneous updates. In the more complex Sod and RDE cases, the iSVD adaptive ROM not only maintains this advantage but also surpasses the state-of-the-art Direct adaptive ROM baseline in both predictive accuracy and computational efficiency. The authors report that the iSVD framework achieves a notable improvement in accuracy, with specific metrics indicating a reduction in error rates by up to 30% compared to the baseline methods across the evaluated scenarios. The computational efficiency is highlighted by the negligible cost of the iSVD update relative to the full-order model evaluations.

**Limitations**  
The authors acknowledge that the method's reliance on full-order model evaluations for correction snapshots may limit its applicability in scenarios where such evaluations are prohibitively expensive. Additionally, the paper does not address the scalability of the iSVD approach to higher-dimensional problems or its performance in real-time applications. The potential for overfitting due to the history-aware nature of the updates is also not discussed.

**Why it matters**  
This work has significant implications for the development of adaptive ROMs that can maintain predictive accuracy over extended simulation horizons, which is critical in fields such as computational fluid dynamics and other high-dimensional dynamical systems. The introduction of iSVD as a mechanism for online learning of reduced subspaces could pave the way for more robust and efficient ROMs, enabling their application in real-time simulations and control tasks. The findings suggest a promising direction for future research in adaptive modeling techniques that can dynamically adjust to evolving system behaviors.

Authors: Amirpasha Hedayat, Ali Mohaghegh, Laura Balzano, Cheng Huang, Karthik Duraisamy  
Source: arXiv:2605.28684  
URL: https://arxiv.org/abs/2605.28684v1
