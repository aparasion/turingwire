---
title: "YoCausal: How Far is Video Generation from World Model? A Causality Perspective"
date: 2026-05-28 17:59:51 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.30346v1"
arxiv_id: "2605.30346"
authors: ["You-Zhe Xie", "Yu-Hsuan Li", "Jie-Ying Lee", "Kaipeng Zhang", "Yu-Lun Liu", "Zhixiang Wang"]
slug: yocausal-how-far-is-video-generation-from-world-model-a-caus
summary_word_count: 443
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in understanding whether video diffusion models (VDMs) genuinely comprehend causality or merely exploit statistical temporal patterns. Existing benchmarks predominantly utilize synthetic datasets, which limits the generalization of VDMs to real-world scenarios due to the sim-to-real gap. The authors propose YoCausal, a novel two-level benchmark that incorporates real-world video data to evaluate causal reasoning in VDMs, inspired by the Violation of Expectation (VoE) paradigm from cognitive science. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
YoCausal consists of two evaluation levels. Level 1 introduces the Reverse Surprise Index (RSI), which quantifies the perception of the arrow of time through a denoising loss function applied to temporally reversed video samples. This allows for the assessment of how well VDMs can recognize temporal inconsistencies. Level 2 introduces the Causality Cognition Index (CCI), which employs a video language model (VLM) to categorize datasets into causal and non-causal subsets. This stratification enables the disentanglement of true causal reasoning from mere temporal biases. The authors do not disclose specific details regarding the architecture of the VDMs evaluated, the exact loss functions used, or the computational resources required for training.

**Results**  
The evaluation of 13 state-of-the-art VDMs using the YoCausal benchmark reveals that these models exhibit a significant gap in causal understanding compared to human-level cognition. The results indicate that while VDMs can perceive the arrow of time (as measured by RSI), this does not equate to an understanding of causality, as evidenced by their performance on the CCI. The paper does not provide specific numerical results or effect sizes against named baselines, which limits the ability to quantify the performance differences.

**Limitations**  
The authors acknowledge that their benchmark relies on the assumption that the Reverse Surprise Index and Causality Cognition Index are valid measures of causal understanding, which may require further validation. Additionally, the reliance on a VLM for dataset stratification could introduce biases based on the VLM's own limitations. The paper does not address potential confounding factors in the evaluation process or the generalizability of the findings across different types of video content.

**Why it matters**  
The implications of this work are significant for the development of VDMs and their application in real-world scenarios. By establishing a benchmark that emphasizes causal reasoning over mere temporal pattern recognition, this research encourages the design of more robust models that can better understand and predict real-world dynamics. This could lead to advancements in various applications, including autonomous systems, video analysis, and interactive AI, where a nuanced understanding of causality is crucial.

Authors: You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu, Zhixiang Wang  
Source: arXiv:2605.30346  
URL: https://arxiv.org/abs/2605.30346v1
