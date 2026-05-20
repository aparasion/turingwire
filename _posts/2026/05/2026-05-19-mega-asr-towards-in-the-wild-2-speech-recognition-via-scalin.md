---
title: "Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation"
date: 2026-05-19 13:26:51 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.19833v1"
arxiv_id: "2605.19833"
authors: ["Zhifei Xie", "Kaiyu Pang", "Haobin Zhang", "Deheng Ye", "Xiaobin Hu", "Shuicheng Yan"]
slug: mega-asr-towards-in-the-wild-2-speech-recognition-via-scalin
summary_word_count: 422
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the "acoustic robustness bottleneck" in automatic speech recognition (ASR), particularly in real-world environments where models struggle with severe acoustic distortions, leading to omissions and hallucinations. Despite advancements in ASR and audio-language models, existing systems lack the robustness required for diverse and challenging acoustic conditions. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose Mega-ASR, a unified framework designed for in-the-wild ASR that integrates scalable compound-data construction with progressive acoustic-to-semantic optimization. A key component is the introduction of the Voices-in-the-Wild-2M dataset, which encompasses 7 classic acoustic phenomena and 54 physically plausible compound scenarios. The training methodology employs Acoustic-to-Semantic Progressive Supervised Fine-Tuning, which iteratively refines the model's understanding of acoustic inputs, and Dual-Granularity WER-Gated Policy Optimization, which optimizes the model's performance based on word error rate (WER) at different granularity levels. The architecture specifics, including model size and training compute, are not disclosed in the abstract.

**Results**  
Mega-ASR demonstrates substantial improvements over state-of-the-art ASR systems on adverse-condition benchmarks. Specifically, it achieves a WER of 45.69% on the VOiCES R4-B-F benchmark, compared to 54.01% from the previous best system. On the NOIZEUS Sta-0 benchmark, Mega-ASR records a WER of 21.49%, outperforming the baseline of 29.34%. Furthermore, in complex compositional acoustic scenarios, Mega-ASR achieves over a 30% relative reduction in WER compared to both open-source and closed-source baselines, indicating its effectiveness in handling challenging acoustic conditions.

**Limitations**  
The authors acknowledge that while Mega-ASR shows significant improvements, the framework's performance may still be limited by the diversity and representativeness of the training data. The reliance on simulated data may not fully capture all real-world acoustic phenomena. Additionally, the scalability of the proposed methods in terms of computational resources and the potential for overfitting on the training dataset are not explicitly discussed. The lack of peer review also raises questions about the robustness of the findings.

**Why it matters**  
The implications of this work are significant for the field of ASR, particularly in applications requiring robust performance in diverse acoustic environments, such as voice-activated systems in public spaces or noisy settings. By establishing a scalable paradigm for robust ASR, Mega-ASR could pave the way for future research focused on enhancing acoustic grounding and reducing hallucinations in ASR systems. This work also highlights the importance of integrating realistic acoustic simulations into training processes, potentially influencing the design of future datasets and training methodologies in the ASR domain.

Authors: Zhifei Xie, Kaiyu Pang, Haobin Zhang, Deheng Ye, Xiaobin Hu, Shuicheng Yan, Chunyan Miao  
Source: arXiv:2605.19833  
URL: [https://arxiv.org/abs/2605.19833v1](https://arxiv.org/abs/2605.19833v1)
