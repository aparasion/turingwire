---
title: "MaD Physics: Evaluating information seeking under constraints in physical environments"
date: 2026-05-11 16:37:19 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10820v1"
arxiv_id: "2605.10820"
authors: ["Moksh Jain", "Mehdi Bennani", "Johannes Bausch", "Yuri Chervonyi", "Bogdan Georgiev", "Simon Osindero"]
slug: mad-physics-evaluating-information-seeking-under-constraints
summary_word_count: 476
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of agents designed for scientific discovery, particularly under resource constraints. Existing benchmarks primarily focus on static knowledge-based reasoning or unconstrained experimental design, failing to assess the ability of agents to make measurements and plan effectively when limited by physical and cost constraints. The authors propose the Measuring and Discovering Physics (MaD Physics) benchmark to fill this void. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The MaD Physics benchmark consists of three distinct environments, each modeled on a different physical law, with modifications to prevent reliance on existing knowledge. Agents are tasked with making measurements within a defined budget, after which they must infer the underlying physical law and predict future states of the system. The benchmark evaluates two core capabilities: (1) model inference from data and (2) planning under constraints. The authors also suggest that MaD Physics can assess additional capabilities such as multimodality and in-context learning. The evaluation employs four variants of the Gemini model (2.5 Flash Lite, 2.5 Flash, 2.5 Pro, and 3 Flash), focusing on their structured exploration and data collection abilities.

**Results**  
The authors benchmarked the Gemini models on the MaD Physics environments, revealing notable deficiencies in their structured exploration and data collection capabilities. While specific numerical results are not disclosed in the abstract, the paper indicates that the models struggled to effectively navigate the constraints imposed by the benchmark, highlighting areas for improvement in scientific reasoning. The results suggest that the models' performance is suboptimal when faced with the complexities of real-world scientific inquiry under resource limitations.

**Limitations**  
The authors acknowledge that the benchmark is limited to three environments, which may not encompass the full spectrum of physical laws and scenarios encountered in scientific discovery. Additionally, the reliance on modified physical laws could impact the generalizability of the findings. The paper does not address potential biases introduced by the specific design of the environments or the training data used for the Gemini models. Furthermore, the evaluation does not consider the computational efficiency of the models, which could be a critical factor in real-world applications.

**Why it matters**  
The introduction of the MaD Physics benchmark has significant implications for the development of AI agents in scientific discovery. By emphasizing the importance of making measurements and planning under constraints, this work encourages the design of more robust and capable agents that can operate effectively in resource-limited environments. The findings from the benchmark can guide future research in improving structured exploration and data collection strategies, ultimately enhancing the ability of AI systems to contribute to scientific inquiry. This work lays the groundwork for further exploration of multimodal and in-context learning capabilities in the context of scientific discovery.

Authors: Moksh Jain, Mehdi Bennani, Johannes Bausch, Yuri Chervonyi, Bogdan Georgiev, Simon Osindero, Nenad Tomašev  
Source: arXiv:2605.10820  
URL: [https://arxiv.org/abs/2605.10820v1](https://arxiv.org/abs/2605.10820v1)
