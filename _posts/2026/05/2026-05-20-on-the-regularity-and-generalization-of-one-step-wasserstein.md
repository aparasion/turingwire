---
title: "On the Regularity and Generalization of One-Step Wasserstein-guided Generative Models for PDE-Induced Measures"
date: 2026-05-20 16:43:55 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21388v1"
arxiv_id: "2605.21388"
authors: ["Likun Lin", "Zhongjian Wang", "Jack Xin", "Zhiwen Zhang"]
slug: on-the-regularity-and-generalization-of-one-step-wasserstein
summary_word_count: 476
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in theoretical understanding of the statistical accuracy and generalization capabilities of generative models, particularly in the context of scientific computing. Despite the empirical success of these models, existing literature offers a pessimistic view regarding their performance in approximating probability measures induced by partial differential equations (PDEs). The authors propose a theoretical framework specifically for one-step Wasserstein-guided generative models, focusing on their application to PDE-induced measures. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution involves establishing a theoretical foundation for the regularity of transport maps and the generalization properties of one-step Wasserstein-guided generative models. The authors consider normalized target densities associated with linear elliptic and parabolic equations, as well as diffusion and Fokker-Planck equations on bounded domains and the torus. They prove that these target measures satisfy doubling conditions under standard structural assumptions. By leveraging regularity theory for optimal transport between doubling measures, the authors demonstrate that the optimal transport map from a uniform source measure to the target measure is Hölder continuous. This regularity provides an approximation-theoretic justification for one-step generative models, which learn PDE-induced distributions through a single pushforward map. The paper specifically analyzes the DeepParticle model, deriving excess-risk bounds that quantify the discrepancy between the learned map and the population-optimal map. Additionally, the authors establish robustness estimates under target shifts.

**Results**  
The theoretical results indicate that the one-step Wasserstein-guided generative models can achieve Hölder continuity in the transport maps, which is a significant finding for the approximation of PDE-induced measures. The authors provide empirical validation through experiments that support the derived rates, although specific numerical results and comparisons to named baselines are not detailed in the abstract. The excess-risk bounds derived for DeepParticle suggest that the model can effectively approximate the target distributions with controlled error rates, although exact figures are not provided in the summary.

**Limitations**  
The authors acknowledge that their theoretical framework relies on standard structural assumptions, which may not hold in all practical scenarios. Additionally, the empirical validation is limited to specific cases, and the generalizability of the results to more complex or high-dimensional PDEs remains an open question. The paper does not address potential computational inefficiencies or scalability issues associated with the one-step generative models, which could impact their applicability in real-world scenarios.

**Why it matters**  
This work has significant implications for the development of generative models in scientific computing, particularly in fields where PDEs are prevalent. By providing a theoretical basis for the regularity and generalization of one-step Wasserstein-guided models, the authors pave the way for more robust and reliable generative approaches to modeling complex distributions. This could enhance the applicability of generative models in simulations, data assimilation, and other areas where accurate representation of PDE-induced measures is critical.

Authors: Likun Lin, Zhongjian Wang, Jack Xin, Zhiwen Zhang  
Source: arXiv:2605.21388  
URL: [https://arxiv.org/abs/2605.21388v1](https://arxiv.org/abs/2605.21388v1)
