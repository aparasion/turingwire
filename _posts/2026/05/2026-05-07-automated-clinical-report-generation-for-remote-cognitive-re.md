---
title: "Automated Clinical Report Generation for Remote Cognitive Remediation: Comparing Knowledge-Engineered Templates and LLMs in Low-Resource Settings"
date: 2026-05-07 17:20:22 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.06594v1"
arxiv_id: "2605.06594"
authors: ["Yongxin Zhou", "Fabien Ringeval", "Fran\u00e7ois Portet"]
slug: automated-clinical-report-generation-for-remote-cognitive-re
summary_word_count: 435
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in automated clinical report generation for remote cognitive remediation therapy, particularly in low-resource settings where traditional reference reports are unavailable. The increasing demand for cognitive remediation, coupled with a shortage of speech therapists, necessitates efficient tools for processing interaction data generated during therapy sessions. The paper evaluates two distinct approaches to report generation, aiming to enhance clinical reliability and linguistic quality in a context where both are critical.

**Method**  
The authors propose and compare two methodologies for generating clinical reports: (1) a rule-based template system that encodes domain knowledge through explicit decision rules and validated templates, ensuring clinical reliability and traceability; and (2) a zero-shot approach utilizing GPT-4, a large language model (LLM), to produce more fluent and concise outputs. Both systems leverage identical pre-extracted, expert-validated structured variables, allowing for a controlled comparison of their outputs. The evaluation involved eight speech therapists and final-year students who assessed the generated reports using a nine-criterion questionnaire, focusing on dimensions such as fluidity, coherence, and presentation of results.

**Results**  
The results indicate a trade-off between clinical reliability and linguistic quality. The template-based system outperformed the LLM in fluidity, coherence, and results presentation, while GPT-4 generated more concise outputs. Although directional differences were noted across evaluation dimensions, none reached statistical significance after correction, likely due to the limited scale of expert clinical evaluation. The authors derived eight design recommendations for clinical reporting systems based on evaluator feedback, emphasizing the need for a balanced approach in report generation.

**Limitations**  
The authors acknowledge several limitations, including the lack of statistical significance in their comparisons, which may stem from the small sample size of evaluators. Additionally, the reliance on a single LLM (GPT-4) may limit the generalizability of findings to other models or configurations. The study also does not explore the long-term implications of using automated systems in clinical practice or the potential biases inherent in the LLM outputs. Furthermore, the evaluation criteria may not encompass all relevant aspects of clinical reporting, potentially overlooking important dimensions of usability and clinician satisfaction.

**Why it matters**  
This work is significant as it provides a replicable methodology for combining expert elicitation, taxonomy-driven generation, and multi-dimensional human evaluation in the context of clinical natural language generation (NLG) in low-resource settings. The findings highlight the importance of balancing clinical reliability with linguistic quality, which is crucial for the responsible adoption of generative AI in healthcare. The design recommendations derived from the study can inform future developments in automated reporting systems, ultimately enhancing the efficiency and effectiveness of cognitive remediation therapies.

Authors: Yongxin Zhou, Fabien Ringeval, François Portet  
Source: arXiv:2605.06594  
URL: [https://arxiv.org/abs/2605.06594v1](https://arxiv.org/abs/2605.06594v1)
