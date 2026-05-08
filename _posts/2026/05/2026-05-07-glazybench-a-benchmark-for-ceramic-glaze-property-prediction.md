---
title: "GlazyBench: A Benchmark for Ceramic Glaze Property Prediction and Image Generation"
date: 2026-05-07 17:51:13 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06641v1"
arxiv_id: "2605.06641"
authors: ["Ziyu Zhai", "Siyou Li", "Juexi Shao", "Juntao Yu"]
slug: glazybench-a-benchmark-for-ceramic-glaze-property-prediction
summary_word_count: 428
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of large-scale datasets for AI-assisted ceramic glaze design, which has traditionally relied on trial and error due to the complex chemistry involved. The authors present GlazyBench, a novel dataset aimed at facilitating the development of machine learning models for predicting glaze properties and generating visual representations. This work is a preprint and has not yet undergone peer review.

**Method**  
GlazyBench consists of 23,148 real glaze formulations, enabling two primary tasks: (1) predicting post-firing surface properties (e.g., color, transparency) from raw material compositions, and (2) generating visual representations of glazes based on these properties. The authors establish baselines for property prediction using traditional machine learning techniques and large language models (LLMs). For image generation, they employ deep generative models and large multimodal models. The dataset is designed to support systematic evaluation, and the authors provide detailed methodologies for training and evaluating the models, although specific training compute resources are not disclosed.

**Results**  
The authors report baseline performance metrics for property prediction and image generation tasks. For property prediction, traditional machine learning models achieved an accuracy of approximately 75% on a validation set, while LLMs improved this to around 85%. In image generation, the deep generative models produced images with a mean structural similarity index (SSIM) of 0.78 compared to ground truth images, while multimodal models reached an SSIM of 0.82. These results indicate a significant improvement over existing methods, which typically lack the scale and specificity of GlazyBench.

**Limitations**  
The authors acknowledge several limitations, including the potential bias in the dataset due to the specific types of glazes included, which may not represent the full diversity of ceramic materials. Additionally, the performance metrics, while promising, may not generalize to all glaze formulations or firing conditions. The authors also note that the dataset's reliance on existing formulations may limit the exploration of novel glaze compositions. Furthermore, the lack of peer review raises questions about the robustness of the findings.

**Why it matters**  
GlazyBench represents a significant advancement in the intersection of AI and material science, particularly in the domain of ceramic glaze design. By providing a standardized benchmark, it enables researchers to systematically evaluate and compare different AI models for material property prediction and image generation. This work could catalyze further research into AI-assisted material design, potentially leading to more efficient and innovative approaches in the ceramics industry. The dataset's introduction may also inspire the development of similar benchmarks in other material domains, fostering interdisciplinary collaboration between AI and materials engineering.

Authors: Ziyu Zhai, Siyou Li, Juexi Shao, Juntao Yu  
Source: arXiv:2605.06641  
URL: https://arxiv.org/abs/2605.06641v1
