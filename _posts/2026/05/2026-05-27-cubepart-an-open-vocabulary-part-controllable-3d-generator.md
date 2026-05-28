---
title: "CubePart: An Open-Vocabulary Part-Controllable 3D Generator"
date: 2026-05-27 17:22:38 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28763v1"
arxiv_id: "2605.28763"
authors: ["Yiheng Zhu", "Kangle Deng", "Jean-Philippe Fauconnier", "Inaki Navarro", "Daiqing Li", "Ava Pun"]
slug: cubepart-an-open-vocabulary-part-controllable-3d-generator
summary_word_count: 513
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the capability of existing generative 3D models to produce semantically meaningful and application-specific part-decomposed meshes. Traditional generative models either yield monolithic meshes or arbitrary decompositions that do not align with the requirements of interactive applications such as games and simulations. The authors present CubePart, a framework that allows for open-vocabulary, part-controllable 3D mesh generation, enabling users to specify part structures explicitly at inference time. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
CubePart employs a two-stage generative architecture that decouples global shape synthesis from part-level decoding. The first stage generates a global mesh based on a text prompt, while the second stage decodes this mesh into user-defined parts according to a specified schema. The authors constructed a large open-vocabulary, part-labeled 3D dataset to train the model, although specific details regarding the dataset size and composition are not disclosed. The architecture leverages a scalable data pipeline to facilitate the generation of diverse 3D assets that can be directly integrated into game engines. The inference process allows for the generation of multiple meshes corresponding to each part in the user-defined schema, ensuring coherence and semantic alignment.

**Results**  
CubePart demonstrates significant improvements over existing baselines in terms of part controllability and semantic coherence. The authors report that their generated meshes can be seamlessly integrated into game engines, outperforming traditional methods in both usability and fidelity. While specific quantitative metrics (e.g., FID scores, IoU) are not provided in the abstract, the qualitative results indicate that the generated assets maintain structural integrity and are suitable for animation and scripted behaviors without requiring manual post-processing. The authors claim that their method can generate complex objects with a high degree of part-specific control, which is a notable advancement in the field.

**Limitations**  
The authors acknowledge that the framework's performance may be limited by the quality and diversity of the training dataset, which could affect the generalization to unseen part schemas. Additionally, the reliance on user-defined part names may introduce variability in the results based on user input. The paper does not address potential computational costs associated with the two-stage architecture or the scalability of the model for real-time applications. Furthermore, the lack of quantitative benchmarks in the abstract limits the ability to fully assess the performance against established state-of-the-art methods.

**Why it matters**  
CubePart has significant implications for the development of interactive 3D content, particularly in gaming and simulation environments where part-specific control is crucial. By enabling open-vocabulary part generation, this framework allows for greater flexibility and creativity in asset creation, potentially reducing the time and effort required for manual modeling. The ability to generate semantically coherent meshes that can be directly utilized in game engines opens new avenues for procedural content generation and enhances the user experience in interactive applications. Future work could explore the integration of CubePart with real-time rendering engines and further refine the part decomposition process to improve usability.

Authors: Yiheng Zhu, Kangle Deng, Jean-Philippe Fauconnier, Inaki Navarro, Daiqing Li, Ava Pun, Yinan Zhang, Peiye Zhuang et al.  
Source: arXiv:2605.28763  
URL: https://arxiv.org/abs/2605.28763v1
