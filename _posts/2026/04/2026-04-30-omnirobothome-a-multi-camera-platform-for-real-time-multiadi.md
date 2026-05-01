---
title: "OmniRobotHome: A Multi-Camera Platform for Real-Time Multiadic Human-Robot Interaction"
date: 2026-04-30 17:59:58 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.28197v1"
arxiv_id: "2604.28197"
authors: ["Junyoung Lee", "Sookwan Han", "Jeonghwan Kim", "Inhee Lee", "Mingi Choi", "Jisoo Kim"]
slug: omnirobothome-a-multi-camera-platform-for-real-time-multiadi
summary_word_count: 469
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding multiadic human-robot collaboration in residential environments, where multiple humans and robots interact concurrently on interleaved tasks. Existing research has primarily focused on dyadic or sequential interactions, leaving a significant void in understanding and implementing real-time, occlusion-robust tracking in complex, dynamic settings. The authors highlight that current platforms lack the capability to provide reliable room-scale perception necessary for effective multiadic collaboration, particularly due to challenges posed by occlusion and rapid state changes in close-proximity interactions. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce OmniRobotHome, a novel platform that integrates 48 hardware-synchronized RGB cameras to achieve wide-area, real-time 3D tracking of multiple humans and objects in a residential setting. The system employs markerless tracking techniques to ensure occlusion robustness and operates within a shared world frame, which is crucial for coordinating the actions of multiple robots. Two Franka arms are incorporated into the platform, allowing for coordinated actuation based on the live state of the environment. The continuous capture of data enables long-horizon human behavior modeling through the accumulation of trajectories. The architecture emphasizes real-time perception and behavior memory, which are critical for enhancing safety and anticipatory assistance in shared human-robot environments.

**Results**  
The authors demonstrate that their platform significantly improves performance in two key areas: safety in shared environments and human-anticipatory robotic assistance. While specific numerical results are not disclosed in the abstract, the paper claims measurable gains in both areas due to the integration of real-time perception and accumulated behavior memory. The effectiveness of OmniRobotHome is evaluated against existing baselines in the context of multiadic collaboration, although detailed comparisons and metrics are expected to be elaborated in the full paper.

**Limitations**  
The authors acknowledge that the platform's reliance on a dense array of cameras may limit scalability and deployment in less controlled environments. Additionally, the complexity of real-time processing and the potential for increased computational load are not fully addressed. The paper does not discuss the limitations related to the physical setup, such as the need for extensive infrastructure to support the camera array or the challenges of maintaining synchronization across multiple devices in dynamic environments.

**Why it matters**  
OmniRobotHome represents a significant advancement in the field of human-robot interaction by enabling experimental exploration of multiadic collaboration in real-world settings. The implications of this work extend to various applications, including domestic robotics, assistive technologies, and collaborative workspaces, where understanding and facilitating interactions among multiple agents is crucial. By providing a robust platform for real-time perception and interaction, this research paves the way for future studies aimed at enhancing the safety and efficiency of human-robot collaboration in complex environments.

Authors: Junyoung Lee, Sookwan Han, Jeonghwan Kim, Inhee Lee, Mingi Choi, Jisoo Kim, Wonjung Woo, Hanbyul Joo  
Source: arXiv:2604.28197  
URL: [https://arxiv.org/abs/2604.28197v1](https://arxiv.org/abs/2604.28197v1)
