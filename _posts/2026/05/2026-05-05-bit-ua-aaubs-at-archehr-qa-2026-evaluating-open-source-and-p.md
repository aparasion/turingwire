---
title: "BIT.UA-AAUBS at ArchEHR-QA 2026: Evaluating Open-Source and Proprietary LLMs via Prompting in Low-Resource QA"
date: 2026-05-05 10:43:56 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03618v1"
arxiv_id: "2605.03618"
authors: ["Richard A. A. Jonker", "Alexander Christiansen", "Alexandros Maniatis", "R\u00faben Garrido", "Rog\u00e9rio Braunschweiger de Freitas Lima", "Roman Jurowetzki"]
slug: bit-ua-aaubs-at-archehr-qa-2026-evaluating-open-source-and-p
summary_word_count: 421
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of clinical question answering (QA) in low-resource settings, particularly in the context of healthcare where data privacy regulations (e.g., GDPR) limit the availability of training data. The authors investigate the performance of both proprietary and open-source Large Language Models (LLMs) in this domain without performing weight updates, which is a notable gap in the literature regarding the application of LLMs in sensitive environments. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors evaluate several state-of-the-art proprietary LLMs alongside open-source alternatives, specifically focusing on the domain-adapted model MedGemma 3 27B. They employ various prompt engineering strategies, including task decomposition, Chain-of-Thought prompting, and in-context learning to enhance model performance. Additionally, they implement ensemble techniques such as majority voting and LLM-as-a-judge to improve predictive robustness. The training compute details are not disclosed, but the emphasis is on leveraging existing models without fine-tuning, which is critical given the constraints of the healthcare domain.

**Results**  
The results indicate that proprietary models demonstrate strong resilience to variations in prompting strategies. However, the domain-adapted open-source model, MedGemma 3 27B, achieves competitive performance when appropriately prompted. The authors secured 1st place in Subtask 4 (evidence citation alignment) and 3rd place in Subtask 3 (patient-friendly answer generation) of the ArchEHR-QA 2026 shared task. Specific performance metrics are not detailed in the abstract, but the competitive placements suggest significant effect sizes relative to baseline models in the same tasks.

**Limitations**  
The authors acknowledge the limitations inherent in their approach, particularly the reliance on prompt engineering without model fine-tuning, which may restrict the generalizability of their findings. They also note the challenges posed by the low-resource setting and the potential biases introduced by the limited data available for evaluation. An additional limitation not explicitly mentioned is the lack of a comprehensive analysis of the models' performance across diverse clinical scenarios, which could affect the robustness of the conclusions drawn.

**Why it matters**  
This research has significant implications for the deployment of LLMs in healthcare settings, particularly in low-resource environments where data privacy is paramount. The findings suggest that with effective prompt engineering, open-source models can achieve performance levels comparable to proprietary counterparts, thereby democratizing access to advanced AI tools in clinical applications. This work lays the groundwork for future research into prompt-based methodologies and the development of more robust, privacy-compliant AI systems in healthcare.

Authors: Richard A. A. Jonker, Alexander Christiansen, Alexandros Maniatis, Rúben Garrido, Rogério Braunschweiger de Freitas Lima, Roman Jurowetzki, Sérgio Matos  
Source: arXiv:2605.03618  
URL: https://arxiv.org/abs/2605.03618v1
