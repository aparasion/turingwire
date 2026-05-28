---
title: "Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?"
date: 2026-05-27 17:38:00 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.28778v1"
arxiv_id: "2605.28778"
authors: ["Gabrielle Kaili-May Liu", "Arman Cohan"]
slug: can-llms-use-linguistic-uncertainty-markers-to-reliably-refl
summary_word_count: 475
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how large language models (LLMs) utilize linguistic uncertainty markers to reflect their intrinsic confidence levels. Previous research indicates that LLMs struggle to employ epistemic markers (e.g., "it is likely...") in a manner that aligns with human expectations. However, there has been limited systematic investigation into whether LLMs can consistently associate these markers with specific confidence levels across various contexts. The authors introduce the concept of marker internal confidence (MIC) to quantify this relationship, aiming to provide a clearer framework for evaluating LLM calibration.

**Method**  
The authors propose a novel evaluation framework that formalizes MIC as the intrinsic confidence a model associates with a specific epistemic marker within a task domain. They develop seven metrics to assess the stability of MICs both within and across different distributions. The study involves a diverse set of LLMs and tasks, allowing for a comprehensive analysis of how these models interpret and apply linguistic markers of uncertainty. The training compute and specific architectures of the models are not disclosed, but the evaluation spans various tasks to ensure robustness in findings.

**Results**  
The findings reveal that LLMs exhibit significant miscalibration in their use of linguistic markers, failing to differentiate between markers based on internal confidence levels across different distributions. Despite this, the models maintain a relatively consistent ranking order of confidence across tasks. The authors provide quantitative metrics demonstrating that the models' MICs do not align with expected human interpretations, indicating a persistent gap in reliable calibration. Specific effect sizes and numerical results are not detailed in the abstract, but the implications suggest a critical need for improved model alignment with human linguistic cues.

**Limitations**  
The authors acknowledge that their study is limited by the scope of models and tasks selected, which may not encompass the full range of LLM capabilities. They also note that the evaluation metrics, while comprehensive, may not capture all nuances of linguistic confidence. An additional limitation is the lack of exploration into the underlying reasons for miscalibration, which could provide deeper insights into model behavior. Furthermore, the study does not address potential improvements or modifications to LLM architectures that could enhance their calibration with linguistic markers.

**Why it matters**  
This work is significant for advancing the understanding of LLM calibration, particularly in the context of trustworthiness and reliability in AI systems. By highlighting the discrepancies between LLMs' internal confidence and their use of linguistic markers, the study underscores the necessity for more aligned and stable marker usage. This has implications for downstream applications where accurate representation of uncertainty is critical, such as in decision-making systems, conversational agents, and any domain where human-AI interaction relies on trust in the model's outputs. The findings advocate for further research into improving LLM calibration mechanisms to enhance their utility in real-world applications.

Authors: Gabrielle Kaili-May Liu, Arman Cohan  
Source: arXiv:2605.28778  
URL: https://arxiv.org/abs/2605.28778v1
