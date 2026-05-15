---
title: "Explainable Detection of Depression Status Shifts from User Digital Traces"
date: 2026-05-14 15:56:38 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.14995v1"
arxiv_id: "2605.14995"
authors: ["Loris Belcastro", "Francesco Gervino", "Fabrizio Marozzo", "Domenico Talia", "Paolo Trunfio"]
slug: explainable-detection-of-depression-status-shifts-from-user-
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the detection and analysis of depression status shifts using user-generated digital traces. While existing methods often focus on static assessments of mental health, this work emphasizes the temporal evolution of mental health signals derived from digital interactions. The authors aim to provide an explainable framework that not only detects these shifts but also interprets them in a human-readable format, which is crucial for understanding user mental health dynamics over time.

**Method**  
The proposed framework employs a multi-faceted approach utilizing BERT-based models to extract various mental health signals, including sentiment, emotion, and depression severity, from user digital traces. These signals are aggregated into user-level temporal trajectories, which are then analyzed to identify significant change points indicative of shifts in mental health status. To enhance interpretability, the framework incorporates a large language model (LLM) that generates concise reports summarizing the evolution of mental health signals and key transitions. The architecture's effectiveness is further validated through an ablation study, which highlights the importance of temporal modeling and segmentation in the overall performance of the system. The training compute details are not disclosed, but the framework is evaluated on two distinct social media datasets.

**Results**  
The framework demonstrates superior performance compared to baseline methods, particularly in generating coherent and informative summaries of user mental health trajectories. Key metrics indicate that the proposed method achieves higher coverage of user history and stronger temporal coherence. Additionally, it shows improved sensitivity to change points when compared to direct LLM-based reporting. While specific numerical results are not provided in the abstract, the qualitative improvements suggest a significant advancement over existing techniques in the domain of mental health signal interpretation.

**Limitations**  
The authors acknowledge that their framework does not aim for clinical diagnosis, which may limit its applicability in clinical settings. Additionally, the reliance on social media datasets may introduce biases inherent to the platforms, such as demographic skew or the nature of user interactions. The paper does not address potential ethical concerns related to privacy and data usage, which are critical in mental health applications. Furthermore, the generalizability of the findings to other forms of digital traces or different populations remains unexamined.

**Why it matters**  
This work has significant implications for both research and practical applications in mental health monitoring. By providing an explainable and interpretable framework for analyzing depression status shifts, it opens avenues for more nuanced understanding of mental health dynamics in real-time. The integration of temporal modeling with LLM-generated reports could enhance user engagement and support non-clinical interventions. Furthermore, the findings could inform future research on the relationship between digital behavior and mental health, potentially leading to more effective monitoring tools and strategies for mental health professionals.

Authors: Loris Belcastro, Francesco Gervino, Fabrizio Marozzo, Domenico Talia, Paolo Trunfio  
Source: arXiv:2605.14995  
URL: [https://arxiv.org/abs/2605.14995v1](https://arxiv.org/abs/2605.14995v1)
