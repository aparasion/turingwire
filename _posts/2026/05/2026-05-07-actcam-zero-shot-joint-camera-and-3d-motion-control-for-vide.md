---
title: "ActCam: Zero-Shot Joint Camera and 3D Motion Control for Video Generation"
date: 2026-05-07 17:59:58 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06667v1"
arxiv_id: "2605.06667"
authors: ["Omar El Khalifi", "Thomas Rossi", "Oscar Fossey", "Thibault Fouque", "Ulysse Mizrahi", "Philip Torr"]
slug: actcam-zero-shot-joint-camera-and-3d-motion-control-for-vide
summary_word_count: 443
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in video generation techniques that require simultaneous control over both character motion and camera trajectory, particularly in artistic applications. Existing methods often lack the capability to jointly manipulate these two aspects effectively, especially in a zero-shot manner. The authors present ActCam, a preprint work, which aims to fill this gap by enabling fine-grained control over intrinsic and extrinsic camera parameters while transferring character motion from a driving video to a new scene.

**Method**  
ActCam leverages a pretrained image-to-video diffusion model that accepts conditioning based on scene depth and character pose. The method operates in two phases during the sampling process. Initially, both pose and sparse depth information are used to condition the model, ensuring geometric consistency across frames. In the second phase, depth conditioning is removed, allowing for pose-only guidance to refine high-frequency details without overly constraining the generation process. This staged conditioning approach is critical for maintaining camera adherence and motion fidelity. The authors do not disclose specific training compute details, as the method is designed for zero-shot application.

**Results**  
ActCam was evaluated against several benchmarks that include diverse character motions and significant viewpoint changes. The results indicate that ActCam outperforms baseline methods that utilize pose-only control and other pose-camera integration techniques. Specifically, it demonstrates improved camera adherence and motion fidelity, with human evaluations indicating a preference for ActCam, particularly in scenarios involving large viewpoint changes. The authors report substantial effect sizes, although exact numerical improvements over baselines are not specified in the summary.

**Limitations**  
The authors acknowledge that while ActCam achieves significant advancements in joint camera and motion control, it may still struggle with extreme camera angles or highly complex scenes where depth estimation is challenging. Additionally, the reliance on pretrained models may limit the adaptability of ActCam to specific artistic styles or unique character motions not represented in the training data. The paper does not address potential computational inefficiencies during the two-phase conditioning process, which could impact real-time applications.

**Why it matters**  
The implications of ActCam are significant for downstream work in video generation, particularly in fields such as film production, gaming, and virtual reality, where precise control over both character and camera dynamics is crucial. By enabling zero-shot capabilities, ActCam opens avenues for more intuitive and flexible video generation workflows, allowing creators to focus on artistic expression without the need for extensive retraining of models. This work could inspire further research into joint control mechanisms in generative models, potentially leading to more sophisticated and user-friendly tools for content creation.

Authors: Omar El Khalifi, Thomas Rossi, Oscar Fossey, Thibault Fouque, Ulysse Mizrahi, Philip Torr, Ivan Laptev, Fabio Pizzati et al.  
Source: arXiv:2605.06667v1  
URL: https://arxiv.org/abs/2605.06667v1
