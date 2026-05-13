---
title: "Classifier Context Rot: Monitor Performance Degrades with Context Length"
date: 2026-05-12 16:34:03 +0000
category: research
subcategory: alignment_safety
company: "Google DeepMind"
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12366v1"
arxiv_id: "2605.12366"
authors: ["Sam Martin", "Fabien Roger"]
slug: classifier-context-rot-monitor-performance-degrades-with-con
summary_word_count: 466
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the evaluation of language models (LMs) for monitoring coding agents, particularly in the context of long transcripts exceeding 500K tokens. Existing benchmarks have primarily focused on shorter transcripts (under 100K tokens), which do not adequately reflect the performance of LMs in real-world scenarios where context length can dramatically affect classification accuracy. The authors highlight that current state-of-the-art models fail to detect dangerous actions in lengthy transcripts, raising concerns about the reliability of these models in critical applications.

**Method**  
The authors conducted experiments using three prominent language models: Opus 4.6, GPT 5.4, and Gemini 3.1. They evaluated the models' performance on a dataset designed to identify subtly dangerous actions taken by coding agents within long transcripts. The core technical contribution lies in the demonstration of context length degradation, where the models exhibited a marked increase in false negatives—missing dangerous actions by factors ranging from 2x to 30x when these actions occurred after 800K tokens of benign activity. To mitigate this degradation, the authors explored prompting techniques, specifically periodic reminders throughout the transcript, and suggested that further improvements could be achieved through enhanced post-training strategies.

**Results**  
The results indicate a substantial decline in the models' ability to detect dangerous actions as the context length increases. Specifically, the models missed dangerous actions significantly more often in longer contexts compared to shorter ones, with the degradation effect quantified as 2x to 30x. This performance drop was consistent across all evaluated models, underscoring the critical need for monitoring evaluations that account for long-context scenarios. The authors provide empirical evidence that traditional evaluation metrics may overestimate the efficacy of these models when applied to real-world tasks involving extensive transcripts.

**Limitations**  
The authors acknowledge that their findings are limited to the specific models tested and the dataset used, which may not encompass all potential scenarios in coding agent monitoring. They also note that while prompting techniques showed promise, the effectiveness of these methods may vary across different contexts and tasks. An additional limitation is the lack of exploration into alternative architectures or training methodologies that could potentially address the identified degradation. Furthermore, the study does not investigate the computational costs associated with the proposed mitigation strategies.

**Why it matters**  
This work has significant implications for the deployment of language models in safety-critical applications, particularly in monitoring coding agents where the risk of dangerous actions is non-negligible. By highlighting the performance degradation associated with long-context transcripts, the authors call for a reevaluation of current benchmarking practices and the development of more robust evaluation frameworks. This research paves the way for future studies aimed at enhancing the reliability of LMs in real-world applications, ensuring that they can effectively monitor and respond to potentially hazardous behaviors in extended contexts.

Authors: Sam Martin, Fabien Roger  
Source: arXiv:2605.12366  
URL: [https://arxiv.org/abs/2605.12366v1](https://arxiv.org/abs/2605.12366v1)
