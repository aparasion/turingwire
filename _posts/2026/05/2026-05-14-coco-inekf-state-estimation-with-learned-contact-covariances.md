---
title: "CoCo-InEKF: State Estimation with Learned Contact Covariances in Dynamic, Contact-Rich Scenarios"
date: 2026-05-14 17:35:06 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.15122v1"
arxiv_id: "2605.15122"
authors: ["Michael Baumgartner", "David M\u00fcller", "Agon Serifi", "Ruben Grandia", "Espen Knoop", "Markus Gross"]
slug: coco-inekf-state-estimation-with-learned-contact-covariances
summary_word_count: 436
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of traditional state estimation methods for legged robots in dynamic, contact-rich environments, particularly the reliance on binary contact states. These methods inadequately represent the complexities of partial contact and directional slippage, which are critical for accurate state estimation in real-world scenarios. The authors present CoCo-InEKF, a novel approach that leverages learned contact covariances to enhance state estimation. This work is a preprint and has not yet undergone peer review.

**Method**  
CoCo-InEKF introduces a differentiable invariant extended Kalman filter (InEKF) that replaces binary contact states with continuous contact velocity covariances. These covariances are predicted by a lightweight neural network, which is trained end-to-end using a state-error loss function, thus eliminating the need for heuristic ground-truth contact labels. The architecture allows for dynamic modulation of contact confidence, adapting to varying conditions from firm contact to slippage. Additionally, the authors propose an automated contact candidate selection procedure, demonstrating that the method's performance is robust to the specific placement of these candidates. The training process and network architecture details are not disclosed, but the end-to-end training approach is emphasized.

**Results**  
The authors validate CoCo-InEKF through experiments on a bipedal robot, showcasing significant improvements in linear velocity estimation accuracy and filter consistency compared to baseline methods. While specific numerical results are not provided in the abstract, the paper claims a superior accuracy-efficiency tradeoff, enabling the execution of complex motions such as dancing and intricate ground interactions. The results suggest that the proposed method outperforms traditional state estimation techniques, particularly in scenarios involving dynamic contact.

**Limitations**  
The authors acknowledge that the method's performance may be sensitive to the quality of the training data used for the neural network, although they do not provide specific metrics on this aspect. Additionally, the reliance on a neural network introduces potential issues related to generalization across diverse environments and contact scenarios. The paper does not discuss the computational overhead introduced by the neural network or the scalability of the approach to larger systems or more complex environments.

**Why it matters**  
The introduction of learned contact covariances in state estimation represents a significant advancement in the field of robotics, particularly for legged robots operating in unpredictable environments. By moving beyond binary contact states, CoCo-InEKF enhances the robustness and adaptability of state estimation methods, which is crucial for real-world applications. This work opens avenues for further research into integrating machine learning with traditional estimation techniques, potentially leading to more sophisticated and resilient robotic systems capable of navigating complex terrains and performing intricate tasks.

Authors: Michael Baumgartner, David Müller, Agon Serifi, Ruben Grandia, Espen Knoop, Markus Gross, Moritz Bächer  
Source: arXiv:2605.15122  
URL: https://arxiv.org/abs/2605.15122v1
