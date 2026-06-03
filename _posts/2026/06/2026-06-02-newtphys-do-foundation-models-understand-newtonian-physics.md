---
title: "NewtPhys: Do Foundation Models Understand Newtonian Physics?"
date: 2026-06-02 17:59:12 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2606.03986v1"
arxiv_id: "2606.03986"
authors: ["Sebastian Cavada", "Soumava Paul", "Tuan-Hung Vu", "Andrei Bursuc", "Raoul de Charette"]
slug: newtphys-do-foundation-models-understand-newtonian-physics
summary_word_count: 454
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces NewtPhys, a dataset for evaluating foundation models' understanding of Newtonian physics through realistic visual scenarios."
---

**Problem**  
Prior research has assessed physics reasoning in foundation models primarily through synthetic or semi-synthetic environments, often focusing on high-level events. This approach lacks the visual fidelity and complexity necessary to evaluate low-level Newtonian physics understanding effectively. The authors identify a gap in the literature regarding the assessment of foundation models in realistic scenarios, particularly in their ability to reason about physical interactions in 4D space. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose NewtPhys, a novel dataset comprising multiview images of real-world scenes, annotated with physics-grounded simulations. The dataset features dense, fine-grained annotations across multiple timesteps, including 3D forces and amodal per-pixel quantities that encompass physics, tracking, semantics, and geometry. This comprehensive annotation allows for a more nuanced evaluation of models' understanding of Newtonian physics. The authors systematically evaluate 56 vision-language models (VLMs), including 54 open-weight models and 2 closed-source frontier models, alongside 10 vision foundation models (VFMs). The evaluation methodology emphasizes low-level physics reasoning, contrasting the performance of these models against the rich annotations provided by NewtPhys.

**Results**  
The evaluation reveals significant limitations in the low-level physics reasoning capabilities of the assessed models. While specific performance metrics are not disclosed in the abstract, the systematic evaluation across a diverse set of models indicates that many foundation models struggle with tasks requiring detailed understanding of physical interactions. The results highlight a clear performance gap when compared to the expectations set by the dataset's annotations, suggesting that current models may not generalize well to complex physical reasoning tasks.

**Limitations**  
The authors acknowledge that the dataset's reliance on real-world scenes may introduce variability that could affect model performance. Additionally, the focus on low-level physics reasoning may not capture the full spectrum of physical understanding required for more complex tasks. The paper does not address potential biases in the dataset or the representativeness of the selected scenes, which could limit the generalizability of the findings. Furthermore, the evaluation is constrained to the models tested, leaving open questions about the performance of other architectures not included in the study.

**Why it matters**  
NewtPhys represents a significant advancement in the evaluation of foundation models' understanding of physics, providing a benchmark that bridges the gap between simplistic synthetic setups and the complexities of real-world scenarios. This dataset not only facilitates a more rigorous assessment of existing models but also lays the groundwork for future research in physics-grounded vision. The implications of this work extend to the development of next-generation physics-aware evaluations, which are crucial for applications in robotics, autonomous systems, and interactive AI. As such, this research is foundational for advancing the capabilities of AI in understanding and interacting with the physical world, as published in [arXiv cs.CV](https://arxiv.org/abs/2606.03986v1).
