---
title: "EQUITRIAGE: A Fairness Audit of Gender Bias in LLM-Based Emergency Department Triage"
date: 2026-05-05 17:20:55 +0000
category: research
subcategory: alignment_safety
company: "Mistral"
secondary_companies: ["DeepSeek"]
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03998v1"
arxiv_id: "2605.03998"
authors: ["Richard J. Young", "Alice M. Matthews"]
slug: equitriage-a-fairness-audit-of-gender-bias-in-llm-based-emer
summary_word_count: 439
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the critical gap in understanding how large language models (LLMs) perform in emergency department triage, particularly concerning gender bias. Existing literature highlights persistent gender disparities in human acuity assessments, yet there is limited empirical evidence on whether LLMs exacerbate or mitigate these biases when used for triage decision support. The study introduces EQUITRIAGE, a framework for auditing the fairness of LLM-based Emergency Severity Index (ESI) assignments.

**Method**  
EQUITRIAGE evaluates five LLMs: Gemini-3-Flash, Nemotron-3-Super, DeepSeek-V3.1, Mistral-Small-3.2, and GPT-4.1-Nano. The evaluation is based on 374,275 assessments of 18,714 vignettes from the MIMIC-IV-ED dataset, employing four distinct prompting strategies. The methodology includes generating gender-swapped counterfactuals for 9,368 original vignettes, allowing for a comparative analysis of model outputs. The authors pre-registered a threshold of 5% for acceptable flip rates, which indicates the proportion of cases where the model's triage decision changes based on gender. The study also explores the effects of demographic blinding and age-preserving variants on bias reduction.

**Results**  
All five models exhibited flip rates exceeding the pre-registered threshold, ranging from 9.9% to 43.8%. Notably, DeepSeek and Gemini demonstrated significant female undertriage, with ratios of 2.15:1 and 1.34:1, respectively. Two models approached parity, while one exhibited high sensitivity but weak male-direction asymmetry. DeepSeek's bias was accompanied by a low calibration gap of 0.013 against MIMIC-IV admissions, indicating a dissociation between within-group calibration and counterfactual invariance. Demographic blinding reduced Gemini's flip rate to 0.5%, while an age-preserving blind variant left DeepSeek with a residual female-to-male ratio of 1.25, suggesting age as a confounding factor. Chain-of-thought prompting negatively impacted accuracy across all models. An ablation study revealed that the underlying mechanisms for bias differed between models: Gemini's bias emerged from the combined name and gender swap, while DeepSeek's was driven by the gender token alone.

**Limitations**  
The authors acknowledge that the study's findings are limited to the specific models and dataset used, which may not generalize to other LLMs or clinical contexts. Additionally, the reliance on counterfactuals may not capture all dimensions of bias present in real-world scenarios. The impact of other demographic factors beyond gender and age was not explored, which could further complicate the fairness landscape.

**Why it matters**  
EQUITRIAGE underscores the necessity for rigorous fairness audits of LLMs before clinical deployment, particularly in high-stakes environments like emergency medicine. The findings highlight that group parity, counterfactual invariance, and gender calibration are distinct fairness properties, necessitating tailored interventions based on model-specific behaviors. This work lays the groundwork for future research on bias mitigation strategies in LLMs, emphasizing the importance of per-model counterfactual auditing to ensure equitable healthcare outcomes.

Authors: Richard J. Young, Alice M. Matthews  
Source: arXiv:2605.03998  
URL: https://arxiv.org/abs/2605.03998v1
