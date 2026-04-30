---
title: "Domain-Adapted Small Language Models for Reliable Clinical Triage"
date: 2026-04-29 15:00:09 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26766v1"
arxiv_id: "2604.26766"
authors: ["Manar Aljohani", "Brandon Ho", "Kenneth McKinley", "Dennis Ren", "Xuan Wang"]
slug: domain-adapted-small-language-models-for-reliable-clinical-t
summary_word_count: 445
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of accurate Emergency Severity Index (ESI) assignment in emergency departments, where inconsistent free-text triage documentation leads to mistriage and workflow inefficiencies. The authors investigate whether open-source small language models (SLMs) can be effectively utilized as reliable, privacy-preserving decision-support tools for clinical triage, filling a gap in the literature regarding the application of SLMs in healthcare settings.

**Method**  
The core technical contribution involves the systematic evaluation of various SLMs, specifically focusing on the Qwen2.5-7B model. The authors employed a domain adaptation approach using expert-curated and silver-standard pediatric triage data to fine-tune the model. They explored multiple prompting pipelines, with a particular emphasis on clinical vignettes—concise summaries of triage narratives—as input for the models. The training process involved substantial computational resources, although specific compute details were not disclosed. The study emphasizes the importance of targeted fine-tuning over more complex inference strategies, suggesting that simpler models can achieve high accuracy with appropriate domain-specific training.

**Results**  
The fine-tuned Qwen2.5-7B model demonstrated a significant reduction in discordance and clinically significant errors compared to baseline models, including advanced proprietary large language models such as GPT-4o. The authors report that Qwen2.5-7B achieved a notable improvement in accuracy and stability, outperforming all evaluated baseline SLMs. While specific numerical results and effect sizes are not detailed in the abstract, the findings indicate a clear advantage of the adapted model in clinical triage tasks, suggesting a robust performance in real-world applications.

**Limitations**  
The authors acknowledge several limitations, including the reliance on curated datasets that may not fully represent the variability of real-world triage documentation. Additionally, the study does not address the potential biases inherent in the training data, which could affect model generalizability. The computational efficiency of the Qwen2.5-7B model, while highlighted, may still pose challenges for deployment in resource-constrained environments. Furthermore, the study does not explore the long-term implications of using SLMs in clinical settings, such as their impact on clinician workflow and patient outcomes.

**Why it matters**  
This work has significant implications for the integration of AI in clinical decision-making, particularly in emergency medicine. By demonstrating the feasibility of using domain-adapted SLMs for ESI assignment, the study paves the way for the development of institution-specific models that can enhance triage accuracy while preserving patient privacy. The findings underscore the potential of targeted fine-tuning strategies to improve model performance without necessitating the complexity of larger models, which could lead to more accessible AI solutions in healthcare. This research may inspire further exploration into the application of SLMs across various medical domains, ultimately contributing to improved patient care and operational efficiency in emergency departments.

Authors: Manar Aljohani, Brandon Ho, Kenneth McKinley, Dennis Ren, Xuan Wang  
Source: arXiv:2604.26766  
URL: [https://arxiv.org/abs/2604.26766v1](https://arxiv.org/abs/2604.26766v1)
