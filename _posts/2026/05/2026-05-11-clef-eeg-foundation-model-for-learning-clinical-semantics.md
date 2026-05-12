---
title: "CLEF: EEG Foundation Model for Learning Clinical Semantics"
date: 2026-05-11 16:34:58 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10817v1"
arxiv_id: "2605.10817"
authors: ["Peng Cao", "Ali Mirzazadeh", "Jong Woo Lee", "Aleksandar Videnovic", "Dina Katabi"]
slug: clef-eeg-foundation-model-for-learning-clinical-semantics
summary_word_count: 439
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in existing EEG foundation models, which primarily focus on short-window decoding and fail to incorporate clinical context for comprehensive EEG interpretation. The authors highlight that current models do not effectively reason over full EEG sessions, which is crucial for clinical applications. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors introduce CLEF, a long-context EEG foundation model that utilizes 3D multitaper spectrogram tokens to represent EEG sessions. This representation allows for efficient modeling with Transformers at the session scale. The model employs contrastive learning objectives to align its embeddings with neurologist reports and structured Electronic Health Record (EHR) data. The training dataset comprises over 260,000 EEG sessions from more than 108,000 patients, and the model is evaluated across a novel benchmark of 234 tasks, which encompass various disease phenotypes, medication exposures, and EEG findings. The architecture leverages reconstruction-only pretraining, which is shown to outperform previous EEG models, while the alignment with clinical reports and EHR data further enhances performance.

**Results**  
CLEF demonstrates significant improvements over prior EEG foundation models, achieving state-of-the-art performance on 229 out of 234 tasks in the benchmark. The mean Area Under the Receiver Operating Characteristic (AUROC) score improved from 0.65 to 0.74, indicating a substantial enhancement in predictive accuracy. The results also suggest that the model's representations are transferable, as evidenced by held-out concept and external-cohort experiments, which indicate that the learned embeddings generalize beyond the specific alignment targets used during training.

**Limitations**  
The authors acknowledge several limitations, including the potential for overfitting due to the large number of tasks relative to the dataset size. They also note that while the model shows promise in aligning EEG data with clinical context, the generalizability of the findings to other clinical settings or populations remains to be fully validated. Additionally, the reliance on structured EHR data may limit applicability in environments where such data is less accessible or standardized.

**Why it matters**  
The introduction of CLEF represents a significant advancement in the field of clinical EEG interpretation by enabling session-scale representation learning that integrates clinical semantics. This approach not only enhances the accuracy of EEG analysis but also sets a precedent for future research in developing foundation models that incorporate broader clinical contexts. The findings suggest that such models could facilitate improved diagnostic and therapeutic decision-making in neurology, ultimately leading to better patient outcomes. The work opens avenues for further exploration of long-context models in other domains of healthcare, where integrating diverse data sources is critical.

Authors: Peng Cao, Ali Mirzazadeh, Jong Woo Lee, Aleksandar Videnovic, Dina Katabi  
Source: arXiv:2605.10817  
URL: [https://arxiv.org/abs/2605.10817v1](https://arxiv.org/abs/2605.10817v1)
