---
title: "Exploring Adversarial Robustness and Safety Alignment in Multilingual Multi-Modal Large Language Models"
date: 2026-06-02 15:42:10 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.03793v1"
arxiv_id: "2606.03793"
authors: ["Hashmat Shadab Malik", "Muzammal Naseer", "Salman Khan"]
slug: exploring-adversarial-robustness-and-safety-alignment-in-mul
summary_word_count: 444
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper investigates adversarial robustness and safety alignment in multilingual multimodal large language models, revealing critical vulnerabilities and safety misalignments."
---

**Problem**  
This work addresses the gap in understanding the adversarial robustness and safety alignment of multilingual multimodal large language models (MLLMs), particularly in non-English contexts. Prior research has predominantly focused on English-centric tasks, leaving a significant void in the exploration of multilingual behavior and vulnerabilities. The authors highlight that existing studies have not systematically evaluated the robustness of MLLMs across diverse languages, which is crucial given the increasing deployment of these models in multilingual settings. This paper is a preprint and has not undergone peer review.

**Method**  
The authors conduct a systematic evaluation of open-source MLLMs that acquire multilingual capabilities through instruction tuning. They employ gradient-based adversarial attacks to assess the models' vulnerabilities across 12 languages. The study examines how adversarial images optimized in one language can induce failures in others, demonstrating cross-lingual transferability of vulnerabilities. The authors also analyze the models' safety alignment by evaluating their responses to harmful instructions issued in various languages. They differentiate between models that integrate multilingual capabilities throughout their training (e.g., Qwen3-VL) and those that rely solely on instruction tuning. The methodology includes a comparative analysis of the models' performance in recognizing and responding to typographic content in both English and non-English scripts.

**Results**  
The findings reveal a significant transferable vulnerability across languages, with adversarial images leading to failures in multiple languages. Specifically, models exhibit a higher propensity for unsafe outputs when harmful intent is expressed in languages with stronger linguistic grounding. For instance, English scripts are reliably recognized, while non-English scripts often go unparsed, leading to a phenomenon termed "safety-by-failure." The study shows that models like Qwen3-VL, which incorporate multilingual training, maintain active refusal across languages, contrasting with those that only fine-tune on translated data, which may create an illusion of safety in low-resource languages. The results indicate that shallow multilingual adaptation can produce misleading safety perceptions.

**Limitations**  
The authors acknowledge that their study is limited by the selection of languages and the specific MLLMs evaluated. They also note that the adversarial attacks employed may not encompass all potential attack vectors, and the findings may not generalize to all MLLMs. Additionally, the reliance on instruction tuning for multilingual capability may not reflect the full spectrum of model performance in real-world applications.

**Why it matters**  
This research has significant implications for the development and deployment of MLLMs in multilingual contexts. Understanding the vulnerabilities and safety misalignments can inform better training practices and model architectures that genuinely align with safety standards across languages. The findings emphasize the need for deeper integration of multilingual capabilities during training rather than relying on superficial adaptations. This work contributes to the ongoing discourse on AI safety and robustness, as published in [arXiv cs.CL](https://arxiv.org/abs/2606.03793v1).
