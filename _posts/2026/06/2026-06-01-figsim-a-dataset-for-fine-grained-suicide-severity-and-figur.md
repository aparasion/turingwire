---
title: "FigSIM: A Dataset for Fine-grained Suicide Severity and Figurative Language in Suicide Memes"
date: 2026-06-01 17:32:29 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02523v1"
arxiv_id: "2606.02523"
authors: ["Liuliu Chen", "Elise R. Carrotte", "Brian E. Chapman", "Jo Robinson", "Mike Conway"]
slug: figsim-a-dataset-for-fine-grained-suicide-severity-and-figur
summary_word_count: 426
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces FigSIM, a novel dataset for analyzing suicide memes, focusing on severity levels and figurative language, to enhance content moderation."
---

**Problem**  
The paper addresses the lack of annotated datasets for suicide memes, which hampers the development of automated content moderation strategies. Despite the increasing prevalence of suicide-related content on social media, existing literature lacks a comprehensive understanding of the characteristics of these memes. This gap is critical, as the absence of fine-grained analysis can lead to ineffective moderation and potential harm to vulnerable users. The work is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The authors introduce FigSIM, a dataset comprising 1,049 suicide memes, each annotated for three key dimensions: (1) fine-grained suicide severity levels, (2) figurative language phenomena (e.g., metaphors), and (3) suicide-related content (e.g., depictions of methods). The dataset facilitates the benchmarking of 16 models, both unimodal and multimodal, across three distinct tasks: figurative language detection, suicide severity assessment, and identification of suicide-related content. The models were trained on the annotated dataset, although specific details regarding the architecture, loss functions, and training compute resources are not disclosed.

**Results**  
The evaluation of the models on the FigSIM dataset reveals significant challenges in accurately detecting higher levels of suicide severity, particularly in memes employing figurative language. The authors report that existing models exhibit a bias towards underpredicting severe cases, indicating a need for improved methodologies in this domain. While specific performance metrics (e.g., accuracy, F1 scores) against named baselines are not provided in the summary, the findings underscore the unique complexities posed by suicide memes for both modeling and content moderation.

**Limitations**  
The authors acknowledge several limitations, including the potential for bias in the dataset due to the subjective nature of meme interpretation and the challenges in capturing the full spectrum of figurative language. They also note that the dataset may not encompass all cultural contexts or meme formats, which could affect generalizability. Additionally, the reliance on automated models for sensitive content moderation raises ethical concerns that are not fully addressed in the paper.

**Why it matters**  
The introduction of FigSIM represents a significant step towards understanding and moderating suicide-related content on social media platforms. By providing a structured dataset for fine-grained analysis, this work lays the groundwork for future research aimed at developing more effective content moderation strategies that can mitigate the risks associated with harmful memes. The implications extend to mental health professionals, social media companies, and researchers in the field of computational linguistics and social media analysis, as they seek to balance freedom of expression with user safety. This work is crucial for advancing the discourse on automated moderation in sensitive contexts, as published in [arXiv](https://arxiv.org/abs/2606.02523v1).
