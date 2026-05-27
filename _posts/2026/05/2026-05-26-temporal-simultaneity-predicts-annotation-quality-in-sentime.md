---
title: "Temporal Simultaneity Predicts Annotation Quality in Sentiment Corpora"
date: 2026-05-26 16:21:20 +0000
category: research
subcategory: evaluation_benchmarks
company: "OpenAI"
secondary_companies: ["Google"]
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.27239v1"
arxiv_id: "2605.27239"
authors: ["Idris Abdulmumin", "Mokgadi Penelope Matloga", "Tadesse Destaw Belay", "Botshelo Kondowe", "Letlhogonolo Mohleleng", "Hareaipha Nkopo Letsoalo"]
slug: temporal-simultaneity-predicts-annotation-quality-in-sentime
summary_word_count: 460
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of sustaining annotation quality in sentiment analysis tasks over extended periods, particularly when using small pools of annotators. The authors investigate the decline in inter-annotator agreement (IAA) over time, specifically within a newly created Setswana sentiment dataset comprising 3,565 tweets annotated by three native speakers across eight batches. The study highlights a significant drop in IAA, as measured by Randolph's free-marginal Kappa, which decreases from an aggregate value of $κ= 0.76$ to over 32 points across the annotation task, indicating a critical gap in understanding the temporal dynamics affecting annotation quality.

**Method**  
The authors conduct six targeted analyses to identify factors contributing to the decline in IAA. Key findings include: (i) label confusion is particularly pronounced at the negative/neutral boundary, (ii) two annotators exhibit run-length drift indicative of autopilot labeling, and (iii) the primary predictor of IAA is temporal simultaneity. Specifically, tweets labeled within one minute achieve a $κ$ of 0.98, while those labeled more than a day apart drop to $κ= 0.65$. The study benchmarks three open multilingual encoders alongside proprietary models (GPT-5 and Gemini) for three-class sentiment classification. Fine-tuning these models results in macro-F1 score improvements ranging from 29 to 43 points over pretrained baselines, with GPT-5 in a few-shot setting achieving the highest score of 62.2 macro-F1.

**Results**  
The findings reveal that temporal simultaneity is a critical factor in maintaining high annotation quality, with a stark contrast in IAA based on the timing of annotations. The benchmark results demonstrate significant performance improvements for fine-tuned models, with GPT-5 outperforming other models in the sentiment classification task. The authors provide detailed metrics, including the aggregate $κ$ values and macro-F1 scores, which serve as a quantitative basis for evaluating the effectiveness of the proposed methodologies against established baselines.

**Limitations**  
The authors acknowledge that their analysis is limited to a specific language (Setswana) and a relatively small dataset, which may affect the generalizability of their findings. They do not address potential biases in annotator selection or the impact of tweet content variability on annotation quality. Additionally, the study does not explore the long-term implications of annotation drift beyond the immediate context of the dataset.

**Why it matters**  
This work has significant implications for the field of natural language processing (NLP), particularly in the context of low-resource languages. By elucidating the factors that influence annotation quality over time, the study provides valuable insights for designing more effective annotation campaigns and improving the reliability of sentiment analysis in diverse linguistic contexts. The release of the dataset, per-annotation timestamps, and analysis code enhances reproducibility and supports future research in African language NLP resources.

Authors: Idris Abdulmumin, Mokgadi Penelope Matloga, Tadesse Destaw Belay, Botshelo Kondowe, Letlhogonolo Mohleleng, Hareaipha Nkopo Letsoalo, Shamsuddeen Hassan Muhammad, Vukosi Marivate  
Source: arXiv:2605.27239  
URL: https://arxiv.org/abs/2605.27239v1
