---
title: "Feedforward 3D Editing Learns from Semantic-Part Transformation"
date: 2026-05-26 17:51:59 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.27351v1"
arxiv_id: "2605.27351"
authors: ["Jiawei Weng", "Saining Zhang", "Zhenxin Diao", "Peishuo Li", "Henghaofan Zhang", "Junhao Chen"]
slug: feedforward-3d-editing-learns-from-semantic-part-transformat
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing 3D editing methodologies, which predominantly rely on training-free editing pipelines and lack high-quality paired supervision. The authors highlight that current datasets often consist of independently generated assets or rely on image-mediated reconstruction, leading to issues such as inaccurate localization, weak preservation of geometry, and limited semantic consistency. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors introduce Pxform, a novel dataset comprising over 100,000 consistent before/after editing pairs across seven distinct edit types, which serves as the foundation for their proposed editing framework. The core technical contribution is PartFlow, a feedforward 3D editing network that leverages semantic-part transformations. PartFlow integrates source-aware latent control into pretrained 3D generative models, enhancing the editing process. Key innovations include mask-aware velocity preservation and render-space consistency supervision, which collectively improve edit fidelity and source preservation without requiring a 3D edit mask during inference. The architecture is designed to ground edits in semantic 3D parts, allowing for more precise and coherent modifications.

**Results**  
PartFlow demonstrates significant improvements over existing baselines on both geometric and appearance editing benchmarks. The authors report state-of-the-art performance metrics, although specific numerical results and comparisons to named baselines are not detailed in the abstract. The experiments indicate that the incorporation of high-quality semantic-part supervision leads to substantial enhancements in edit quality, suggesting a marked effect size in the context of 3D editing tasks.

**Limitations**  
The authors acknowledge that their approach may still be limited by the quality and diversity of the Pxform dataset, which, while extensive, may not encompass all possible editing scenarios. Additionally, the reliance on pretrained generative priors could introduce biases inherent to those models. The paper does not address potential computational overhead associated with the proposed methods, nor does it explore the scalability of the approach in real-time applications.

**Why it matters**  
This work has significant implications for the field of 3D content creation, particularly in advancing the capabilities of feedforward generative models in 3D editing. By establishing a framework that utilizes semantic-part transformations, the authors pave the way for more accurate and controllable editing processes, which could enhance applications in gaming, virtual reality, and design. The introduction of Pxform as a high-quality dataset also sets a precedent for future research in 3D editing, potentially leading to more robust and versatile editing tools.

Authors: Jiawei Weng, Saining Zhang, Zhenxin Diao, Peishuo Li, Henghaofan Zhang, Junhao Chen, Hao Zhao  
Source: arXiv:2605.27351  
URL: [https://arxiv.org/abs/2605.27351v1](https://arxiv.org/abs/2605.27351v1)
