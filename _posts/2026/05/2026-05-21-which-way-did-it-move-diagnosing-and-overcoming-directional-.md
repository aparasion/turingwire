---
title: "Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs"
date: 2026-05-21 17:59:56 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.22823v1"
arxiv_id: "2605.22823"
authors: ["Jongseo Lee", "Hyuntak Lee", "Sunghun Kim", "Sooa Kim", "Jihoon Chung", "Jinwoo Choi"]
slug: which-way-did-it-move-diagnosing-and-overcoming-directional-
summary_word_count: 462
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the capabilities of Video Large Language Models (Video-LLMs) regarding their understanding of directional motion in video sequences. Despite advancements in temporal video comprehension, many Video-LLMs exhibit a phenomenon termed "directional motion blindness," where they struggle to accurately perceive and interpret the direction of motion (left, right, up, down) in simple video scenarios. The authors highlight that existing models perform near chance levels on these tasks, with any above-chance performance being attributed to prediction biases rather than true comprehension. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach to mitigate directional motion blindness through two main contributions: the introduction of the MoDirect dataset family for motion direction instruction tuning and the DeltaDirect objective for diagnosis-driven training. MoDirect consists of synthetic and real-world benchmarks designed specifically for evaluating motion direction understanding. DeltaDirect is a projector-level objective that predicts normalized 2-D motion vectors based on feature deltas from adjacent frames. The authors demonstrate that while motion direction information is accessible through the Video-LLM architecture, the binding of this information to the correct verbal outputs is inadequate. Instruction tuning with DeltaDirect is shown to enhance the model's ability to bind motion direction signals effectively.

**Results**  
The results indicate substantial improvements in motion direction accuracy following the application of DeltaDirect. On the MoDirect-SynBench, the accuracy increased from 25.9% to 85.4% after instruction tuning. In real-world scenarios evaluated on MoDirect-RealBench, the DeltaDirect approach yielded a 21.9 percentage point improvement over the baseline model, achieving significant gains without the need for additional real-world tuning data. These results underscore the effectiveness of the proposed methods in enhancing the directional motion understanding capabilities of Video-LLMs.

**Limitations**  
The authors acknowledge that while synthetic motion direction instruction tuning improves performance, the visual complexity of real-world videos can diminish the signal strength of motion direction information, potentially limiting generalization. They also note that the current approach may not fully address all aspects of motion understanding, particularly in more complex scenarios involving multiple moving objects or occlusions. Additionally, the reliance on synthetic data for training raises questions about the robustness of the model in diverse real-world applications.

**Why it matters**  
This work has significant implications for the development of more perceptually aware Video-LLMs, which are crucial for applications in video analysis, autonomous systems, and human-computer interaction. By addressing the binding gap in motion direction understanding, the proposed methods can enhance the interpretability and reliability of Video-LLMs in real-world contexts. Furthermore, the introduction of the MoDirect dataset family sets a foundation for future research in motion perception, potentially leading to more sophisticated models capable of nuanced temporal understanding.

Authors: Jongseo Lee, Hyuntak Lee, Sunghun Kim, Sooa Kim, Jihoon Chung, Jinwoo Choi  
Source: arXiv cs.CV  
URL: [https://arxiv.org/abs/2605.22823v1](https://arxiv.org/abs/2605.22823v1)
