---
title: "HarmoVid: Relightful Video Portrait Harmonization"
date: 2026-05-27 17:59:02 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.28811v1"
arxiv_id: "2605.28811"
authors: ["Jun Myeong Choi", "Jae Shin Yoon", "Luchao Qi", "Roni Sengupta", "Joon-Young Lee"]
slug: harmovid-relightful-video-portrait-harmonization
summary_word_count: 463
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of harmonizing the lighting of foreground videos to match a target background scene, a task referred to as relightful harmonization. The authors highlight a significant gap in the literature regarding the acquisition of labeled video data, as it is impractical to obtain paired video samples with identical motions under varying lighting conditions. Existing methods that apply image-based harmonization techniques to video frames often result in temporal inconsistencies, leading to visual artifacts such as flickering. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach called HarmoVid, which integrates a lighting deflickering model to stabilize both global and local lighting fluctuations in videos. The architecture employs a video diffusion model trained on a combination of real and synthetic video datasets, which enhances the quality of the harmonization process. The training process leverages an asymmetric alpha mask conditioning technique that effectively learns clean boundaries from real video data. This method allows for improved delineation between the foreground and background, contributing to the overall quality of the harmonization. The authors do not disclose specific details regarding the training compute or the exact volume of data used, but they emphasize the importance of both real and synthetic video inputs in achieving robust results.

**Results**  
HarmoVid demonstrates superior performance in terms of temporal coherence, naturalness, and boundary clarity compared to existing image-based and video-based harmonization methods. The authors report significant improvements in relighting expressiveness, although specific quantitative metrics (e.g., PSNR, SSIM) and comparisons against named baselines are not provided in the abstract. The qualitative results indicate that the model effectively mitigates flickering artifacts while maintaining physically plausible lighting behavior, suggesting a strong advancement over prior techniques.

**Limitations**  
The authors acknowledge that their method may still face challenges in extreme lighting conditions or highly dynamic scenes, which could affect the quality of harmonization. Additionally, the reliance on synthetic data for training may introduce biases that do not generalize well to all real-world scenarios. The paper does not discuss the computational efficiency of the model or the potential for real-time applications, which are critical considerations for practical deployment.

**Why it matters**  
The implications of this work are significant for various applications in video editing, augmented reality, and film production, where consistent lighting across foreground and background elements is crucial. By addressing the limitations of existing methods and providing a solution that enhances temporal coherence and visual quality, HarmoVid sets a new standard for video harmonization tasks. This research opens avenues for further exploration in the integration of advanced machine learning techniques for video processing, particularly in scenarios requiring real-time performance and adaptability to diverse lighting conditions.

Authors: Jun Myeong Choi, Jae Shin Yoon, Luchao Qi, Roni Sengupta, Joon-Young Lee  
Source: arXiv:2605.28811  
URL: [https://arxiv.org/abs/2605.28811v1](https://arxiv.org/abs/2605.28811v1)
