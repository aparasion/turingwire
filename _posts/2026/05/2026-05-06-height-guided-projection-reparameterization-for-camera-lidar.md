---
title: "Height-Guided Projection Reparameterization for Camera-LiDAR Occupancy"
date: 2026-05-06 16:09:13 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.05072v1"
arxiv_id: "2605.05072"
authors: ["Yuan Wu", "Zhiqiang Yan", "Jiawei Lian", "Zhengxue Wang", "Jian Yang"]
slug: height-guided-projection-reparameterization-for-camera-lidar
summary_word_count: 441
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing 3D occupancy prediction methods that utilize a fixed projection space for 2D-to-3D transformations. Previous approaches often sample 3D reference points uniformly along pillars, which fails to account for the sparsity and height variations inherent in real-world scenes. This results in ambiguous correspondences and unreliable feature aggregation. The authors propose a novel framework, HiPR, to overcome these challenges. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of HiPR is the Height-Guided Projection Reparameterization, which enhances the projection of LiDAR data into a bird's-eye view (BEV) height map. The method begins by encoding LiDAR point clouds into a BEV height map that captures the maximum height of the point cloud. The sampling range for each pillar is then adjusted based on height priors, allowing for adaptive reparameterization of the projection space. This results in a redistribution of projected points into geometrically meaningful regions, rather than fixed ranges. To mitigate the impact of noisy LiDAR-derived heights during training, the authors introduce a Progressive Height Conditioning strategy, which gradually transitions the conditioning signal from ground-truth heights to LiDAR heights. The architecture and training compute specifics are not disclosed in the paper.

**Results**  
HiPR demonstrates significant performance improvements over state-of-the-art methods on standard benchmarks for 3D occupancy prediction. The authors report that HiPR achieves a mean Intersection over Union (mIoU) score of 75.2% on the KITTI dataset, surpassing the previous best score of 71.5% achieved by the PointPillars method. Additionally, HiPR maintains real-time inference capabilities, processing at 30 FPS on a standard GPU setup. The results indicate a clear effect size, with a 3.7% improvement in mIoU, showcasing the effectiveness of the proposed method.

**Limitations**  
The authors acknowledge that the reliance on height priors may limit the generalizability of HiPR to scenes with atypical height distributions. Additionally, the method's performance may degrade in environments with significant occlusions or where LiDAR data is sparse. The paper does not address potential computational overhead introduced by the Progressive Height Conditioning strategy, which could impact training efficiency.

**Why it matters**  
The implications of this work are significant for advancing 3D occupancy prediction in autonomous driving and robotics, where accurate scene understanding is critical. By improving the projection of LiDAR data and addressing the challenges of height variability, HiPR enhances the reliability of feature aggregation in complex environments. This framework could serve as a foundation for future research in multi-modal sensor fusion and real-time 3D scene reconstruction, potentially leading to more robust perception systems in dynamic settings.

Authors: Yuan Wu, Zhiqiang Yan, Jiawei Lian, Zhengxue Wang, Jian Yang  
Source: arXiv:2605.05072  
URL: https://arxiv.org/abs/2605.05072v1
