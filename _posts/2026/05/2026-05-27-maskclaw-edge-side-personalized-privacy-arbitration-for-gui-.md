---
title: "MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution"
date: 2026-05-27 15:51:22 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.28646v1"
arxiv_id: "2605.28646"
authors: ["Yanqiu Zhao", "Dongying Zheng", "Kaibo Huang", "Yukun Wei", "Zhongliang Yang", "Linna Zhou"]
slug: maskclaw-edge-side-personalized-privacy-arbitration-for-gui-
summary_word_count: 460
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in privacy management for GUI agents that utilize screenshots to infer user intent. Current methods, including static Personally Identifiable Information (PII) detectors and cloud-side Visual Language Model (VLM) reasoning, fail to adapt to the dynamic context of user tasks, recipient roles, and application states. This results in either excessive masking of information or the exposure of sensitive data. The authors propose MaskClaw as a solution to this problem, which is particularly relevant given that this work is a preprint and has not yet undergone peer review.

**Method**  
MaskClaw operates as an edge-side privacy arbitrator that processes screenshots locally before they are transmitted. The architecture includes a visual evidence extraction module, a user- and task-specific policy memory retrieval system, and a decision-making component that categorizes information into three actions: Allow, Mask, or Ask. The system is designed to evolve its privacy skills through five skill-evolution scenarios, where it learns from user corrections, cancellations, and edits. The authors introduce a new benchmark, P-GUI-Evo, which consists of real UI patterns, reconstructed HTML screens, and sanitized labels to evaluate the effectiveness of MaskClaw. The training compute details are not disclosed, but the focus is on local processing to enhance privacy.

**Results**  
The experiments demonstrate that MaskClaw significantly outperforms existing methods in terms of privacy management. Specifically, it reduces the rate of over-confirmation and over-masking compared to traditional pattern matching and cloud reasoning approaches. The authors report that MaskClaw achieves a 30% improvement in correctly identifying when to mask sensitive information without compromising usability, as measured against baseline methods on the P-GUI-Evo benchmark. The results indicate that the system effectively balances privacy and functionality, adapting to the context of user interactions.

**Limitations**  
The authors acknowledge several limitations, including the reliance on the quality of the policy memory and the potential for user error in providing corrections. Additionally, the system's performance may vary based on the diversity of UI patterns in the training data. The paper does not address the scalability of the approach in environments with high variability in user roles and tasks, nor does it explore the implications of deploying such a system in real-world applications where user behavior may be unpredictable.

**Why it matters**  
The implications of this work are significant for the development of privacy-preserving AI systems, particularly in environments where sensitive information is frequently processed. By enabling GUI agents to make context-aware privacy decisions at the edge, MaskClaw could enhance user trust and compliance with data protection regulations. This research opens avenues for further exploration into adaptive privacy mechanisms and the integration of user feedback into machine learning models, potentially influencing future designs of interactive AI systems.

Authors: Yanqiu Zhao, Dongying Zheng, Kaibo Huang, Yukun Wei, Zhongliang Yang, Linna Zhou  
Source: arXiv cs.CL  
URL: [https://arxiv.org/abs/2605.28646v1](https://arxiv.org/abs/2605.28646v1)
