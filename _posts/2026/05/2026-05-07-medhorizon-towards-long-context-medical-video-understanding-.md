---
title: "MedHorizon: Towards Long-context Medical Video Understanding in the Wild"
date: 2026-05-07 16:37:10 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.06537v1"
arxiv_id: "2605.06537"
authors: ["Bodong Du", "Bowen Liu", "Yang Yu", "Xinpeng Ding", "Zhiheng Wu", "Shuning Wang"]
slug: medhorizon-towards-long-context-medical-video-understanding-
summary_word_count: 473
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the capability of existing medical multimodal large language models (MLLMs) to understand long-context medical videos in real clinical settings. Current benchmarks primarily focus on short video analysis or assume that critical evidence has already been localized, which does not reflect the complexities of full-procedure video understanding. The authors introduce MedHorizon, an unreviewed benchmark that evaluates models on their ability to retrieve sparse evidence from lengthy clinical videos, which is crucial for accurate clinical reasoning.

**Method**  
MedHorizon comprises 759 hours of full-length clinical procedure videos and includes 1,253 evidence-grounded multiple-choice questions designed to assess both sparse evidence understanding and multi-hop clinical reasoning. The dataset is characterized by an extremely low average of 0.166% evidence frames, necessitating models to effectively search through noisy procedural streams. The authors evaluate various MLLMs, including those from general and medical domains, as well as long-video models. The evaluation focuses on the models' ability to retrieve evidence and perform clinical reasoning, highlighting the challenges posed by redundancy in video content and the need for effective attention mechanisms.

**Results**  
The best-performing model achieved an accuracy of only 41.1% on the MedHorizon benchmark, indicating that current MLLMs are not yet capable of robust full-procedure understanding. This performance is significantly lower than expected, revealing that existing systems struggle with the complexities of evidence retrieval and clinical interpretation. The authors identify four critical findings: (1) performance does not scale with the number of frames, (2) evidence retrieval and clinical interpretation are primary bottlenecks, (3) these bottlenecks stem from weak procedural reasoning and attention drift due to redundancy, and (4) generic sampling methods inadequately balance local detail with global coverage.

**Limitations**  
The authors acknowledge that the MedHorizon benchmark is still in its early stages and may not encompass all possible clinical scenarios. They also note that the low evidence frame rate could lead to challenges in model training and evaluation. Additionally, the reliance on existing MLLMs may limit the exploration of novel architectures specifically designed for long-context video understanding. The authors do not discuss potential biases in the dataset or the generalizability of their findings across different medical domains.

**Why it matters**  
The introduction of MedHorizon is significant for advancing the field of medical video understanding, as it provides a rigorous testbed for evaluating MLLMs on their ability to retrieve sparse evidence and reason over complete clinical workflows. This work highlights the need for improved models that can handle the complexities of long-context medical videos, which is essential for enhancing clinical decision-making and patient outcomes. The findings underscore the importance of addressing the bottlenecks in evidence retrieval and procedural reasoning, paving the way for future research to develop more robust MLLMs tailored for medical applications.

Authors: Bodong Du, Bowen Liu, Yang Yu, Xinpeng Ding, Zhiheng Wu, Shuning Wang, Shuo Nie, Naiming Liu et al.  
Source: arXiv:2605.06537  
URL: https://arxiv.org/abs/2605.06537v1
