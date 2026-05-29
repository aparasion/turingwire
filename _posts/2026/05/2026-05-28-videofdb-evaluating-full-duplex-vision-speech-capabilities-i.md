---
title: "VideoFDB: Evaluating Full-Duplex Vision-Speech Capabilities in Conversational Agents"
date: 2026-05-28 17:20:01 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.30256v1"
arxiv_id: "2605.30256"
authors: ["Amrita Mazumdar", "Seonwook Park", "Rajarshi Roy", "Nikhil Srihari", "Shengze Wang", "Yuhao Zhou"]
slug: videofdb-evaluating-full-duplex-vision-speech-capabilities-i
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of conversational agents by introducing VideoFDB, the first benchmark specifically designed for full-duplex audio-visual-to-audio-visual (AV2AV) interactions. Existing benchmarks primarily focus on speech, neglecting the critical role of nonverbal cues in human conversation. The authors highlight that current systems fail to model the simultaneous processing of audio and visual information, which is essential for natural human-agent interaction. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contributions of VideoFDB include:  
1. A dataset comprising 237 dyadic video clips that capture 11 distinct nonverbal conversational dynamics from real-world video calls.  
2. A taxonomy that differentiates between perception and generation behaviors in conversational agents, allowing for a more nuanced evaluation of their capabilities.  
3. An innovative rubric-based evaluation framework, termed LM-as-judge, which employs language models to assess conversational quality across interpretable axes related to nonverbal dynamics. This framework facilitates a structured analysis of how well agents can replicate human-like conversational behaviors.

The evaluation reveals systematic failure modes in existing vision-speech agents, such as "captioning collapse" and "visual-stream ignorance." The authors also investigate cascaded speech-to-avatar systems, concluding that their architectural limitations hinder the production of full-duplex nonverbal cues.

**Results**  
The authors benchmark various open- and closed-source vision-speech agents against the VideoFDB dataset. They report that these systems exhibit significant deficiencies in leveraging visual information for joint audiovisual grounding, which is crucial for natural conversation. For instance, while agents perform adequately in explicit visual question answering tasks, they struggle with maintaining coherent audiovisual interactions. The paper does not provide specific quantitative metrics or effect sizes against named baselines, focusing instead on qualitative assessments of failure modes.

**Limitations**  
The authors acknowledge several limitations, including the relatively small size of the VideoFDB dataset, which may restrict the generalizability of their findings. They also note that the focus on dyadic interactions may not fully capture the complexities of group conversations. Additionally, the evaluation framework, while innovative, may introduce biases based on the language model's inherent limitations. The authors do not address potential ethical considerations related to the use of real-world video data or the implications of deploying such systems in sensitive contexts.

**Why it matters**  
The introduction of VideoFDB is a pivotal step toward advancing multimodal conversational agents capable of full-duplex interactions. By establishing a comprehensive evaluation framework that incorporates nonverbal dynamics, this work lays the groundwork for future research aimed at enhancing the realism and effectiveness of human-agent interactions. The findings underscore the necessity for agents to integrate visual and auditory cues seamlessly, which could lead to more intuitive and engaging user experiences in applications ranging from virtual assistants to telepresence systems.

Authors: Amrita Mazumdar, Seonwook Park, Rajarshi Roy, Nikhil Srihari, Shengze Wang, Yuhao Zhou, Julia Wang, Koki Nagano et al.  
Source: arXiv:2605.30256  
URL: [https://arxiv.org/abs/2605.30256v1](https://arxiv.org/abs/2605.30256v1)
