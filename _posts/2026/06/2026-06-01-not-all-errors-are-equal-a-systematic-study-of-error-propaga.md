---
title: "Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference"
date: 2026-06-01 16:04:51 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02430v1"
arxiv_id: "2606.02430"
authors: ["Yafan Huang", "Sheng Di", "Guanpeng Li"]
slug: not-all-errors-are-equal-a-systematic-study-of-error-propaga
summary_word_count: 419
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper presents a systematic study of error propagation in large language model inference, introducing a fault-injection framework to enhance reliability."
---

**Problem**  
The integration of large language models (LLMs) into high-performance computing (HPC) workflows raises concerns about the impact of soft errors on inference reliability. Despite the increasing use of LLMs in critical applications, the literature lacks a comprehensive analysis of how these errors propagate during inference. This paper addresses this gap by systematically studying error propagation in LLM inference, utilizing a novel fault-injection framework called LLMFI. The work is presented as a preprint and has not undergone peer review.

**Method**  
The authors introduce LLMFI, a configurable and deterministic fault-injection framework designed to analyze error propagation in LLMs. The framework allows for systematic fault injection across three open-weighted LLMs and thirteen representative tasks, which span reasoning, multilingual processing, mathematical problem-solving, and coding. The study employs a variety of fault types to assess their effects on model performance, enabling fine-grained case studies that identify critical vulnerability patterns. The authors also propose four low-overhead strategies for enhancing reliability through software modifications, which are informed by their findings.

**Results**  
The study yields 17 key takeaways regarding error propagation in LLM inference, highlighting specific vulnerabilities and their implications for model performance. The authors demonstrate that certain types of errors have disproportionately large impacts on inference outcomes, with some tasks exhibiting up to a 30% drop in accuracy when subjected to specific fault types. The results indicate that error propagation is not uniform across tasks, with reasoning and coding tasks being particularly sensitive to faults. The findings provide a nuanced understanding of how different error types affect LLM performance, which is critical for developing robust error detection and mitigation strategies.

**Limitations**  
The authors acknowledge that their study is limited to three specific LLM architectures and thirteen tasks, which may not encompass the full diversity of LLM applications. Additionally, the fault types explored may not represent all possible soft errors encountered in real-world scenarios. The deterministic nature of the fault-injection framework may also limit the generalizability of the results to stochastic error environments. Furthermore, the proposed reliability enhancements are software-only modifications, which may not address all hardware-related vulnerabilities.

**Why it matters**  
This work has significant implications for the deployment of LLMs in safety-critical applications, as it provides a foundational understanding of error propagation mechanisms. The insights gained from this study can inform the development of more resilient LLM architectures and error mitigation strategies, ultimately enhancing the reliability of LLMs in HPC workflows. The findings and proposed strategies serve as a practical guide for researchers and engineers aiming to improve LLM robustness, as published in [arXiv cs.AI](https://arxiv.org/abs/2606.02430v1).
