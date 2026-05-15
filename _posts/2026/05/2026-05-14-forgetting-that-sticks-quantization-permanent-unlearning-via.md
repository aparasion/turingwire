---
title: "Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution"
date: 2026-05-14 17:44:10 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.15138v1"
arxiv_id: "2605.15138"
authors: ["Saisab Sadhu", "Pratinav Seth", "Vinay Kumar Sankarapu"]
slug: forgetting-that-sticks-quantization-permanent-unlearning-via
summary_word_count: 439
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the literature regarding the effectiveness of unlearning methods in the context of quantized language models. Traditional evaluations of unlearning focus on behavioral suppression in full precision immediately after training, neglecting the impact of quantization, which is standard in deployed models. Previous studies have indicated that 4-bit post-training quantization can reverse machine unlearning, revealing a dual failure in existing methods: those that achieve effective forgetting lose this capability under quantization, while those that maintain performance do not effectively forget. This paper formalizes the issue as a sparsity-permanence tradeoff, where per-parameter updates are insufficient to clear quantization bin boundaries.

**Method**  
The authors propose MANSU (Mechanistic-Aligned Null-Space Unlearning), a novel framework that integrates several advanced techniques to address the identified failures. MANSU employs causal circuit attribution to isolate the minimal forget-set subgraph, ensuring that only the necessary parameters are targeted for unlearning. It utilizes circuit-restricted null-space projection with a diagonal-Fisher retain bound to maintain model integrity during the unlearning process. Additionally, a per-parameter magnitude floor is introduced to guarantee that updates survive quantization. The paper also introduces Circuit Attribution Divergence (CAD), a new metric for mechanistic verification that differentiates between structural erasure and mere behavioral suppression, a distinction that existing metrics fail to capture.

**Results**  
MANSU demonstrates superior performance across multiple model families and hazard benchmarks. It is the first method to jointly satisfy four critical properties: meaningful forgetting, retain preservation, a non-positive post-training quantization (PTQ) gap, and structural erasure. In contrast, gradient-based baselines only manage to recover an accuracy improvement of up to +0.05 under compression, highlighting the effectiveness of MANSU in maintaining model performance while achieving unlearning.

**Limitations**  
The authors acknowledge that while MANSU addresses the dual failure of existing methods, it may still be sensitive to the choice of quantization parameters and the specific architecture of the models used. Additionally, the reliance on causal circuit attribution may limit the applicability of MANSU to architectures where such attribution can be effectively computed. The paper does not explore the scalability of MANSU to extremely large models or its performance in real-world applications, which could present further challenges.

**Why it matters**  
This work has significant implications for the deployment of machine learning models in privacy-sensitive applications, where the ability to unlearn specific data points is crucial. By providing a robust method for quantization-permanent unlearning, MANSU enhances the reliability of unlearning techniques in practical scenarios, ensuring that models can be updated without retaining unwanted information. This advancement could lead to more secure and privacy-compliant AI systems, fostering greater trust in machine learning applications.

Authors: Saisab Sadhu, Pratinav Seth, Vinay Kumar Sankarapu  
Source: arXiv:2605.15138  
URL: [https://arxiv.org/abs/2605.15138v1](https://arxiv.org/abs/2605.15138v1)
