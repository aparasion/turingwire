---
title: "Does Continued Pretraining on a Learner Corpus Improve Automated Essay Scoring on English Proficiency Tests? Evidence from EFCAMDAT"
date: 2026-05-25 15:04:37 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.25924v1"
arxiv_id: "2605.25924"
authors: ["Duy Anh Nguyen"]
slug: does-continued-pretraining-on-a-learner-corpus-improve-autom
summary_word_count: 407
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in automated essay scoring (AES) for English proficiency tests, specifically the inadequacy of pretrained transformer models that are typically trained on general-domain English data. Such models may not effectively capture the nuances of second-language learner writing. The study investigates whether domain-adaptive continued pretraining (DAPT) on the EFCAMDAT learner corpus can enhance the performance of transformer-based AES systems.

**Method**  
The authors apply DAPT to three transformer encoder architectures, although specific architectures are not disclosed. The models are pretrained on the EFCAMDAT corpus, which consists of essays written by English language learners. The evaluation is conducted on two benchmarks: the First Certificate in English (FCE) and the International English Language Testing System (IELTS). The study examines both in-domain scoring and few-shot cross-dataset transfer. The authors conduct a proficiency-based ablation study using subsets of the EFCAMDAT corpus aligned with the Common European Framework of Reference for Languages (CEFR) to assess the impact of targeted DAPT versus full-corpus DAPT.

**Results**  
The results indicate that full-corpus DAPT yields mixed outcomes across the models, datasets, and evaluation metrics. Specifically, targeted DAPT using CEFR-aligned subsets demonstrates more consistent improvements in scoring, particularly for the FCE dataset with B1-B2 proficiency levels. However, these enhancements do not translate into improved performance on cross-dataset transfer tasks. The study quantifies the effect sizes but does not provide specific numerical results in the abstract.

**Limitations**  
The authors acknowledge that the mixed results may stem from mismatches in proficiency levels, writing genres, and communicative purposes between the EFCAMDAT corpus and the downstream datasets. They also note that while targeted DAPT shows promise, it does not guarantee improved transferability across different English proficiency tests. An additional limitation is the lack of detailed performance metrics and comparisons against established baselines, which could provide clearer insights into the effectiveness of the proposed methods.

**Why it matters**  
This research has significant implications for the development of AES systems tailored for second-language learners. It suggests that continued pretraining on learner-specific corpora can enhance scoring accuracy in contexts where the training data aligns closely with the assessment criteria. However, the findings also caution against assuming that improvements in in-domain performance will generalize to other datasets, highlighting the need for careful consideration of the training data's characteristics. This work encourages further exploration of domain adaptation techniques in the context of language learning and assessment, potentially influencing future research on AES and related applications.

Authors: Duy Anh Nguyen  
Source: arXiv:2605.25924  
URL: https://arxiv.org/abs/2605.25924v1
