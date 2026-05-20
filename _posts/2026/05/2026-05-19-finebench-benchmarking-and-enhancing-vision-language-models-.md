---
title: "FineBench: Benchmarking and Enhancing Vision-Language Models for Fine-grained Human Activity Understanding"
date: 2026-05-19 13:40:26 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.19846v1"
arxiv_id: "2605.19846"
authors: ["Gueter Josmy Faure", "Min-Hung Chen", "Jia-Fong Yeh", "Hung-Ting Su", "Winston H. Hsu"]
slug: finebench-benchmarking-and-enhancing-vision-language-models-
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacy of existing Vision-Language Models (VLMs) in fine-grained human activity understanding, particularly in the context of nuanced interpretations of human actions and interactions in long-form videos. While prior benchmarks have evaluated aspects like fairness and emotion perception, they lack comprehensive coverage of dense question-answering (QA) across long videos with frame-level spatial and temporal grounding. This work introduces FineBench, a new benchmark designed to fill this gap, providing a robust framework for evaluating VLMs on fine-grained human-centric tasks. The paper is a preprint and has not yet undergone peer review.

**Method**  
The authors present FineBench, a benchmark consisting of 199,420 multiple-choice QA pairs derived from 64 long-form videos, each approximately 15 minutes in length. The focus is on detailed annotations regarding person movement, interactions, and object manipulation, including compositional actions. To enhance VLM performance on this benchmark, the authors propose FineAgent, a modular framework that integrates two components: a Localizer, which improves spatial reasoning, and a Descriptor, which enhances the understanding of actions and interactions. The training and evaluation of FineAgent are conducted on various open-source VLMs, demonstrating its effectiveness in addressing the identified weaknesses in spatial reasoning and subtle action differentiation.

**Results**  
The evaluation reveals that proprietary models, such as GPT-5, achieve notable performance on FineBench, but open-source VLMs exhibit significant deficiencies, particularly in spatial reasoning within multi-person scenes. The paper does not disclose specific performance metrics or effect sizes against named baselines, but it emphasizes that FineAgent consistently improves the performance of these open VLMs across the benchmark, indicating a clear advantage in fine-grained human activity understanding.

**Limitations**  
The authors acknowledge that FineBench is limited to the specific types of human activities and interactions represented in the selected videos, which may not encompass the full diversity of real-world scenarios. Additionally, the reliance on open-source VLMs may introduce variability in performance due to differences in architecture and training data. The paper does not address potential biases in the dataset or the generalizability of the results to other domains or types of video content.

**Why it matters**  
FineBench establishes a rigorous testbed for evaluating VLMs in the context of fine-grained human-centric video understanding, which is critical for applications in surveillance, human-computer interaction, and robotics. The introduction of FineAgent provides a practical methodology for enhancing existing VLMs, potentially leading to significant advancements in the field. This work lays the groundwork for future research aimed at improving the interpretative capabilities of VLMs in complex, real-world scenarios, thereby contributing to the development of more sophisticated AI systems capable of nuanced human activity recognition.

Authors: Gueter Josmy Faure, Min-Hung Chen, Jia-Fong Yeh, Hung-Ting Su, Winston H. Hsu  
Source: arXiv:2605.19846  
URL: [https://arxiv.org/abs/2605.19846v1](https://arxiv.org/abs/2605.19846v1)
