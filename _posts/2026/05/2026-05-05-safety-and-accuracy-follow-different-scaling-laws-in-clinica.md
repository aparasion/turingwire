---
title: "Safety and accuracy follow different scaling laws in clinical large language models"
date: 2026-05-05 17:57:19 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.04039v1"
arxiv_id: "2605.04039"
authors: ["Sebastian Wind", "Tri-Thien Nguyen", "Jeta Sopa", "Mahshad Lotfinia", "Sebastian Bickelhaup", "Michael Uder"]
slug: safety-and-accuracy-follow-different-scaling-laws-in-clinica
summary_word_count: 464
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacy of existing scaling laws in clinical large language models (LLMs), which often assume that increased model size and complexity lead to improved safety and accuracy. The authors argue that in clinical settings, particularly in medicine, a few high-risk errors can have significant consequences, making average performance metrics insufficient. They propose a framework, SaFE-Scale, to systematically evaluate how safety metrics change with various scaling factors, including model size, evidence quality, and retrieval strategies.

**Method**  
The core technical contribution is the SaFE-Scale framework, which evaluates clinical LLM safety across multiple dimensions. To operationalize this framework, the authors introduce RadSaFE-200, a benchmark consisting of 200 multiple-choice questions specifically designed for radiology. This benchmark includes clinician-defined categories for clean evidence, conflict evidence, and option-level labels for high-risk errors, unsafe answers, and evidence contradictions. The authors evaluated 34 LLMs under six deployment conditions: closed-book prompting (zero-shot), clean evidence, conflict evidence, standard retrieval-augmented generation (RAG), agentic RAG, and max-context prompting. The evaluation metrics focus on accuracy, high-risk error rates, contradiction rates, and dangerous overconfidence.

**Results**  
The results indicate that using clean evidence significantly enhances model performance, with mean accuracy increasing from 73.5% to 94.1%. Concurrently, high-risk errors decreased from 12.0% to 2.6%, contradictions from 12.7% to 2.3%, and dangerous overconfidence from 8.0% to 1.6%. In contrast, while agentic RAG improved accuracy over standard RAG and reduced contradiction rates, it did not effectively lower high-risk errors or dangerous overconfidence. Max-context prompting led to increased latency without improving safety metrics, and additional inference-time compute yielded only marginal gains. A worst-case analysis revealed that clinically significant errors were concentrated in a small subset of questions, underscoring the need for targeted interventions.

**Limitations**  
The authors acknowledge that their findings are limited to the specific context of radiology and may not generalize across other medical domains. They also note that the evaluation is based on a fixed set of questions, which may not capture the full variability of clinical scenarios. Additionally, the reliance on clinician-defined labels may introduce subjective bias. The study does not explore the long-term implications of deploying these models in real-world clinical settings, nor does it address the potential for model drift over time.

**Why it matters**  
This work has significant implications for the development and deployment of clinical LLMs. It challenges the prevailing assumption that scaling inherently leads to safer models, emphasizing the importance of evidence quality and retrieval strategies in ensuring patient safety. The SaFE-Scale framework and RadSaFE-200 benchmark provide a structured approach for future research, enabling the identification of critical factors that influence model safety. This could lead to more robust clinical decision support systems and ultimately improve patient outcomes.

Authors: Sebastian Wind, Tri-Thien Nguyen, Jeta Sopa, Mahshad Lotfinia, Sebastian Bickelhaup, Michael Uder, Harald Köstler, Gerhard Wellein et al.  
Source: arXiv:2605.04039  
URL: https://arxiv.org/abs/2605.04039v1
