---
title: "CCS: Clinical Consensus Selection for Radiology Report Generation"
date: 2026-05-28 15:59:29 +0000
category: research
subcategory: multimodal
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.30131v1"
arxiv_id: "2605.30131"
authors: ["Xi Zhang", "Yingshu Li", "Zaiqiao Meng", "Jake Lever", "Edmond S. L. Ho"]
slug: ccs-clinical-consensus-selection-for-radiology-report-genera
summary_word_count: 448
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing radiology report generation (RRG) systems, which typically rely on a single-path generation approach using multimodal large language models (MLLMs). The authors identify a gap in the literature regarding inference-time decision-making, noting that fixed MLLMs often produce higher-quality reports within their candidate pool than the report selected by default decoding methods. This suggests that the process of selecting the final report from multiple candidates is an overlooked bottleneck in improving report quality. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework called Clinical Consensus Selection (CCS), which operates independently of the decoding mechanism used in MLLMs. CCS involves generating multiple candidate reports and selecting the one with the highest clinical consensus from this pool. The framework integrates two types of utilities: a text-based utility and a radiology-adapted utility derived from a multimodal embedder trained on both images and reports. This dual utility approach allows for a more nuanced evaluation of candidate reports, measuring agreement beyond mere textual similarity. The authors evaluate CCS across three datasets and multiple radiology MLLMs, although specific details regarding the architecture of the MLLMs, loss functions, and training compute are not disclosed.

**Results**  
CCS demonstrates consistent improvements in inference-time performance compared to both single-path decoding and generic Best-of-N baselines. The authors report significant gains in clinical metrics, although specific numerical results and effect sizes are not detailed in the abstract. The analysis indicates that the image-grounded utility provides a distinct selection axis that complements textual consensus, suggesting that CCS effectively captures clinically relevant information that may be overlooked by traditional methods.

**Limitations**  
The authors acknowledge that while CCS improves report quality, there remains substantial headroom for further enhancements in RRG at inference time. They do not discuss potential limitations related to the computational overhead introduced by generating multiple candidates or the scalability of the CCS framework across different clinical contexts. Additionally, the reliance on a multimodal embedder raises questions about the generalizability of the approach to other medical domains or modalities.

**Why it matters**  
The implications of this work are significant for the field of medical AI, particularly in enhancing the quality of automated radiology reports. By addressing the inference-time decision-making process, CCS has the potential to improve clinical outcomes by ensuring that the most clinically relevant reports are selected. This could lead to better diagnostic accuracy and more effective communication of findings in clinical settings. Furthermore, the framework's dual utility approach may inspire future research into more sophisticated methods for evaluating candidate outputs in other multimodal tasks.

Authors: Xi Zhang, Yingshu Li, Zaiqiao Meng, Jake Lever, Edmond S. L. Ho  
Source: arXiv:2605.30131  
URL: [https://arxiv.org/abs/2605.30131v1](https://arxiv.org/abs/2605.30131v1)
