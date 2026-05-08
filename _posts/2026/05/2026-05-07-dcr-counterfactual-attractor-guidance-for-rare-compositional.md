---
title: "DCR: Counterfactual Attractor Guidance for Rare Compositional Generation"
date: 2026-05-07 16:22:21 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.06512v1"
arxiv_id: "2605.06512"
authors: ["Taewon Kang", "Matthias Zwicker"]
slug: dcr-counterfactual-attractor-guidance-for-rare-compositional
summary_word_count: 452
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the issue of default completion bias in diffusion models, particularly in the context of generating rare but plausible compositions. Despite the advancements in diffusion models for realistic visual content generation, they often default to more common alternatives when presented with underrepresented combinations, such as "a snowy beach" or "a rainbow at night." The authors highlight that existing guidance mechanisms do not adequately model this bias, leading to suboptimal performance in generating rare compositions. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework called Default Completion Repulsion (DCR), which operates without the need for retraining or architectural modifications. DCR constructs a counterfactual attractor by relaxing the rare compositional factor while maintaining the surrounding semantic context. This approach induces an alternative denoising trajectory that reflects the model's preferred completion. The key technical contribution is the definition of counterfactual drift, which quantifies the discrepancy between the target and attractor trajectories. A projection-based repulsion mechanism is then employed to suppress guidance components that align with this drift direction, effectively mitigating the influence of common completions while preserving other semantic elements. The method integrates seamlessly into the standard diffusion sampling process.

**Results**  
DCR was evaluated on a set of rare compositional prompts, demonstrating significant improvements in compositional fidelity compared to baseline diffusion models. The authors report that DCR enhances the generation of rare compositions while maintaining high visual quality. Specific quantitative results include a marked increase in the fidelity of generated images for rare prompts, although exact numerical metrics and comparisons to specific baseline models are not detailed in the abstract. The results indicate that DCR effectively counteracts intrinsic model biases, providing a more robust framework for controllable generation.

**Limitations**  
The authors acknowledge that DCR does not address all forms of bias in diffusion models and is specifically tailored to counteract default completion bias. They do not discuss potential limitations related to the generalizability of the method across different datasets or the computational efficiency of the projection-based repulsion mechanism. Additionally, the lack of extensive quantitative benchmarks in the abstract limits the ability to fully assess the performance improvements over existing methods.

**Why it matters**  
The implications of this work are significant for the field of generative modeling, particularly in enhancing the capability of diffusion models to produce rare and complex compositions. By explicitly modeling and suppressing default completion behavior, DCR offers a new perspective on controllable generation that extends beyond traditional constraint enforcement. This framework could pave the way for future research focused on improving the diversity and fidelity of generated content in various applications, including creative industries and automated content generation.

Authors: Taewon Kang, Matthias Zwicker  
Source: arXiv:2605.06512  
URL: https://arxiv.org/abs/2605.06512v1
