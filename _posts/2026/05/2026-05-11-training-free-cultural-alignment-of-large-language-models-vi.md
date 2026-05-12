---
title: "Training-Free Cultural Alignment of Large Language Models via Persona Disagreement"
date: 2026-05-11 16:55:16 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10843v1"
arxiv_id: "2605.10843"
authors: ["Huynh Trung Kiet", "Dao Sy Duy Minh", "Tuan Nguyen", "Chi-Nguyen Tran", "Phu-Hoa Pham", "Nguyen Lam Phu Quy"]
slug: training-free-cultural-alignment-of-large-language-models-vi
summary_word_count: 470
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in cultural alignment of large language models (LLMs) in scenarios where fine-tuning is impractical due to the lack of per-country preference data and the constraints of black-box model access, particularly in commercial APIs. The authors highlight that existing methods either require extensive fine-tuning or assume transparency in model internals, which is often not available. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose DISCA (Disagreement-Informed Steering for Cultural Alignment), an inference-time method that leverages sociodemographic disagreement among persona agents representing different cultural perspectives. Each country is modeled as a panel of agents grounded in the World Values Survey, which captures diverse moral preferences. DISCA operates by converting the disagreement among these agents into a bounded, loss-averse logit correction applied during inference, rather than modifying the model weights. The method is evaluated across 20 countries and 7 open-weight model backbones ranging from 2 billion to 70 billion parameters, demonstrating its applicability across various model sizes without requiring additional training compute.

**Results**  
DISCA achieves a reduction in cultural misalignment on the MultiTP benchmark by 10–24% for six model backbones with parameter counts greater than or equal to 3.8 billion, and by 2–7% in open-ended scenarios. These results are significant when compared to baseline models that do not utilize DISCA, indicating a marked improvement in aligning LLM outputs with culturally diverse moral frameworks. The authors provide quantitative evidence supporting the efficacy of their method, showcasing its potential as a scalable solution for cultural alignment.

**Limitations**  
The authors acknowledge that DISCA's performance may vary based on the quality and representativeness of the underlying persona agents derived from the World Values Survey. Additionally, the method's reliance on public data may limit its effectiveness in capturing nuanced cultural preferences that are not well-represented in the survey. The authors do not discuss potential biases introduced by the selection of countries or the specific parameters of the models used, which could affect generalizability. Furthermore, the method's performance in low-resource settings or with less diverse datasets remains unexamined.

**Why it matters**  
The implications of this work are significant for the deployment of LLMs in culturally diverse contexts, particularly in applications involving moral and ethical decision-making. By providing a method that allows for real-time cultural alignment without the need for extensive retraining, DISCA offers a practical solution for developers and researchers aiming to mitigate biases in AI systems. This approach could facilitate the responsible use of LLMs in global applications, ensuring that they better reflect the moral values of diverse user bases. The findings encourage further exploration of inference-time calibration techniques as viable alternatives to traditional fine-tuning methods.

Authors: Huynh Trung Kiet, Dao Sy Duy Minh, Tuan Nguyen, Chi-Nguyen Tran, Phu-Hoa Pham, Nguyen Lam Phu Quy, The Anh Han, Long Tran-Thanh  
Source: arXiv:2605.10843  
URL: https://arxiv.org/abs/2605.10843v1
