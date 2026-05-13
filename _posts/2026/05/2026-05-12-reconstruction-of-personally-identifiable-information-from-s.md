---
title: "Reconstruction of Personally Identifiable Information from Supervised Finetuned Models"
date: 2026-05-12 15:29:33 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.12264v1"
arxiv_id: "2605.12264"
authors: ["Sae Furukawa", "Alina Oprea"]
slug: reconstruction-of-personally-identifiable-information-from-s
summary_word_count: 464
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in understanding the privacy implications of Supervised Finetuning (SFT) of large language models (LLMs), specifically regarding the potential reconstruction of personally identifiable information (PII) from these models. The authors highlight that while SFT is widely used for adapting LLMs to specific tasks, the datasets employed often contain sensitive user data, raising significant privacy concerns. This work is particularly notable as it is the first to systematically investigate the reconstruction of PII from SFT models, using multi-turn, user-centric Q&A datasets in sensitive domains such as medical and legal contexts. The paper is a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a novel decoding algorithm named COVA, designed to reconstruct PII from SFT models under prefix-based attack scenarios. COVA leverages the structure of the fine-tuning datasets, which consist of instruction-response pairs that may include PII. The evaluation involves adversaries with varying levels of knowledge about the fine-tuning dataset, allowing for a nuanced analysis of how this knowledge impacts the success of PII reconstruction. The datasets created for this study are specifically tailored to reflect realistic scenarios in sensitive domains, enhancing the validity of the findings. The training compute used for the models and the specific architectures employed are not disclosed in the paper.

**Results**  
The results demonstrate that COVA significantly outperforms existing extraction methods in reconstructing PII. The authors report that even with partial knowledge of the fine-tuning dataset, adversaries can achieve a notable increase in reconstruction success rates. The leakage of PII varies considerably across different types of information, indicating that certain PII categories are more susceptible to reconstruction than others. While specific numerical results and effect sizes are not detailed in the abstract, the findings suggest a concerning level of vulnerability in SFT models regarding PII leakage.

**Limitations**  
The authors acknowledge several limitations, including the focus on specific domains (medical and legal) which may not generalize to other contexts. Additionally, the study primarily examines prefix-based attacks, leaving other potential attack vectors unexplored. The datasets used for evaluation may also not encompass the full diversity of real-world scenarios involving PII. Furthermore, the lack of peer review means that the findings should be interpreted with caution until validated by the community.

**Why it matters**  
This research has significant implications for the development and deployment of LLMs in sensitive applications. It underscores the need for robust privacy-preserving techniques in SFT processes, particularly when handling datasets that may contain PII. The findings could inform future work on model training protocols, data handling practices, and the design of adversarial defenses against PII reconstruction. As the use of LLMs continues to expand, understanding and mitigating privacy risks will be crucial for maintaining user trust and compliance with data protection regulations.

Authors: Sae Furukawa, Alina Oprea  
Source: arXiv:2605.12264  
URL: https://arxiv.org/abs/2605.12264v1
