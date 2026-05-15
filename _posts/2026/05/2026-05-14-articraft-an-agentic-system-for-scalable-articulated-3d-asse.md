---
title: "Articraft: An Agentic System for Scalable Articulated 3D Asset Generation"
date: 2026-05-14 17:59:18 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.15187v1"
arxiv_id: "2605.15187"
authors: ["Matt Zhou", "Ruining Li", "Xiaoyang Lyu", "Zhaomou Song", "Zhening Huang", "Chuanxia Zheng"]
slug: articraft-an-agentic-system-for-scalable-articulated-3d-asse
summary_word_count: 433
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the significant gap in the availability of large and diverse datasets for articulated 3D object generation, which is crucial for advancing the understanding and manipulation of such objects in various applications. The authors propose a novel approach to generate articulated 3D assets at scale using large language models (LLMs). This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of an agentic system named Articraft, which automates the generation of articulated 3D assets by writing programs that construct these assets. The system utilizes a domain-specific software development kit (SDK) that allows the LLM to define parts, compose geometry, specify joints, and write tests for validation. The architecture includes a programmatic interface that restricts the LLM's workspace to prevent distractions from complex software environments, such as authoring URDF files. The harness provides structured feedback on the generated assets, enhancing the quality of the output. The training compute details are not disclosed, but the authors emphasize the efficiency of the LLM in generating high-quality assets compared to existing methods.

**Results**  
Articraft was evaluated against state-of-the-art articulated asset generators and general-purpose coding agents. The results indicate that Articraft produces higher-quality articulated assets, although specific quantitative metrics (e.g., FID scores, accuracy rates) are not provided in the summary. The authors also introduce Articraft-10K, a curated dataset comprising over 10,000 articulated assets across 245 categories, demonstrating its utility for training models and applications in robotics simulation and virtual reality.

**Limitations**  
The authors acknowledge that the reliance on LLMs may introduce biases inherent to the training data of these models. Additionally, the system's performance may be limited by the expressiveness of the domain-specific SDK and the complexity of articulated asset specifications. The paper does not address potential scalability issues when generating assets beyond the 10K dataset or the generalizability of the generated assets across different domains.

**Why it matters**  
The implications of this work are significant for downstream applications in robotics, virtual reality, and computer graphics, where high-quality articulated 3D assets are essential. By leveraging LLMs to automate the generation of these assets, Articraft not only fills a critical gap in dataset availability but also sets a precedent for using AI-driven approaches to enhance the efficiency and quality of 3D asset creation. This could lead to advancements in training models for tasks that require understanding and manipulation of articulated objects, ultimately contributing to more sophisticated AI systems in various fields.

Authors: Matt Zhou, Ruining Li, Xiaoyang Lyu, Zhaomou Song, Zhening Huang, Chuanxia Zheng, Christian Rupprecht, Andrea Vedaldi et al.  
Source: arXiv:2605.15187  
URL: https://arxiv.org/abs/2605.15187v1
