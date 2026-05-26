---
title: "Causal Tongue-Tie: LLMs Can Encode Causal Direction, But Their Yes/No Outputs Fail to Express"
date: 2026-05-25 14:19:51 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.25891v1"
arxiv_id: "2605.25891"
authors: ["Ziyi Ding", "Xiao-Ping Zhang"]
slug: causal-tongue-tie-llms-can-encode-causal-direction-but-their
summary_word_count: 495
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a critical gap in understanding the causal reasoning capabilities of large language models (LLMs). Specifically, it highlights a discrepancy between the causal information encoded in the hidden states of LLMs and the outputs they generate in response to causal questions. The authors introduce the concept of "Causal Tongue-Tie," which refers to the phenomenon where LLMs possess the necessary internal representations to answer causal questions correctly, yet their verbal outputs (Yes/No responses) do not reflect this understanding. This work challenges the prevailing assumptions about LLMs' causal reasoning abilities based solely on output accuracy metrics.

**Method**  
The authors employ a fixed linear probe to analyze the hidden states of LLMs when presented with anti-commonsense items from the CLadder benchmark. The probe is designed to extract the evidence-supported answers from the model's internal representations. The study reports an impressive accuracy of approximately 0.97 when using the probe, indicating that the model has encoded the correct causal information. In contrast, the verbal outputs yield an accuracy of around 0.5, suggesting a significant disconnect between internal representation and external expression. The authors categorize the failure modes of the Yes/No outputs into two distinct types: (1) a lack of internal signal, where the model does not encode the correct causal direction, and (2) a situation where the model has the correct signal but is unable to articulate it through the verbal interface.

**Results**  
The findings reveal a substantial gap of approximately +0.5 between the accuracy of the linear probe and the Yes/No outputs on the CLadder benchmark. This discrepancy underscores the limitations of relying solely on output accuracy to assess LLMs' causal reasoning capabilities. The authors argue that a benchmark deemed "correct" does not necessarily imply that the model has comprehended the causal relationships involved, while a "wrong" output does not definitively indicate a lack of understanding. This nuanced perspective calls for a reevaluation of how causal reasoning in LLMs is measured and interpreted.

**Limitations**  
The authors acknowledge that their analysis is limited to the CLadder benchmark and may not generalize across other datasets or tasks. Additionally, the study does not explore the underlying mechanisms that contribute to the observed Causal Tongue-Tie phenomenon, leaving open questions regarding the model architecture and training processes that could influence these outputs. Furthermore, the reliance on a fixed linear probe may not capture the full complexity of the model's internal representations.

**Why it matters**  
This work has significant implications for the evaluation of LLMs in causal reasoning tasks. It suggests that current benchmarks may misrepresent the true capabilities of these models, leading to potentially misleading conclusions about their understanding of causal relationships. By highlighting the disconnect between internal representations and verbal outputs, the authors advocate for more sophisticated evaluation methods that consider both the model's internal state and its ability to communicate that understanding. This could pave the way for improved model architectures and training paradigms that enhance causal reasoning in LLMs.

Authors: Ziyi Ding, Xiao-Ping Zhang  
Source: arXiv:2605.25891  
URL: [https://arxiv.org/abs/2605.25891v1](https://arxiv.org/abs/2605.25891v1)
