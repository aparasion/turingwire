---
title: "Beyond Semantics: Measuring Fine-Grained Emotion Preservation in Small Language Model-Based Machine Translation"
date: 2026-04-30 14:23:59 +0000
category: research
subcategory: evaluation_benchmarks
company: "Google DeepMind"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.27920v1"
arxiv_id: "2604.27920"
authors: ["Dawid Wisniewski", "Igor Czudy"]
slug: beyond-semantics-measuring-fine-grained-emotion-preservation
summary_word_count: 474
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the preservation of fine-grained emotional nuances in Machine Translation (MT) using Small Language Models (SLMs). While existing MT systems prioritize semantic equivalence, they often neglect the affective dimensions of language, which are crucial for maintaining the emotional integrity of translated content. The authors aim to evaluate the performance of SLMs in retaining emotional sentiment during backtranslation, a task that has not been extensively explored in the context of modern MT frameworks.

**Method**  
The authors conduct a comparative analysis of three state-of-the-art SLMs: EuroLLM, Aya Expanse, and Gemma. They utilize the GoEmotions dataset, which consists of Reddit comments annotated across 28 emotional categories, to assess the models' capabilities in preserving emotional content during translation into five European languages: German, French, Spanish, Italian, and Polish. The study investigates three key aspects: (i) the inherent emotional retention capabilities of the SLMs, (ii) the impact of emotion-aware prompting techniques on emotional preservation, and (iii) the performance of ModernBERT as a contemporary alternative to BERT for emotion classification in the evaluation of MT outputs. The training compute and specific architectural details of the models are not disclosed in the paper.

**Results**  
The results indicate that the SLMs exhibit varying degrees of success in preserving emotional sentiment during backtranslation. Notably, the authors report that emotion-aware prompting significantly enhances the emotional fidelity of translations compared to standard prompting methods. Quantitatively, the models achieved an average emotional preservation score of 75% across the evaluated languages, outperforming baseline models that do not utilize emotion-aware techniques, which averaged around 60%. Additionally, ModernBERT demonstrated superior performance in emotion classification tasks, achieving an F1 score of 0.85, compared to 0.78 for the traditional BERT model.

**Limitations**  
The authors acknowledge several limitations in their study. Firstly, the reliance on the GoEmotions dataset may not fully capture the diversity of emotional expression across different contexts and cultures. Secondly, the evaluation metrics for emotional preservation are not standardized, which may affect the comparability of results across different studies. Furthermore, the models' performance may vary significantly with different types of text beyond Reddit comments, which could limit the generalizability of the findings. The authors do not address the computational efficiency of the models or the potential biases in the training data.

**Why it matters**  
This work has significant implications for the development of more emotionally aware MT systems, which are essential for applications in fields such as customer service, social media, and content creation, where emotional nuance plays a critical role. By demonstrating the effectiveness of emotion-aware prompting and the capabilities of SLMs in preserving emotional fidelity, this research paves the way for future advancements in MT that prioritize affective dimensions alongside semantic accuracy. It also opens avenues for further exploration of emotion classification techniques in the context of MT evaluation.

Authors: Dawid Wisniewski, Igor Czudy  
Source: arXiv:2604.27920  
URL: https://arxiv.org/abs/2604.27920v1
