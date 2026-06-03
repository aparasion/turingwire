---
title: "Benchmarking Visual State Tracking in Multimodal Video Understanding"
date: 2026-06-02 17:12:05 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2606.03920v1"
arxiv_id: "2606.03920"
authors: ["Sihyun Yu", "Nanye Ma", "Pinzhi Huang", "Hyunseok Lee", "Shusheng Yang", "June Suk Choi"]
slug: benchmarking-visual-state-tracking-in-multimodal-video-under
summary_word_count: 439
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces the Visual STAte Tracking benchmark (VSTAT) to evaluate visual state tracking capabilities in Multimodal Large Language Models (MLLMs)."
---

**Problem**  
The paper addresses a significant gap in the evaluation of Multimodal Large Language Models (MLLMs) regarding their ability to perform visual state tracking in video understanding. While existing benchmarks primarily focus on isolated moment recognition, they do not assess the continuous tracking of entities, states, and events over time. This limitation is critical, as effective video understanding requires integrating information across entire video streams. The authors present VSTAT, a novel benchmark designed to diagnose visual state tracking capabilities in MLLMs. This work is a preprint and has not undergone peer review.

**Method**  
VSTAT comprises 834 video clips sourced from both synthetic and real-world contexts, accompanied by 1,500 questions that necessitate continuous perception and integration of events throughout the video. The questions are structured to ensure that answers cannot be derived from isolated frames or short segments, thus compelling MLLMs to engage in temporal reasoning. The authors evaluate state-of-the-art MLLMs against this benchmark, analyzing their performance in terms of reasoning traces compared to the underlying video content. The study highlights the discrepancies between MLLMs' textual reasoning capabilities and their visual perception skills, revealing a critical area for improvement.

**Results**  
The evaluation reveals that state-of-the-art MLLMs significantly underperform compared to human benchmarks on VSTAT, achieving only modest improvements over answer-prior baselines. Specific performance metrics are not disclosed in the abstract, but the authors indicate that MLLMs struggle with visual perception, leading to failures in tracking necessary events. The preliminary findings suggest that even recent agentic approaches, including MLLM-based video agents and coding agents, do not adequately address these shortcomings, as they still fall short on VSTAT.

**Limitations**  
The authors acknowledge that their findings are preliminary and that the benchmark itself may require further refinement to fully capture the complexities of visual state tracking. They also note that the performance metrics for MLLMs on VSTAT are not detailed, which limits the ability to quantify the extent of the performance gap. Additionally, the reliance on a specific set of video clips may not generalize across all video understanding tasks, potentially constraining the benchmark's applicability.

**Why it matters**  
The introduction of VSTAT has significant implications for the development of MLLMs, as it highlights the critical need for improved visual perception capabilities in video understanding tasks. By identifying the specific areas where MLLMs fail, this benchmark can guide future research towards enhancing the integration of visual and textual reasoning. The findings underscore the importance of continuous tracking in video analysis, which is essential for applications in various domains, including autonomous systems and interactive AI. This work contributes to the ongoing discourse in multimodal learning, as discussed in related literature, and is available on [arXiv](https://arxiv.org/abs/2606.03920v1).
