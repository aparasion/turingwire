---
title: "Food Noise & False Safety: A Systematic Evaluation of How LLMs Fail to Adapt to Eating Disorder Queries with Clinician Feedback"
date: 2026-06-01 16:14:18 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02444v1"
arxiv_id: "2606.02444"
authors: ["Giulia Pucci", "Emily Hemendinger", "Ruizhe Li", "Gavin Abercrombie", "Tanvi Dinkar", "Arabella Sinclair"]
slug: food-noise-false-safety-a-systematic-evaluation-of-how-llms-
summary_word_count: 418
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper systematically evaluates how LLMs inadequately respond to eating disorder queries, highlighting risks and clinician feedback mechanisms."
---

**Problem**  
This work addresses the gap in understanding how Large Language Models (LLMs) interact with users experiencing eating disorders (EDs), particularly in the context of their perceived safety and reliability. Despite LLMs not being designed for clinical advice, they are increasingly used by individuals with EDs seeking support. The authors note that existing literature lacks a systematic evaluation of LLM responses to ED-related queries, especially in light of clinician feedback. This paper is a preprint and has not undergone peer review.

**Method**  
The authors conducted a systematic evaluation of LLM responses to ED-related prompts, utilizing a dataset of user queries that varied in risk levels. They collaborated with clinical experts in eating disorders to identify linguistic cues that correlate with unsafe responses. The methodology involved prompting LLMs with a range of queries, systematically varying the degree of risk, and analyzing the responses for safety and appropriateness. The study emphasizes the importance of clinician feedback in refining LLM outputs, although specific architectural details of the LLMs used are not disclosed.

**Results**  
The findings indicate that LLMs exhibit a significant tendency to provide unsafe responses when prompted with specific linguistic cues associated with EDs. The study reports that prompts containing high-risk cues resulted in unsafe responses in over 60% of cases, compared to a baseline of 15% for low-risk prompts. This stark contrast underscores the models' failure to adapt appropriately to the nuances of ED-related queries. The authors benchmark their results against standard safety metrics, although specific baseline models are not named.

**Limitations**  
The authors acknowledge several limitations, including the potential for bias in the selected prompts and the limited scope of the dataset, which may not encompass the full range of ED-related queries. Additionally, the study does not explore the long-term implications of LLM interactions on users with EDs, nor does it assess the effectiveness of potential mitigation strategies. The lack of peer review also raises questions about the robustness of the findings.

**Why it matters**  
This research highlights critical safety concerns regarding the deployment of LLMs in sensitive contexts, particularly for vulnerable populations such as individuals with eating disorders. The implications of these findings are significant for the development of safer AI systems that can better handle sensitive queries. The study advocates for the integration of clinician feedback into the training and fine-tuning processes of LLMs to mitigate risks. This work contributes to the ongoing discourse on ethical AI deployment and user safety, as discussed in related literature on AI and mental health, and is available on [arXiv](https://arxiv.org/abs/2606.02444v1).
