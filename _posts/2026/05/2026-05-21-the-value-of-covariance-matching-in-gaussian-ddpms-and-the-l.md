---
title: "The Value of Covariance Matching in Gaussian DDPMs and the Lanczos Sampler"
date: 2026-05-21 16:57:27 +0000
category: research
subcategory: efficiency_inference
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22723v1"
arxiv_id: "2605.22723"
authors: ["Md Sahil Akhtar", "Aymane El Gadarri", "Vivek F. Farias", "Adam D. Jozefiak"]
slug: the-value-of-covariance-matching-in-gaussian-ddpms-and-the-l
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the performance of Gaussian Denoising Diffusion Probabilistic Models (DDPMs) by focusing on the path-space KL divergence between the exact reverse chain and the learned Gaussian reverse process. The authors highlight that existing isotropic reverse covariances incur a path-KL error of \(Ω(1/T)\) as the number of denoising steps \(T\) increases, which limits the effectiveness of techniques like classifier guidance that perturb the entire reverse trajectory. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of full posterior covariance matching, which significantly reduces the path-KL error to \(O(1/T^2)\). To facilitate practical implementation, the authors propose the Lanczos Gaussian Sampler (LGS), a training-free and matrix-free method for sampling from the optimal reverse covariance. LGS operates using covariance-vector products derived from Jacobian-vector products of the posterior mean, thus avoiding the need for dense covariance storage or auxiliary covariance models. The authors demonstrate that the approximation error of LGS decays exponentially with the number of Lanczos steps, where each step requires only a single Jacobian-vector product. This method allows for efficient sampling while maintaining high sample quality.

**Results**  
Empirical evaluations show that LGS, utilizing just three Lanczos steps, outperforms strong diagonal-covariance baselines, including OCM-DDPM, across standard image benchmarks. The authors report significant improvements in sample quality, although specific quantitative metrics (e.g., FID scores) are not detailed in the abstract. The results indicate that full covariance matching not only enhances theoretical understanding but also translates into practical benefits for DDPM sampling.

**Limitations**  
The authors acknowledge that while LGS provides a substantial improvement in sample quality, it may still be limited by the computational cost associated with Jacobian-vector products, especially in high-dimensional settings. Additionally, the reliance on the Lanczos method may introduce its own set of numerical stability concerns, which are not explicitly addressed. The paper does not explore the scalability of LGS in extremely large models or datasets, nor does it compare against non-Gaussian approaches that might yield different performance characteristics.

**Why it matters**  
This work has significant implications for the development of more efficient and effective sampling methods in diffusion models. By demonstrating that full covariance matching can be both theoretically sound and practically implementable, the authors pave the way for future research to explore advanced covariance structures in generative models. The findings could lead to improved performance in various applications, including image synthesis and other generative tasks, where sample quality is paramount.

Authors: Md Sahil Akhtar, Aymane El Gadarri, Vivek F. Farias, Adam D. Jozefiak  
Source: arXiv:2605.22723  
URL: [https://arxiv.org/abs/2605.22723v1](https://arxiv.org/abs/2605.22723v1)
