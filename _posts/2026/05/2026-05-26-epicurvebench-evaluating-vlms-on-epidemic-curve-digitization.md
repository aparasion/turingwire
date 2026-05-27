---
title: "EpiCurveBench: Evaluating VLMs on Epidemic Curve Digitization"
date: 2026-05-26 15:48:29 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.27195v1"
arxiv_id: "2605.27195"
authors: ["Thomas Berkane", "Maimuna S. Majumder"]
slug: epicurvebench-evaluating-vlms-on-epidemic-curve-digitization
summary_word_count: 486
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations in evaluating vision-language models (VLMs) for chart-to-data extraction, particularly in the context of epidemic curve digitization. Existing benchmarks, such as ChartQA, exhibit diminishing returns, with top-performing models achieving over 89% accuracy. Furthermore, current evaluation metrics treat extracted data points as unordered key-value pairs, neglecting the temporal structure inherent in time series data. This oversight leads to a penalization of minor alignment errors as significant failures. The authors present EpiCurveBench, a new benchmark comprising 1,000 real-world epidemic curve images, and introduce EpiCurveSimilarity (ECS), a metric designed to address these gaps. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
EpiCurveBench consists of 1,000 curated images of epidemic curves sourced from various public health datasets. The core technical contribution is the ECS metric, which employs dynamic programming to align predicted and ground-truth time series. ECS tolerates local temporal shifts and gaps, applying proportional penalties for misalignments rather than treating them as catastrophic errors. The authors evaluate six models: three state-of-the-art closed VLMs, one open VLM, and two specialized chart-extraction systems. The training compute details are not disclosed, but the evaluation focuses on the performance of these models against the ECS metric, which is designed to better reflect the accuracy of time series extraction.

**Results**  
The strongest model evaluated achieves an ECS score of 52.3%, indicating significant room for improvement in VLM performance on this task. In contrast, traditional key-value metrics such as Root Mean Square (RMS) and Structured Chart Recognition Metric (SCRM) compress the performance of the four general-purpose VLMs into a narrow 5-point range, while ECS differentiates them across a 25-point spectrum. Additionally, ECS demonstrates a strong correlation with four downstream epidemiological summary statistics, predicting smaller errors in total counts, peak timing, and peak magnitude. The correlation coefficients for ECS range from 1.5 to 3.6 times stronger than those obtained using Dynamic Time Warping, which lacks a gap penalty and fails to distinguish between truncated and temporally faithful predictions.

**Limitations**  
The authors acknowledge that the ECS metric, while more robust than existing methods, may still be sensitive to the quality of the input images and the inherent variability in epidemic curves. They do not address potential biases in the dataset selection or the generalizability of the benchmark across different types of time series data. Additionally, the computational resources required for training and evaluating the models are not specified, which may limit reproducibility.

**Why it matters**  
EpiCurveBench and the ECS metric have significant implications for public health research, as they enable the extraction of valuable data from historical outbreak figures that have been previously inaccessible. By improving the evaluation of VLMs in this domain, the work facilitates better data-driven decision-making in epidemiology. Furthermore, the methodologies developed here can be applied to other structured time-series chart-extraction tasks, potentially broadening the impact of this research across various fields.

Authors: Thomas Berkane, Maimuna S. Majumder  
Source: arXiv:2605.27195  
URL: [https://arxiv.org/abs/2605.27195v1](https://arxiv.org/abs/2605.27195v1)
