---
title: "Learning When to Think While Listening in Large Audio-Language Models"
date: 2026-05-26 15:43:11 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27190v1"
arxiv_id: "2605.27190"
authors: ["Zhiyuan Song", "Weici Zhao", "Yang Xiao", "Suhao Yu", "Cheng Zhu", "Jiatao Gu"]
slug: learning-when-to-think-while-listening-in-large-audio-langua
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of optimizing reasoning quality and responsiveness in Large Audio-Language Models (LALMs) during real-time spoken interactions. The authors identify a gap in existing models that either delay reasoning until the speech endpoint—thereby improving answer quality but increasing response latency—or answer prematurely, risking incorrect responses due to insufficient evidence. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a learnable wait-think-answer control mechanism for LALMs, which is designed to operate under partial audio evidence. The core architecture is based on the Qwen2.5-Omni-7B model. The control mechanism is trained using aligned wait-think-answer traces derived from spoken reasoning data. The training process involves supervised fine-tuning (SFT) followed by the application of Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO). The reward function is multifaceted, incorporating metrics such as answer correctness, action validity, update timing, latency synchronization, reasoning quality, and chain consistency. This holistic approach optimizes the entire wait-think-answer trajectory rather than focusing solely on the final answer.

**Results**  
The proposed six-reward DAPO controller demonstrates a significant improvement in performance on a synthetic spoken reasoning question answering (SRQA) benchmark, achieving a row-weighted accuracy increase from 67.6% to 70.3%. Additionally, it reduces the post-endpoint final-think length by 14% while maintaining the same deployment conditions with the Qwen model. On the Real Audio Bench, which consists of 186 human-recorded items, the SFT variant achieves the highest accuracy, while the DAPO controller is the only learned variant that reduces final-think length below that of the base model. These results indicate that the controller effectively learns to make intermediate reasoning explicit during audio streams.

**Limitations**  
The authors acknowledge that their approach is contingent on the quality of the training data used to construct the wait-think-answer traces. They also note that the performance improvements are evaluated in a controlled setting, which may not fully capture the complexities of real-world interactions. Additionally, the reliance on a specific base model (Qwen2.5-Omni-7B) may limit the generalizability of the findings to other architectures or tasks.

**Why it matters**  
This work has significant implications for the development of more responsive and contextually aware LALMs, particularly in applications requiring real-time spoken interaction, such as virtual assistants and conversational agents. By optimizing the timing of reasoning updates, the proposed method enhances user experience by balancing the trade-off between response quality and latency. Future research can build on this framework to explore adaptive reasoning strategies in diverse audio-language contexts, potentially leading to more sophisticated human-computer interaction paradigms.

Authors: Zhiyuan Song, Weici Zhao, Yang Xiao, Suhao Yu, Cheng Zhu, Jiatao Gu  
Source: arXiv:2605.27190  
URL: [https://arxiv.org/abs/2605.27190v1](https://arxiv.org/abs/2605.27190v1)
