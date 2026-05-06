---
title: "Flow Sampling: Learning to Sample from Unnormalized Densities via Denoising Conditional Processes"
date: 2026-05-05 17:07:37 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.03984v1"
arxiv_id: "2605.03984"
authors: ["Aaron Havens", "Brian Karrer", "Neta Shaul"]
slug: flow-sampling-learning-to-sample-from-unnormalized-densities
summary_word_count: 429
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of sampling from unnormalized densities, a problem that has not been extensively covered in the literature, particularly in the context of efficient sampling methods that do not rely on data samples. The authors propose a novel framework, Flow Sampling, which leverages diffusion models and flow matching in a data-free setting. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Flow Sampling introduces a training objective that is conditioned on a noise sample, regressing onto a denoising diffusion drift derived from a known energy function. This contrasts with traditional diffusion models, which condition on data samples and regress onto a noising diffusion drift. The authors utilize an interpolant process to minimize the number of evaluations of the energy function during training, enhancing efficiency and scalability. Additionally, the framework is designed to extend to Riemannian manifolds, allowing for diffusion-based sampling in non-Euclidean geometries. The authors derive a closed-form expression for the conditional drift on constant curvature manifolds, including hyperspheres and hyperbolic spaces, which broadens the applicability of their method.

**Results**  
Flow Sampling demonstrates strong empirical performance across several benchmarks. The authors evaluate their method on synthetic energy benchmarks, small peptides, and large-scale amortized molecular conformer generation. While specific numerical results are not detailed in the abstract, the paper claims that Flow Sampling outperforms existing baselines in these contexts, indicating significant effect sizes. The benchmarks include distributions supported on the sphere, showcasing the method's versatility in handling complex geometries.

**Limitations**  
The authors acknowledge that their method's performance may be sensitive to the choice of the energy function and the noise distribution used during training. They also note that while the method is efficient, the computational cost of evaluating the energy function remains a consideration, particularly in high-dimensional spaces. An additional limitation not explicitly mentioned is the potential difficulty in generalizing the method to more complex or less structured energy landscapes, which may not conform to the assumptions made in their derivations.

**Why it matters**  
The implications of Flow Sampling are significant for the field of generative modeling, particularly in scenarios where data is scarce or unavailable. By providing a framework for efficient sampling from unnormalized densities, this work opens avenues for applications in molecular generation, physics simulations, and other domains where energy functions are prevalent. The ability to extend the method to Riemannian manifolds also suggests potential for broader applications in geometric deep learning and manifold learning, thereby enriching the toolkit available for researchers and practitioners in these areas.

Authors: Aaron Havens, Brian Karrer, Neta Shaul  
Source: arXiv:2605.03984  
URL: [https://arxiv.org/abs/2605.03984v1](https://arxiv.org/abs/2605.03984v1)
