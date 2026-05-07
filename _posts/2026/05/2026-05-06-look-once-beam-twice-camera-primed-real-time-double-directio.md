---
title: "Look Once, Beam Twice: Camera-Primed Real-Time Double-Directional mmWave Beam Management for Vehicular Connectivity"
date: 2026-05-06 16:07:26 +0000
category: research
subcategory: agents_robotics
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.05071v1"
arxiv_id: "2605.05071"
authors: ["Avhishek Biswas", "Apala Pramanik", "Eylem Ekici", "Mehmet C. Vuran"]
slug: look-once-beam-twice-camera-primed-real-time-double-directio
summary_word_count: 419
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of real-time double-directional beam management for vehicle-to-everything (V2X) connectivity in millimeter-wave (mmWave) networks. Existing methods are hindered by high training overhead and limited generalization to novel scenarios, which is critical given the dynamic nature of vehicular environments. The authors propose a solution that integrates camera sensing to enhance beam alignment efficiency, a gap in the current literature that is particularly relevant for real-time applications. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the VIsion-based BEamforming (VIBE) architecture, which combines model-based reasoning with machine learning and closed-loop RF feedback. VIBE utilizes camera observations to significantly reduce the beam-search space, thus accelerating the beam-pair establishment process. The architecture includes lightweight mechanisms for beam refinement and offset tracking, allowing for adaptive adjustments based on real-time application requirements. The training compute details are not disclosed, but the authors emphasize the reduction of exhaustive training overhead compared to traditional methods. VIBE is implemented and evaluated in various environments, including indoor/outdoor testbeds and real-time vehicular scenarios.

**Results**  
VIBE demonstrates superior performance compared to 5G NR hierarchical beamforming, consistently achieving lower outage rates. Specifically, VIBE maintains outage rates between 1.1% and 1.4% across different test scenarios. When benchmarked against state-of-the-art end-to-end machine learning models for beam selection on public datasets, VIBE outperforms these models, showcasing its strong generalization capabilities. The results indicate that the hybrid model-based approach is more effective for real-world mmWave vehicular connectivity than purely end-to-end trained models.

**Limitations**  
The authors acknowledge that while VIBE shows promising results, its performance may vary under extreme mobility conditions or in highly obstructed environments, which were not extensively tested. Additionally, the reliance on camera sensing may limit applicability in scenarios where visual data is not available or reliable. The paper does not address potential computational overhead introduced by the camera integration, nor does it explore the scalability of the approach in larger vehicular networks.

**Why it matters**  
The implications of this work are significant for the development of robust V2X communication systems, particularly as the automotive industry moves towards more connected and autonomous vehicles. By demonstrating that a hybrid model-based approach can outperform traditional methods, this research paves the way for more efficient beam management strategies that can adapt to real-time conditions. The findings encourage further exploration of sensor fusion techniques in mmWave communications, potentially leading to enhanced connectivity solutions in urban environments and beyond.

Authors: Avhishek Biswas, Apala Pramanik, Eylem Ekici, Mehmet C. Vuran  
Source: arXiv:2605.05071  
URL: https://arxiv.org/abs/2605.05071v1
