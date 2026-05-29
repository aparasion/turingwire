---
title: "Benchmarking Single-Factor Physical Video-to-Audio Generation"
date: 2026-05-28 17:59:09 +0000
category: research
subcategory: evaluation_benchmarks
company: "NVIDIA"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.30339v1"
arxiv_id: "2605.30339"
authors: ["Tingle Li", "Siddharth Gururani", "Kevin J. Shih", "Gantavya Bhatt", "Sang-gil Lee", "Zhifeng Kong"]
slug: benchmarking-single-factor-physical-video-to-audio-generatio
summary_word_count: 452
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of generative video-to-audio (V2A) models, specifically the lack of focus on physical correctness in audio generation. Existing benchmarks primarily assess perceptual realism without rigorously testing the models' ability to capture underlying physical processes. The authors introduce FlatSounds, a novel benchmark designed to evaluate the physical reasoning capabilities of V2A models through controlled interventions. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the FlatSounds benchmark, which consists of two main evaluation strategies: (1) controlled counterfactual pairs that vary a single physical factor, and (2) single-video pattern tests that assess internal consistency and directional trends in audio generation. The benchmark aims to determine whether the generated audio accurately reflects specific physical properties and their temporal dynamics. The authors evaluate several state-of-the-art V2A models, analyzing their reliance on text captions versus visual input for inferring physical and semantic information. The study highlights a trade-off where captions enhance physical and semantic accuracy but negatively impact temporal alignment.

**Results**  
The evaluation reveals that models exhibit a consistent dependency on textual information, which improves physical and semantic accuracy but leads to degraded temporal alignment. The authors report that their physics-based metrics correlate strongly with human preference tests, indicating that models that perform well on these metrics are also favored by human evaluators. While specific numerical results are not disclosed in the abstract, the findings suggest a clear need for models to learn physical processes directly from visual data rather than relying heavily on textual descriptions.

**Limitations**  
The authors acknowledge that their benchmark may not cover all aspects of physical reasoning in V2A models and that the reliance on controlled counterfactuals may limit the generalizability of the findings. Additionally, the study does not explore the impact of varying the complexity of the physical scenarios presented to the models. An obvious limitation not flagged by the authors is the potential overfitting of models to the benchmark, as they may perform well on the specific tasks defined by FlatSounds without generalizing to broader, real-world scenarios.

**Why it matters**  
This work has significant implications for the development of V2A models, emphasizing the importance of integrating physical reasoning into generative processes. By moving beyond mere audio quality and focusing on the accurate representation of physical processes, future models can achieve greater realism and applicability in real-world contexts. The introduction of FlatSounds as a benchmark sets a precedent for evaluating generative models in a more holistic manner, potentially influencing subsequent research directions in multimodal learning and generative modeling.

Authors: Tingle Li, Siddharth Gururani, Kevin J. Shih, Gantavya Bhatt, Sang-gil Lee, Zhifeng Kong, Arushi Goel, Gopala Anumanchipalli et al.  
Source: arXiv:2605.30339  
URL: [https://arxiv.org/abs/2605.30339v1](https://arxiv.org/abs/2605.30339v1)
