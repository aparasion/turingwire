---
title: "From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents"
date: 2026-05-14 17:22:42 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.15104v1"
arxiv_id: "2605.15104"
authors: ["Md Tahmid Rahman Laskar", "Xue-Yong Fu", "Seyyed Saeed Sarfjoo", "Quinten McNamara", "Jonas Robertson", "Shashi Bhushan TN"]
slug: from-text-to-voice-a-reproducible-and-verifiable-framework-f
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in evaluating tool-calling capabilities of large language models (LLMs) in audio contexts, as existing benchmarks are predominantly text-based. The authors propose a reproducible and verifiable framework to convert these text benchmarks into audio-based evaluations without the need for re-annotation of tool schemas and gold labels. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a dataset-agnostic framework that leverages text-to-speech (TTS) synthesis, speaker variation, and environmental noise to generate paired text-audio instances while maintaining the original dataset annotations. The framework is evaluated using seven omni-modal models on audio-converted versions of two benchmarks: Confetti and When2Call. The models include Gemini-3.1-Flash-Live and GPT-Realtime-1.5, among others. The evaluation metrics focus on the performance of these models in tool-calling tasks, with specific attention to the text-to-voice performance gap. The authors also implement a reference-free LLM-as-judge protocol to validate model outputs against human preferences, enhancing the robustness of their evaluation framework.

**Results**  
The results indicate that model performance is highly dependent on both the model architecture and the specific task. Gemini-3.1-Flash-Live achieved the highest score of 70.4 on the Confetti benchmark, while GPT-Realtime-1.5 outperformed others with a score of 71.9 on When2Call. The analysis reveals a text-to-voice performance gap ranging from 1.8 points for Qwen3-Omni to 4.8 points for GPT-Realtime-1.5 on Confetti. Additionally, the authors report that open-source Qwen3 models with at least 8 billion parameters achieved over 80% agreement with proprietary judges, indicating a promising avenue for privacy-preserving evaluations.

**Limitations**  
The authors acknowledge that their framework is limited by the inherent challenges of TTS systems, which may introduce errors in argument value interpretation during speech. They also note that the performance degradation observed in certain cases reflects these misunderstandings. Furthermore, the framework's reliance on existing text benchmarks may not fully capture the nuances of audio-based interactions, and the generalizability of results across different domains remains to be established.

**Why it matters**  
This work has significant implications for the development of voice agents that require reliable tool usage from speech inputs. By providing a systematic approach to evaluate audio-based tool calling capabilities, the framework enables researchers to better understand the limitations and strengths of various LLMs in real-world scenarios. The findings also suggest that open-source models can achieve competitive performance, promoting further research into privacy-preserving methodologies in LLM evaluations. Overall, this framework serves as a foundational step towards more comprehensive assessments of audio-based AI systems.

Authors: Md Tahmid Rahman Laskar, Xue-Yong Fu, Seyyed Saeed Sarfjoo, Quinten McNamara, Jonas Robertson, Shashi Bhushan TN  
Source: arXiv:2605.15104  
URL: [https://arxiv.org/abs/2605.15104v1](https://arxiv.org/abs/2605.15104v1)
