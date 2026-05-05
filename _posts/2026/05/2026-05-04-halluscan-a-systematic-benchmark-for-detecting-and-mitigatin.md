---
title: "HalluScan: A Systematic Benchmark for Detecting and Mitigating Hallucinations in Instruction-Following LLMs"
date: 2026-05-04 10:43:27 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02443v1"
arxiv_id: "2605.02443"
authors: ["Ahmed Cherif"]
slug: halluscan-a-systematic-benchmark-for-detecting-and-mitigatin
summary_word_count: 411
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the critical issue of hallucinations in Large Language Models (LLMs), which generate content that is factually incorrect or misaligned with user instructions. Despite the advancements in LLM capabilities, the prevalence of hallucinations remains a significant challenge. The authors present HalluScan, a systematic benchmark framework designed to evaluate and mitigate these hallucinations. This work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contributions of this paper include the introduction of HalluScore, Adaptive Detection Routing (ADR), and a systematic error cascade decomposition. HalluScore is a composite metric that correlates with human expert judgments, achieving a Pearson correlation coefficient of r = 0.41. ADR is an intelligent routing algorithm that optimizes detection costs, achieving a 2.0x reduction in computational expense with only a 0.1% degradation in AUROC. The benchmark evaluates hallucination detection across 72 configurations, which encompass 6 detection methods, 4 open-weight model families, and 3 diverse domains. The authors systematically analyze the types of hallucination errors, providing insights into their variation across different contexts.

**Results**  
The experimental results indicate that the NLI Verification method achieves the highest overall AUROC of 0.88, establishing it as a strong baseline for hallucination detection. The RAV method follows with a second-highest AUROC of 0.66. These results demonstrate the effectiveness of the proposed benchmark and methods in identifying and mitigating hallucinations in LLMs, providing a quantitative foundation for future research in this area.

**Limitations**  
The authors acknowledge several limitations, including the potential for bias in human expert judgments that inform the HalluScore metric. Additionally, the benchmark's reliance on specific model families and domains may limit its generalizability to other contexts. The authors do not address the scalability of ADR beyond the tested configurations or the potential impact of model size on hallucination rates. Furthermore, the paper does not explore the implications of hallucination mitigation on the overall performance of LLMs in real-world applications.

**Why it matters**  
The implications of this work are significant for the development of more reliable LLMs. By providing a systematic framework for evaluating hallucinations, HalluScan enables researchers to identify weaknesses in existing models and develop targeted mitigation strategies. The introduction of HalluScore and ADR offers new tools for enhancing the robustness of LLMs, which is crucial for applications in sensitive domains such as healthcare, legal, and educational settings. This benchmark sets the stage for future research aimed at reducing hallucinations, ultimately leading to more trustworthy AI systems.

Authors: Ahmed Cherif  
Source: arXiv:2605.02443  
URL: https://arxiv.org/abs/2605.02443v1
