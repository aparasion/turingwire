---
title: "Annotation Quality in Aspect-Based Sentiment Analysis: A Case Study Comparing Experts, Students, Crowdworkers, and Large Language Model"
date: 2026-05-05 10:54:05 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03624v1"
arxiv_id: "2605.03624"
authors: ["Niklas Donhauser", "Jakob Fehle", "Nils Constantin Hellwig", "Markus Weinberger", "Udo Kruschwitz", "Christian Wolff"]
slug: annotation-quality-in-aspect-based-sentiment-analysis-a-case
summary_word_count: 451
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in high-quality annotated datasets for Aspect-Based Sentiment Analysis (ABSA) in German, a language that has received less attention compared to English in this domain. The authors highlight the variability in annotation quality from different sources—experts, students, crowdworkers, and Large Language Models (LLMs)—and its implications for model performance. The study aims to establish a reliable ground truth for evaluating these varying annotation sources, which is critical for advancing ABSA methodologies in under-resourced languages.

**Method**  
The authors re-annotated an existing German ABSA dataset using expert annotators to create a ground truth benchmark. They then compared the quality of annotations from students, crowdworkers, and LLMs against this benchmark. The evaluation metrics included Inter-Annotator Agreement (IAA) to quantify annotation consistency. For model performance assessment, they employed state-of-the-art architectures such as BERT, T5, and LLaMA, utilizing both fine-tuning and in-context learning with instruction prompts. The study specifically focused on two ABSA subtasks: Aspect Category Sentiment Analysis (ACSA) and Target Aspect Sentiment Detection (TASD). The training compute details were not disclosed, but the models were evaluated on their ability to generalize across the different annotation sources.

**Results**  
The findings indicate that expert annotations yield the highest IAA scores, significantly outperforming those from students and crowdworkers. LLM-generated annotations showed variable quality, with some instances approaching expert-level performance, particularly in ACSA tasks. The authors report that models fine-tuned on expert annotations achieved an F1 score of 85.2 on ACSA, compared to 75.1 for student annotations and 70.3 for crowdworker annotations. For TASD, the expert-tuned models reached an F1 score of 82.5, while student and crowdworker models scored 72.0 and 68.5, respectively. These results underscore the critical role of annotation quality in downstream model performance.

**Limitations**  
The authors acknowledge that their study is limited by the scope of the dataset and the specific languages considered, focusing solely on German. They also note that the generalizability of their findings to other languages or domains remains untested. Additionally, the reliance on a single expert-annotated dataset may not capture the full spectrum of linguistic variability. The authors do not address potential biases in the LLMs used for annotation, which could affect the reliability of their results.

**Why it matters**  
This work has significant implications for the development of ABSA systems in under-resourced languages, providing a framework for evaluating annotation quality across different sources. The insights gained can inform best practices for dataset construction, particularly in scenarios where expert annotators are scarce. By highlighting the trade-offs between annotation reliability and efficiency, this study encourages further exploration into leveraging LLMs for high-quality data generation, potentially accelerating advancements in multilingual sentiment analysis.

Authors: Niklas Donhauser, Jakob Fehle, Nils Constantin Hellwig, Markus Weinberger, Udo Kruschwitz, Christian Wolff  
Source: arXiv:2605.03624  
URL: https://arxiv.org/abs/2605.03624v1
