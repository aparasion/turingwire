---
title: "SN-WER: Script-Normalized WER for Multi-Script Indic ASR Evaluation"
date: 2026-06-01 17:49:10 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02548v1"
arxiv_id: "2606.02548"
authors: ["Priyaranjan Pattnayak"]
slug: sn-wer-script-normalized-wer-for-multi-script-indic-asr-eval
summary_word_count: 419
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces Script-Normalized WER (SN-WER), a novel metric for evaluating ASR systems in multilingual contexts with script variations."
---

**Problem**  
The paper addresses the limitations of the traditional Word Error Rate (WER) metric in automatic speech recognition (ASR) evaluations, particularly in multilingual settings where the same words may be represented in different scripts. This issue is prevalent in Indic languages, where ASR models often produce romanized outputs. The authors highlight that WER can inflate error rates due to script mismatches, leading to misleading evaluations of ASR performance. This work is a preprint and has not undergone peer review.

**Method**  
The authors propose Script-Normalized WER (SN-WER), a training-free, evaluation-only metric that transliterates both reference and hypothesis texts into a canonical script specific to the language before calculating WER. This approach allows for a more accurate assessment of ASR performance by mitigating the impact of script discrepancies. The evaluation of SN-WER is conducted across five Indic languages, utilizing two datasets: curated FLEURS data and noisier Common Voice data. The authors employ three different ASR models to validate the robustness of SN-WER. The method demonstrates resilience to variations in transliterator choice and normalization processes, with token-collision rates remaining below 0.1%.

**Results**  
On the curated FLEURS dataset, SN-WER effectively reduces inflated model gaps by up to 12% compared to traditional WER. In contrast, results on the Common Voice dataset show smaller or inconsistent reductions, suggesting that these discrepancies may reflect genuine recognition weaknesses rather than mere script mismatches. Controlled experiments reveal that SN-WER attenuates artificial WER inflation caused by romanization by 67%. Additionally, lexical-substitution controls indicate that SN-WER maintains a similar sensitivity to semantic errors, with a Delta SN-WER / Delta WER ratio of approximately 1.09.

**Limitations**  
The authors acknowledge that while SN-WER provides a more accurate evaluation metric, its effectiveness may vary across different datasets and ASR models. The smaller reductions observed on the Common Voice dataset suggest that the metric may not fully account for all sources of error in ASR outputs. Furthermore, the study does not explore the implications of SN-WER in real-world applications beyond the evaluated datasets, which may limit its generalizability.

**Why it matters**  
The introduction of SN-WER as a companion metric to WER and Character Error Rate (CER) is significant for the evaluation of ASR systems, particularly in multilingual contexts where script variations are common. By providing a more nuanced assessment of ASR performance, SN-WER can enhance the reliability of evaluations that inform downstream applications such as search, indexing, and multilingual large language model (LLM) pipelines. This work underscores the importance of considering script normalization in ASR evaluations, as highlighted in the findings available on [arXiv](https://arxiv.org/abs/2606.02548v1).
