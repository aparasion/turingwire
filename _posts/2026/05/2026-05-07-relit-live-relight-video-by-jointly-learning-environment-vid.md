---
title: "Relit-LiVE: Relight Video by Jointly Learning Environment Video"
date: 2026-05-07 17:58:15 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.06658v1"
arxiv_id: "2605.06658"
authors: ["Weiqing Xiao", "Hong Li", "Xiuyu Yang", "Houyuan Chen", "Wenyi Li", "Tianqi Liu"]
slug: relit-live-relight-video-by-jointly-learning-environment-vid
summary_word_count: 392
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing video relighting techniques that rely on intrinsic scene decomposition, which is often inaccurate for real-world videos. The authors highlight that current methods lead to distorted appearances, broken materials, and temporal artifacts during relighting. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors introduce Relit-LiVE, a video relighting framework that integrates raw reference images into the rendering process. This approach allows the model to recover essential scene cues that are typically lost in intrinsic representations. The framework employs a novel environment video prediction formulation that generates both relit videos and per-frame environment maps in a unified diffusion process. This joint prediction mechanism enhances geometric-illumination alignment and accommodates dynamic lighting and camera motion without requiring prior knowledge of camera pose. The architecture leverages large-scale video diffusion models, although specific details regarding the model architecture, loss functions, and training compute are not disclosed.

**Results**  
Relit-LiVE demonstrates superior performance compared to state-of-the-art video relighting and neural rendering methods across various benchmarks, both synthetic and real-world. The authors report significant improvements in physical consistency and temporal stability, although specific quantitative metrics (e.g., PSNR, SSIM) and comparisons against named baselines are not detailed in the abstract. The results suggest a marked reduction in visual artifacts and improved realism in relit videos.

**Limitations**  
The authors acknowledge that while their method improves upon existing techniques, it still relies on the quality of the raw reference images, which may vary in real-world scenarios. Additionally, the framework's performance in highly complex scenes with extreme lighting conditions is not thoroughly evaluated. The lack of detailed quantitative results in the abstract limits the ability to fully assess the effectiveness of the proposed method against specific baselines.

**Why it matters**  
Relit-LiVE has significant implications for various downstream applications, including scene-level rendering, material editing, object insertion, and streaming video relighting. By improving the physical consistency and temporal stability of video relighting, this framework can enhance the realism of computer-generated imagery in film, gaming, and virtual reality. Furthermore, the ability to operate without prior camera pose knowledge broadens the applicability of the method in real-world scenarios, potentially leading to advancements in interactive media and augmented reality experiences.

Authors: Weiqing Xiao, Hong Li, Xiuyu Yang, Houyuan Chen, Wenyi Li, Tianqi Liu, Shaocong Xu, Chongjie Ye et al.  
Source: arXiv:2605.06658  
URL: [https://arxiv.org/abs/2605.06658v1](https://arxiv.org/abs/2605.06658v1)
