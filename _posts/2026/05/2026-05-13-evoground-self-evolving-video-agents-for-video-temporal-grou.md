---
title: "EvoGround: Self-Evolving Video Agents for Video Temporal Grounding"
date: 2026-05-13 17:25:51 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.13803v1"
arxiv_id: "2605.13803"
authors: ["Minjoon Jung", "Byoung-Tak Zhang", "Lorenzo Torresani"]
slug: evoground-self-evolving-video-agents-for-video-temporal-grou
summary_word_count: 415
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of video temporal grounding (VTG) without relying on large, manually annotated datasets, which are often expensive and time-consuming to create. The authors propose EvoGround, a self-evolving framework that utilizes two coupled agents to learn from raw video data, thereby filling a significant gap in the literature regarding unsupervised or weakly supervised approaches to VTG. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
EvoGround consists of two main components: a proposer and a solver, both initialized from the same backbone architecture. The proposer generates query-moment pairs from untrimmed videos, while the solver learns to ground these pairs temporally. The learning process is structured as a self-reinforcing reinforcement learning loop, where the solver provides feedback to the proposer, enhancing its query generation capabilities over iterations. The training is conducted on a dataset of 2,500 unlabeled videos, leveraging the mutual improvement of the agents to refine their performance. The specific architecture details, loss functions, and training compute resources are not disclosed in the paper.

**Results**  
EvoGround demonstrates competitive performance against fully supervised models across multiple VTG benchmarks. Notably, it matches or surpasses state-of-the-art results in fine-grained video captioning tasks without any manual labels. The authors report significant improvements in grounding accuracy, although specific numerical results and effect sizes compared to named baselines are not detailed in the abstract. The benchmarks used for evaluation include standard datasets in the VTG domain, but exact performance metrics are not provided in the summary.

**Limitations**  
The authors acknowledge that the proposed method may struggle with highly complex queries or videos with ambiguous content, as the lack of labeled data could hinder the learning of nuanced temporal relationships. Additionally, the reliance on a self-evolving mechanism may lead to convergence issues or suboptimal performance if the initial query generation is poor. The paper does not discuss potential scalability issues or the generalizability of the model to diverse video domains beyond those used in training.

**Why it matters**  
EvoGround's approach to VTG without manual annotations has significant implications for the field of video understanding and natural language processing. By demonstrating that self-evolving agents can effectively learn from raw video data, this work opens avenues for further research into unsupervised learning paradigms in multimodal contexts. The framework could inspire future developments in other areas of video analysis, such as action recognition and video summarization, where labeled data scarcity is a common challenge.

Authors: Minjoon Jung, Byoung-Tak Zhang, Lorenzo Torresani  
Source: arXiv:2605.13803  
URL: [https://arxiv.org/abs/2605.13803v1](https://arxiv.org/abs/2605.13803v1)
