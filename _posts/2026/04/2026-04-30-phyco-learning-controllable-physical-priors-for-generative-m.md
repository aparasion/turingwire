---
title: "PhyCo: Learning Controllable Physical Priors for Generative Motion"
date: 2026-04-30 17:53:03 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28169v1"
arxiv_id: "2604.28169"
authors: ["Sriram Narayanan", "Ziyu Jiang", "Srinivasa Narasimhan", "Manmohan Chandraker"]
slug: phyco-learning-controllable-physical-priors-for-generative-m
summary_word_count: 456
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in generative video models regarding physical consistency, specifically in the context of video diffusion models that excel in appearance synthesis but fail to maintain realistic physical interactions, such as object drift, collision responses, and material properties. The authors present PhyCo, a framework designed to incorporate controllable physical priors into video generation. This work is a preprint and has not yet undergone peer review.

**Method**  
PhyCo integrates three main components to achieve its objectives:  
1. **Dataset**: A large-scale dataset comprising over 100,000 photorealistic simulation videos is introduced, where key physical parameters such as friction, restitution, deformation, and force are systematically varied across diverse scenarios. This dataset serves as the foundation for training and fine-tuning the model.
2. **Physics-Supervised Fine-Tuning**: The authors employ a pretrained diffusion model, which is fine-tuned using a ControlNet architecture. This model is conditioned on pixel-aligned physical property maps, allowing it to learn the relationships between visual features and physical attributes.
3. **VLM-Guided Reward Optimization**: A vision-language model (VLM) is utilized to evaluate the generated videos based on targeted physics queries. This model provides differentiable feedback, enabling the optimization of the generative process to enhance physical realism.

The training process leverages the large dataset and the physics-supervised fine-tuning to ensure that the generated videos exhibit controllable physical attributes without requiring a simulator or geometry reconstruction during inference.

**Results**  
PhyCo demonstrates significant improvements in physical realism on the Physics-IQ benchmark compared to strong baselines. The authors report that their method achieves a notable increase in performance metrics, although specific numerical results are not disclosed in the abstract. Additionally, human studies indicate that users perceive clearer and more faithful control over physical attributes in the generated videos, suggesting a qualitative enhancement in user experience.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a large-scale dataset that may not encompass all possible physical scenarios, potentially limiting generalization. They also note that while the model improves physical consistency, it may still struggle with complex interactions not represented in the training data. Furthermore, the absence of peer review raises questions about the robustness of the findings and the potential for undisclosed biases in the dataset or model evaluation.

**Why it matters**  
PhyCo's approach represents a significant advancement in the field of generative video modeling by introducing a framework that allows for the generation of physically consistent and controllable outputs. This has implications for various downstream applications, including robotics, virtual reality, and simulation environments, where realistic physical interactions are crucial. The ability to generate videos that adhere to physical laws without the need for complex simulations opens new avenues for research and development in generative modeling and interactive systems.

Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
Source: arXiv:2604.28169  
URL: [https://arxiv.org/abs/2604.28169v1](https://arxiv.org/abs/2604.28169v1)
