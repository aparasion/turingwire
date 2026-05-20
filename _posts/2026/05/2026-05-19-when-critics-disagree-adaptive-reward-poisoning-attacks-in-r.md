---
title: "When Critics Disagree: Adaptive Reward Poisoning Attacks in RIS-Aided Wireless Control System"
date: 2026-05-19 15:59:43 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.20037v1"
arxiv_id: "2605.20037"
authors: ["Deemah H. Tashman", "Soumaya Cherkaoui"]
slug: when-critics-disagree-adaptive-reward-poisoning-attacks-in-r
summary_word_count: 426
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the vulnerability of learning-based wireless control systems to reward-poisoning attacks, specifically in the context of Cognitive Radio Networks (CRNs) enhanced by Reconfigurable Intelligent Surfaces (RIS). The authors propose a novel attack strategy, Disagreement-Guided Reward Poisoning (DGRP), which exploits the discrepancies between dual critics in a Soft Actor-Critic (SAC) framework. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the DGRP attack, which targets the reward signals received by the SAC agent. The SAC architecture employs two critics to estimate the value function, and DGRP specifically corrupts rewards when there is significant disagreement between these critics, particularly in high-leverage and high-uncertainty states. The attack is adaptive, meaning it adjusts based on the critics' outputs, leading to distorted value estimations that misguide the policy towards suboptimal actions. The authors analyze various attack parameters, such as timing and the degree of disagreement, to assess their impact on the learning process. The experimental setup involves a CRN environment where the SAC agent optimizes both the transmission power of secondary users (SUs) and the RIS phase shifts.

**Results**  
The DGRP attack significantly undermines the performance of the SAC agent compared to baseline strategies, including periodic-timing and exploration-triggered attacks. The authors report that DGRP leads to a marked degradation in transmission quality and performance improvements typically afforded by RIS are substantially diminished. While specific numerical results are not detailed in the abstract, the consistent superiority of DGRP in inflicting damage suggests a robust effect size that warrants attention in the context of DRL robustness evaluations.

**Limitations**  
The authors acknowledge that their study primarily focuses on the SAC architecture and may not generalize to other DRL frameworks. Additionally, the exploration of attack parameters, while comprehensive, may not cover all possible configurations in real-world scenarios. The paper does not address potential defenses against DGRP or the implications of varying network conditions, which could influence the attack's effectiveness. Furthermore, the lack of empirical validation in diverse environments limits the generalizability of the findings.

**Why it matters**  
This research highlights a critical gap in the security of DRL systems in wireless communication, particularly in environments enhanced by RIS technology. By demonstrating the effectiveness of disagreement-aware attacks, the work underscores the need for robust evaluation frameworks that account for such vulnerabilities. The implications extend to the design of more resilient learning algorithms and the development of countermeasures against adaptive poisoning attacks, which are essential for the deployment of DRL in safety-critical applications.

Authors: Deemah H. Tashman, Soumaya Cherkaoui  
Source: arXiv:2605.20037  
URL: https://arxiv.org/abs/2605.20037v1
