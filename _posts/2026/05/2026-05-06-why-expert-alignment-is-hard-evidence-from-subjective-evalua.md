---
title: "Why Expert Alignment Is Hard: Evidence from Subjective Evaluation"
date: 2026-05-06 14:28:09 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.04972v1"
arxiv_id: "2605.04972"
authors: ["Tzu-Mi Lin", "Wataru Hirota", "Tatsuya Ishigaki", "Lung-Hao Lee", "Chung-Chi Chen"]
slug: why-expert-alignment-is-hard-evidence-from-subjective-evalua
summary_word_count: 470
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of aligning large language models (LLMs) with expert judgment in subjective evaluation tasks. The authors highlight a gap in understanding how expert evaluations can vary due to disagreement among experts, reliance on tacit criteria, and temporal changes in judgment. The paper aims to elucidate the complexities of expert alignment, which has not been thoroughly explored in existing literature.

**Method**  
The authors conducted a series of studies involving expert evaluations and follow-up questionnaires to analyze the factors influencing expert alignment. They examined how different forms of expert information—such as explicit criteria and reasoning—affect alignment outcomes. The study involved a diverse set of evaluation dimensions, focusing on both content-grounded and value-based judgments. The methodology emphasizes qualitative insights from expert feedback rather than solely quantitative metrics, allowing for a nuanced understanding of alignment challenges.

**Results**  
The findings reveal four key patterns regarding expert alignment:  
1. **Variability in Alignment Difficulty**: There is significant variability in alignment difficulty across different experts, indicating diverse evaluation styles and their distance from the model's prior behavior.
2. **Impact of Explicit Criteria**: The introduction of explicit criteria and reasoning does not consistently enhance alignment, suggesting that expert judgment encompasses more than just verbalized rules.
3. **Sensitivity to Edits**: The alignment process is sensitive to both the number and identity of examples used for evaluation. Small edits can yield useful but unstable improvements in alignment.
4. **Dimension-Dependent Difficulty**: Alignment challenges vary across evaluation dimensions; those grounded in proposal content are easier to align with, while dimensions requiring external knowledge or subjective value judgments are more difficult.

These results suggest that expert alignment is complicated not only by the limitations of the models but also by the inherent heterogeneity and instability of subjective evaluations.

**Limitations**  
The authors acknowledge that their findings are based on a limited set of expert evaluations, which may not be representative of all expert domains. They also note that the reliance on qualitative data may introduce biases in interpretation. Additionally, the study does not explore the potential for automated methods to assist in expert alignment, which could be a valuable avenue for future research. An obvious limitation not flagged by the authors is the potential overfitting to the specific expert cohort studied, which may not generalize across different contexts or expert groups.

**Why it matters**  
This work has significant implications for the development of LLMs and their applications in subjective evaluation tasks. Understanding the complexities of expert alignment can inform the design of more robust evaluation frameworks that account for the variability and tacit nature of expert judgment. This research could lead to improved methodologies for training models that better align with human evaluators, ultimately enhancing the reliability and applicability of AI systems in real-world scenarios.

Authors: Tzu-Mi Lin, Wataru Hirota, Tatsuya Ishigaki, Lung-Hao Lee, Chung-Chi Chen  
Source: arXiv:2605.04972  
URL: [https://arxiv.org/abs/2605.04972v1](https://arxiv.org/abs/2605.04972v1)
