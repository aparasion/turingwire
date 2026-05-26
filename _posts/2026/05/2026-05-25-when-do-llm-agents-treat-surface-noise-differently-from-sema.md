---
title: "When Do LLM Agents Treat Surface Noise Differently from Semantic Noise? A 68-Cell Measurement Study with a Held-Out Trace-Level Validation"
date: 2026-05-25 15:57:11 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.25981v1"
arxiv_id: "2605.25981"
authors: ["Liyun Zhang", "Jiayi Guo"]
slug: when-do-llm-agents-treat-surface-noise-differently-from-sema
summary_word_count: 432
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a gap in understanding how large language model (LLM) agents differentiate between surface noise (e.g., formatting changes) and semantic noise (e.g., paraphrasing) during reasoning tasks. Prior literature has not systematically quantified the impact of these perturbations on model outputs across various architectures. The study investigates this phenomenon using a comprehensive empirical approach, focusing on the inconsistency in model responses when subjected to different types of noise.

**Method**  
The authors conduct a measurement study involving ten LLMs from seven architecture families, analyzing their responses across 68 cells derived from three benchmarks: GSM8K, MATH, and HotpotQA. The study employs a paired t-test to assess the impact of semantic versus presentation perturbations, with a focus on severity matching. The perturbation corpus includes 1,530 original instances and approximately 11,150 variants. The authors validate their findings using a held-out model (qwen2.5-14B-Instruct) on 1,800 trajectories, and they explore trace-level mechanisms through four specific probes. The study introduces the concept of "stealth-divergence," where semantic perturbations lead to divergence in reasoning paths while preserving initial actions.

**Results**  
The study reports a significant inconsistency gap of +19.69 percentage points (pp) favoring semantic perturbations over presentation perturbations after severity matching (paired t=9.58, p<0.0001), with 64 out of 68 cells showing positive results. This gap remains significant even when excluding qwen models, yielding a reduced but still notable gap of +11.10 pp (p<0.0001). The validation on the held-out model shows a small positive effect, with 3 out of 4 cells indicating a significant difference (pooled Welch t=3.81, p=9.6×10^-4). The study also highlights that several stress tests, including cluster-bootstrap significance and cross-architecture generator swaps, fail to replicate the initial findings, indicating potential fragility in the observed effects.

**Limitations**  
The authors acknowledge limitations in their findings, particularly the failure to replicate two prior mechanism claims, which they explicitly retract. Additionally, the moderate agreement (κ=0.50) between a second LLM judge raises questions about the robustness of the results. The study's reliance on specific architectures and the limited scope of perturbations may also restrict the generalizability of the findings.

**Why it matters**  
This work has significant implications for the understanding of LLM behavior in response to different types of noise, which is crucial for developing more robust AI systems. By elucidating the mechanisms through which semantic perturbations affect reasoning, the study provides a foundation for future research aimed at improving model interpretability and reliability. The findings may inform the design of training protocols and evaluation metrics that account for the nuanced ways in which LLMs process information, ultimately enhancing their performance in real-world applications.

Authors: Liyun Zhang, Jiayi Guo  
Source: arXiv:2605.25981  
URL: [https://arxiv.org/abs/2605.25981v1](https://arxiv.org/abs/2605.25981v1)
