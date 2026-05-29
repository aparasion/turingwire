---
title: "PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions"
date: 2026-05-28 17:29:19 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30268v1"
arxiv_id: "2605.30268"
authors: ["Omer Benishu", "Gal Fiebelman", "Sagie Benaim"]
slug: phygenhoi-physically-aware-4d-generation-of-dynamic-human-ob
summary_word_count: 445
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in generating physically accurate and visually coherent 4D Human-Object Interactions (HOI), a task that has not been sufficiently explored in existing literature. The authors highlight the limitations of current methods that either lack physical realism or fail to integrate dynamic interactions effectively. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce PhyGenHOI, a framework that combines generative human motion with explicit physical object simulation. The human is modeled as a semantic agent using a Motion Diffusion Model (MDM), while the object is represented as a physical agent through the Material Point Method (MPM). Both entities are unified under a differentiable representation using 3D Gaussian Splats (3DGS). The interaction is supervised through three mechanisms:  
1. **Windowed Attraction Loss**: This loss function ensures temporal synchronization between the generated human motion and the target object, facilitating interception during interactions.  
2. **Contact-Driven Re-simulation**: This step enforces physically consistent momentum transfer upon contact, enhancing realism in the interaction dynamics.  
3. **Masked Video-SDS Objective**: This objective incorporates video-based priors to improve the fidelity of contact interactions, ensuring that the generated scenes align closely with real-world physics.

The training process leverages a dataset of diverse human-object interactions, although specific details regarding the dataset size and training compute are not disclosed.

**Results**  
PhyGenHOI demonstrates superior performance in generating physically consistent 4D HOI compared to several baseline models. The authors report significant improvements in interaction fidelity across various actions, humans, and objects. While specific quantitative metrics are not provided in the abstract, the results indicate that PhyGenHOI outperforms existing methods in terms of both physical accuracy and visual coherence, suggesting a robust capability in dynamic scene generation.

**Limitations**  
The authors acknowledge several limitations, including the potential computational intensity of the MPM and the need for extensive training data to capture a wide range of interactions. They also note that the framework may struggle with highly complex interactions that involve multiple objects or intricate human movements. Additionally, the reliance on video-based priors may limit generalization to unseen scenarios not represented in the training data.

**Why it matters**  
The implications of this work are significant for downstream applications in robotics, virtual reality, and animation, where realistic human-object interactions are crucial. By providing a framework that integrates physical simulation with generative modeling, PhyGenHOI paves the way for advancements in interactive systems that require real-time responsiveness and physical accuracy. This research could inspire further exploration into hybrid models that combine generative techniques with physics-based simulations, potentially leading to more sophisticated AI systems capable of understanding and predicting human behavior in dynamic environments.

Authors: Omer Benishu, Gal Fiebelman, Sagie Benaim  
Source: arXiv:2605.30268  
URL: https://arxiv.org/abs/2605.30268v1
