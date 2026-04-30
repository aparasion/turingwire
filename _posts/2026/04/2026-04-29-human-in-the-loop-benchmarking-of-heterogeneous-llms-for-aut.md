---
title: "Human-in-the-Loop Benchmarking of Heterogeneous LLMs for Automated Competency Assessment in Secondary Level Mathematics"
date: 2026-04-29 12:36:19 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26607v1"
arxiv_id: "2604.26607"
authors: ["Jatin Bhusal", "Nancy Mahatha", "Aayush Acharya", "Raunak Regmi"]
slug: human-in-the-loop-benchmarking-of-heterogeneous-llms-for-aut
summary_word_count: 416
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in automated competency assessment in secondary-level mathematics, particularly in the context of Competency-Based Education (CBE). The transition from traditional marks-based assessment to qualitative competency mapping presents a significant manual challenge for educators. The authors propose a "Human-in-the-Loop" benchmarking framework to evaluate the effectiveness of various large language models (LLMs) in automating this assessment process, specifically tailored to the Grade 10 Optional Mathematics curriculum in Nepal.

**Method**  
The authors developed a multi-dimensional rubric encompassing four mathematical topics and four cross-cutting competencies: Comprehension, Knowledge, Operational Fluency, and Behavior and Correlation. They benchmarked a multi-provider ensemble of LLMs, including open-weight models (Eagle, Llama 3.1-8B; Orion, Llama 3.3-70B) and proprietary models (Nova, Gemini 2.5 Flash; Lyra, Gemini 3 Pro). The evaluation was conducted against a ground truth established by two senior mathematics faculty members, achieving a weighted kappa (kappa_w) of 0.8652. The study highlights an "Architecture-compatibility gap," where the performance of models varied significantly based on their architectural design rather than just their parameter scale.

**Results**  
The results indicate that the Gemini-based Mixture-of-Experts (Sparse MoE) models achieved a "Fair Agreement" with a kappa_w of approximately 0.38. In contrast, the larger Orion model (70B parameters) demonstrated "No Agreement" with a kappa_w of -0.0261. These findings suggest that architectural compliance with instructional constraints is more critical than the sheer number of parameters when performing rubric-constrained tasks. The authors conclude that while LLMs are not yet capable of autonomous certification, they can provide valuable assistive support for preliminary evidence extraction within a "Human-in-the-Loop" framework.

**Limitations**  
The authors acknowledge that the current LLMs are not suitable for fully autonomous competency assessment and highlight the need for human oversight in the evaluation process. They also note the potential limitations of their benchmarking framework, including the reliance on a specific curriculum and the subjective nature of the ground truth established by faculty members. Additionally, the study does not explore the scalability of the proposed framework across different educational contexts or subjects.

**Why it matters**  
This work has significant implications for the integration of AI in educational assessment, particularly in enhancing the efficiency of competency mapping in CBE. By identifying the architectural factors that influence LLM performance, this research provides insights for future model development and deployment in educational settings. The findings underscore the importance of a hybrid approach that combines human expertise with AI capabilities, paving the way for more effective and scalable assessment solutions in education.

Authors: Jatin Bhusal, Nancy Mahatha, Aayush Acharya, Raunak Regmi  
Source: arXiv:2604.26607  
URL: [https://arxiv.org/abs/2604.26607v1](https://arxiv.org/abs/2604.26607v1)
