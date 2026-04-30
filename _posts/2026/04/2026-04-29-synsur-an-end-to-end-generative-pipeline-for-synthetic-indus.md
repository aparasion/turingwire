---
title: "SynSur: An end-to-end generative pipeline for synthetic industrial surface defect generation and detection"
date: 2026-04-29 12:57:32 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26633v1"
arxiv_id: "2604.26633"
authors: ["Paul Julius K\u00fchn", "Mika Pommeranz", "Arjan Kuijper", "Saptarshi Neil Sinha"]
slug: synsur-an-end-to-end-generative-pipeline-for-synthetic-indus
summary_word_count: 444
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the critical gap in the availability of labeled data for training models in industrial defect detection. The authors highlight that the scarcity of defect data, due to the rarity of defects and the high cost of annotations, limits the effectiveness of learning-based approaches. Existing literature lacks comprehensive solutions that effectively generate synthetic defect data while ensuring realistic annotations, which is essential for training robust models.

**Method**  
The authors propose an end-to-end generative pipeline, SynSur, which integrates several advanced techniques: Vision-Language-Model-based prompts for generating defect descriptions, LoRA (Low-Rank Adaptation) for fine-tuning diffusion models, and mask-guided inpainting for realistic defect synthesis. The pipeline also includes sample filtering mechanisms using DreamSim and CLIPScore to evaluate the quality of generated samples and derive automatic labels. The evaluation is conducted on a dataset of pitting defects on ball screw drives and a subset of the Mobile phone screen surface defect segmentation dataset (MSD) to assess cross-domain transferability. The training process leverages both synthetic and real data, with a focus on understanding the contributions of each component in the pipeline.

**Results**  
The results indicate that while synthetic-only training does not outperform models trained solely on real data, the combination of synthetic and real data yields modest performance improvements in specific training regimes. For instance, when using YOLOv26, YOLOX, and LW-DETR, the integration of synthetic defects with real data maintained performance levels and provided enhancements in certain scenarios. The MSD transfer study further demonstrates that the pipeline's structure is applicable across different industrial domains, emphasizing the necessity for domain-specific adaptation and rigorous annotation quality control.

**Limitations**  
The authors acknowledge that synthetic data cannot fully replace real data, as the performance gains are modest and context-dependent. They also note the importance of careful prompt construction and the selection of LoRA parameters, which may not generalize across all defect types or industrial applications. Additionally, the reliance on specific datasets for evaluation may limit the generalizability of the findings. The paper does not extensively explore the computational costs associated with the proposed pipeline, which could be a consideration for practical deployment.

**Why it matters**  
This work has significant implications for the field of industrial defect detection, particularly in scenarios where labeled data is scarce. By demonstrating an effective method for generating synthetic defects that can augment real datasets, the authors provide a pathway for improving model robustness and performance in industrial applications. The insights gained from analyzing the pipeline stages can inform future research on synthetic data generation and its integration into machine learning workflows, potentially leading to more efficient data utilization in various domains.

Authors: Paul Julius Kühn, Mika Pommeranz, Arjan Kuijper, Saptarshi Neil Sinha  
Source: arXiv:2604.26633  
URL: [https://arxiv.org/abs/2604.26633v1](https://arxiv.org/abs/2604.26633v1)
