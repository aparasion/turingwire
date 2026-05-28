---
title: "Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests"
date: 2026-05-27 16:55:15 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28734v1"
arxiv_id: "2605.28734"
authors: ["Richard J. Young", "Gregory D. Moody"]
slug: code-as-a-weapon-a-consensus-labeled-prompt-bank-for-measuri
summary_word_count: 453
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of coding models' compliance with malicious-code requests, highlighting the asymmetry in the consequences of compliance between general-purpose language models and coding-specialized models. The existing benchmarks for refusal rates are fragmented and do not adequately differentiate between requests for executable malicious code and those for harmful security knowledge. This lack of a standardized measurement framework impedes the ability to assess whether coding models adhere to a higher refusal standard necessary for handling executable outputs. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a consensus-labeled prompt bank designed to provide a reliable framework for measuring coding-model compliance. This prompt bank consolidates eight existing corpora (ASTRA, CySecBench, AdvBench/harmful_behaviors, JailbreakBench, MalwareBench, RedCode, RMCBench, Scam2Prompt) into a unified dataset of 6,675 prompts, which were evaluated by a panel of five judges. The consensus protocol employed achieved a Fleiss' kappa of 0.767, indicating substantial agreement among judges. The final dataset comprises 4,748 prompts classified as consensus-CODE (executable malicious code requests) and 1,923 as consensus-KNOWLEDGE (harmful security knowledge requests). The authors provide a detailed methodology for the classification process and the consensus-building approach, ensuring the reliability of the prompt bank as a measurement tool.

**Results**  
The prompt bank demonstrates high inter-judge reliability, with 95.0% of prompts receiving at least four agreeing judges and 76.9% achieving unanimous agreement. The authors also report a Cohen's kappa of 0.952 on the 3,133 shared prompts from the earlier four-corpus release, reinforcing the robustness of the classification. While specific performance metrics of coding models against this prompt bank are not disclosed, the establishment of a reliable and validated instrument for compliance measurement is a significant contribution to the field.

**Limitations**  
The authors acknowledge that the prompt bank is limited to the specific corpora included and may not encompass all potential malicious requests. Additionally, the reliance on a panel of judges introduces subjectivity, although the high kappa values suggest substantial agreement. The paper does not address the potential for adversarial prompts that could exploit weaknesses in the classification system or the evolving nature of malicious code, which may outpace the prompt bank's relevance over time.

**Why it matters**  
This work provides a critical resource for researchers and engineers developing coding models, as it establishes a standardized method for evaluating compliance with malicious requests. By differentiating between executable and informational requests, the prompt bank enables more rigorous testing of coding models against a higher refusal standard. This has implications for the safe deployment of AI in coding applications, particularly in security-sensitive environments, and sets a precedent for future research in model compliance and ethical AI development.

Authors: Richard J. Young, Gregory D. Moody  
Source: arXiv:2605.28734  
URL: [https://arxiv.org/abs/2605.28734v1](https://arxiv.org/abs/2605.28734v1)
