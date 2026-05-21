---
title: "HITL-D: Human In The Loop Diffusion Assisted Shared Control"
date: 2026-05-20 17:49:56 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21460v1"
arxiv_id: "2605.21460"
authors: ["Riley Zilka", "Sergey Khlynovskiy", "Allie Wang", "Martin Jagersand"]
slug: hitl-d-human-in-the-loop-diffusion-assisted-shared-control
summary_word_count: 440
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in integrating human expertise with diffusion-based policies in shared control systems for autonomous manipulation tasks. While autonomous systems have advanced significantly, the literature lacks a comprehensive framework that effectively combines human input with autonomous decision-making in multi-step, insertion, and fine manipulation tasks. The authors present Human-In-The-Loop Diffusion (HITL-D) as a novel approach to enhance user performance in these scenarios. This work is a preprint and has not yet undergone peer review.

**Method**  
HITL-D introduces a shared control framework that utilizes diffusion-based policies to assist human operators in controlling robotic end effectors. The architecture incorporates a scene point cloud and the Cartesian position of the end effector to condition the autonomous updates of end effector orientation. This design reduces the number of joystick control axes required, thereby minimizing the cognitive load on the operator. The authors conducted a user study with 12 participants to evaluate the effectiveness of HITL-D against traditional teleoperation methods. The study involved multi-task scenarios that required fine manipulation, allowing for a direct comparison of task performance and user experience metrics.

**Results**  
The results of the user study indicate that HITL-D significantly outperforms traditional teleoperation methods. Specifically, HITL-D reduced average task completion times by 40% and decreased perceived workload by 37%. Additionally, participants reported improved ratings on a Likert scale for independence, intuitiveness, and confidence when using HITL-D compared to conventional approaches. These findings suggest a substantial effect size in both objective performance metrics and subjective user experience, highlighting the framework's effectiveness in enhancing human-robot collaboration.

**Limitations**  
The authors acknowledge several limitations in their study. The sample size of 12 participants may not be representative of the broader population, potentially affecting the generalizability of the results. Furthermore, the study focuses on specific manipulation tasks, which may not encompass the full range of scenarios encountered in real-world applications. The reliance on subjective Likert-scale ratings could introduce bias, as individual perceptions of workload and confidence may vary widely. Additionally, the framework's performance in dynamic or unstructured environments remains untested, which could limit its applicability in more complex settings.

**Why it matters**  
The HITL-D framework has significant implications for the future of human-robot interaction, particularly in applications requiring fine manipulation and complex decision-making. By effectively integrating human expertise with autonomous assistance, HITL-D not only enhances task performance but also improves user experience, making robotic systems more intuitive and accessible. This work paves the way for further research into hybrid control systems that leverage both human and machine strengths, potentially leading to advancements in fields such as teleoperation, robotic surgery, and collaborative manufacturing.

Authors: Riley Zilka, Sergey Khlynovskiy, Allie Wang, Martin Jagersand  
Source: arXiv:2605.21460  
URL: [https://arxiv.org/abs/2605.21460v1](https://arxiv.org/abs/2605.21460v1)
