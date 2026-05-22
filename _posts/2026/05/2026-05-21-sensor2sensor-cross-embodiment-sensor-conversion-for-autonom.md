---
title: "Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving"
date: 2026-05-21 17:57:17 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.22809v1"
arxiv_id: "2605.22809"
authors: ["Jiahao Wang", "Bo Sun", "Yijing Bai", "Vincent Casser", "Songyou Peng", "Zehao Zhu"]
slug: sensor2sensor-cross-embodiment-sensor-conversion-for-autonom
summary_word_count: 464
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the availability of diverse and high-fidelity datasets for training and validating Autonomous Driving Systems (ADS). While proprietary data from Autonomous Vehicle (AV) fleets is high-quality, it suffers from limitations in scale, sensor diversity, and geographic coverage. Conversely, in-the-wild data from dashcams offers extensive diversity and captures critical long-tail scenarios but is unstructured and incompatible with the structured, multi-modal sensor inputs required by ADS. The authors propose Sensor2Sensor, a generative modeling framework to convert unstructured dashcam videos into structured multi-modal sensor data, thereby bridging this data gap. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of Sensor2Sensor is its generative modeling paradigm that employs a two-step process. First, it utilizes 4D Gaussian Splatting (4DGS) for reconstructing real AV logs into dashcam-style videos, enabling the generation of paired data from unpaired sources. Second, a diffusion architecture is employed to perform the generative conversion from dashcam videos to high-fidelity multi-modal sensor outputs, including multi-view camera images and LiDAR point clouds. The training process leverages a large corpus of unstructured dashcam footage, although specific details regarding the training compute and hyperparameters are not disclosed.

**Results**  
The authors conduct comprehensive quantitative evaluations to assess the fidelity and realism of the generated sensor data. They demonstrate that Sensor2Sensor can effectively convert challenging in-the-wild dashcam footage into realistic multi-modal data formats. While specific numerical results and comparisons against baseline models are not detailed in the abstract, the authors claim significant improvements in the realism and utility of the generated data for AV development, suggesting a substantial effect size in practical applications.

**Limitations**  
The authors acknowledge the challenge of the lack of paired training data, which is a fundamental limitation of their approach. Additionally, they do not discuss potential biases in the generated data that may arise from the source dashcam footage, nor do they address the computational efficiency of the 4DGS reconstruction and diffusion processes. The reliance on the quality of the input dashcam videos may also limit the generalizability of the model across different environments and sensor configurations.

**Why it matters**  
The implications of this work are significant for the field of autonomous driving, as it opens up vast external data sources for training and validation of ADS. By enabling the conversion of unstructured dashcam footage into structured sensor data, Sensor2Sensor can facilitate the development of more robust and diverse training datasets, ultimately improving the performance and safety of autonomous systems. This approach could lead to advancements in the scalability of data collection for AVs, particularly in underrepresented scenarios, thereby enhancing the overall reliability of ADS in real-world applications.

Authors: Jiahao Wang, Bo Sun, Yijing Bai, Vincent Casser, Songyou Peng, Zehao Zhu, Meng-Li Shih, Xander Masotto et al.  
Source: arXiv:2605.22809  
URL: https://arxiv.org/abs/2605.22809v1
