---
title: "Stop Holding Your Breath: CT-Informed Gaussian Splatting for Dynamic Bronchoscopy"
date: 2026-04-30 17:57:19 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.28179v1"
arxiv_id: "2604.28179"
authors: ["Andrea Dunn Beltran", "Daniel Rho", "Aarav Mehta", "Xinqi Xiong", "Ra\u00fal San Jos\u00e9 Est\u00e9par", "Ron Alterovitz"]
slug: stop-holding-your-breath-ct-informed-gaussian-splatting-for-
summary_word_count: 447
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of accurately localizing bronchoscopic navigation in the presence of respiratory motion, which can cause airway deformation of 5-20 mm, leading to CT-to-body divergence. Traditional methods rely on breath-hold protocols to align intraoperative anatomy with static CT scans, which are difficult to implement and disrupt clinical workflows. The authors propose a novel approach that eliminates the need for these protocols by utilizing patient-specific respiratory modeling derived from paired inhale-exhale CT scans.

**Method**  
The core technical contribution is a Gaussian splatting framework that integrates a lightweight estimator to infer the breathing phase directly from endoscopic RGB video. The method involves registering paired inhale-exhale CT scans to define a patient-specific deformation space, allowing for the reduction of respiratory motion to a single scalar breathing phase per frame. This representation is embedded within a mesh-anchored Gaussian splatting architecture, enabling continuous and deformation-aware reconstruction throughout the respiratory cycle without the need for breath-holds or external sensing. The authors also introduce RESPIRE, a bronchoscopy simulation pipeline that provides per-frame ground truth for geometry, pose, breathing phase, and deformation, facilitating quantitative evaluation of the proposed method.

**Results**  
The proposed method demonstrates significant improvements over traditional unconstrained single-CT baselines. Specifically, it achieves a target localization accuracy of 1.22 mm, which is within the clinically relevant tolerance of 3 mm. Additionally, the training process is reported to be over 20 times faster compared to existing methods. The results indicate that the proposed approach not only enhances geometrical fidelity in reconstruction but also streamlines the clinical workflow by removing the need for breath-holding.

**Limitations**  
The authors acknowledge that their method relies on the availability of paired inhale-exhale CT scans, which may not be feasible in all clinical settings. Additionally, the performance of the method may be influenced by the quality and resolution of the endoscopic RGB input. The study does not address potential variations in patient anatomy that could affect the generalizability of the model across diverse populations. Furthermore, the reliance on a simulation pipeline for evaluation may not fully capture the complexities of real-world scenarios.

**Why it matters**  
This work has significant implications for the field of dynamic bronchoscopy, as it offers a method to improve localization accuracy while enhancing the clinical workflow by eliminating breath-hold requirements. The integration of patient-specific respiratory modeling could lead to more personalized and effective bronchoscopic interventions. Furthermore, the introduction of the RESPIRE simulation pipeline provides a valuable tool for future research and development in this domain, potentially paving the way for advancements in other areas of medical imaging and navigation.

Authors: Andrea Dunn Beltran, Daniel Rho, Aarav Mehta, Xinqi Xiong, Raúl San José Estépar, Ron Alterovitz, Marc Niethammer, Roni Sengupta  
Source: arXiv:2604.28179  
URL: https://arxiv.org/abs/2604.28179v1
