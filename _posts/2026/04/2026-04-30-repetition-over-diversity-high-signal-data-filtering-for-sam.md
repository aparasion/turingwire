---
title: "Repetition over Diversity: High-Signal Data Filtering for Sample-Efficient German Language Modeling"
date: 2026-04-30 16:21:28 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28075v1"
arxiv_id: "2604.28075"
authors: ["Ansar Aynetdinov", "Patrick Haller", "Alan Akbik"]
slug: repetition-over-diversity-high-signal-data-filtering-for-sam
summary_word_count: 393
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the trade-off between data diversity and quality in training language models for high-resource non-English languages, specifically German. While previous research has demonstrated that filtering English web corpora enhances training efficiency, the implications of such filtering strategies for non-English languages remain underexplored. The authors investigate whether prioritizing high-quality data through repeated training epochs yields better performance than training on diverse, lightly filtered datasets.

**Method**  
The authors propose a hierarchical quality filtering approach applied to a dataset of 500 million German web documents. They compare two training paradigms: (1) multi-epoch training on high-quality filtered subsets and (2) single-pass training on a diverse corpus. The filtering process involves selecting high-signal data that maintains semantic richness while reducing noise. The experiments are conducted across various model scales and token budgets, although specific architectural details and compute resources are not disclosed. The models trained on the filtered data are named "Boldt," and the authors provide cleaned evaluation benchmarks for the research community.

**Results**  
The results indicate that models trained on high-quality, repeated data consistently outperform those trained on larger, less filtered datasets. Notably, the performance gap remains significant even after seven epochs of training. The Boldt models achieve state-of-the-art results while utilizing 10 to 360 times fewer tokens compared to comparable models. The authors provide quantitative metrics, although specific numbers and baseline models are not detailed in the summary.

**Limitations**  
The authors acknowledge that their findings are specific to the German language and may not generalize to other high-resource non-English languages without further validation. Additionally, the study does not explore the impact of varying the number of epochs beyond seven or the potential diminishing returns of repeated training on high-quality data. The lack of detailed architectural and computational resource disclosures limits reproducibility and broader applicability of the findings.

**Why it matters**  
This work has significant implications for the development of language models in non-English contexts, suggesting that a focus on high-quality data filtering can lead to more efficient training processes. The findings challenge the prevailing notion that maximizing data volume is the optimal strategy for language model training. By releasing the Boldt models and evaluation benchmarks, the authors provide valuable resources for future research, potentially influencing best practices in data curation and model training for non-English language processing tasks.

Authors: Ansar Aynetdinov, Patrick Haller, Alan Akbik  
Source: arXiv:2604.28075  
URL: [https://arxiv.org/abs/2604.28075v1](https://arxiv.org/abs/2604.28075v1)
