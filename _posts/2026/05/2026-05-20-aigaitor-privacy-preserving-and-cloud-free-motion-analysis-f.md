---
title: "AIGaitor: Privacy-preserving and cloud-free motion analysis for everyone, using edge computing"
date: 2026-05-20 17:14:57 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.21421v1"
arxiv_id: "2605.21421"
authors: ["Lauhitya Reddy", "Trisha M. Kesar", "Hyeokhyen Kwon"]
slug: aigaitor-privacy-preserving-and-cloud-free-motion-analysis-f
summary_word_count: 412
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in accessible and privacy-preserving motion analysis tools for clinical applications, particularly in gait analysis. Traditional motion capture systems are often prohibitively expensive, technically complex, and raise significant privacy concerns. The authors present AIGaitor, a novel system that operates entirely on consumer smartphones, thus eliminating the need for cloud computing. This work is a preprint and has not yet undergone peer review.

**Method**  
AIGaitor employs a markerless monocular motion-capture pipeline that integrates several optimized components for mobile iOS devices. Key technical contributions include:
- **Pose Estimation**: Utilizes lightweight models like ViTPose-s for real-time 2D and 3D pose estimation.
- **Pose Optimization**: Enhances the accuracy of the captured motion data.
- **Skeleton-based Deep Learning**: Implements models for gait classification and action recognition, achieving sub-millisecond inference times.
- **Vision-Language Model**: Integrates multimodal analysis to enhance interpretability and usability.
The end-to-end pipeline processes a 10-second 4K 60 fps video clip in 77 seconds on an iPhone 14, outperforming a high-end NVIDIA H200 cloud server when accounting for network transfer times (94 seconds at global mobile-average uplink and 66 seconds at developed-world Wi-Fi).

**Results**  
AIGaitor demonstrates significant performance metrics:
- The end-to-end processing time of 77 seconds on an iPhone 14 for a 10-second video clip is competitive with cloud-based solutions.
- Real-time keypoint extraction is achieved with ViTPose-s, while skeleton-based action recognition models provide gait classification in under 1 millisecond.
- The system's performance indicates that it can match or exceed traditional methods in both speed and efficiency, making it suitable for clinical applications.

**Limitations**  
The authors acknowledge several limitations:
- The reliance on consumer smartphone hardware may restrict performance compared to dedicated motion capture systems.
- The study's sample size for clinician surveys (74 participants) may not fully represent the broader clinical community.
- The system's effectiveness in diverse real-world environments and with varied populations remains to be validated.
- Potential challenges in handling occlusions or complex movement patterns are not explicitly addressed.

**Why it matters**  
AIGaitor's development has significant implications for the future of motion analysis in clinical settings. By providing a low-cost, privacy-preserving solution that operates on widely available consumer technology, it democratizes access to advanced gait analysis tools. This could lead to broader adoption in rehabilitation and physical therapy, ultimately improving patient outcomes. Furthermore, the integration of on-device processing aligns with trends towards edge computing, reducing reliance on cloud infrastructure and enhancing data security.

Authors: Lauhitya Reddy, Trisha M. Kesar, Hyeokhyen Kwon  
Source: arXiv:2605.21421  
URL: [https://arxiv.org/abs/2605.21421v1](https://arxiv.org/abs/2605.21421v1)
