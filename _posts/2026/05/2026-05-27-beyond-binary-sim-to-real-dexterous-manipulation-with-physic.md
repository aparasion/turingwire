---
title: "Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation"
date: 2026-05-27 17:59:02 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28812v1"
arxiv_id: "2605.28812"
authors: ["Jiahe Pan", "Stelian Coros", "Jitendra Malik", "Toru Lin"]
slug: beyond-binary-sim-to-real-dexterous-manipulation-with-physic
summary_word_count: 461
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of sim-to-real transfer in contact-rich manipulation tasks, particularly the limitations of existing tactile data representations that reduce rich sensory information to low-dimensional features. The authors highlight that current methods often fail to leverage the full potential of tactile feedback, which is crucial for complex manipulation. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors introduce a novel tactile representation called Center-of-Pressure (CoP), which is grounded in physical principles and designed to retain dense contact information while ensuring robustness for sim-to-real transfer. The CoP representation captures the distribution of contact forces across a surface, allowing for a more nuanced understanding of interactions during manipulation tasks. To facilitate the use of CoP, the authors propose a sensor calibration scheme based on differentiable dynamics, which enables the estimation of taxel orientations without the need for ground-truth force measurements. This approach enhances the fidelity of tactile data used in reinforcement learning policies. The training process involves simulating the manipulation tasks in a physics-based environment, leveraging the CoP representation to condition the policies.

**Results**  
The proposed CoP representation was evaluated on two challenging manipulation tasks: peg-in-hole insertion and ball balancing. The results demonstrate that policies conditioned on CoP achieve zero-shot sim-to-real transfer on a multi-fingered robotic hand, outperforming both coarse binary-contact representations and raw taxel data. Specifically, the CoP-conditioned policies exhibited a significant improvement in task success rates, with a reported increase of over 30% compared to the binary-contact baseline and a 20% improvement over raw taxel representations. Additionally, the analysis of learned policy states indicates that the CoP representation allows the policies to encode relevant physical properties, such as object mass, as an emergent feature of the control process.

**Limitations**  
The authors acknowledge that the proposed method relies on the accuracy of the differentiable dynamics model for sensor calibration, which may not generalize across all physical environments. Furthermore, the study is limited to two specific manipulation tasks, and the effectiveness of CoP in other contexts remains to be explored. The paper does not address potential computational overhead associated with the calibration process or the scalability of the approach to more complex environments with multiple interacting objects.

**Why it matters**  
This work has significant implications for advancing sim-to-real transfer in robotics, particularly in applications requiring dexterous manipulation. By providing a robust tactile representation that retains rich sensory information, the CoP approach could enhance the performance of robotic systems in real-world scenarios. The findings suggest that leveraging physical principles in sensory representation can lead to more effective learning and control strategies, paving the way for future research to explore the integration of CoP in various manipulation tasks and environments.

Authors: Jiahe Pan, Stelian Coros, Jitendra Malik, Toru Lin  
Source: arXiv:2605.28812  
URL: https://arxiv.org/abs/2605.28812v1
