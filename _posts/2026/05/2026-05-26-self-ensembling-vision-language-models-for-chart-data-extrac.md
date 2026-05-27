---
title: "Self-Ensembling Vision-Language Models for Chart Data Extraction"
date: 2026-05-26 17:10:51 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.27298v1"
arxiv_id: "2605.27298"
authors: ["Thomas Berkane", "Qianyi Wang", "Maimuna S. Majumder"]
slug: self-ensembling-vision-language-models-for-chart-data-extrac
summary_word_count: 443
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of automatic chart-to-table extraction, a task critical for unlocking quantitative data embedded in chart images. Existing vision-language models (VLMs) have shown limited performance, particularly on charts with numerous data points or significant stylistic variations. The authors identify a gap in the literature regarding the effectiveness of VLMs in handling complex chart data, which often leads to inaccuracies in data extraction.

**Method**  
The authors propose a self-ensembling approach for VLMs that generates multiple tabular outputs from a single chart image. The core technical contribution involves aggregating these outputs at the cell level to enhance accuracy. Specifically, the method samples multiple outputs, aligns candidate tables, and computes per-cell medians for numerical values to create a consensus table. The approach incorporates convergence detection to terminate sampling once the aggregated table stabilizes, and it provides uncertainty estimation based on the dispersion of sampled outputs. The model is trained on a new benchmark, WB-ChartExtract, which features more complex charts derived from World Bank data, significantly increasing the number of data points compared to existing benchmarks.

**Results**  
The proposed method demonstrates substantial improvements in extraction accuracy over single-pass VLM outputs. On the WB-ChartExtract benchmark, the self-ensembling approach achieves up to a 23% relative improvement in accuracy. Additionally, the method is evaluated on the ChartQA benchmark, where it also outperforms existing models, although specific numbers for this dataset are not disclosed. The results indicate that the self-ensembling technique effectively enhances the reliability of chart data extraction, particularly for complex visualizations.

**Limitations**  
The authors acknowledge that the performance gains are contingent on the quality of the initial VLM outputs; if the base model performs poorly, the benefits of ensembling may be limited. They also note that the method's reliance on median aggregation may not capture all nuances in the data, particularly in cases of extreme outliers. Furthermore, the new WB-ChartExtract benchmark, while more complex than previous datasets, may still not encompass the full diversity of chart styles encountered in real-world applications. The paper does not address the computational overhead introduced by the self-ensembling process, which may impact scalability.

**Why it matters**  
This work has significant implications for the field of data extraction and analysis, as it provides a robust method for converting chart images into usable tabular data. By improving the accuracy of chart data extraction, the proposed approach facilitates the reuse of quantitative information that is often locked in visual formats, thereby enhancing data accessibility for researchers and analysts. The introduction of the WB-ChartExtract benchmark also sets a new standard for evaluating chart extraction methods, potentially driving further advancements in this area.

Authors: Thomas Berkane, Qianyi Wang, Maimuna S. Majumder  
Source: arXiv:2605.27298  
URL: [https://arxiv.org/abs/2605.27298v1](https://arxiv.org/abs/2605.27298v1)
