---
title: "Spatially Prompted Visual Trajectory Prediction for Egocentric Manipulation"
date: 2026-05-19 16:39:30 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.20085v1"
arxiv_id: "2605.20085"
authors: ["Yifan Li", "Xinyu Zhou", "Yunhao Ge", "Yu Kong"]
slug: spatially-prompted-visual-trajectory-prediction-for-egocentr
summary_word_count: 433
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the literature regarding the specification of robotic manipulation tasks in cluttered environments, particularly when similar objects are present. Traditional methods often rely on language instructions or task identifiers, which can be ambiguous in complex scenes. The authors introduce the concept of Spatially Prompted Visual Trajectory Prediction (SP-VTP), formalizing a new setting where spatial prompts (e.g., bounding boxes or points) are used to define task objectives. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel architecture called SPOT (Spatially Prompted Object-Target Policy) to tackle the SP-VTP problem. SPOT consists of three main components: 
1. **Task Encoder**: Processes first-frame visual inputs and spatial prompts to encode task objectives.
2. **Observation Encoder**: Integrates current visual data and historical context to inform trajectory predictions.
3. **Trajectory Generator**: Outputs future end-effector trajectories based on the encoded information.

The model is trained on a newly collected dataset, EgoSPT, which includes egocentric spatially prompted manipulation trajectories with annotations for object and target grounding, as well as recovered 3D end-effector motion. The training compute details are not disclosed, but the dataset is designed to facilitate the learning of trajectory predictions in dynamic environments where the task specification remains static.

**Results**  
SPOT demonstrates significant improvements in cross-scene trajectory prediction compared to non-prompted and single-source prompted baselines. The authors report that SPOT achieves a notable increase in prediction accuracy, although specific numerical results and effect sizes are not detailed in the abstract. The experiments are conducted under strict scene-level splits, ensuring that the model's generalization capabilities are rigorously evaluated.

**Limitations**  
The authors acknowledge that the static nature of task specifications in SP-VTP presents inherent challenges, particularly as the scene configuration evolves. They do not discuss potential limitations related to the dataset size or diversity, which could affect the model's robustness in real-world applications. Additionally, the reliance on spatial prompts may limit the model's applicability in scenarios where such prompts are not feasible or available.

**Why it matters**  
The introduction of SP-VTP and the SPOT architecture has significant implications for the field of robotic manipulation, particularly in environments with high object density and similarity. By formalizing the use of spatial prompts, this work opens avenues for more intuitive and effective human-robot interaction, allowing robots to better understand and execute tasks based on visual cues. The establishment of the EgoSPT dataset also provides a valuable resource for future research in trajectory prediction and manipulation tasks, potentially leading to advancements in autonomous systems and robotics.

Authors: Yifan Li, Xinyu Zhou, Yunhao Ge, Yu Kong  
Source: arXiv:2605.20085  
URL: https://arxiv.org/abs/2605.20085v1
