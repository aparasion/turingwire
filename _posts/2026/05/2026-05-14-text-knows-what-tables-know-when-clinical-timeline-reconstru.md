---
title: "Text Knows What, Tables Know When: Clinical Timeline Reconstruction via Retrieval-Augmented Multimodal Alignment"
date: 2026-05-14 17:55:27 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.15168v1"
arxiv_id: "2605.15168"
authors: ["Sayantan Kumar", "Shahriar Noroozizadeh", "Juyong Kim", "Jeremy C. Weiss"]
slug: text-knows-what-tables-know-when-clinical-timeline-reconstru
summary_word_count: 429
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of reconstructing precise clinical timelines from heterogeneous data sources, specifically unstructured clinical narratives and structured electronic health records (EHR). Existing methods often fail to leverage the strengths of both modalities: narratives provide rich semantic context but lack temporal precision, while EHRs offer precise timestamps but miss significant clinical events. The authors aim to bridge this gap to enhance the temporal accuracy of clinical timelines, which is crucial for modeling patient trajectories and risk forecasting in conditions like sepsis.

**Method**  
The authors propose a retrieval-augmented multimodal alignment framework that employs a graph-based multistep process for timeline reconstruction. The method consists of three main components: 
1. **Anchor Event Extraction**: Central events are extracted from clinical narratives to form an initial temporal scaffold.
2. **Relative Placement**: Non-central events are positioned relative to this scaffold, establishing a preliminary timeline.
3. **Calibration with EHR Data**: The timeline is refined using retrieved structured EHR rows as external temporal evidence, enhancing the overall temporal accuracy. The framework utilizes instruction-tuned large language models for processing and aligning the multimodal data. The training compute specifics are not disclosed, but the evaluation is conducted on the i2m4 benchmark, which includes datasets from MIMIC-III and MIMIC-IV.

**Results**  
The proposed framework demonstrates significant improvements in absolute timestamp accuracy (AULTC) and temporal concordance across nearly all evaluated models compared to unimodal text-only reconstruction. The authors report that their method achieves a marked increase in AULTC, with specific effect sizes not disclosed in the abstract. Additionally, their empirical gap analysis reveals that 34.8% of events derived from text are absent in tabular records, underscoring the importance of integrating both modalities for a more comprehensive reconstruction of patient timelines.

**Limitations**  
The authors acknowledge that their approach may be limited by the quality and completeness of the EHR data used for calibration. They also do not address potential biases in the narratives or EHRs that could affect the alignment process. Furthermore, the reliance on large language models may introduce variability based on model architecture and training data, which is not fully explored in the paper.

**Why it matters**  
This work has significant implications for clinical informatics and patient care, as improved timeline reconstruction can enhance the understanding of patient trajectories and inform risk assessment strategies. By effectively integrating unstructured and structured data, the proposed framework could lead to better clinical decision-making and outcomes in complex conditions like sepsis. Future research could build on this methodology to explore other applications in healthcare analytics and predictive modeling.

Authors: Sayantan Kumar, Shahriar Noroozizadeh, Juyong Kim, Jeremy C. Weiss  
Source: arXiv:2605.15168  
URL: https://arxiv.org/abs/2605.15168v1
