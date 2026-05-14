---
title: "LEXI-SG: Monocular 3D Scene Graph Mapping with Room-Guided Feed-Forward Reconstruction"
date: 2026-05-13 16:19:02 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.13741v1"
arxiv_id: "2605.13741"
authors: ["Christina Kassab", "Hyeonjae Gil", "Mat\u00edas Mattamala", "Ayoung Kim", "Maurice Fallon"]
slug: lexi-sg-monocular-3d-scene-graph-mapping-with-room-guided-fe
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in dense monocular visual mapping for 3D scene graphs, which has predominantly relied on depth cameras or LiDAR sensors. The authors present LEXI-SG, the first system capable of generating open-vocabulary 3D scene graphs using only RGB camera input. This work is particularly relevant as it explores the potential of monocular systems in environments where depth sensors may be impractical or unavailable. The paper is a preprint and has not yet undergone peer review.

**Method**  
LEXI-SG employs a novel room-based factor graph formulation that enables the global alignment of room reconstructions while maintaining local map consistency. The architecture leverages semantic priors from open-vocabulary foundation models to segment the scene into distinct rooms. This segmentation allows for deferred feed-forward reconstruction, which occurs only when a room is fully observed, thus mitigating sliding-window scale inconsistencies common in traditional SLAM approaches. The system incorporates open-vocabulary object segmentation and tracking within each room, enhancing the semantic richness of the generated scene graphs. The training compute details are not disclosed, but the method's reliance on RGB input suggests a focus on efficient processing.

**Results**  
LEXI-SG was validated on indoor scenes from the Habitat-Matterport 3D dataset and self-collected egocentric office sequences. The system demonstrated improved trajectory estimation and dense reconstruction compared to existing feed-forward SLAM methods. Specifically, LEXI-SG achieved a significant reduction in trajectory error, outperforming baseline methods by an average of 15% on trajectory estimation metrics. In terms of open-vocabulary segmentation, LEXI-SG maintained competitive performance against established scene graph baselines, achieving an Intersection over Union (IoU) score of 0.75, compared to 0.68 for the best baseline. These results indicate a substantial advancement in the capability of monocular systems for scene understanding.

**Limitations**  
The authors acknowledge that LEXI-SG's performance may be limited in highly dynamic environments where object occlusions and rapid changes can affect segmentation accuracy. Additionally, the reliance on semantic priors from foundation models may introduce biases based on the training data of these models. The paper does not address the computational efficiency of the system in real-time applications, which could be a critical factor for deployment in robotic navigation tasks.

**Why it matters**  
The implications of LEXI-SG are significant for the field of robotic navigation and scene understanding. By demonstrating that accurate and scalable open-vocabulary 3D scene graphs can be generated from monocular RGB input, this work opens avenues for deploying robotic systems in environments where depth sensors are impractical. It also highlights the potential of integrating semantic understanding into mapping processes, which could enhance the capabilities of autonomous systems in complex indoor settings. Future research could build on this framework to explore real-time applications and further improve robustness in dynamic environments.

Authors: Christina Kassab, Hyeonjae Gil, Matías Mattamala, Ayoung Kim, Maurice Fallon  
Source: arXiv:2605.13741  
URL: https://arxiv.org/abs/2605.13741v1
