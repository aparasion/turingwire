---
title: "BlitzGS: City-Scale Gaussian Splatting at Lightning Speed"
date: 2026-05-13 17:13:59 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.13794v1"
arxiv_id: "2605.13794"
authors: ["Zhongtao Wang", "Huishan Au", "Yilong Li", "Mai Su", "Haojie Jin", "Yisong Chen"]
slug: blitzgs-city-scale-gaussian-splatting-at-lightning-speed
summary_word_count: 449
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in city-scale 3D reconstruction using Gaussian splatting, particularly the high computational workload associated with rendering large datasets. The authors present BlitzGS, a distributed framework that aims to optimize Gaussian workload management for faster rendering. This work is a preprint and has not yet undergone peer review, indicating that the findings should be interpreted with caution.

**Method**  
BlitzGS introduces a multi-level approach to manage Gaussian workloads effectively. At the system level, it employs an innovative sharding strategy that partitions Gaussians across GPUs based on index parity rather than traditional spatial blocks. This method reduces visibility redundancy that typically arises from spatial partitioning. The framework also implements a single cross-GPU exchange during rendering, which routes projected Gaussians to their respective tile owners, streamlining the rendering process.

At the model level, BlitzGS incorporates scheduled importance-scoring passes that dynamically reduce the global Gaussian population. During these passes, it computes a per-Gaussian visibility weight to prioritize density-control updates for contributing primitives and generates a per-view importance mask to enhance the view-level rendering efficiency. 

At the view level, the framework utilizes a distance-based Level of Detail (LOD) gate to filter out excessively fine primitives that are not relevant to the current camera frustum. Additionally, an importance-based culling mask is applied to skip Gaussians that contribute minimally across views, further optimizing the rendering pipeline.

**Results**  
BlitzGS demonstrates significant performance improvements over existing large-scale baselines. The framework achieves rendering quality comparable to state-of-the-art methods while delivering an order-of-magnitude speedup, enabling city-scale scene training in mere tens of minutes. Specific quantitative results are not disclosed in the abstract, but the authors claim substantial efficiency gains, suggesting a transformative impact on the speed of 3D reconstruction tasks.

**Limitations**  
The authors acknowledge that while BlitzGS significantly reduces rendering time, the framework's reliance on GPU sharding may introduce challenges in scenarios with uneven workload distribution across GPUs. Additionally, the importance-scoring mechanism may not generalize well to all types of scenes, particularly those with highly variable Gaussian distributions. The paper does not address potential limitations related to the scalability of the framework beyond city-scale scenes or the impact of varying hardware configurations on performance.

**Why it matters**  
The implications of BlitzGS are substantial for the field of computer vision and graphics, particularly in applications requiring real-time rendering of large-scale environments, such as urban planning, virtual reality, and autonomous navigation. By significantly reducing the computational burden associated with Gaussian splatting, this framework paves the way for more efficient and scalable 3D reconstruction techniques, potentially enabling broader adoption in both academic research and industry applications.

Authors: Zhongtao Wang, Huishan Au, Yilong Li, Mai Su, Haojie Jin, Yisong Chen, Meng Gai, Fei Zhu et al.  
Source: arXiv:2605.13794  
URL: https://arxiv.org/abs/2605.13794v1
