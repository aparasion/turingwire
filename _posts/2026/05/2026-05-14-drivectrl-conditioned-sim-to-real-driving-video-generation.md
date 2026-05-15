---
title: "DriveCtrl: Conditioned Sim-to-Real Driving Video Generation"
date: 2026-05-14 17:29:35 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.15116v1"
arxiv_id: "2605.15116"
authors: ["Haonan Zhao", "Yiting Wang", "Jingkun Chen", "Valentina Donzella", "Thomas Bashford-Rogers", "Kurt Debattista"]
slug: drivectrl-conditioned-sim-to-real-driving-video-generation
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the significant domain gap between synthetic and real-world driving videos, which limits the utility of simulation-generated data for training autonomous driving systems. Existing video generation methods inadequately preserve essential attributes such as scene structure, object dynamics, temporal consistency, and visual realism, which are critical for maintaining the validity of annotations in generated data. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce DriveCtrl, a depth-conditioned controllable sim-to-real video generation framework. DriveCtrl is built upon a pretrained video foundation model and incorporates a structure-aware adapter that facilitates depth-guided generation. This architecture ensures that the generated videos maintain the scene layout and motion patterns of the source simulation, resulting in temporally coherent driving videos aligned with the original simulated sequences. The framework employs a scalable data generation pipeline that transforms simulator videos into realistic driving footage, matching the visual style of a target real-world dataset. The pipeline supports three conditioning signals: structural depth, reference-dataset style, and text prompts, while preserving frame-level annotations for downstream perception tasks. Additionally, the authors propose a novel evaluation metric, the Driving Video Realism Score (DVRS), specifically designed to assess the realism of generated driving videos.

**Results**  
DriveCtrl demonstrates superior performance compared to baseline models and competing alternatives across multiple dimensions. The authors report significant improvements in realism and temporal quality, as well as enhanced performance in downstream perception tasks. While specific numerical results are not disclosed in the abstract, the paper claims that DriveCtrl substantially narrows the sim-to-real gap for driving video generation, indicating a meaningful effect size in the context of driving video realism.

**Limitations**  
The authors acknowledge that the proposed method may still face challenges in fully replicating the complexities of real-world driving scenarios, particularly in edge cases or rare events that may not be well-represented in the training data. Additionally, the reliance on a pretrained video foundation model may limit the generalizability of the approach to other domains outside of driving. The paper does not discuss potential computational costs associated with the depth conditioning and the scalability of the data generation pipeline.

**Why it matters**  
DriveCtrl has significant implications for the development of autonomous driving systems, as it provides a robust framework for generating high-fidelity driving videos that can be used for training and evaluation. By effectively bridging the sim-to-real gap, this work enhances the potential for using synthetic data in real-world applications, thereby reducing the reliance on large-scale labeled real-world datasets. The introduction of the DVRS metric also contributes to the evaluation landscape for video generation in the driving domain, paving the way for future research to build upon these findings.

Authors: Haonan Zhao, Yiting Wang, Jingkun Chen, Valentina Donzella, Thomas Bashford-Rogers, Kurt Debattista  
Source: arXiv:2605.15116  
URL: [https://arxiv.org/abs/2605.15116v1](https://arxiv.org/abs/2605.15116v1)
